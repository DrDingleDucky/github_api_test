from pprint import pprint

import requests

# Your personal access token.
token = "YOUR_PERSONAL_ACCESS_TOKEN"

# Repository Settings
name = "Test_Repository_1"
description = "This repository was created with an API call."
include_all_branches = False
private = False

# Set the API endpoint URL.
url = "https://api.github.com/user/repos"

# Set the headers for authenticated requests.
headers = {
    "Authorization": f"Bearer {token}"
}

# Set the request data.
data = {
    "name": name,
    "description": description,
    "include_all_branches": include_all_branches,
    "private": private
}

# Send the PATCH request.
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(f"Authentication successful! - {response}")
else:
    print(f"Authentication failed. - {response}")

pprint(response.json())
