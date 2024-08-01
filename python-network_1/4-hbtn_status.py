#!/usr/bin/python3
"""
Fetch https://intranet.hbtn.io/status and display the response.

This module uses the requests library to send an HTTP GET request to the
specified URL, retrieves the response, and prints the details about the
response body, including its type and content.
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
