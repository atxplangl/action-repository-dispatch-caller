#!/usr/bin/python3
# usage: python action-repository-dispatch-caller.py
# action-repository-dispatch-caller.py action repository dispatch caller
###############################################################################

import requests
import json
import os

def main():
    org_name = os.environ.get("ORG_NAME")
    repo_name = os.environ.get("REPO_NAME")
    github_token = os.environ.get("GITHUB_TOKEN")
    event = os.environ.get("EVENT")
    version = os.environ.get("VERSION")

    url = "https://api.github.com/repos/" + org_name + "/" + repo_name + "/dispatches"
    print(url)
    data = '{
      "event_type": event,
      "client_payload": {
          "version": version
      }
    }'
    print(data)

    headers = {
      "Accept": "application/vnd.github.v3+json",
      "Authorization": f"token {github_token}",
    }

    response = requests.post(url=url, data=data, headers=headers)
    print(response)
main()

