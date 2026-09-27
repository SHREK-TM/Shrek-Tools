# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import ctypes
import threading
import time
import sys
import os
import emoji as ej
import requests
from colorama import Fore, Style

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.common import *
from utilities.core.helpers import randstr
from utilities.core.context import return_to_menu

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
    # ---- Ajout de set_console_title() comme dans bruteforce_zip.py ----
    from utilities.core.shrek_ui import set_console_title
    from utilities.core.paths import TOKENS_FILE
    set_console_title('Reaction Spammer | Shrek Multi Tools')
    
    clear_screen()
    # ---- SUPPRESSION de ctypes.windll.kernel32.SetConsoleTitleW(...) ----
    
    print(f"""
  {Fore.GREEN}
     ██▀███   ▓█████ ▄▄▄       ▄████▄ ▄▄▄█████▓  ██▓ ▒█████   ███▄    █       ██████  ██▓███   ▄▄▄      ███▄ ▄███▓
    ▓██ ▒ ██▒ ▓█   ▀▒████▄    ▒██▀ ▀█ ▓  ██▒ ▓▒▒▓██▒▒██▒  ██▒ ██ ▀█   █     ▒██    ▒ ▓██░  ██ ▒████▄   ▓██▒▀█▀ ██▒
    ▓██ ░▄█ ▒ ▒███  ▒██  ▀█▄  ▒▓█    ▄▒ ▓██░ ▒░▒▒██▒▒██░  ██▒▓██  ▀█ ██▒    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄ ▓██    ▓██░
    ▒██▀▀█▄   ▒▓█  ▄░██▄▄▄▄██▒▒▓▓▄ ▄██░ ▓██▓ ░ ░░██░▒██   ██░▓██▒  ▐▌██▒      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██▒██    ▒██ 
    ░██▓ ▒██▒▒░▒████▒▓█   ▓██░▒ ▓███▀   ▒██▒ ░ ░░██░░ ████▓▒░▒██░   ▓██░    ▒██████▒▒▒██▒ ░  ░▒▓█   ▓██▒██▒   ░██▒
    ░ ▒▓ ░▒▓░░░░ ▒░ ░▒▒   ▓▒█░░ ░▒ ▒    ▒ ░░    ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒     ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░▒▒   ▓▒█░ ▒░   ░  ░
      ░▒ ░ ▒ ░ ░ ░  ░ ░   ▒▒    ░  ▒      ░    ░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░    ░ ░▒  ░ ░░▒ ░     ░ ░   ▒▒ ░  ░      ░
      ░░   ░     ░    ░   ▒   ░         ░      ░ ▒ ░░ ░ ░ ▒     ░   ░ ░     ░  ░  ░  ░░         ░   ▒  ░      ░   
       ░     ░   ░        ░   ░ ░                ░      ░ ░           ░           ░                 ░         ░  


    """)

    # ---- Vérifier tokens.txt (à la racine) ----
    token_file = TOKENS_FILE
    if not os.path.exists(token_file):
        warn(f'tokens.txt not found at {token_file}!')
        time.sleep(1)
        run()
        return

    with open(token_file, 'r') as f:
        tokens = [line.strip() for line in f if line.strip()]

    if not tokens:
        warn('No tokens found in tokens.txt!')
        time.sleep(1)
        run()
        return

    # ---- Inputs ----
    chd = input_prompt('Channel ID')
    if not chd:
        warn('Channel ID cannot be empty!')
        time.sleep(1)
        run()
        return

    iddd = input_prompt('Message ID')
    if not iddd:
        warn('Message ID cannot be empty!')
        time.sleep(1)
        run()
        return

    emoji_input = input_prompt('Emoji (e.g., :thumbsup:)')
    if not emoji_input:
        warn('Emoji cannot be empty!')
        time.sleep(1)
        run()
        return

    try:
        delay = float(input_prompt('Delay (seconds)'))
        if delay < 0:
            warn('Delay cannot be negative!')
            time.sleep(1)
            run()
            return
    except ValueError:
        warn('Please enter a valid number!')
        time.sleep(1)
        run()
        return

    # ---- Fonction Reaction ----
    def reaction(chd, iddd, org, token):
        try:
            headers = {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US",
                "Cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "DNT": "1",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "TE": "Trailers",
                "authorization": token,
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            }
            emoji_str = ej.emojize(org, use_aliases=True)
            r = requests.put(
                f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji_str}/@me",
                headers=headers,
            )
            if r.status_code == 204:
                success(f'Reaction {org} sent')
            else:
                warn(f'Error: {r.status_code}')
        except Exception as e:
            warn(f'Error: {e}')

    # ---- Lancer les threads ----
    info(f'Starting reaction spammer for {len(tokens)} tokens...')
    for token in tokens:
        threading.Thread(target=reaction, args=(chd, iddd, emoji_input, token)).start()
        time.sleep(delay)

    info('All reactions sent!')
    time.sleep(3)
    return_to_menu()