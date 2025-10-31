#!/bin/bash

# Sauti Platform Startup Script
# This script starts both the public frontend and admin dashboard

echo "🚀 Starting Sauti Platform..."
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
ORANGE='\033[0;33m'
NC='\033[0m' # No Color

# Check if node_modules exist in both projects
check_dependencies() {
    echo "📦 Checking dependencies..."
    
    if [ ! -d "sauti-frontend/node_modules" ]; then
        echo "${ORANGE}⚠️  Installing dependencies for sauti-frontend...${NC}"
        cd sauti-frontend && npm install && cd ..
    fi
    
    if [ ! -d "sauti-admin/node_modules" ]; then
        echo "${ORANGE}⚠️  Installing dependencies for sauti-admin...${NC}"
        cd sauti-admin && npm install && cd ..
    fi
    
    echo "${GREEN}✅ Dependencies ready${NC}"
    echo ""
}

# Start services
start_services() {
    echo "${BLUE}🌐 Starting Public Frontend (Port 3000)...${NC}"
    cd sauti-frontend
    npm run dev &
    FRONTEND_PID=$!
    cd ..
    
    sleep 2
    
    echo "${ORANGE}👑 Starting Admin Dashboard (Port 3002)...${NC}"
    cd sauti-admin
    npm run dev -- --port 3002 &
    ADMIN_PID=$!
    cd ..
    
    sleep 3
    
    echo ""
    echo "${GREEN}✅ All services started!${NC}"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "${BLUE}📱 Public Frontend:${NC}    http://localhost:3000"
    echo "${ORANGE}⚙️  Admin Dashboard:${NC}   http://localhost:3002"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "🔐 Admin Credentials:"
    echo "   Username: admin"
    echo "   Password: admin123"
    echo ""
    echo "Press Ctrl+C to stop all services"
    echo ""
}

# Cleanup on exit
cleanup() {
    echo ""
    echo "${ORANGE}🛑 Shutting down services...${NC}"
    kill $FRONTEND_PID 2>/dev/null
    kill $ADMIN_PID 2>/dev/null
    echo "${GREEN}✅ All services stopped${NC}"
    exit 0
}

# Set trap to catch Ctrl+C
trap cleanup INT

# Main execution
check_dependencies
start_services

# Keep script running
wait
