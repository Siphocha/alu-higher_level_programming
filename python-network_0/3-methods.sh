#!/bin/bash
#Takes HTTP Post request and displays HTTP methods server will accept.
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut  -c 2- | rev
