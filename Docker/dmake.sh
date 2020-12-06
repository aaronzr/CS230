#!/bin/bash
# Docker "Makefile"
docker build -t test .
docker run -v $PWD/src/:/workspace/ -it test
