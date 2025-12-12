# Multi-stage build for Vue.js Admin Dashboard

# Build stage
FROM node:20-alpine as build-stage

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies (including devDependencies needed for build)
RUN npm ci

# Set build arguments BEFORE copying source code
ARG VITE_API_URL=/api
ARG VITE_APP_TITLE="Sauti Admin Dashboard"
ARG VITE_APP_VERSION="1.0.0"

# Set environment variables for build
ENV VITE_API_URL=${VITE_API_URL}
ENV VITE_APP_TITLE=${VITE_APP_TITLE}
ENV VITE_APP_VERSION=${VITE_APP_VERSION}

# Copy application code (this will respect .dockerignore)
COPY . .

# Build the application
RUN npm run build

# Production stage with Nginx
FROM nginx:1.25-alpine as production-stage

# Copy built assets from build stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Add healthcheck
RUN apk add --no-cache curl

# Expose port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
