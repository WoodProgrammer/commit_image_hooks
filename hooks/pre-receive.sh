#!/bin/bash
echo "Adding CURRENT_PATH"

CURRENT_PATH=$(pwd)
echo $CURRENT_PATH | awk'{split($0,a,"/");}' 


docker build ../../ 
OUT=$?

if [ OUT -eq 0 ]; then
    echo "Dockerfile Building error"
else
    VERSION_NUMBER=$(awk -F= '/VERSION_NUMBER/ { print $2 }' ferruh)
    TAG_NAME=$(awk -F= '/TAG_NAME/ { print $2 }' ferruh)

fi


