#!/usr/bin/python3
"""
This module fetches the status from https://alu-intranet.hbtn.io/status
using urllib, and displays the response body.
"""

import urllib.request

def fetch_status():
    """Fetches the status from the given URL and prints the response details."""
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
