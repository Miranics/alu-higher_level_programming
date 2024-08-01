#!/usr/bin/python3
"""
This module fetches the status from https://alu-intranet.hbtn.io/status
using the requests package and displays the response body details.
"""

import requests

def fetch_status():
    """Fetches the status from the specified URL and prints the response details."""
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")

if __name__ == "__main__":
    fetch_status()
