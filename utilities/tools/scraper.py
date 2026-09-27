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
from utilities.core.paths import MEMBER_ID_FILE
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


def run():
    clear_screen()
    set_console_title('ID Scraper | Shrek Multi Tools')
    
    print(f'''
    {Fore.GREEN}
  ██ ▓█████▄       ██████   ▄████▄  ██▀███   ▄▄▄      ██▓███   ▓█████ ██▀███  
▒▓██ ▒██▀ ██▌    ▒██    ▒  ▒██▀ ▀█ ▓██ ▒ ██▒▒████▄   ▓██░  ██  ▓█   ▀▓██ ▒ ██▒
░▒██ ░██   █▌    ░ ▓██▄    ▒▓█    ▄▓██ ░▄█ ▒▒██  ▀█▄ ▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒
 ░██▒░▓█▄   ▌      ▒   ██▒▒▒▓▓▄ ▄██▒██▀▀█▄  ░██▄▄▄▄██▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄  
 ░██░░▒████▓     ▒██████▒▒░▒ ▓███▀ ░██▓ ▒██▒▒▓█   ▓██▒██▒ ░  ░▒░▒████░██▓ ▒██▒
 ░▓ ░ ▒▒▓  ▒     ▒ ▒▓▒ ▒ ░░░ ░▒ ▒  ░ ▒▓ ░▒▓░░▒▒   ▓▒█▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
  ▒   ░ ▒  ▒     ░ ░▒  ░     ░  ▒    ░▒ ░ ▒ ░ ░   ▒▒ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ 
  ▒   ░ ░  ░     ░  ░  ░   ░         ░░   ░   ░   ▒  ░░           ░    ░░   ░ 
  ░     ░              ░   ░ ░        ░           ░           ░   ░     ░     

    
    ''')
    
    tukan = input_prompt('What is the token you want to use to scrape?')
    if not tukan:
        warn('Token cannot be empty!')
        time.sleep(1)
        run()
        return

    guildd = input_prompt('What is the Server ID you want to scrape?')
    if not guildd:
        warn('Server ID cannot be empty!')
        time.sleep(1)
        run()
        return

    chann = input_prompt('Any channel id in the server')
    if not chann:
        warn('Channel ID cannot be empty!')
        time.sleep(1)
        run()
        return

    bot = discum.Client(token=tukan)
    
    def closefetching(resp, guildid):
        if bot.gateway.finishedMemberFetching(guildid):
            lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
            print(str(lenmembersfetched))
            bot.gateway.removeCommand({'function': closefetching, 'params': {'guildid': guildid}})
            bot.gateway.close()
    
    def getmembers(guildid, channelid):
        bot.gateway.fetchMembers(guildid, channelid, keep='all', wait=1)
        bot.gateway.command({'function': closefetching, 'params': {'guildid': guildid}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guildid).members
    
    info('Fetching members...')
    members = getmembers(guildd, chann)
    
    memberids = []
    
    for memberId in members:
        memberids.append(memberId)
    
    clear_screen()
    
    member_file = MEMBER_ID_FILE
    with open(member_file, 'w') as ids:
        for element in memberids:
            ids.write(element + '\n')    
    
    success(f'Finished Scraping {len(memberids)} members!')
    info(f'Check {member_file} for the ids')
    time.sleep(3)
    return_to_menu()

if __name__ == '__main__':
    run()