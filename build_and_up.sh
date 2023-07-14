#!/bin/bash

echo "Building containers..."
docker-compose build
echo "Build successful!"
docker-compose up -d
echo "Up successful!"
