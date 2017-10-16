#!/bin/bash

default_registry_port=5000
registry_name=$1
echo "Docker version Controlling.. "
echo 'DockerVersion :' $(docker --version)

echo "Registry Setup is Starting"

port_control=$(lsof -i tcp:5000)

if [ "$port_control" = "" ]; then
    echo "Port is open for create registry ... "

    $(docker run -d -p 5000:5000 --name $registry_name registry:2 2>> registry_setup_error) 

    echo "For error log registry_setup_error."

 
else
    echo "using another port registry "
fi;



