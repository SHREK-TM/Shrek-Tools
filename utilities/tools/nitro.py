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
     ███▄    █   ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████  ▓█████ ███▄    █ 
     ██ ▀█   █ ▒▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒     ██▒ ▀█ ▓█   ▀ ██ ▀█   █ 
    ▓██  ▀█ ██▒▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒    ▒██░▄▄▄ ▒███  ▓██  ▀█ ██▒
    ▓██▒  ▐▌██▒░░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░    ░▓█  ██ ▒▓█  ▄▓██▒  ▐▌██▒
    ▒██░   ▓██░░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░    ▒▓███▀▒▒░▒████▒██░   ▓██░
    ░ ▒░   ▒ ▒  ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░░ ▒░ ░ ▒░   ▒ ▒ 
    ░ ░░   ░ ▒░░ ▒ ░    ░      ░▒ ░ ▒   ░ ▒ ▒░      ░   ░ ░ ░ ░  ░ ░░   ░ ▒░
       ░   ░ ░ ░ ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░   ░     ░     ░   ░ ░ 
             ░   ░              ░         ░ ░           ░ ░   ░           ░ 
"""

def run():
    clear_screen()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Nitro Generator")
    print(BANNER)
    print()
    
    webhooklink = input_prompt('Webhook URL')
    if not webhooklink:
        warn("Webhook URL cannot be empty!")
        time.sleep(1)
        return_to_menu()
        return
    
    info("Starting Nitro generator... Press Ctrl+C to stop")
    print()
    
    count = 0
    
    def generate_nitro():
        nonlocal count
        while True:
            try:
                code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
                nitro_link = f"https://discord.com/billing/promotions/{code}"
                
                post = {"content": nitro_link}
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    'content-type': 'application/json'
                }
                
                count += 1
                success(f'Generated Nitro | [{count}] - {nitro_link}')
                
                r = requests.post(webhooklink, json=post, headers=headers)
                if r.status_code != 204:
                    warn(f"Error sending to webhook: {r.status_code}")
                
                time.sleep(0.5)  # Petit délai pour éviter le rate-limit
                
            except KeyboardInterrupt:
                info("Stopped by user")
                break
            except Exception as e:
                warn(f"Error: {e}")
                time.sleep(1)
                break
    
    try:
        generate_nitro()
    except KeyboardInterrupt:
        info("Stopped by user")
    finally:
        print()
        info(f"Total nitro codes generated: {count}")
        time.sleep(3)
        return_to_menu()

if __name__ == '__main__':
    run()