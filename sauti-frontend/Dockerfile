# Build stage
FROM node:20-alpine as build-stage

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --production=false

# Copy source code
COPY . .

# Build arguments
ARG VITE_BASE_URL=/
ARG VITE_API_URL=/api
ARG VITE_APP_NAME="Sauti 116 helpline"
ARG VITE_HOTLINE=116
ARG VITE_WHATSAPP="+256743889999"
ARG VITE_EMAIL="info@sauti.mglsd.go.ug"

ENV VITE_BASE_URL=${VITE_BASE_URL}
ENV VITE_API_URL=${VITE_API_URL}
ENV VITE_APP_NAME=${VITE_APP_NAME}
ENV VITE_HOTLINE=${VITE_HOTLINE}
ENV VITE_WHATSAPP=${VITE_WHATSAPP}
ENV VITE_EMAIL=${VITE_EMAIL}

# Build
RUN npm run build

# Production stage
FROM nginx:1.25-alpine

# Create sub-directory for /sauti/ path
RUN mkdir -p /usr/share/nginx/html/sauti

# Copy built files into the sub-directory
COPY --from=build-stage /app/dist /usr/share/nginx/html/sauti

# Copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Healthcheck support
RUN apk add --no-cache curl

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
