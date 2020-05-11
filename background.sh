#!/bin/bash

# Simple Bash Script For Multiple Requests In The Background

for i in {1..10}
do
   python3 request.py &
done
