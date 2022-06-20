#!/bin/bash

./buildtools/bin/clang -mllvm -mba -mllvm -mba-prob=100 -mllvm -gle -o mba mba.c
FLAG=`cat flag.txt` PASS=`cat password.txt` ./mba
