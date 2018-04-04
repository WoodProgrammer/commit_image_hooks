#!/bin/bash
echo "Adding CURRENT_PATH"

CURRENT_PATH=$(pwd)
REGISTRY_URL=$(echo $FERRUH_DOCKER_REGISTRY)
VERSION_NUMBER=$(awk -F= '/VERSION_NUMBER/ { print $2 }' ../..)
TAG_NAME=$(awk -F= '/TAG_NAME/ { print $2 }' ../../)

echo $CURRENT_PATH | awk'{split($0,a,"/");}' 


docker build -t  $TAG_NAME:$VERSION_NUMBER test/.
OUT=$?


if [ OUT -eq 0 ]; then
    echo "Dockerfile Building error"
else

    docker tag $TAG_NAME:$VERSION_NUMBER $REGISTRY_URL/$TAG_NAME:$VERSION_NUMBER
    docker push $REGISTRY_URL/$TAG_NAME:$VERSION_NUMBER
fi


