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

def run():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Shrek™ Support")
    print(f'''
    {Fore.GREEN}
     ██████   ██░ ██  ██▀███  ▓█████ ▀██ ▄█▀    ▄▄▄█████▓  ███▄ ▄███▓    
    ▒██    ▒ ▒▓██░ ██ ▓██ ▒ ██▒▓█   ▀  ██▄█▒     ▓  ██▒ ▓▒ ▓██▒▀█▀ ██▒    
    ░ ▓██▄   ░▒██▀▀██ ▓██ ░▄█ ▒▒███   ▓███▄░     ▒ ▓██░ ▒░ ▓██    ▓██░    
      ▒   ██▒ ░▓█ ░██ ▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄     ░ ▓██▓ ░  ▒██    ▒██     
    ▒██████▒▒ ░▓█▒░██▓░██▓ ▒██▒░▒████ ▒██▒ █▄      ▒██▒ ░ ▒▒██▒   ░██▒    
    ▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒▓ ░▒▓░░░ ▒░  ▒ ▒▒ ▓▒      ▒ ░░   ░░ ▒░   ░  ░    
    ░ ░▒  ░    ▒ ░▒░ ░  ░▒ ░ ▒░ ░ ░   ░ ░▒ ▒░        ░    ░░  ░      ░    
    ░  ░  ░    ░  ░░ ░   ░   ░    ░   ░ ░░ ░       ░ ░     ░      ░       
      ░    ░  ░  ░   ░        ░   ░  ░                ░       ░       
    
    
    ''')  
    whichserver = int(input(f"""
    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Shrek™ Discord server
    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Shrek™ Github 
    {Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] {Fore.WHITE}Quit
    
    
    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}"""))
    
    
    if whichserver == 1:
      webbrowser.open('https://discord.gg/JKsRYZ244U')
    elif whichserver == 2:
      webbrowser.open('https://github.com/SHREK-TM/Shrek-Tools')
    elif whichserver == 0:
      return_to_menu()
      return
    else:
      print("Invalid Option.")

