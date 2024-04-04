#!/usr/bin/python3
"""Script that takes in URL then sends request back.
This is so it can display the URL response on the page."""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read()
            print("{}".format(html.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
