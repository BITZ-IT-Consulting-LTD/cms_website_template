# CMS Website Template

This project is a monorepo-style system that contains multiple Vite frontends and a Django backend.

## Infrastructure Overview

The infrastructure has been refactored to use a clean, environment-driven Docker setup.

- **Centralized Configuration:** All Docker and Nginx configurations are located in the `/docker` directory.
- **Separation of Concerns:** There are separate Dockerfiles and Docker Compose files for development and production environments.
- **Environment-Driven:** All configurations, such as base paths and API URLs, are driven by environment variables.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### 1. Create Environment Files

Before running the project, you need to create the environment files. Copy the `env.example` file to the following locations and fill in the required values:

- `sauti_cms/.env`
- `sauti-admin/.env.development`
- `sauti-admin/.env.production`
- `sauti-frontend/.env.development`
- `sauti-frontend/.env.production`

### 2. Run the Project

**For Local Development (with Hot Reload):**

```bash
docker-compose -f docker/docker-compose.dev.yml up --build
```

**For Production Build & Run:**

```bash
docker-compose -f docker/docker-compose.prod.yml up --build -d
```

## Validation Checklist

- **How do I know which env file is active?**
    - For Vite, `vite` logs the mode (`development` or `production`) to the console on startup/build, which determines the file loaded. For Django, the `env_file` directive in the active `docker-compose.*.yml` file is the source of truth.
- **How do I verify the correct Vite mode?**
    - When running `docker-compose ... up`, check the logs for the frontend services. Vite will print `Vite build mode: development` or `Vite build mode: production`.
- **How do I confirm assets resolve correctly?**
    - Open your browser's developer tools. In the "Network" tab, check that requests for JS/CSS files (e.g., `/admin/assets/index-....js`) return a `200 OK` status with the correct `Content-Type` (`application/javascript`, `text/css`), not `text/html`.
- **How do I confirm the frontend is talking to the correct backend?**
    - In the "Network" tab, find the API requests (e.g., to `/api/posts/`). Inspect the request URL. In development, it should be a request to your local Nginx proxy (e.g., `http://localhost/api/posts/`), not a hard-coded production URL.