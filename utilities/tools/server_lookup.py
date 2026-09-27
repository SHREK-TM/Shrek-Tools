# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import os
import sys
import time
import requests
import colorama
from time import sleep
from colorama import Fore, init, Style

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.common import *
from utilities.core.context import return_to_menu
from utilities.core.shrek_ui import set_console_title

init(autoreset=True)

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
    set_console_title('Server Info | Shrek Multi Tools')
    
    print(f"""
{Fore.GREEN}
     ██▓    ▒█████   ▒█████   ▀██ ▄█▀ █    ██  ██▓███  
    ▓██▒   ▒██▒  ██▒▒██▒  ██▒  ██▄█▒  ██  ▓██▒▓██░  ██ 
    ▒██░   ▒██░  ██▒▒██░  ██▒ ▓███▄░ ▓██  ▒██░▓██░ ██▓▒
    ▒██░   ▒██   ██░▒██   ██░ ▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
    ░██████░ ████▓▒░░ ████▓▒░ ▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
    ░ ▒░▓  ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒ ▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
    ░ ░ ▒    ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░ ░▒░ ░ ░ ░▒ ░     
      ░ ░  ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░   ░░ ░ ░ ░░       
        ░      ░ ░      ░ ░   ░  ░      ░          
""")
    print()
    
    token = input_prompt('Token')
    if not token:
        warn('Token cannot be empty!')
        time.sleep(1)
        run()
        return

    guild_id = input_prompt('Server ID')
    if not guild_id:
        warn('Server ID cannot be empty!')
        time.sleep(1)
        run()
        return

    headers = {
        'Authorization': token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    info('Fetching data...')
    time.sleep(1)

    res = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}?with_counts=true", headers=headers)
    
    if res.status_code != 200:
        warn(f"Error: Could not find server. Check your Token and ID. (Status: {res.status_code})")
        time.sleep(2)
        run()
        return

    data = res.json()
    owner_id = data.get('owner_id')
    owner_res = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/members/{owner_id}", headers=headers)
    
    owner_name = "Unknown"
    if owner_res.status_code == 200:
        owner_data = owner_res.json()
        user = owner_data.get('user', {})
        owner_name = f"{user.get('username')}#{user.get('discriminator', '0000')}"

    print()
    info("Server Information")
    print()
    print(f'    {Fore.GREEN}Name{Fore.WHITE}        : {data.get("name")}')
    print(f'    {Fore.GREEN}ID{Fore.WHITE}          : {data.get("id")}')
    print(f'    {Fore.GREEN}Owner{Fore.WHITE}       : {owner_name}')
    print(f'    {Fore.GREEN}Owner ID{Fore.WHITE}    : {owner_id}')
    print(f'    {Fore.GREEN}Members{Fore.WHITE}     : {data.get("approximate_member_count")}')
    print(f'    {Fore.GREEN}Region{Fore.WHITE}      : {data.get("region")}')
    print(f'    {Fore.GREEN}Icon URL{Fore.WHITE}    : https://cdn.discordapp.com/icons/{guild_id}/{data.get("icon")}.webp?size=256')
    print()
    
    success("Data fetched successfully!")
    time.sleep(2)
    return_to_menu()

if __name__ == '__main__':
    run()