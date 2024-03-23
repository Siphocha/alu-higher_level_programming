#!/usr/bin/python3
"""Takes POST request of email and takes parameters to make into text for displaying."""
import requests
import sys

if __name__ == "__main__":
    i = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print("{}".format(i.text))