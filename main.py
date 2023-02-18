from pprint import pprint

import requests

token = "your_personal_access_token"

repo_name = "Test-Repository-1"
repo_description = "This repository was created with an API call."
include_all_branches = False
private = False

url = "https://api.github.com/user/repos"

headers = {
    "Authorization": f"Bearer {token}"
}

data = {
    "name": repo_name,
    "description": repo_description,
    "include_all_branches": include_all_branches,
    "private": private
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(f"Authentication successful! - {response}")
else:
    print(f"Authentication failed. - {response}")

pprint(response.json())
