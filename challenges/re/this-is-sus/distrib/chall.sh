#!/bin/bash

./sus

ret=$?
if [ $ret -ne 0 ]; then
    echo "That's not what I want to hear!"
else
    echo "You have a beautiful voice! :'D"
fi
