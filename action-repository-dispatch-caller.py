#!/usr/bin/python3
# usage: python action-repository-dispatch-caller.py
# action-repository-dispatch-caller.py action repository dispatch caller
###############################################################################

import requests
import os
import json

def main():
    org_name = os.environ.get("ORG_NAME")
    repo_name = os.environ.get("REPO_NAME")
    github_token = os.environ.get("GITHUB_TOKEN")
    event = os.environ.get("EVENT")
    github_ref = os.environ.get("GITHUB_REF")
    github_sha = os.environ.get("GITHUB_SHA")
    version = os.environ.get("VERSION")

    url = "https://api.github.com/repos/" + org_name + "/" + repo_name + "/dispatches"
    print(url)

    payload = {
        "event_type": event,
        "client_payload": {
            "version": version,
            "ref": github_ref,
            "sha": github_sha,
        }
    }

    headers = {
      "Accept": "application/vnd.github.v3+json",
      "Authorization": f"token {github_token}" ,
    }

    response = requests.post(url=url, json=payload, headers=headers)
    print(response)
main()

