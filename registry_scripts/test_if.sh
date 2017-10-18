#!/bin/bash 
port_control=$(lsof -i tcp:5000)

if [ "$port_control" = "" ]; then 
    echo "Port is open for create registry ... " 
else
    echo "using another port registry "  
fi;
