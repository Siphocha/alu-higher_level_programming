#!/usr/bin/python3
""" Takes a letter and sends  POST request to
    https://0.0.0.0:5000/search_user the letter is the  parameter
    letter is variable q.
    displays [<id>]<name> if repsonse is properly JSON formatted"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}

    i = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        i_json = i.json()
        if i_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(i_json['id'], i_json['name']))
    except ValueError:
        print("Not a valid JSON")