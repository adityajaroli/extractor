#!/bin/sh

# Go to the location of docker-compose.yml
cd ./tests/component

# If containers are already running, dispose them
docker-compose down --volumes

# Build the images which are needed to be built in docker-compose file
docker-compose build

# Start containers only if build was successful
if [ $? -eq 0 ]; then
  # start containers in the detached mode
  docker-compose up -d

  # print logs of component test container
  docker-compose logs -f component-test-service
fi

# Dispose all the containers
docker-compose down --volumes