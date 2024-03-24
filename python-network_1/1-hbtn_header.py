#!/usr/bin/python3
"""Takes URL (post) sends request back to display value "x-request-id"""
import sys
import requests

if __name__ == '__main__':
    reqs = requests.get(sys.argv[1])
    print(reqs.headers.get("X-Request-Id"))