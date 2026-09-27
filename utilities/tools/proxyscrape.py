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
     ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓
    ▓██░  ██ ▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒
    ▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░
    ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░
    ▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░
    ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒ 
    ░▒ ░       ░▒ ░ ▒   ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░ 
    ░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░  
                ░         ░ ░   ░    ░   ░ ░     
"""

def run():
    clear_screen()
    set_console_title('Proxy Scraper | Shrek Multi Tools')
    print(BANNER)
    print()
    
    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Http/https')
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Socks4')
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Socks5')
    print(f'    {Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] {Fore.WHITE}Quit')
    print()
    
    typeproxy = input_prompt('Choice')
    
    # ---- OPTION 0 : Quit ----
    if typeproxy == '0':
        return_to_menu()
        return
    
    # Créer le dossier data si nécessaire
    data_dir = os.path.join(root_path, 'data')
    os.makedirs(data_dir, exist_ok=True)
    out_file = os.path.join(data_dir, 'proxy.txt')
    
    # ---- OPTION 1 : HTTP/HTTPS ----
    if typeproxy == '1':
        info(f'Scraping HTTP/HTTPS proxies...')
        
        try:
            r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt', timeout=30)
            r2 = requests.get('https://api.openproxylist.xyz/http.txt', timeout=30)
            
            if r1.status_code != 200 or r2.status_code != 200:
                warn('Error fetching proxies from one or both sources!')
                time.sleep(1)
                return_to_menu()
                return
            
            with open(out_file, 'w', encoding='utf-8') as proxies:
                proxies.write(r1.text)
                proxies.write(r2.text)
            
            num1 = len(r1.text.splitlines())
            num2 = len(r2.text.splitlines())
            total = num1 + num2
            
            success(f'Done! Successfully added {total} proxies to {out_file}')
            info(f'Check {os.path.abspath(out_file)}')
            
        except Exception as e:
            warn(f'Error: {e}')
    
    # ---- OPTION 2 : SOCKS4 ----
    elif typeproxy == '2':
        info(f'Scraping SOCKS4 proxies...')
        
        try:
            r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt', timeout=30)
            r2 = requests.get('https://api.openproxylist.xyz/socks4.txt', timeout=30)
            
            if r1.status_code != 200 or r2.status_code != 200:
                warn('Error fetching proxies from one or both sources!')
                time.sleep(1)
                return_to_menu()
                return
            
            with open(out_file, 'w', encoding='utf-8') as proxies:
                proxies.write(r1.text)
                proxies.write(r2.text)
            
            num1 = len(r1.text.splitlines())
            num2 = len(r2.text.splitlines())
            total = num1 + num2
            
            success(f'Done! Successfully added {total} proxies to {out_file}')
            info(f'Check {os.path.abspath(out_file)}')
            
        except Exception as e:
            warn(f'Error: {e}')
    
    # ---- OPTION 3 : SOCKS5 ----
    elif typeproxy == '3':
        info(f'Scraping SOCKS5 proxies...')
        
        try:
            r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt', timeout=30)
            r2 = requests.get('https://api.openproxylist.xyz/socks5.txt', timeout=30)
            
            if r1.status_code != 200 or r2.status_code != 200:
                warn('Error fetching proxies from one or both sources!')
                time.sleep(1)
                return_to_menu()
                return
            
            with open(out_file, 'w', encoding='utf-8') as proxies:
                proxies.write(r1.text)
                proxies.write(r2.text)
            
            num1 = len(r1.text.splitlines())
            num2 = len(r2.text.splitlines())
            total = num1 + num2
            
            success(f'Done! Successfully added {total} proxies to {out_file}')
            info(f'Check {os.path.abspath(out_file)}')
            
        except Exception as e:
            warn(f'Error: {e}')
    
    else:
        warn('Invalid option')
        time.sleep(1)
        run()
        return
    
    time.sleep(1)
    return_to_menu()

if __name__ == '__main__':
    run()