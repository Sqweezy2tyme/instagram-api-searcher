#!/usr/bin/env python3

import sys
import json
import requests

session = requests.Session()
session.headers.update({'User-Agent': 'Instagram 101.0.0.15.120'})

def lookup_user(username):
    payload = {'signed_body': f'SIGNATURE.{json.dumps({"q": username, "skip_recovery": "1"})}'}
    return session.post('https://i.instagram.com/api/v1/users/lookup/', data=payload).json()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)

    print(json.dumps(lookup_user(sys.argv[1]), indent=2))
