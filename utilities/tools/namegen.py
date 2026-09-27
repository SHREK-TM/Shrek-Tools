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

BANNER = f"""
{Fore.GREEN}
     ███▄    █  ▄▄▄      ███▄ ▄███▓ ▓█████       ▄████  ▓█████ ███▄    █ 
     ██ ▀█   █ ▒████▄   ▓██▒▀█▀ ██▒ ▓█   ▀    ▒ ██▒ ▀█▒ ▓█   ▀ ██ ▀█   █ 
    ▓██  ▀█ ██▒▒██  ▀█▄ ▓██    ▓██░ ▒███      ░▒██░▄▄▄░ ▒███  ▓██  ▀█ ██▒
    ▓██▒  ▐▌██▒░██▄▄▄▄██▒██    ▒██  ▒▓█  ▄    ░░▓█  ██▓ ▒▓█  ▄▓██▒  ▐▌██▒
    ▒██░   ▓██░▒▓█   ▓██▒██▒   ░██▒▒░▒████    ░▒▓███▀▒░▒░▒████▒██░   ▓██░
    ░ ▒░   ▒ ▒ ░▒▒   ▓▒█░ ▒░   ░  ░░░░ ▒░      ░▒   ▒  ░░░ ▒░ ░ ▒░   ▒ ▒ 
    ░ ░░   ░ ▒░░ ░   ▒▒ ░  ░      ░░ ░ ░        ░   ░  ░ ░ ░  ░ ░░   ░ ▒░
       ░   ░ ░   ░   ▒  ░      ░       ░      ░ ░   ░ ░    ░     ░   ░ ░ 
             ░       ░         ░   ░   ░            ░  ░   ░           ░ 

"""

def run():
    clear_screen()
    set_console_title('Name Generator | Shrek Multi Tools')
    print(BANNER)
    print()

    try:
        howmanynames = int(input_prompt('How many names do you want? (max 200)'))
    except ValueError:
        warn("Please enter a valid number!")
        time.sleep(1)
        return_to_menu()
        return

    if howmanynames > 200:
        warn('Maximum amount of names is 200!')
        time.sleep(1)
        return_to_menu()
        return

    if howmanynames < 1:
        warn('Minimum amount of names is 1!')
        time.sleep(1)
        return_to_menu()
        return

    num1 = howmanynames / 2

    def getnames(urll):
        try:
            r = requests.get(urll, timeout=10)
            if r.status_code != 200:
                warn(f"API error: {r.status_code}")
                return
            data = r.json().get('data', [])
            if not data:
                warn("No names returned from API")
                return
            names = [value['name'] for value in data]
            
            names_file = os.path.join(root_path, 'output', 'names.txt')
            with open(names_file, 'a', encoding='utf-8') as name:
                for line in names:
                    name.write(line + '\n')
        except requests.exceptions.Timeout:
            warn("API timeout, please try again")
        except Exception as e:
            warn(f"Error fetching names: {e}")

    getnames(f'https://story-shack-cdn-v2.glitch.me/generators/username-generator?count={num1}')
    getnames(f'https://story-shack-cdn-v2.glitch.me/generators/gamertag-generator?count={num1}')

    success(f'Done! Added {howmanynames} names to names.txt')
    names_file = os.path.join(root_path, 'output', 'names.txt')
    info(f'File saved: {names_file}')
    time.sleep(3)
    return_to_menu()

if __name__ == '__main__':
    run()