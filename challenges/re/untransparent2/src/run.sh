#!/bin/bash

python3 sourceGen.py "grey{y0u_aR3_a_Pr0fe551on4l}"
./bin/clang-4.0 -mllvm -bcf -mllvm -sub -mllvm -fla -mllvm -split -s -o pain pain.c
cat flag.txt | ./pain

