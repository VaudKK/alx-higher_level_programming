#!/bin/bash
# Methods accepted
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
