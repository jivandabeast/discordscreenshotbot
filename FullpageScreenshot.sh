#!/bin/bash

xdotool key  --clearmodifiers --delay 40 "super+1" 
xdotool key --clearmodifiers --delay 40 "ctrl+t"
xdotool type --clearmodifiers --delay 40 "$1"
xdotool key --clearmodifiers --delay 40 "Return"
xdotool key  --clearmodifiers --delay 40 "ctrl+shift+k" 
sleep 5
xdotool type  --clearmodifiers --delay 40 ":screenshot screenshot --fullpage" 
xdotool key --clearmodifiers --delay 40 "Return"
