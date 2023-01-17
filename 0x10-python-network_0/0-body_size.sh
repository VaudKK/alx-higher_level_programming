#!/bin/bash
# Get body size
curl -sIL "$1" | grep "Content-Length:" | cut -d' ' -f 2
