#!/bin/bash

gcc -static -O3 -m32 -no-pie -o sus sus.c rc4.c
strip -s sus
upx -9 sus
cp sus distrib/