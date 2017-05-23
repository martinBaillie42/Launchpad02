#!/bin/sh

if pgrep Live; then
    osascript -e 'tell application "System Events"
        set frontmost of process "Live" to true
        keystroke "q" using command down
        tell application "System Events" to keystroke (ASCII character 28) --left arrow
        tell application "System Events" to keystroke (ASCII character 28) --left arrow
        keystroke return
    end tell'
fi

while pgrep Live; do
  sleep 1
done

find . -name \*.pyc -delete

open -a 'Ableton Live 9 Lite.app'
