#!/usr/bin/env python
# -*- coding: utf-8 -*-

# NOTE: if you don't know your public ip use the publicIP.py script

# coded by N17RO (noob hackers)

# modules required
import argparse
import requests, json
from sys import argv

from utils import *

# arguments and parser
parser = argparse.ArgumentParser()
parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )
args = parser.parse_args()
ip = args.target


# banner
printBanner()

try:
        data = requests.get(API+ip).json()
        flush()

        printA("[Victim]:", data['query'])
        printB("[ISP]:", data['isp'])
        printA("[Organisation]:", data['org'])
        printB("[City]:", data['city'])
        printA("[Region]:", data['region'])
        printB("[Longitude]:", data['lon'])
        printA("[Latitude]:", data['lat'])
        printB("[Time zone]:", data['timezone'])
        printA("[Zip code]:", data['zip'])

except KeyboardInterrupt:
        terminate()

except requests.exceptions.ConnectionError as e:
        error()
