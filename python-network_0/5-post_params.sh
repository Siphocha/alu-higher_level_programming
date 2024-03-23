#!/bin/bash
#POST DELETE request to URL passed then display RESPONSE from server
curl -s -X "POST" "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"