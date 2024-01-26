#!/bin/bash
# cURL a JSON file
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
