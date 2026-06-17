#!/bin/bash

set -ex

echo "Waiting for PostgreSQL..."
while ! pg_isready -h ${DB_HOST} -p ${DB_PORT} -U ${DB_USER}; do
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

echo "Populating site content..."
# Use comprehensive populate script (clears old content for fresh start)
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

# Note: These are Django management commands found in app/management/commands/
echo "Running site content population..."
python manage.py populate_site_content

echo "Running sitesettings population..."
python manage.py populate_sitesettings

echo "Running FAQs population..."
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