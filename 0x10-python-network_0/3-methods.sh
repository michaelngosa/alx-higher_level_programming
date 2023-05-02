#!/bin/bash
#script that takes in URL and displays all HTTP methods the server will accept
curl -sIL -X OPTIONS "$1" | grep -i Allow |awk -F ": " '{print $2}'
