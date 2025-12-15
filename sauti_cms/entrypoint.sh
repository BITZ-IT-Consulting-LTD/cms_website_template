#!/bin/bash

set -e

echo "Waiting for PostgreSQL..."
while ! pg_isready -h ${DB_HOST} -p ${DB_PORT} -U ${DB_USER}; do
  sleep 1
done
echo "PostgreSQL is ready!"

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Populating site content..."
python /app/populate_all_content.py

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Creating superuser if it doesn't exist..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@sauti.org', 'changeme123')
    print('Superuser created: admin/changeme123')
else:
    print('Superuser already exists')
END

echo "Starting application..."
exec "$@"