#!/bin/bash
#script that takes in URL as an argument sends a GET request to the URL aand displays the body of the response
curl -s -H "X-School-User-Id:98" -X GET "$1"
