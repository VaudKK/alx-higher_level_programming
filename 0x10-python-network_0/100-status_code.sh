#!/bin/bash
# Status code the trick way
curl -o /dev/null -w '%{http_code}' -sLI "$1"
