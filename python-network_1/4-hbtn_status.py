#!/usr/bin/python3
"""
Fetch https://intranet.hbtn.io/status and display the response.

This script uses the requests library to perform an HTTP GET request
to the specified URL, and prints the response details, including the
type and content of the response body.
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
