# Multi-stage build for Vue.js Frontend

# Build stage
FROM node:20-alpine as build-stage

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Set build arguments BEFORE copying source code
ARG VITE_API_URL=/api
ARG VITE_APP_NAME="Sauti 116 helpline"
ARG VITE_HOTLINE=116
ARG VITE_WHATSAPP="+256743889999"
ARG VITE_EMAIL="info@sauti.mglsd.go.ug"

# Set environment variables for build
ENV VITE_API_URL=${VITE_API_URL}
ENV VITE_APP_NAME=${VITE_APP_NAME}
ENV VITE_HOTLINE=${VITE_HOTLINE}
ENV VITE_WHATSAPP=${VITE_WHATSAPP}
ENV VITE_EMAIL=${VITE_EMAIL}

# Copy application code
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

# Expose ports
EXPOSE 80 443

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
