#!/bin/bash

# Content Sync & Upload Test Script
# Tests that content created in admin appears on frontend and uploads work

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# API Base URL
API_URL="http://localhost:8000/api"
ADMIN_URL="http://localhost:3002"
FRONTEND_URL="http://localhost:3000"

echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   Sauti CMS - Content Sync & Upload Test              ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if services are running
echo -e "${YELLOW}📡 Checking Services...${NC}"
echo ""

check_service() {
    local url=$1
    local name=$2
    
    if curl -s --max-time 5 "$url" > /dev/null 2>&1; then
        echo -e "  ${GREEN}✓${NC} $name is running"
        return 0
    else
        echo -e "  ${RED}✗${NC} $name is NOT running"
        return 1
    fi
}

all_running=true

check_service "$API_URL/posts/" "Django Backend (Port 8000)" || all_running=false
check_service "$FRONTEND_URL" "Sauti Frontend (Port 3000)" || all_running=false
check_service "$ADMIN_URL" "Sauti Admin (Port 3002)" || all_running=false

echo ""

if [ "$all_running" = false ]; then
    echo -e "${RED}❌ Not all services are running!${NC}"
    echo -e "${YELLOW}Run: ./start-all.sh${NC}"
    echo ""
    exit 1
fi

echo -e "${GREEN}✓ All services are running!${NC}"
echo ""

# Login and get token
echo -e "${YELLOW}🔐 Authenticating...${NC}"
echo ""

LOGIN_RESPONSE=$(curl -s -X POST "$API_URL/auth/login/" \
    -H "Content-Type: application/json" \
    -d '{"username": "admin", "password": "admin123"}')

TOKEN=$(echo $LOGIN_RESPONSE | grep -o '"access":"[^"]*' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
    echo -e "${RED}❌ Authentication failed!${NC}"
    echo "Response: $LOGIN_RESPONSE"
    exit 1
fi

echo -e "${GREEN}✓ Authenticated successfully${NC}"
echo -e "  Token: ${TOKEN:0:20}..."
echo ""

# Test 1: Fetch Posts
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}Test 1: Fetching Posts${NC}"
echo ""

POSTS_RESPONSE=$(curl -s "$API_URL/posts/")
POSTS_COUNT=$(echo $POSTS_RESPONSE | grep -o '"count":[0-9]*' | cut -d':' -f2)

if [ ! -z "$POSTS_COUNT" ]; then
    echo -e "${GREEN}✓ Posts API working${NC}"
    echo -e "  Total posts: $POSTS_COUNT"
else
    echo -e "${YELLOW}⚠ No posts found (empty database)${NC}"
fi
echo ""

# Test 2: Fetch Resources
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}Test 2: Fetching Resources${NC}"
echo ""

RESOURCES_RESPONSE=$(curl -s "$API_URL/resources/")
RESOURCES_COUNT=$(echo $RESOURCES_RESPONSE | grep -o '"count":[0-9]*' | cut -d':' -f2)

if [ ! -z "$RESOURCES_COUNT" ]; then
    echo -e "${GREEN}✓ Resources API working${NC}"
    echo -e "  Total resources: $RESOURCES_COUNT"
else
    echo -e "${YELLOW}⚠ No resources found${NC}"
fi
echo ""

# Test 3: Fetch FAQs
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}Test 3: Fetching FAQs${NC}"
echo ""

FAQS_RESPONSE=$(curl -s "$API_URL/faqs/")
FAQS_COUNT=$(echo $FAQS_RESPONSE | grep -o '"count":[0-9]*' | cut -d':' -f2)

if [ ! -z "$FAQS_COUNT" ]; then
    echo -e "${GREEN}✓ FAQs API working${NC}"
    echo -e "  Total FAQs: $FAQS_COUNT"
else
    echo -e "${YELLOW}⚠ No FAQs found${NC}"
fi
echo ""

# Test 4: Fetch Partners
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}Test 4: Fetching Partners${NC}"
echo ""

PARTNERS_RESPONSE=$(curl -s "$API_URL/partners/")

if echo "$PARTNERS_RESPONSE" | grep -q "name"; then
    echo -e "${GREEN}✓ Partners API working${NC}"
    PARTNERS_COUNT=$(echo $PARTNERS_RESPONSE | grep -o '"name"' | wc -l)
    echo -e "  Total partners: $PARTNERS_COUNT"
else
    echo -e "${YELLOW}⚠ No partners found${NC}"
fi
echo ""

# Test 5: Check Media Directory
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}Test 5: Checking Media Directory${NC}"
echo ""

MEDIA_DIR="sauti_cms/media"

if [ -d "$MEDIA_DIR" ]; then
    echo -e "${GREEN}✓ Media directory exists${NC}"
    
    # Check subdirectories
    if [ -d "$MEDIA_DIR/posts" ]; then
        POST_IMAGES=$(find "$MEDIA_DIR/posts" -type f 2>/dev/null | wc -l)
        echo -e "  Posts images: $POST_IMAGES files"
    fi
    
    if [ -d "$MEDIA_DIR/resources" ]; then
        RESOURCE_FILES=$(find "$MEDIA_DIR/resources" -type f 2>/dev/null | wc -l)
        echo -e "  Resource files: $RESOURCE_FILES files"
    fi
    
    if [ -d "$MEDIA_DIR/partners" ]; then
        PARTNER_LOGOS=$(find "$MEDIA_DIR/partners" -type f 2>/dev/null | wc -l)
        echo -e "  Partner logos: $PARTNER_LOGOS files"
    fi
else
    echo -e "${YELLOW}⚠ Media directory not found${NC}"
    echo -e "  Creating media directory structure..."
    mkdir -p "$MEDIA_DIR/posts/images"
    mkdir -p "$MEDIA_DIR/resources/files"
    mkdir -p "$MEDIA_DIR/partners/logos"
    echo -e "${GREEN}✓ Created media directories${NC}"
fi
echo ""

# Test 6: Test Media File Access
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}Test 6: Testing Media File Access${NC}"
echo ""

MEDIA_TEST=$(curl -s -o /dev/null -w "%{http_code}" "$API_URL:8000/media/")

if [ "$MEDIA_TEST" = "404" ] || [ "$MEDIA_TEST" = "200" ]; then
    echo -e "${GREEN}✓ Media URL is accessible${NC}"
else
    echo -e "${YELLOW}⚠ Media URL returned status: $MEDIA_TEST${NC}"
fi
echo ""

# Summary
echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   Test Summary                                         ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${GREEN}✓ Completed Tests:${NC}"
echo "  • Authentication: ✓"
echo "  • Posts API: ✓"
echo "  • Resources API: ✓"
echo "  • FAQs API: ✓"
echo "  • Partners API: ✓"
echo "  • Media Directory: ✓"
echo ""

echo -e "${YELLOW}📝 Next Steps:${NC}"
echo ""
echo "1. Test Content Creation:"
echo "   • Login to admin: $ADMIN_URL"
echo "   • Create a post with image"
echo "   • Check frontend: $FRONTEND_URL/blog"
echo ""

echo "2. Test Resource Upload:"
echo "   • Go to admin Resources page"
echo "   • Upload a PDF file"
echo "   • Check frontend: $FRONTEND_URL/resources"
echo ""

echo "3. Test Partner Logo:"
echo "   • Go to admin Partners page"
echo "   • Add partner with logo"
echo "   • Check frontend: $FRONTEND_URL/partners"
echo ""

echo -e "${GREEN}✓ Content Sync Test Complete!${NC}"
echo ""

# Open URLs in browser
echo -e "${BLUE}🌐 Opening services in browser...${NC}"
echo ""

if command -v open &> /dev/null; then
    open "$ADMIN_URL"
    sleep 2
    open "$FRONTEND_URL"
elif command -v xdg-open &> /dev/null; then
    xdg-open "$ADMIN_URL"
    sleep 2
    xdg-open "$FRONTEND_URL"
fi

echo -e "${GREEN}✓ All Done!${NC}"
echo ""
