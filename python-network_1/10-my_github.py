#!/usr/bin/python3
"""This script takes Github credentials (username&password).
Then uses GITHUB's API to display your Id for you."""

import sys
import requests
from requests.auth import HTTPBasicAuth 

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    i = requests.get("https://api.github.com/user", auth=auth)
    print(i.json().get("id"))