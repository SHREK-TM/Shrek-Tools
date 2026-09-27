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

def validateToken(token):
    try:
        r = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
        return r.status_code == 200
    except:
        return False

BANNER = f"""
{Fore.GREEN}
     ██▀███   ▓█████ ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ▓█████ ██▀███  
    ▓██ ▒ ██▒ ▓█   ▀▓██░  ██ ▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒ ▓█   ▀▓██ ▒ ██▒
    ▓██ ░▄█ ▒ ▒███  ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░ ▒███  ▓██ ░▄█ ▒
    ▒██▀▀█▄   ▒▓█  ▄▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░  ▒▓█  ▄▒██▀▀█▄  
    ░██▓ ▒██▒▒░▒████▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒░▒████░██▓ ▒██▒
    ░ ▒▓ ░▒▓░░░░ ▒░ ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░░░ ▒░ ░ ▒▓ ░▒▓░
      ░▒ ░ ▒ ░ ░ ░  ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒     ░    ░ ░ ░    ░▒ ░ ▒ 
      ░░   ░     ░  ░░       ░ ░ ░ ▒    ░░   ░   ░          ░    ░░   ░ 
       ░     ░   ░               ░ ░     ░              ░   ░     ░  
       
"""

def run():
    clear_screen()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Mass Report")
    print(BANNER)

    print(f"    {Fore.GREEN}- {Fore.WHITE}  The token you enter is the account that will send the reports")
    print()
    print()

    token = input_prompt('Token')
    if not validateToken(token):
        warn("Invalid token!")
        time.sleep(1)
        return_to_menu()
        return

    guild_id1 = input_prompt('Server ID')
    channel_id1 = input_prompt('Channel ID')
    message_id1 = input_prompt('Message ID')

    print()
    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Illegal content')
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Harassment')
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Spam or phishing link')
    print(f'    {Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}Self-harm')
    print(f'    {Fore.GREEN}[{Fore.WHITE}5{Fore.GREEN}] {Fore.WHITE}NSFW content')
    print()

    reason_choice = input_prompt('Reason (1-5)')

    reason_map = {
        '1': 0, 'Illegal content': 0,
        '2': 1, 'Harassment': 1,
        '3': 2, 'Spam or phishing link': 2,
        '4': 3, 'Self-harm': 3,
        '5': 4, 'NSFW content': 4
    }

    if reason_choice not in reason_map:
        warn("Invalid reason!")
        time.sleep(1)
        return_to_menu()
        return

    reason = reason_map[reason_choice]

    def _report(tok, gid, cid, mid, reason):
        try:
            r = requests.post(
                "https://discordapp.com/api/v8/report",
                json={"channel_id": cid, "message_id": mid, "guild_id": gid, "reason": reason},
                headers={
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                    "Authorization": tok,
                    "User-Agent": "Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0",
                },
            )
            if r.status_code == 201:
                success("Report sent!")
            else:
                warn(f"Error: {r.status_code}")
        except Exception as e:
            warn(f"Error: {e}")

    info("Starting mass report... (500-1000 reports)")
    threads = []
    for i in range(500, 1000):
        t = threading.Thread(target=_report, args=(token, guild_id1, channel_id1, message_id1, reason))
        t.daemon = True
        t.start()
        threads.append(t)
        time.sleep(0.05)

    info(f"Started {len(threads)} threads")
    input_prompt("Press Enter to return to menu")
    return_to_menu()

if __name__ == '__main__':
    run()