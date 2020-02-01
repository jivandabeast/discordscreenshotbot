#!/bin/bash

xdotool key  --clearmodifiers --delay 40 "super+1" 

# Uncomment this line and comment the other to change the script to continuously open new tabs instead of using the same one
#xdotool key --clearmodifiers --delay 40 "ctrl+t"
xdotool key --clearmodifiers --delay 40 "F6"

xdotool type --clearmodifiers --delay 40 "$1"
xdotool key --clearmodifiers --delay 40 "Return"
xdotool key  --clearmodifiers --delay 40 "ctrl+shift+k" 
sleep 5
xdotool type  --clearmodifiers --delay 40 ":screenshot screenshot --fullpage" 
xdotool key --clearmodifiers --delay 40 "Return"
