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
from utilities.core.paths import GROUPS_FILE

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
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Group Spammer")
    
    print(f"""
    {Fore.GREEN}
     ▄████  ██▀███   ▒█████   █    ██  ██▓███        ██████  ██▓███   ▄▄▄      ███▄ ▄███▓ ███▄ ▄███▓ ▓█████ ██▀███  
     ██▒ ▀█▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓██░  ██     ▒██    ▒ ▓██░  ██ ▒████▄   ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒ ▓█   ▀▓██ ▒ ██▒
    ▒██░▄▄▄▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██░ ██▓▒    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄ ▓██    ▓██░▓██    ▓██░ ▒███  ▓██ ░▄█ ▒
    ░▓█  ██▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▒██▄█▓▒ ▒      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██▒██    ▒██ ▒██    ▒██  ▒▓█  ▄▒██▀▀█▄  
    ▒▓███▀▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██▒ ░  ░    ▒██████▒▒▒██▒ ░  ░▒▓█   ▓██▒██▒   ░██▒▒██▒   ░██▒▒░▒████░██▓ ▒██▒
    ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░▒▒   ▓▒█░ ▒░   ░  ░░ ▒░   ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
     ░   ░   ░▒ ░ ▒   ░ ▒ ▒░ ░░▒░ ░ ░ ░▒ ░         ░ ░▒  ░ ░░▒ ░     ░ ░   ▒▒ ░  ░      ░░  ░      ░░ ░ ░    ░▒ ░ ▒ 
     ░   ░   ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░ ░░           ░  ░  ░  ░░         ░   ▒  ░      ░   ░      ░       ░    ░░   ░ 
     ░    ░         ░ ░     ░                        ░                 ░         ░          ░   ░   ░     ░     
    
        """)
    
    # ---- Inputs ----
    token = input_prompt('Token')
    if not token:
        warn('Token cannot be empty!')
        time.sleep(1)
        run()
        return

    user_id = input_prompt('User ID')
    if not user_id:
        warn('User ID cannot be empty!')
        time.sleep(1)
        run()
        return

    group_name = input_prompt('Group name')
    if not group_name:
        warn('Group name cannot be empty!')
        time.sleep(1)
        run()
        return

    try:
        manygr = int(input_prompt('How many groups?'))
        if manygr <= 0:
            warn('Number of groups must be positive!')
            time.sleep(1)
            run()
            return
    except ValueError:
        warn('Please enter a valid number!')
        time.sleep(1)
        run()
        return

    os.makedirs(os.path.dirname(GROUPS_FILE), exist_ok=True)
    groups_file = GROUPS_FILE

    headers = mainHeader(token)
    info(f'Creating {manygr} groups...')

    for i in range(manygr):
        try:
            r = requests.post('https://discord.com/api/v9/users/@me/channels', 
                              headers=headers, json={"recipients": []})
            jsr = json.loads(r.content)
            group_id = jsr['id']
            time.sleep(0.5)
            
            r1 = requests.patch(f'https://discord.com/api/v9/channels/{group_id}', 
                                headers=headers, json={'name': group_name})
            if r1.status_code == 200:
                success(f'Group {i+1}/{manygr} created: {group_name}')
            
            with open(groups_file, 'a') as f:
                f.write(group_id + '\n')
                
        except Exception as e:
            if 'retry_after' in str(e):
                warn(f'RateLimited, retry after {jsr["retry_after"]} seconds')
                time.sleep(jsr.get('retry_after', 5))
            else:
                warn(f'Error creating group: {e}')
            time.sleep(1)
            continue

    # ---- Ajouter l'utilisateur aux groupes ----
    info('Adding user to groups...')
    try:
        with open(groups_file, 'r') as f:
            group_ids = [line.strip() for line in f if line.strip()]
        
        for gr_id in group_ids:
            try:
                r2 = requests.put(
                    f'https://discord.com/api/v9/channels/{gr_id}/recipients/{user_id}',
                    headers={'Authorization': token}
                )
                if r2.status_code == 204:
                    success(f'User {user_id} added to group {gr_id[:8]}...')
                else:
                    warn(f'Error adding user to {gr_id[:8]}...: {r2.status_code}')
            except Exception as e:
                warn(f'Error: {e}')
            time.sleep(0.5)
    except Exception as e:
        warn(f'Error reading groups file: {e}')

    info('All groups processed!')
    time.sleep(1)
    return_to_menu()

if __name__ == '__main__':
    run()