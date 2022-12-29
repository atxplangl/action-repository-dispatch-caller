#!/usr/bin/python3
# usage: python action-repository-dispatch-caller.py
# action-repository-dispatch-caller.py action repository dispatch caller
###############################################################################

import requests
import json
import os

def main():
    org_name = os.environ["ORG_NAME"]
    repo_name = os.environ["REPO_NAME"]
    github_token = os.environ["GITHUB_TOKEN"]
    event = os.environ["EVENT"]
    client_payload_data = os.environ["CLIENT_PAYLOAD"]

    url = "https://api.github.com/repos/" + org_name + "/" + repo_name + "/dispatches"

    payload = {"event_type": event, "client_payload": client_payload_data}

    header = {"Accept": "application/vnd.github+json", "Authorization": "token " + github_token}
    payload = json.dumps(payload)
    response = requests.post(url=url, headers=header, json=payload)

main()

