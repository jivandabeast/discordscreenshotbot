#!/bin/bash

xdotool key  --clearmodifiers --delay 40 "super+1" 
xdotool key  --clearmodifiers --delay 40 "ctrl+shift+k" 
sleep 2
xdotool type  --clearmodifiers --delay 40 ":screenshot --fullpage" 
xdotool key --clearmodifiers --delay 40 "Return"
