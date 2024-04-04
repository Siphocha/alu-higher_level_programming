#!/usr/bin/python3
"""Script takes URL and if itsall good prints URL page."""

import requests
import sys

if __name__ == "__main__":
    i = requests.get(sys.argv[1])
    if i.status_code >= 400:
        print("Error code: {}".format(i.status_code))
    else:
        print("{}".format(i.text))
