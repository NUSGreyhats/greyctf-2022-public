#!/bin/bash

gcc -static -O3 -m32 -no-pie -o sus sus.c rc4.c
./sus
