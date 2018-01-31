#!/bin/bash
echo "Enter Registry URL ::: "
read registry_url

if [ "$registry_url" = "" ]; then 

    echo "Docker Hub"
    export FERRUH_DOCKER_REGISTRY='docker_hub'
    data=$(docker --version)
    echo $data
    echo "Docker Login"
    docker login
    OUT=$?

    if [ OUT -eq 0 ]; then
        echo "You logged to the Docker ! "
        
    else
        echo "Login ERROR! "
        docker login
    fi
else
    export FERRUH_DOCKER_REGISTRY="$registry_url"

fi;


