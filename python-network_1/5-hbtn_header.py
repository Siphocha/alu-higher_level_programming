#!/usr/bin/python3
"""Takes URL, sends request back to it asking to display
value of variable X-Request-Id"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    i = requests.get(url)
    print(i.headers.get("X-Request-Id"))