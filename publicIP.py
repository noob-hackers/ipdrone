#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In case if you want to know your public IP address use this script
usage: python publicIP.py
or: python3 publicIP.py
"""

import requests, json

API = "https://api.ipify.org/?format=json"

IP = requests.get(API).json()['ip']

print("[+] Your public IP Address is:", IP)