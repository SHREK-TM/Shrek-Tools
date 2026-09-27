# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import os
import sys
import time
import json
import random
import string
import ctypes
import base64
import shutil
import subprocess
import threading
import webbrowser
from json import loads, dumps
from time import sleep
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from socket import socket, AF_INET, SOCK_DGRAM
from urllib.request import urlopen, Request
from re import findall

import requests
import colorama
import discum
import pyautogui
import keyboard
import websocket
from colorama import Fore, Back, Style
from discord.ext import commands
import discord
from websocket import WebSocket

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.common import *
from utilities.core.context import get_user_name, set_user_name, yeslist, nolist, return_to_menu
from utilities.core.helpers import randstr, useragent, mainHeader, secondHeader
from utilities.core.paths import TOKENS_FILE

# ---- Style Functions ----
def success(text):
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def info(text):
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def warn(text):
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def input_prompt(prompt):
    return input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} {prompt}: {Style.RESET_ALL}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def run():
    clear_screen()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Friend Spammer")
    
    print(f'''
       {Fore.GREEN}
     ▓█████ ██▀███  ▓█████  ██ ███▄    █  ▓█████▄       ██████  ██▓███   ▄▄▄       ███▄ ▄███▓  ███▄ ▄███▓▓█████ ██▀███  
    ▒██    ▓██ ▒ ██▒▓█   ▀▒▓██ ██ ▀█   █  ▒██▀ ██▌    ▒██    ▒ ▓██░  ██ ▒████▄    ▓██▒▀█▀ ██▒ ▓██▒▀█▀ ██▒▓█   ▀▓██ ▒ ██
    ▒████  ▓██ ░▄█ ▒▒███  ░▒██▓██  ▀█ ██▒ ░██   █▌    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░ ▓██    ▓██░▒███  ▓██ ░▄█ 
    ░▓█▒   ▒██▀▀█▄  ▒▓█  ▄ ░██▓██▒  ▐▌██▒▒░▓█▄   ▌      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██  ▒██    ▒██ ▒▓█  ▄▒██▀▀█▄  
    ░▒█░   ░██▓ ▒██▒░▒████ ░██▒██░   ▓██░░░▒████▓     ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒▒██▒   ░██▒░▒████░██▓ ▒██
     ▒ ░   ░ ▒▓ ░▒▓░░░ ▒░  ░▓ ░ ▒░   ▒ ▒ ░ ▒▒▓  ▒     ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░   ░  ░░░ ▒░ ░ ▒▓ ░▒▓
     ░       ░▒ ░ ▒░ ░ ░    ▒ ░ ░░   ░ ▒░  ░ ▒  ▒     ░ ░▒  ░  ░▒ ░       ░   ▒▒ ░░  ░      ░░░  ░      ░ ░ ░    ░▒ ░ ▒
     ░ ░      ░   ░    ░    ▒    ░   ░ ░   ░ ░  ░     ░  ░  ░  ░░         ░   ▒   ░      ░    ░      ░      ░     ░   ░ 
              ░        ░    ░          ░     ░              ░                 ░  ░       ░   ░       ░      ░     ░     

    ''')
    
    # ---- Vérifier tokens.txt ----
    token_file = TOKENS_FILE
    if not os.path.exists(token_file):
        warn(f'tokens.txt not found at {token_file}!')
        time.sleep(1)
        run()
        return

    with open(token_file, 'r') as f:
        tokens = [line.strip() for line in f if line.strip()]

    if not tokens:
        warn('No tokens found in tokens.txt!')
        time.sleep(1)
        run()
        return

    # ---- Input ----
    discord_input = input_prompt("Discord name + numbers (e.g., Name#1234)")
    if not discord_input:
        warn('Input cannot be empty!')
        time.sleep(1)
        run()
        return

    try:
        name, num = discord_input.split('#')
        if not name or not num:
            raise ValueError
    except ValueError:
        warn('Invalid format! Use Name#1234')
        time.sleep(1)
        run()
        return

    info(f'Adding friend for {len(tokens)} tokens...')
    url = 'https://discord.com/api/v9/users/@me/relationships'

    for token in tokens:
        try:
            headers = {
                "Authorization": token,
                "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
                "Content-Type": "application/json"
            }
            payload = {"username": name, "discriminator": num}
            r = requests.post(url, headers=headers, json=payload)
            
            if r.status_code == 204 or r.status_code == 200:
                success(f'Friend request sent for {token[:20]}...')
            else:
                warn(f'Error for {token[:20]}...: {r.status_code}')
        except Exception as e:
            warn(f'Error: {e}')
        time.sleep(0.5)

    info('All friend requests sent!')
    time.sleep(3)
    return_to_menu()

if __name__ == '__main__':
    run()