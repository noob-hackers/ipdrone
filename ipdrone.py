#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coded by N17RO (noob hackers)

# modules required
import argparse
import requests, json
import sys
from sys import argv
import os

from utils import API
from utils import printA, printB, printBanner


# arguments and parser
parser = argparse.ArgumentParser()
parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )
args = parser.parse_args()
ip = args.target


# banner
printBanner()

try:
        data = requests.get(API+ip).json()
        sys.stdout.flush()

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
        print('Terminating, Bye'+LGREEN)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print(RED+"[~]"+" check your internet connection!"+CLEAR)
        
sys.exit(1)
