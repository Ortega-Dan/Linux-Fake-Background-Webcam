#! /bin/bash

# only for usage at Dan Ortega's environments (adjust if interested)

sudo modprobe v4l2loopback devices=1 exclusive_caps=1 card_label="fake-cam"

camera=$(python3 myrunner-2.py)

if [ $camera == "NONE" ]; then
    echo "Unable to find camera 4. Make sure it is plugged in"
else
    python3 fake.py --no-foreground --no-background -w $camera -v /dev/video4 -W 640 -H 480
fi
