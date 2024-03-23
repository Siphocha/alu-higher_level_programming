#!/usr/bin/python3
"""Takes URL (post) sends request back to display value "x-request-id"""
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.info()["X-Request-Idi"])