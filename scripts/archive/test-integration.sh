#!/bin/bash

# Quick Integration Test Script
# Tests that posts created in admin appear on frontend

echo "🧪 Sauti Integration Test"
echo "========================="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# Check if services are running
check_service() {
    local port=$1
    local name=$2
    
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null ; then
        echo -e "${GREEN}✓${NC} $name is running on port $port"
        return 0
    else
        echo -e "${RED}✗${NC} $name is NOT running on port $port"
        return 1
    fi
}

echo "Checking services..."
check_service 8000 "Django Backend"
DJANGO_OK=$?

check_service 3000 "Public Frontend"
FRONTEND_OK=$?

check_service 3002 "Admin Dashboard"
ADMIN_OK=$?

echo ""

if [ $DJANGO_OK -ne 0 ] || [ $FRONTEND_OK -ne 0 ] || [ $ADMIN_OK -ne 0 ]; then
    echo -e "${RED}❌ Not all services are running!${NC}"
    echo ""
    echo "Start all services with:"
    echo "  ./start-all.sh"
    exit 1
fi

echo -e "${GREEN}✅ All services are running!${NC}"
echo ""

# Test Django API
echo "Testing Django API..."
API_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/posts/)

if [ "$API_RESPONSE" = "200" ]; then
    echo -e "${GREEN}✓${NC} Django API is responding"
else
    echo -e "${RED}✗${NC} Django API returned status $API_RESPONSE"
fi

# Test Frontend
echo "Testing Frontend..."
FRONTEND_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/)

if [ "$FRONTEND_RESPONSE" = "200" ]; then
    echo -e "${GREEN}✓${NC} Frontend is responding"
else
    echo -e "${RED}✗${NC} Frontend returned status $FRONTEND_RESPONSE"
fi

# Test Admin
echo "Testing Admin Dashboard..."
ADMIN_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3002/)

if [ "$ADMIN_RESPONSE" = "200" ]; then
    echo -e "${GREEN}✓${NC} Admin Dashboard is responding"
else
    echo -e "${RED}✗${NC} Admin Dashboard returned status $ADMIN_RESPONSE"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✅ Integration Test Complete!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔗 Service URLs:"
echo "   Django API:      http://localhost:8000/api"
echo "   Admin Dashboard: http://localhost:3002"
echo "   Public Frontend: http://localhost:3000"
echo ""
echo "🧪 Manual Test Steps:"
echo "   1. Open http://localhost:3002"
echo "   2. Login: admin / admin123"
echo "   3. Create a blog post"
echo "   4. Open http://localhost:3000/blog"
echo "   5. Verify post appears!"
echo ""

# Get post count
POST_COUNT=$(curl -s http://localhost:8000/api/posts/ | grep -o '"count":[0-9]*' | grep -o '[0-9]*')

if [ ! -z "$POST_COUNT" ]; then
    echo -e "${BLUE}📊 Current posts in database: $POST_COUNT${NC}"
fi

echo ""
