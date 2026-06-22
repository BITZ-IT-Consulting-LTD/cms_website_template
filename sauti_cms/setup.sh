#!/bin/bash
# Quick Setup Script for Sauti CMS Backend
# This script automates the initial setup for local development

set -e  # Exit on error

echo "🚀 Sauti CMS Backend - Quick Setup"
echo "===================================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "  Python version: $python_version"

# Check PostgreSQL
echo ""
echo "✓ Checking PostgreSQL..."
if command -v psql &> /dev/null; then
    echo "  PostgreSQL is installed"
else
    echo "  ⚠️  PostgreSQL not found. Please install PostgreSQL first:"
    echo "     Ubuntu/Debian: sudo apt install postgresql postgresql-contrib"
    echo "     macOS: brew install postgresql"
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  Virtual environment created"
else
    echo "  Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
echo ""
echo "⚙️  Setting up environment variables..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "  .env file created from .env.example"
    
    # Generate SECRET_KEY
    SECRET_KEY=$(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
    sed -i.bak "s|your-secret-key-here-change-in-production|$SECRET_KEY|g" .env
    
    # Generate ENCRYPTION_KEY
    ENCRYPTION_KEY=$(python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
    sed -i.bak "s|your-encryption-key-here|$ENCRYPTION_KEY|g" .env
    
    rm .env.bak 2>/dev/null || true
    
    echo "  ✓ Generated SECRET_KEY"
    echo "  ✓ Generated ENCRYPTION_KEY"
    echo ""
    echo "  ⚠️  Please update .env with your database credentials!"
else
    echo "  .env file already exists"
fi

# Create PostgreSQL database
echo ""
echo "🗄️  Database Setup..."
read -p "Do you want to create a PostgreSQL database? (y/n): " create_db
if [ "$create_db" = "y" ]; then
    echo "  Creating database 'sauti_cms'..."
    sudo -u postgres psql -c "CREATE DATABASE sauti_cms;" 2>/dev/null || echo "  Database may already exist"
    sudo -u postgres psql -c "CREATE USER sauti_user WITH PASSWORD 'postgres';" 2>/dev/null || echo "  User may already exist"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE sauti_cms TO sauti_user;" 2>/dev/null
    echo "  ✓ Database setup complete"
fi

# Run migrations
echo ""
echo "📊 Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo ""
echo "👤 Create superuser account..."
read -p "Do you want to create a superuser now? (y/n): " create_superuser
if [ "$create_superuser" = "y" ]; then
    python manage.py createsuperuser
fi

# Create media directories
echo ""
echo "📁 Creating media directories..."
mkdir -p media/posts/images
mkdir -p media/resources/files
mkdir -p media/resources/thumbnails
mkdir -p media/partners/logos
mkdir -p media/reports/attachments
echo "  ✓ Media directories created"

echo ""
echo "✅ Setup Complete!"
echo "==================="
echo ""
echo "Next steps:"
echo "1. Update .env file with your database credentials (if not already done)"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python manage.py runserver"
echo "4. Access:"
echo "   - API: http://localhost:8000/api/"
echo "   - Admin: http://localhost:8000/admin/"
echo "   - API Docs: http://localhost:8000/api/docs/"
echo ""
echo "📚 Read README.md for more information"
echo ""
