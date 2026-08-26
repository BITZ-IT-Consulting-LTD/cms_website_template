"""
Shared helper for generating server-side image derivatives (thumbnail /
medium) on save, so card and list views in the public frontend don't have
to download whatever full-resolution file an editor happened to upload.

Usage from a model's save():

    from imaging.derivatives import sync_image_derivatives

    def save(self, *args, **kwargs):
        ...
        sync_image_derivatives(self, [
            ('featured_image', 'featured_image_thumbnail', THUMBNAIL_SIZE),
            ('featured_image', 'featured_image_medium', MEDIUM_SIZE),
        ])
        super().save(*args, **kwargs)

Call this BEFORE super().save() -- it only assigns in-memory File objects to
the derivative fields on the instance; the caller's own super().save() is
what actually persists everything (source + derivatives) together in one
write, exactly like Resource.save() already does for file_type/file_size.

Design notes:
- A derivative is (re)generated when either:
    (a) the source field was reassigned in this request and not yet
        committed to storage (FieldFile._committed is False -- Django sets
        this the moment a new upload is assigned, and flips it back to True
        only once FileField.pre_save() commits it during save()), or
    (b) the source file exists but the derivative field is still empty
        (covers rows created before this feature existed, and lets a
        one-off backfill management command force regeneration by just
        clearing/looping over existing rows).
- Failure to decode/resize (corrupt upload, unsupported format) is swallowed
  -- the derivative field is simply left as-is, and callers/serializers must
  fall back to the original image. This must never be able to block a save.
- Pillow's Image.thumbnail() is a contain-fit resize that never upscales,
  so a source smaller than the target size is left at its own size.
"""
from io import BytesIO
import os

from django.core.files.base import ContentFile

try:
    from PIL import Image
except ImportError:  # pragma: no cover - Pillow is a hard requirement, but fail soft
    Image = None


# Bounding boxes for the two standard derivatives. Aspect ratio is preserved;
# these are the *maximum* width/height, not a fixed crop.
THUMBNAIL_SIZE = (480, 480)
MEDIUM_SIZE = (1200, 1200)

_SUPPORTED_FORMATS = {'JPEG', 'PNG', 'WEBP'}
_EXT_BY_FORMAT = {'JPEG': 'jpg', 'PNG': 'png', 'WEBP': 'webp'}


def _resize_to_content(file_obj, size, quality=82):
    """
    Read an already-open file-like object (a FieldFile, an UploadedFile, or
    anything Pillow can Image.open()) and return (ContentFile, extension) for
    a copy resized to fit within `size`, or None if it can't be processed.
    Leaves the source file's position at 0 so a subsequent read (e.g. by
    Django's own FileField.pre_save()) still sees the whole file.
    """
    if Image is None:
        return None
    try:
        file_obj.seek(0)
    except Exception:
        pass
    try:
        image = Image.open(file_obj)
        image.load()
    except Exception:
        return None
    finally:
        try:
            file_obj.seek(0)
        except Exception:
            pass

    fmt = (image.format or 'JPEG').upper()
    if fmt not in _SUPPORTED_FORMATS:
        fmt = 'JPEG'

    if fmt == 'JPEG' and image.mode not in ('RGB', 'L'):
        image = image.convert('RGB')
    elif fmt == 'PNG' and image.mode not in ('RGB', 'RGBA', 'L', 'LA', 'P'):
        image = image.convert('RGBA')

    image.thumbnail(size, Image.LANCZOS)

    buffer = BytesIO()
    save_kwargs = {'optimize': True}
    if fmt in ('JPEG', 'WEBP'):
        save_kwargs['quality'] = quality
    try:
        image.save(buffer, format=fmt, **save_kwargs)
    except Exception:
        return None
    buffer.seek(0)
    return ContentFile(buffer.read()), _EXT_BY_FORMAT[fmt]


def sync_image_derivatives(instance, specs, update_fields=None):
    """
    instance: the model instance being saved (not yet persisted this call).
    specs: iterable of (source_field_name, derivative_field_name, size)
           tuples, e.g. ('featured_image', 'featured_image_thumbnail',
           THUMBNAIL_SIZE).
    update_fields: pass through whatever `update_fields` the caller's own
        save(*args, **kwargs) received (kwargs.get('update_fields')). Several
        call sites in this codebase do a narrow `instance.save(update_fields=
        [...])` for an unrelated column (e.g. Post view-count increments,
        Partner phone/email sync) -- generating a derivative there would
        write a new file to storage that the same save() call then never
        persists to the DB (update_fields excludes the derivative column),
        silently orphaning it. When update_fields is given, only specs whose
        source field is actually in it are considered.

    For each qualifying spec, (re)generates the derivative when needed and
    assigns it (unsaved -- save=False) onto instance.<derivative_field_name>.
    Call this before super().save() so the derivative is written in the same
    INSERT/UPDATE as everything else.
    """
    if update_fields is not None:
        specs = [spec for spec in specs if spec[0] in update_fields]

    for source_name, derivative_name, size in specs:
        source = getattr(instance, source_name, None)
        if not source:
            continue

        derivative = getattr(instance, derivative_name, None)
        committed = getattr(source, '_committed', True)
        already_has_derivative = bool(derivative)

        if committed and already_has_derivative:
            continue  # nothing changed and a derivative already exists

        result = _resize_to_content(source, size)
        if result is None:
            continue
        content, ext = result

        base_name = os.path.splitext(os.path.basename(source.name or 'image'))[0]
        filename = f"{base_name}_{derivative_name}.{ext}"
        getattr(instance, derivative_name).save(filename, content, save=False)
