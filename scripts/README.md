# Development Scripts

This folder contains archived development and testing scripts.

## Active Scripts (Root Directory)

### `start-all.sh`
**Location**: Project root
**Purpose**: Starts Django backend + both Vue frontends for local development
**When to use**: Local development without Docker
**Status**: ✅ Active (documented in `docs/CLAUDE.md`)

```bash
# From project root:
./start-all.sh
```

## Active Scripts (Backend Directory)

### `sauti_cms/setup.sh`
**Purpose**: First-time backend setup script
**Features**:
- Creates virtual environment
- Installs Python dependencies
- Generates SECRET_KEY and ENCRYPTION_KEY
- Creates PostgreSQL database
- Runs migrations
- Creates superuser
- Sets up media directories

**When to use**: First-time local development setup (non-Docker)

```bash
cd sauti_cms
./setup.sh
```

### `sauti_cms/verify_setup.sh`
**Purpose**: Verifies backend configuration
**Features**:
- Checks Python version
- Verifies virtual environment
- Validates .env configuration
- Tests PostgreSQL connection
- Checks Django dependencies
- Verifies migrations
- Tests media directories
- Checks API availability

**When to use**: Troubleshooting local development setup

```bash
cd sauti_cms
./verify_setup.sh
```

---

## Archived Scripts

These scripts were used during development and QA but are now **obsolete** with the Docker-based workflow.

### `archive/start-frontends.sh`
**Purpose**: Started only the two Vue frontends
**Why archived**: Redundant with `start-all.sh`

### `archive/test-content-sync.sh`
**Purpose**: Comprehensive content sync testing
**Why archived**:
- Tests for local development workflow
- Now using Docker containers
- QA testing documented in `docs/TEST_RESULTS.md`

### `archive/test-integration.sh`
**Purpose**: Quick integration tests between services
**Why archived**:
- Tests for local development workflow
- Now using Docker containers
- Integration verified in Docker setup

---

## Current Recommended Workflow

### Production/Testing (Docker)
```bash
# Start all services
docker compose --env-file .env.docker -f docker-compose-full.yml up -d

# Stop all services
docker compose --env-file .env.docker -f docker-compose-full.yml down
```

See `docs/FIRST_TIME_SETUP.md` for details.

### Local Development (Without Docker)
```bash
# Option 1: Start everything
./start-all.sh

# Option 2: Start individually
cd sauti_cms && python manage.py runserver
cd sauti-frontend && npm run dev
cd sauti-admin && npm run dev -- --port 3002
```

See `docs/CLAUDE.md` for details.

---

**Last Updated**: October 31, 2025
