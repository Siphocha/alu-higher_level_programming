#!/bin/bash
#Takes URL as argument & pushes GET request with more info inbeded.
curl -s -H "X-HolbertonSchool-User-Id":98 "$1"
