#!/bin/bash
set -e
echo "Stopping containers..."
docker-compose -f /root/task/docker-compose.yml down --volumes --remove-orphans || true
echo "Removing Docker system unused resources..."
docker system prune -a --volumes -f
echo "Removing application and Redis images if exist..."
docker rmi -f $(docker images -q | grep -E 'docker_image_name|redis:7-alpine' || true) || true
echo "Deleting /root/task directory..."
rm -rf /root/task
find /root/task -type d -name "__pycache__" -exec rm -rf {} + || true
echo "Cleanup completed successfully! Droplet is now clean."
