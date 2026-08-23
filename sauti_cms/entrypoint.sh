#!/bin/bash

set -ex

echo "Waiting for PostgreSQL..."
while ! pg_isready -h ${DB_HOST:-db} -p ${DB_PORT:-5432} -U ${DB_USER:-postgres}; do
  echo "Postgres unavailable - sleeping"
  sleep 1
done
echo "PostgreSQL is ready!"

pip install -r requirements.txt
echo "Cleaning up old migrations and cache..."
find . -path "*/migrations/*.pyc" -delete
find . -path "*/__pycache__/*" -delete
# Generate migrations for all apps
python manage.py makemigrations
python manage.py migrate --noinput --verbosity 2

echo "Checking for existing site content..."
# The comprehensive populate scripts delete-all and/or update_or_create, which
# overwrites content edited through the CMS admin. They must therefore only run
# against a FRESH (empty) database — never on a redeploy/restart of a populated
# one, or admins would lose their edits every deploy. The idempotent
# `populate_site_content` management command below uses get_or_create, so it
# safely adds any new keys on every deploy without touching existing values.
EXISTING_CONTENT=$(python manage.py shell -c "from content.models import SiteContent; print(SiteContent.objects.count())" 2>/dev/null | tail -n 1)
echo "Existing SiteContent rows: ${EXISTING_CONTENT:-unknown}"

if [ "$EXISTING_CONTENT" = "0" ]; then
    echo "Fresh database detected - running comprehensive content seed..."
    if [ -f "/app/populate_comprehensive_content.py" ]; then
        echo "Running populate_comprehensive_content.py..."
        python /app/populate_comprehensive_content.py
    elif [ -f "/app/populate_initial_content.py" ]; then
        echo "Running populate_initial_content.py..."
        python /app/populate_initial_content.py
    elif [ -f "/app/populate_all_content.py" ]; then
        echo "Running populate_all_content.py..."
        python /app/populate_all_content.py
    else
        echo "WARNING: No populate scripts found"
    fi
else
    echo "Existing site content found (${EXISTING_CONTENT} rows) - skipping destructive comprehensive seed to preserve CMS edits."
fi

# Note: These are Django management commands found in app/management/commands/
echo "Running site content population..."
python manage.py populate_site_content

# Both commands below are additive by default (get_or_create): they add any
# new keys/FAQs introduced by a release without touching rows an admin has
# edited. They only overwrite when passed --force, which must never be done
# here. Before 2026-08, both used update_or_create unconditionally and reset
# every seeded site setting and all 22 seeded FAQs on each deploy.
echo "Running sitesettings population (additive)..."
python manage.py populate_sitesettings

echo "Running FAQs population (additive)..."
python manage.py populate_faqs

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Creating superusers..."
if [ -f "/app/create_admin.py" ]; then
    python /app/create_admin.py
else
    # Fallback if file missing
    python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@sauti.org', 'changeme123', role='ADMIN')
    print('Fallback: Superuser created: admin/changeme123')
END
fi

echo "Starting application..."
exec "$@"