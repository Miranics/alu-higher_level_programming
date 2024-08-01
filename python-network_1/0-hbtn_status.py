#!/usr/bin/python3

import urllib.request

# The URL to fetch the status from
url = 'https://alu-intranet.hbtn.io/status'

# Open the URL and fetch the response using a with statement
with urllib.request.urlopen(url) as response:
    # Read the response body as bytes
    body = response.read()
    # Decode the body to a UTF-8 string
    utf8_content = body.decode('utf-8')

# Display the response body information
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {utf8_content}")
