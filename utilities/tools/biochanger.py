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
from utilities.core.shrek_ui import set_console_title
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
    set_console_title('Bio Changer | Shrek Multi Tools')  
    
    print(f'''
    {Fore.GREEN}
      ▄▄▄▄     ██ ▒█████       ▄████▄   ██░ ██  ▄▄▄      ███▄    █    ▄████ ▓█████ ██▀███  
     ▓█████▄ ▒▓██▒██▒  ██▒    ▒██▀ ▀█ ▒▓██░ ██ ▒████▄    ██ ▀█   █ ▒ ██▒ ▀█▒▓█   ▀▓██ ▒ ██▒
     ▒██▒ ▄██░▒██▒██░  ██▒    ▒▓█    ▄░▒██▀▀██ ▒██  ▀█▄ ▓██  ▀█ ██▒░▒██░▄▄▄░▒███  ▓██ ░▄█ ▒
     ▒██░█▀   ░██▒██   ██░    ▒▓▓▄ ▄██ ░▓█ ░██ ░██▄▄▄▄██▓██▒  ▐▌██▒░░▓█  ██▓▒▓█  ▄▒██▀▀█▄  
    ▒░▓█  ▀█▓ ░██░ ████▓▒░    ▒ ▓███▀  ░▓█▒░██▓ ▓█   ▓██▒██░   ▓██░░▒▓███▀▒░░▒████░██▓ ▒██▒
    ░░▒▓███▀▒ ░▓ ░ ▒░▒░▒░     ░ ░▒ ▒    ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒░   ▒ ▒  ░▒   ▒  ░░ ▒░ ░ ▒▓ ░▒▓░
    ░▒░▒   ░   ▒   ░ ▒ ▒░       ░  ▒    ▒ ░▒░ ░  ░   ▒▒ ░ ░░   ░ ▒░  ░   ░   ░ ░    ░▒ ░ ▒░
      ░    ░   ▒ ░ ░ ░ ▒      ░         ░  ░░ ░  ░   ▒     ░   ░ ░ ░ ░   ░ ░   ░     ░   ░ 
    ░ ░        ░     ░ ░      ░ ░       ░  ░  ░      ░           ░       ░     ░     ░
    ''')
    print()
    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Custom bio')
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Random bio')
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Shrek bio')
    print(f'    {Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] {Fore.WHITE}Quit')
    print()
    
    choice = input_prompt('Choice')
    
    if choice == '0':
        return_to_menu()
        return

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

    url = 'https://discord.com/api/v9/users/@me'

    # ---- OPTION 1 : CUSTOM BIO ----
    if choice in ['01', '1']:
        bio = input_prompt('What do you want the bio to say?')
        if not bio:
            warn('Bio cannot be empty!')
            time.sleep(1)
            run()
            return
        payload = {'bio': bio}
        info(f'Changing bio for {len(tokens)} tokens...')
        
        for token in tokens:
            try:
                headers = {
                    "Authorization": token,
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",
                    "Content-Type": "application/json"
                }
                r = requests.patch(url, headers=headers, json=payload)
                if r.status_code == 200 or r.status_code == 204:
                    success(f'Bio changed for {token[:20]}...')
                else:
                    warn(f'Error for {token[:20]}...: {r.status_code}')
            except Exception as e:
                warn(f'Error: {e}')
            time.sleep(0.5)

    # ---- OPTION 2 : RANDOM BIO ----
    elif choice in ['02', '2']:
        bio_file = input_prompt('File with bios (must be in the same folder)')
        if not os.path.exists(bio_file):
            warn(f'File "{bio_file}" not found!')
            time.sleep(1)
            run()
            return
        
        with open(bio_file, 'r', encoding='utf-8') as f:
            bios = [line.strip() for line in f if line.strip()]
        
        if not bios:
            warn('No bios found in file!')
            time.sleep(1)
            run()
            return
        
        payload = {'bio': random.choice(bios)}
        info(f'Changing bio for {len(tokens)} tokens...')
        
        for token in tokens:
            try:
                headers = {
                    "Authorization": token,
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",
                    "Content-Type": "application/json"
                }
                r = requests.patch(url, headers=headers, json=payload)
                if r.status_code == 200 or r.status_code == 204:
                    success(f'Bio changed for {token[:20]}...')
                else:
                    warn(f'Error for {token[:20]}...: {r.status_code}')
            except Exception as e:
                warn(f'Error: {e}')
            time.sleep(0.5)

    # ---- OPTION 3 : SHREK BIO ----
    elif choice in ['03', '3']:
        payload = {'bio': 'NUKED BY Shrek Multi Tool'}
        info(f'Changing bio to Shrek bio for {len(tokens)} tokens...')
        
        for token in tokens:
            try:
                headers = {
                    "Authorization": token,
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",
                    "Content-Type": "application/json"
                }
                r = requests.patch(url, headers=headers, json=payload)
                if r.status_code == 200 or r.status_code == 204:
                    success(f'Bio changed for {token[:20]}...')
                else:
                    warn(f'Error for {token[:20]}...: {r.status_code}')
            except Exception as e:
                warn(f'Error: {e}')
            time.sleep(0.5)

    else:
        warn('Invalid option')
        time.sleep(1)
        run()
        return

    info('All tokens processed!')
    time.sleep(1)
    return_to_menu()

if __name__ == '__main__':
    run()