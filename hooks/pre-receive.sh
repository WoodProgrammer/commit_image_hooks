#!/bin/bash

CURRENT_PATH=$(pwd)
echo $CURRENT_PATH | awk'{split($0,a,"/");}' 

#!/bin/bash

docker build ../../ 
OUT=$?

if [ OUT -eq 0 ]; then
    echo "Dockerfile Building error"
else
    last_image_id=cat data |grep built | awk '{split($0,a," "); print a[3]}'

fi