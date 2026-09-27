# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import ctypes
import time
from concurrent.futures import ThreadPoolExecutor
from json import dumps, loads
import sys
import os
import requests
from colorama import Fore, Style
from websocket import WebSocket

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.common import *
from utilities.core.context import return_to_menu
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
    set_console_title('VC Spammer | Shrek Multi Tools')
    
    print(f"""
  {Fore.GREEN}
     ██▒   █▓ ▄████▄       ██████  ██▓███   ▄▄▄       ███▄ ▄███▓  ███▄ ▄███▓▓█████ ██▀███  
    ▓██░   █▒▒██▀ ▀█     ▒██    ▒ ▓██░  ██ ▒████▄    ▓██▒▀█▀ ██▒ ▓██▒▀█▀ ██▒▓█   ▀▓██ ▒ ██▒
     ▓██  █▒░▒▓█    ▄    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░ ▓██    ▓██░▒███  ▓██ ░▄█ ▒
      ▒██ █░░▒▓▓▄ ▄██      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██  ▒██    ▒██ ▒▓█  ▄▒██▀▀█▄  
       ▒▀█░  ▒ ▓███▀     ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒▒██▒   ░██▒░▒████░██▓ ▒██▒
       ░ ▐░  ░ ░▒ ▒      ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░   ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
       ░ ░░    ░  ▒      ░ ░▒  ░  ░▒ ░       ░   ▒▒ ░░  ░      ░░░  ░      ░ ░ ░    ░▒ ░ ▒░
         ░░  ░           ░  ░  ░  ░░         ░   ▒   ░      ░    ░      ░      ░     ░   ░ 
          ░  ░ ░               ░                 ░  ░       ░   ░       ░      ░     ░     
    """)
    print()

    # ---- Vérifier tokens.txt ----
    token_file = TOKENS_FILE
    if not os.path.exists(token_file):
        warn(f'tokens.txt not found at {token_file}!')
        time.sleep(1)
        run()
        return

    with open(token_file, 'r') as f:
        tokenlist = [line.strip() for line in f if line.strip()]

    if not tokenlist:
        warn('No tokens found in tokens.txt!')
        time.sleep(1)
        run()
        return

    # ---- Inputs ----
    channel = input_prompt('Voice Channel ID')
    if not channel:
        warn('Channel ID cannot be empty!')
        time.sleep(1)
        run()
        return

    server = input_prompt('Server ID')
    if not server:
        warn('Server ID cannot be empty!')
        time.sleep(1)
        run()
        return

    deaf = input_prompt('Deafen? (y/n)').lower() == 'y'
    mute = input_prompt('Mute? (y/n)').lower() == 'y'
    stream = input_prompt('Stream? (y/n)').lower() == 'y'
    video = input_prompt('Video? (y/n)').lower() == 'y'

    info(f'Starting VC spammer for {len(tokenlist)} tokens...')
    info('Press Ctrl+C to stop')

    def join_vc(token):
        try:
            while True:
                ws = WebSocket()
                ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
                ws.recv()
                ws.send(dumps({"op": 2, "d": {"token": token, "properties": {"$os": "windows", "$browser": "Discord", "$device": "desktop"}}}))
                ws.send(dumps({"op": 4, "d": {"guild_id": server, "channel_id": channel, "self_mute": mute, "self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
                ws.send(dumps({"op": 18, "d": {"type": "guild", "guild_id": server, "channel_id": channel, "preferred_region": "singapore"}}))
                ws.send(dumps({"op": 1, "d": None}))
                time.sleep(0.1)
        except Exception as e:
            warn(f'Error with token: {e}')

    try:
        executor = ThreadPoolExecutor(max_workers=1000)
        for token in tokenlist:
            executor.submit(join_vc, token)
            success(f'Joined VC for {token[:20]}...')
            time.sleep(0.01)
        
        input_prompt('Press Enter to stop VC Spammer')
    except KeyboardInterrupt:
        info('Stopped by user')
    finally:
        executor.shutdown(wait=False)
        info('All threads stopped')
        time.sleep(3)
        return_to_menu()

if __name__ == '__main__':
    run()