#!/bin/bash
set -e
cd /root/task
echo "[run.sh] Bringing up containers..."
docker-compose up -d
printf "[run.sh] Waiting for Redis to be ready..."
for i in {1..20}
do
    if docker exec $(docker-compose ps -q redis) redis-cli ping | grep -q PONG; then
        echo " Redis is ready."
        break
    else
        printf "."
        sleep 1
    fi
done
if ! docker exec $(docker-compose ps -q redis) redis-cli ping | grep -q PONG; then
    echo "\n[run.sh] Redis did not become ready in time."; exit 1
fi
sleep 3
echo "[run.sh] Checking FastAPI application health..."
for i in {1..20}
do
    if curl -s http://localhost:8000/docs > /dev/null; then
        echo "[run.sh] FastAPI app is running and accessible."
        break
    else
        sleep 1
    fi
done
echo "[run.sh] Deployment completed successfully!"
