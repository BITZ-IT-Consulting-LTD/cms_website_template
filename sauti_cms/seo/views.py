"""
Crawler-facing Open Graph previews (item 10: link previews).

Link-preview crawlers (WhatsApp, Facebook, X/Twitter, LinkedIn, Telegram, ...)
fetch a shared URL and read its <meta> tags WITHOUT executing JavaScript. The
public site is a client-rendered Vue SPA, so those crawlers only ever saw the
static site-wide tags in sauti-frontend/index.html -- every shared article
looked identical (generic title/description/logo), which is why pasting an
article link into WhatsApp showed no real preview.

This module renders a minimal, crawler-only HTML document carrying that one
post's own og:title / og:description / og:image / og:url. It is not meant to
be seen by a human visitor: nginx is configured to route a request to
/blogs/<slug> (dev) or /sauti/blogs/<slug> (prod) here ONLY when the request's
User-Agent matches a known link-preview crawler -- see
docker/nginx/dev.conf, docker/nginx/prod.conf and
docker/nginx/host/sauticms/cms_logic.inc. Every other visitor keeps hitting
the normal Vue SPA at that same URL; this endpoint is otherwise only reached
directly at GET /api/seo/post/<slug>/.

No app registration (INSTALLED_APPS/TEMPLATES) is required: there are no
models here, and the HTML is built by hand (not django.template) with every
interpolated value passed through django.utils.html.escape.
"""
from django.http import HttpResponse, Http404
from django.utils.html import escape, strip_tags
from decouple import config

from posts.models import Post

# Public origin (scheme + host, no path) used to build absolute og:image URLs.
# Override with the OG_SITE_ORIGIN env var per environment.
SITE_ORIGIN = config('OG_SITE_ORIGIN', default='https://sauti.mglsd.go.ug').rstrip('/')

# Base path the public SPA is served under in production -- mirrors
# sauti-frontend's VITE_PUBLIC_BASE_URL / VITE_BASE_PATH. Override with
# OG_FRONTEND_BASE_PATH for a differently-deployed environment.
FRONTEND_BASE_PATH = config('OG_FRONTEND_BASE_PATH', default='/sauti').rstrip('/')

# Shown when a post has no featured_image.
DEFAULT_OG_IMAGE = config('OG_DEFAULT_IMAGE', default=f'{SITE_ORIGIN}/logo.png')

SITE_NAME = 'Sauti 116'
MAX_DESCRIPTION_LENGTH = 300


def _absolute_media_url(image_field):
    """Turn an ImageField into an absolute URL on SITE_ORIGIN, or None.

    Crawlers fetch og:image directly (they don't share the browser's proxy
    or relative-URL context), so this must be a fully-qualified URL.
    """
    if not image_field:
        return None
    try:
        url = image_field.url
    except (ValueError, AttributeError):
        return None
    if url.startswith('http://') or url.startswith('https://'):
        return url
    return f"{SITE_ORIGIN}{url}"


def _build_description(post):
    """Plain-text excerpt for og:description, falling back to stripped body
    content when no excerpt was written, trimmed to a crawler-friendly length.
    """
    raw = post.excerpt or post.content or ''
    text = strip_tags(raw).strip()
    text = ' '.join(text.split())  # collapse newlines/repeated whitespace
    if len(text) > MAX_DESCRIPTION_LENGTH:
        text = text[:MAX_DESCRIPTION_LENGTH - 1].rsplit(' ', 1)[0].rstrip(',.;:') + '…'
    return text


def _og_html(*, title, description, url, image, og_type='article'):
    """Minimal OG/Twitter-Card HTML document. All values are HTML-escaped."""
    title = escape(title)
    description = escape(description)
    url = escape(url)
    image = escape(image)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:secure_url" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{image}">
</head>
<body>
<h1>{title}</h1>
<p>{description}</p>
<p><a href="{url}">{url}</a></p>
</body>
</html>
"""


def post_og_preview(request, slug):
    """GET /api/seo/post/<slug>/ -- crawler-facing OG HTML for one post.

    Only PUBLISHED posts are servable here (draft/unknown slugs 404), same
    visibility rule as the public post API.
    """
    try:
        post = Post.objects.select_related('category').get(
            slug=slug, status=Post.Status.PUBLISHED
        )
    except Post.DoesNotExist:
        raise Http404('Post not found')

    canonical_url = f"{SITE_ORIGIN}{FRONTEND_BASE_PATH}/blogs/{post.slug}"
    image = _absolute_media_url(post.featured_image) or DEFAULT_OG_IMAGE
    description = _build_description(post) or f'Read this article on {SITE_NAME}.'

    html = _og_html(
        title=post.title,
        description=description,
        url=canonical_url,
        image=image,
    )
    response = HttpResponse(html, content_type='text/html; charset=utf-8')
    # Crawlers re-fetch fairly often on their own; a short cache absorbs
    # bursts (e.g. a link posted to a busy WhatsApp group) without serving a
    # stale title/image for long after an edit.
    response['Cache-Control'] = 'public, max-age=300'
    return response
