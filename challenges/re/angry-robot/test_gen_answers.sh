#!/bin/sh

mkdir -p answers/bin/
for file in `ls bin/`
do
    python3 solve.py bin/$file
done
