# Nginx Infrastructure Documentation - SAUTI 116

This document outlines the transition from a monolithic `nginx.conf` to a modular, separated infrastructure implemented in January 2026.

## 1. Directory Structure
All domain-specific configuration for `sauti.mglsd.go.ug` is now located in:
`/etc/nginx/sauticms/`

| File | Purpose | Contents |
| :--- | :--- | :--- |
| `sauti_main.conf` | **Main Entry Point** | SSL certificates, domain names, and the primary port 80/443 logic. |
| `cms_logic.inc` | **New CMS Proxy** | Rules for the Dockerized website and admin dashboard (Port 8080). |
| `helpline_logic.inc` | **Legacy Support** | PHP-FPM rules for the legacy helpline and wallboard apps. |
| `extra_ports.conf` | **Secondary Ports** | SSL configurations for WebSockets on ports 8384 and 8394. |

## 2. Key Improvements
*   **Separation of Concerns**: You can update the CMS logic without touching the legacy Helpline code, and vice versa.
*   **Clean Default**: The main `/etc/nginx/nginx.conf` is now a minimal loader, reducing the risk of server-wide configuration errors.
*   **Conflict Resolution**: Fixed "conflicting server name" errors by centralizing the domain definition in `sauti_main.conf`.
*   **API Pathing**: Implemented a transition rule to redirect legacy `/cms-api/` requests to the new `/sauti/api/` path.

## 3. Deployment Flow
When making changes to the CMS app:
1.  Update code in the repository.
2.  Run `git pull` on the production server.
3.  Rebuild containers: `docker compose -f docker/docker-compose.prod.yml up -d --build --force-recreate`
4.  If Nginx routing needs changing, edit the relevant `.inc` file in `/etc/nginx/sauticms/`.

## 4. Troubleshooting Logs
*   **Host Traffic**: `tail -f /var/log/nginx/sauti_access.log`
*   **Host Errors**: `tail -f /var/log/nginx/sauti_error.log`
*   **CMS App Logs**: `docker logs -f sauti_backend_prod`

---
*Last Updated: January 4, 2026*
