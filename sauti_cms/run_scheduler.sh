#!/bin/sh
# Scheduler script to publish scheduled posts and videos
# Runs every minute to check for due content

while true; do
    echo "[$(date)] Running scheduled content publisher..."
    python manage.py publish_scheduled
    echo "[$(date)] Sleeping for 60 seconds..."
    sleep 60
done
