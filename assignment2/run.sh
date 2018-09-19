#!/bin/sh
for i in ./test_files/*
do
    python3 pluck.py $i
done
