#!/bin/bash
#Getting byte sizes of HTTP response header for website
curl -s "$1" | wc -c
