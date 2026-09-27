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
from utilities.core.shrek_ui import set_console_title  # ← AJOUT

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
     █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ██▀███   ▄▄▄       ██ ▓█████▄ ▓█████ ██▀███  
    ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▓██ ▒ ██▒▒████▄   ▒▓██ ▒██▀ ██▌▓█   ▀▓██ ▒ ██▓
    ▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ▓██ ░▄█ ▒▒██  ▀█▄ ░▒██ ░██   █▌▒███  ▓██ ░▄█ ▒
    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒██▀▀█▄  ░██▄▄▄▄██ ░██▒░▓█▄   ▌▒▓█  ▄▒██▀▀█▄  
    ░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ░██▓ ▒██▒ ▓█   ▓██ ░██░░▒████▓ ░▒████░██▓ ▒██▒
    ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ▒▓ ░▒▓░ ▒▒   ▓▒█ ░▓ ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
      ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░▒ ░ ▒░  ░   ▒▒   ▒   ░ ▒  ▒  ░ ░    ░▒ ░ ▒░
      ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░        ░   ░   ░   ▒    ▒   ░ ░  ░    ░     ░   ░ 
        ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░          ░           ░    ░     ░       ░     ░     
"""

def run():
    global options2
    clear_screen()
    set_console_title('Webhook Raiders | Shrek Multi Tools')
    print(BANNER)
    print()
    print(f'    {Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}] {Fore.WHITE}Check webhook')
    print(f'    {Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}] {Fore.WHITE}Webhook info')
    print(f'    {Fore.GREEN}[{Fore.WHITE}03{Fore.GREEN}] {Fore.WHITE}Delete webhook')
    print(f'    {Fore.GREEN}[{Fore.WHITE}04{Fore.GREEN}] {Fore.WHITE}Spam webhook')
    print(f'    {Fore.GREEN}[{Fore.WHITE}05{Fore.GREEN}] {Fore.WHITE}Create webhooks')
    print(f'    {Fore.GREEN}[{Fore.WHITE}06{Fore.GREEN}] {Fore.WHITE}Create + spam webhooks')
    print(f'    {Fore.GREEN}[{Fore.WHITE}00{Fore.GREEN}] {Fore.WHITE}Quit')
    print()
    options2 = input_prompt('Choice')

    if options2 in ['1', '01']:
        clear_screen()
        set_console_title('Webhook Checker | Shrek Multi Tools')
        print(BANNER)
        print()
        webhook = input_prompt('What is your webhook link?')
        try:
            r = requests.get(webhook)
            if r.status_code == 200:
                success("Valid webhook link!")
            else:
                warn("Webhook link not valid!")
        except Exception:
            warn("Error checking webhook")
        time.sleep(2)

    elif options2 in ['2', '02']:
        clear_screen()
        set_console_title('Webhook Information | Shrek Multi Tools')
        print(BANNER)
        print()
        webhook = input_prompt('What is your webhook link?')
        try:
            r = requests.get(webhook)
            if r.status_code == 200:
                data = r.json()
                info(f"Webhook name: {data.get('name', 'N/A')}")
                info(f"Webhook id: {data.get('id', 'N/A')}")
                info(f"Guild id: {data.get('guild_id', 'N/A')}")
                info(f"Channel id: {data.get('channel_id', 'N/A')}")
                if data.get('avatar'):
                    info(f"Avatar: https://cdn.discordapp.com/avatars/{data['id']}/{data['avatar']}")
                else:
                    info("Avatar: none")
                info(f"Token: {data.get('token', 'N/A')}")
            else:
                warn("Webhook link not valid!")
        except Exception:
            warn("Error getting webhook info")
        time.sleep(2)

    elif options2 in ['3', '03']:
        clear_screen()
        set_console_title('Webhook Deleter | Shrek Multi Tools')
        print(BANNER)
        print()
        webhook = input_prompt('Webhook link')
        try:
            r = requests.delete(webhook)
            if r.status_code == 204:
                success("Webhook successfully deleted")
            else:
                warn(f"Error deleting webhook (status: {r.status_code})")
        except Exception:
            warn("Error deleting webhook")
        time.sleep(2)

    elif options2 in ['4', '04']:
        clear_screen()
        set_console_title('Webhook Spammer | Shrek Multi Tools')
        print(BANNER)
        print()
        webhook = input_prompt('Webhook link')
        message = input_prompt('Message')
        delay = float(input_prompt('Delay (seconds)'))

        info("Starting spam... press Ctrl+C to stop")
        try:
            while True:
                try:
                    time.sleep(delay)
                    r = requests.post(webhook, json={'content': message})
                    if r.status_code == 204:
                        success(f"Message sent: {message}")
                    else:
                        warn(f"Error: {r.status_code}")
                except KeyboardInterrupt:
                    info("Stopped by user")
                    break
                except Exception:
                    warn("Error sending message")
                    time.sleep(delay)
        except Exception:
            pass

    elif options2 in ['5', '05']:
        clear_screen()
        set_console_title('Webhook Creator | Shrek Multi Tools')
        print(BANNER)
        print()
        chanid = input_prompt('Channel id')
        token = input_prompt('Discord token')

        info("Creating webhooks...")
        url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

        def randstr(lenn):
            alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
            return ''.join(random.choice(alpha) for _ in range(lenn))

        header = {
            "Authorization": token,
            "User-Agent": useragent(),
            "Content-Type": "application/json"
        }

        ids = []
        for x in range(10):
            try:
                r = requests.post(url, headers=header, json={'name': 'Nuked By Shrek'})
                if r.status_code == 201:
                    data = r.json()
                    ids.append(data['id'])
                    success(f"Created webhook {x+1}/10")
                else:
                    warn(f"Failed to create webhook {x+1}/10")
            except Exception:
                warn(f"Error creating webhook {x+1}/10")
            time.sleep(0.5)

        if ids:
            success(f"Created {len(ids)} webhooks")
        else:
            warn("No webhooks created")
        time.sleep(2)

    elif options2 in ['6', '06']:
        clear_screen()
        set_console_title('Webhook Maker & Spammer | Shrek Multi Tools')
        print(BANNER)
        print()
        chanid = input_prompt('Channel id')
        msg = input_prompt('Message to spam')
        token = input_prompt('Discord token')

        info("Creating and spamming webhooks...")
        url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

        def randstr(lenn):
            alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
            return ''.join(random.choice(alpha) for _ in range(lenn))

        header = {
            "Authorization": token,
            "User-Agent": useragent(),
            "Content-Type": "application/json"
        }

        ids = []
        for x in range(10):
            try:
                r = requests.post(url, headers=header, json={'name': 'Nuked By Shrek'})
                if r.status_code == 201:
                    data = r.json()
                    ids.append(data['id'])
                    success(f"Created webhook {x+1}/10")
                else:
                    warn(f"Failed to create webhook {x+1}/10")
            except Exception:
                warn(f"Error creating webhook {x+1}/10")
            time.sleep(0.5)

        if ids:
            success(f"Created {len(ids)} webhooks, starting spam...")
            for webhook_id in ids:
                try:
                    webhook_url = f'https://discord.com/api/webhooks/{webhook_id}'
                    for y in range(5):
                        r = requests.post(webhook_url, json={'content': msg})
                        if r.status_code == 204:
                            success(f"Sent message {y+1}/5 to webhook {webhook_id}")
                        else:
                            warn(f"Error sending to webhook {webhook_id}")
                        time.sleep(0.5)
                except Exception:
                    warn(f"Error with webhook {webhook_id}")
        else:
            warn("No webhooks created")
        time.sleep(2)

    elif options2 in ['0', '00']:
        return_to_menu()
        return
    else:
        warn('Invalid option')
        time.sleep(2)

    run()

if __name__ == '__main__':
    run()