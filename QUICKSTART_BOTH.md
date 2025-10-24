# 🚀 Quick Start Guide - Running Both Frontends

## Prerequisites
- Node.js installed
- Both projects have dependencies installed

## 🎯 Start Both Frontends

### Option 1: Two Terminal Windows (Recommended)

**Terminal 1 - Public Frontend (Port 3000):**
```bash
cd sauti-frontend
npm run dev
```
Then open: **http://localhost:3000**

**Terminal 2 - Admin Dashboard (Port 3002):**
```bash
cd sauti-admin
npm run dev -- --port 3002
```
Then open: **http://localhost:3002**

### Option 2: Background Processes
```bash
# From project root
cd sauti-frontend && npm run dev &
cd ../sauti-admin && npm run dev -- --port 3002 &
```

## 🔐 Login Credentials

**Admin Dashboard:** http://localhost:3002/login
- Username: `admin`
- Password: `admin123`

## 📍 URLs

| Service | URL | Purpose |
|---------|-----|---------|
| Public Frontend | http://localhost:3000 | Citizen-facing website |
| Admin Dashboard | http://localhost:3002 | Content management |
| Django Backend | http://localhost:8000 | REST API (needs to be started separately) |

## ✅ Verification Steps

1. ✅ **Frontend Running:** Visit http://localhost:3000 - should see Sauti homepage
2. ✅ **Admin Running:** Visit http://localhost:3002 - should see login page
3. ✅ **Login Works:** Use admin/admin123 credentials
4. ✅ **Navigation Works:** Click through pages on both sites

## 🔄 What's Synchronized?

- **✅ Colors:** Both use #CC5500 (Sauti Orange)
- **✅ Fonts:** Both use Inter font family  
- **✅ API:** Both connect to http://localhost:8000/api
- **✅ Auth:** Both use JWT tokens (separate storage)
- **✅ Data:** Both fetch from same Django backend

## 🛑 Stopping Services

Press `Ctrl+C` in each terminal window

Or if running in background:
```bash
# Kill by port
lsof -ti:3000 | xargs kill -9  # Frontend
lsof -ti:3002 | xargs kill -9  # Admin
```

## 🐛 Troubleshooting

**Port Already in Use:**
```bash
# Kill existing process
lsof -ti:3000 | xargs kill -9
lsof -ti:3002 | xargs kill -9
```

**Dependencies Missing:**
```bash
cd sauti-frontend && npm install
cd ../sauti-admin && npm install
```

**Can't Connect to API:**
- Start Django backend: `cd sauti_cms && python manage.py runserver`
- Currently using mock auth in admin (works without Django)

## 📚 Next Steps

1. Read [FRONTEND_SYNC.md](./FRONTEND_SYNC.md) for detailed sync info
2. Read [SYNC_GUIDE.md](./SYNC_GUIDE.md) for architecture details
3. Start Django backend to enable real API calls
4. Test creating content in Admin and viewing on Frontend
