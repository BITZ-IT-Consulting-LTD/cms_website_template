#!/bin/bash
# Sauti CMS - System Verification Script
# Checks if all components are properly configured and working

set -e

echo "🔍 Sauti CMS Backend - System Verification"
echo "==========================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counter for passed/failed checks
PASSED=0
FAILED=0

check_pass() {
    echo -e "${GREEN}✓${NC} $1"
    ((PASSED++))
}

check_fail() {
    echo -e "${RED}✗${NC} $1"
    ((FAILED++))
}

check_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Check 1: Python version
echo "1. Checking Python..."
if python3 --version &> /dev/null; then
    python_version=$(python3 --version 2>&1 | awk '{print $2}')
    check_pass "Python $python_version installed"
else
    check_fail "Python 3 not found"
fi

# Check 2: Virtual environment
echo ""
echo "2. Checking virtual environment..."
if [ -d "venv" ]; then
    check_pass "Virtual environment exists"
else
    check_fail "Virtual environment not found (run setup.sh)"
fi

# Check 3: .env file
echo ""
echo "3. Checking environment configuration..."
if [ -f ".env" ]; then
    check_pass ".env file exists"
    
    # Check for default values that should be changed
    if grep -q "your-secret-key-here" .env; then
        check_warn "SECRET_KEY still has default value"
    else
        check_pass "SECRET_KEY is configured"
    fi
    
    if grep -q "your-encryption-key-here" .env; then
        check_warn "ENCRYPTION_KEY still has default value"
    else
        check_pass "ENCRYPTION_KEY is configured"
    fi
else
    check_fail ".env file not found (run setup.sh)"
fi

# Check 4: PostgreSQL
echo ""
echo "4. Checking PostgreSQL..."
if command -v psql &> /dev/null; then
    check_pass "PostgreSQL is installed"
    
    # Try to connect to database
    if psql -U postgres -d sauti_cms -c "SELECT 1;" &> /dev/null; then
        check_pass "Database 'sauti_cms' is accessible"
    else
        check_warn "Cannot connect to database 'sauti_cms'"
    fi
else
    check_fail "PostgreSQL not found"
fi

# Check 5: Django dependencies
echo ""
echo "5. Checking Django dependencies..."
source venv/bin/activate 2>/dev/null || true

if python -c "import django" 2>/dev/null; then
    check_pass "Django is installed"
else
    check_fail "Django not installed (run: pip install -r requirements.txt)"
fi

if python -c "import rest_framework" 2>/dev/null; then
    check_pass "Django REST Framework is installed"
else
    check_fail "DRF not installed"
fi

if python -c "import rest_framework_simplejwt" 2>/dev/null; then
    check_pass "Simple JWT is installed"
else
    check_fail "Simple JWT not installed"
fi

# Check 6: Database migrations
echo ""
echo "6. Checking database migrations..."
if python manage.py showmigrations 2>/dev/null | grep -q "\[ \]"; then
    check_warn "Some migrations not applied (run: python manage.py migrate)"
else
    check_pass "All migrations appear to be applied"
fi

# Check 7: Media directories
echo ""
echo "7. Checking media directories..."
media_dirs=("media/posts/images" "media/resources/files" "media/partners/logos" "media/reports/attachments")
all_exist=true

for dir in "${media_dirs[@]}"; do
    if [ -d "$dir" ]; then
        check_pass "$dir exists"
    else
        check_fail "$dir not found"
        all_exist=false
    fi
done

# Check 8: Django apps configuration
echo ""
echo "8. Checking Django apps..."
apps=("users" "posts" "resources" "faqs" "partners" "reports")
for app in "${apps[@]}"; do
    if [ -d "$app" ] && [ -f "$app/models.py" ]; then
        check_pass "App '$app' is present"
    else
        check_fail "App '$app' not found or incomplete"
    fi
done

# Check 9: Static files
echo ""
echo "9. Checking static files..."
if [ -d "staticfiles" ]; then
    check_pass "Static files directory exists"
else
    check_warn "Static files not collected (run: python manage.py collectstatic)"
fi

# Check 10: API endpoints (if server is running)
echo ""
echo "10. Checking API availability..."
if curl -s http://localhost:8000/api/docs/ > /dev/null 2>&1; then
    check_pass "API is accessible at http://localhost:8000"
else
    check_warn "API not accessible (is the server running?)"
fi

# Summary
echo ""
echo "==========================================="
echo "Verification Summary"
echo "==========================================="
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ System is ready!${NC}"
    echo ""
    echo "To start the server:"
    echo "1. source venv/bin/activate"
    echo "2. python manage.py runserver"
    echo ""
    echo "Access points:"
    echo "- API: http://localhost:8000/api/"
    echo "- Admin: http://localhost:8000/admin/"
    echo "- API Docs: http://localhost:8000/api/docs/"
    exit 0
else
    echo -e "${RED}✗ Some issues need to be resolved${NC}"
    echo ""
    echo "Run setup.sh to fix common issues, or check README.md for manual setup"
    exit 1
fi
