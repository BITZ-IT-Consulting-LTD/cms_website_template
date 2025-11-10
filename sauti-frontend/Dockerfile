# Multi-stage build for Sauti Public Frontend
# Stage 1: Build the Vue application
FROM node:18-alpine AS build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application files
COPY . .

# Build argument for API URL
ARG VITE_API_URL=/api
ARG VITE_APP_NAME="Sauti 116 helpline"
ARG VITE_HOTLINE=116
ARG VITE_WHATSAPP="+256743889999"
ARG VITE_EMAIL="info@sauti.mglsd.go.ug"

# Set environment variables for build
ENV VITE_API_URL=$VITE_API_URL
ENV VITE_APP_NAME=$VITE_APP_NAME
ENV VITE_HOTLINE=$VITE_HOTLINE
ENV VITE_WHATSAPP=$VITE_WHATSAPP
ENV VITE_EMAIL=$VITE_EMAIL

# Build the application
RUN npm run build

# Stage 2: Serve with nginx
FROM nginx:alpine

# Copy built files from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
