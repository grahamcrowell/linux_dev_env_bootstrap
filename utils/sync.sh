#!/bin/bash

SOURCE=$1
DEST=$2
REGEX=$3

echo $1
echo $2
echo $3

# ls -pl /media/usb/Video --format=single-column | grep -e "^[A|B].*" | grep -e ".*/" -v

for i in $( ls -pl /media/usb/Video --format=single-column | grep -e "^[A|B].*" | grep -e ".*/" -v ); do
    echo item: $i
done