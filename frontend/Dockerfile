# Use nginx as base image
FROM nginx:alpine

# Copy your HTML into Nginx's default static file directory
COPY index.html /usr/share/nginx/html/index.html

# Nginx automatically serves from /usr/share/nginx/html
EXPOSE 80