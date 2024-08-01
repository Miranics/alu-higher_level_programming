#!/usr/bin/python3
"""
This module defines a function to fetch and display the status of a web page.

The function fetch_status sends an HTTP GET request to the URL 'https://alu-intranet.hbtn.io/status'
using the urllib package, retrieves the response, and prints the details of the response body.
The details include the type of the response body, the content as bytes, and the UTF-8 decoded content.

Usage:
    This script should be run directly to fetch and display the status from the specified URL.
"""

import urllib.request


def fetch_status():
    """Fetches the status from the specified URL and prints the response details."""
    url = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {utf8_content}")


if __name__ == "__main__":
    fetch_status()
