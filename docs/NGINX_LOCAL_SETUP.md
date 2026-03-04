# Nginx Local Development Setup

This guide will help you configure nginx on your Mac so you can access the app locally as if it's in production.

## Prerequisites

1. Install nginx using Homebrew:
```bash
brew install nginx
```

## Setup Steps

### 1. Add Local Domain to Hosts File

Add `sauti.local` to your `/etc/hosts` file:

```bash
sudo sh -c 'echo "127.0.0.1 sauti.local www.sauti.local" >> /etc/hosts'
```

### 2. Configure Nginx

Copy the nginx configuration:

```bash
# For Apple Silicon Mac (M1/M2/M3)
sudo cp nginx-local-dev.conf /opt/homebrew/etc/nginx/servers/sauti.conf

# For Intel Mac
sudo cp nginx-local-dev.conf /usr/local/etc/nginx/servers/sauti.conf
```

Test nginx configuration:
```bash
nginx -t
```

### 3. Start/Restart Nginx

```bash
# Start nginx
brew services start nginx

# Or restart if already running
brew services restart nginx
```

### 4. Start Your Development Servers

You need to run all three services on specific ports:

**Terminal 1 - Backend (Django):**
```bash
cd sauti_cms
# Make sure PostgreSQL is running (via Docker or locally)
# Run migrations if needed
python manage.py migrate
python manage.py runserver 8000
```

**Terminal 2 - Frontend (Public Site):**
```bash
cd sauti-frontend
npm install
npm run dev  # Runs on port 3000
```

**Terminal 3 - Admin Dashboard:**
```bash
cd sauti-admin
npm install
npm run dev  # Runs on port 3002
```

### 5. Access Your Application

- **Public Frontend**: http://sauti.local
- **Admin Dashboard**: http://sauti.local/admin/
- **API**: http://sauti.local/api/
- **Django Admin**: http://sauti.local/django-admin/

## Environment Variables

The `.env.local` files have been created for each component:

- `/.env.local` - Backend Django configuration
- `/sauti-admin/.env.local` - Admin dashboard configuration
- `/sauti-frontend/.env.local` - Frontend configuration

Make sure to update these files if you need different settings.

## Database Setup

If you're not using Docker for PostgreSQL, make sure you have it installed:

```bash
brew install postgresql@15
brew services start postgresql@15

# Create database
createdb sauti_cms

# Update .env.local with your PostgreSQL credentials
```

## Troubleshooting

### Port Already in Use
If port 80 is already in use:
```bash
# Check what's using port 80
sudo lsof -i :80

# Stop the service or change nginx to use a different port
```

### Nginx Not Found
```bash
# Check nginx installation
which nginx

# If not found, install it
brew install nginx
```

### Permission Denied
```bash
# Nginx needs permission to bind to port 80
sudo nginx
```

### Frontend/Backend Not Connecting
1. Check that all three services are running on the correct ports
2. Check nginx error logs:
```bash
tail -f /opt/homebrew/var/log/nginx/error.log
# or for Intel Macs:
tail -f /usr/local/var/log/nginx/error.log
```

### DNS Not Resolving
Verify `/etc/hosts` entry:
```bash
cat /etc/hosts | grep sauti.local
```

## Stop Services

```bash
# Stop nginx
brew services stop nginx

# Stop Django (Ctrl+C in terminal)
# Stop Vite dev servers (Ctrl+C in terminals)
```

## Production Notes

This setup mimics production by:
- Using a single domain with path-based routing
- Proxying all requests through nginx
- Supporting file uploads (50MB limit)
- Enabling hot module replacement (HMR) for Vite

The main differences from production:
- Using HTTP instead of HTTPS
- Using Vite dev server instead of built static files
- Django in debug mode
- Local database instead of production database
