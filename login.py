from re import S
import requests
import os
import subprocess
import sys
import getpass
import json

usr = input('Enter your username: ')
print('Username: ', usr)
pwd = getpass.getpass(prompt = 'Enter your password: ', stream = None)

def get_token():
    url = 'https://10.10.20.14/api/aaaLogin.json'

    payload = {
        'aaaUser': {
            'attributes': {
                'name':'%s' % usr,
                'pwd':'%s' % pwd
            }
        }
    }

    headers = {
        'Content-Type' : 'application/json'
    }

    requests.packages.urllib3.disable_warnings()
    response = requests.post(url, data = json.dumps(payload), headers = headers, verify = False).json()

    token = response['imdata'][0]['aaaLogin']['attributes']['token']
    return token

def main():
    token = get_token()
    print('The token is:', token)

if __name__ == '__main__':
    main()