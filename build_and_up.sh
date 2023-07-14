#!/bin/bash

echo "Building containers..."
docker-cokpose build
echo "Build successful!"
docker-compose up -d
echo "Up successful!"
