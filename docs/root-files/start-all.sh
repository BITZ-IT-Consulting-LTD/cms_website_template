#!/bin/bash

# Sauti Complete System Startup Script
# This starts Django backend + both frontends

echo "🚀 Starting Complete Sauti Platform..."
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
ORANGE='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if in correct directory
if [ ! -d "sauti_cms" ] || [ ! -d "sauti-frontend" ] || [ ! -d "sauti-admin" ]; then
    echo "${RED}❌ Error: Must run from project root directory${NC}"
    exit 1
fi

# Start Django Backend
start_django() {
    echo "${BLUE}🐍 Starting Django Backend (Port 8000)...${NC}"
    export DB_ENGINE=sqlite
    cd sauti_cms
    
    # Activate virtual environment
    if [ -d "venv" ]; then
        source venv/bin/activate
    elif [ -d ".venv" ]; then
        source .venv/bin/activate
    fi
    
    # Check if database exists
    if [ ! -f "db.sqlite3" ]; then
        echo "${ORANGE}📦 Database not found. Running migrations...${NC}"
        python3 manage.py migrate
    fi
    
    # Start server
    python3 manage.py runserver &
    DJANGO_PID=$!
    cd ..
    
    sleep 3
    echo "${GREEN}✅ Django backend started (PID: $DJANGO_PID)${NC}"
}

# Start Frontend
start_frontend() {
    echo "${BLUE}🌐 Starting Public Frontend (Port 3000)...${NC}"
    cd sauti-frontend
    
    # Check dependencies
    if [ ! -d "node_modules" ]; then
        echo "${ORANGE}📦 Installing frontend dependencies...${NC}"
        npm install
    fi
    
    npm run dev &
    FRONTEND_PID=$!
    cd ..
    
    sleep 2
    echo "${GREEN}✅ Public frontend started (PID: $FRONTEND_PID)${NC}"
}

# Start Admin
start_admin() {
    echo "${ORANGE}👑 Starting Admin Dashboard (Port 3002)...${NC}"
    cd sauti-admin
    
    # Check dependencies
    if [ ! -d "node_modules" ]; then
        echo "${ORANGE}📦 Installing admin dependencies...${NC}"
        npm install
    fi
    
    npm run dev -- --port 3002 &
    ADMIN_PID=$!
    cd ..
    
    sleep 2
    echo "${GREEN}✅ Admin dashboard started (PID: $ADMIN_PID)${NC}"
}

# Display info
show_info() {
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "${GREEN}✅ All services are running!${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "${BLUE}🔗 Service URLs:${NC}"
    echo "   Django API:         http://localhost:8000/api"
    echo "   Public Frontend:    http://localhost:3000"
    echo "   Admin Dashboard:    http://localhost:3002"
    echo ""
    echo "${ORANGE}🔐 Admin Credentials:${NC}"
    echo "   Username: admin"
    echo "   Password: admin123"
    echo ""
    echo "${GREEN}📝 Quick Test:${NC}"
    echo "   1. Open http://localhost:3002"
    echo "   2. Login with admin/admin123"
    echo "   3. Create a blog post"
    echo "   4. Open http://localhost:3000/blog"
    echo "   5. Your post should appear!"
    echo ""
    echo "Press Ctrl+C to stop all services"
    echo ""
}

# Cleanup function
cleanup() {
    echo ""
    echo "${ORANGE}🛑 Shutting down all services...${NC}"
    
    # Kill Django
    if [ ! -z "$DJANGO_PID" ]; then
        kill $DJANGO_PID 2>/dev/null
        echo "  Stopped Django (PID: $DJANGO_PID)"
    fi
    
    # Kill Frontend
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null
        echo "  Stopped Frontend (PID: $FRONTEND_PID)"
    fi
    
    # Kill Admin
    if [ ! -z "$ADMIN_PID" ]; then
        kill $ADMIN_PID 2>/dev/null
        echo "  Stopped Admin (PID: $ADMIN_PID)"
    fi
    
    # Kill any remaining processes on these ports
    lsof -ti:8000 | xargs kill -9 2>/dev/null
    lsof -ti:3000 | xargs kill -9 2>/dev/null
    lsof -ti:3002 | xargs kill -9 2>/dev/null
    
    echo "${GREEN}✅ All services stopped${NC}"
    exit 0
}

# Set trap for Ctrl+C
trap cleanup INT TERM

# Main execution
echo "Starting services..."
echo ""

start_django
start_frontend
start_admin

show_info

# Keep script running
wait
