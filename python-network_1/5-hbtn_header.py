#!/usr/bin/python3
"""Takes URL, sends request back to it asking to display
value of variable X-Request-Id"""

import requests
import sys

if __name__ == "__main__":
    i = requests.get(sys.argv[1])
    print("{}".format(i.headers["X-Request-Id"]))