# utilities for ipdrone.py (helper functions and constants)

import sys

# URL of the API
API = "http://ip-api.com/json/"

# colors
RED = '\033[31m'
YELLOW = '\033[93m'
LGREEN = '\033[92m'
CLEAR = '\033[0m'
BOLD = '\033[01m'
CYAN = '\033[96m'
WHITE = "\u001b[37m"

# banner
def printBanner():
    print(f"""
{RED}
██╗██████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗███████╗
██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║██████╔╝██║  ██║██████╔╝██║   ██║██╔██╗ ██║█████╗  
██║██╔═══╝ ██║  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══╝  
██║██║     ██████╔╝██║  ██║╚██████╔╝██║ ╚████║███████╗
╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                      v 1.0
{RED}
{LGREEN+BOLD}
            <===[[ coded by N17RO ]]===>
{CLEAR}
{YELLOW+BOLD}
    <---(( search on youtube Noob Hackers ))-->
{CLEAR}
        """)

def printA(*text):
    print(LGREEN + BOLD+ "[$]", *text)
    print(RED + "<--------------->" + RED)

def printB(*text):
    print(CYAN + BOLD + "[$]", *text)
    print(RED + "<--------------->" + RED)

def flush():
    sys.stdout.flush()