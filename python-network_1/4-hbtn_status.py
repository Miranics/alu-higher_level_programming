#!/usr/bin/python3
"""
Fetch http://0.0.0.0:5050/status and display the response.

This module uses the requests library to send an HTTP GET request to the specified URL,
retrieves the response, and prints the details about the response body, including its type
and content.
"""

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
