# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import discord
from discord.ext import commands
import requests
import re
from urllib.parse import quote
from bs4 import BeautifulSoup
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
from colorama import init, Fore, Style
import sys
import platform
import os
import hashlib
from time import sleep
from datetime import datetime, UTC

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title

# Initialize with autoreset
init(autoreset=True)

# ---- Style functions ----
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

def get_input(prompt):
    """Affiche le prompt, gère les entrées vides avec effacement de l'erreur."""
    prompt_text = f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} {prompt}: {Style.RESET_ALL}'
    while True:
        user_input = input(prompt_text)
        if user_input.strip() != '':
            return user_input.strip()
        else:
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.flush()
            warn('Please enter a valid value')
            time.sleep(0.8)
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.flush()

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def clean_username(username):
    return re.sub(r'#\d+$', '', username)

async def discord_dox(target_id):
    info('Fetching Discord info...')
    results = {'discord_info': {}}
    try:
        user = await bot.fetch_user(int(target_id))
        full_username = f'{user.name}#{user.discriminator}'
        results['discord_info'] = {
            'username': full_username,
            'clean_username': clean_username(full_username),
            'id': str(user.id),
            'created_at': str(user.created_at),
            'avatar': str(user.avatar.url) if user.avatar else 'No avatar',
            'servers': [guild.name for guild in user.mutual_guilds]
        }
    except discord.errors.HTTPException as e:
        results['discord_info'] = {'error': f'Error: {str(e)}. Bot must share a server with user.'}
        warn(results['discord_info']['error'])
    except Exception as e:
        results['discord_info'] = {'error': f'General error: {str(e)}'}
        warn(results['discord_info']['error'])
    return results

def init_driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36')
    options.add_argument('--disable-blink-features=AutomationControlled')
    return webdriver.Chrome(options=options)

def external_dox(username):
    info('Scanning external platforms...')
    clean_name = quote(clean_username(username))
    results = {
        'youtube': ['No profile found'],
        'tiktok': ['No profile found'],
        'snapchat': ['No profile found'],
        'instagram': ['No profile found'],
        'github': ['No profile found']
    }
    platforms = {
        'youtube': f'https://www.youtube.com/@{clean_name}',
        'tiktok': f'https://www.tiktok.com/@{clean_name}',
        'snapchat': f'https://www.snapchat.com/add/{clean_name}',
        'instagram': f'https://www.instagram.com/{clean_name}/'
    }
    driver = init_driver()
    for platform, url in platforms.items():
        info(f'Checking {platform.capitalize()}...')
        for attempt in range(2):
            try:
                driver.get(url)
                time.sleep(5)
                page_source = driver.page_source.lower()
                title = driver.title.lower()
                if platform == 'youtube':
                    if '404' not in title:
                        results[platform] = [url]
                elif platform == 'tiktok':
                    if 'couldn\'t find this account' not in page_source:
                        results[platform] = [url]
                elif platform == 'snapchat':
                    if ' on snapchat' in title:
                        results[platform] = [url]
                elif platform == 'instagram':
                    if 'page not found' not in title and 'this account is private' not in page_source and 'sorry, this page isn\'t available' not in page_source:
                        results[platform] = [url]
            except Exception as e:
                warn(f'Error checking {platform} (attempt {attempt + 1}): {str(e)}')
                if attempt == 1:
                    results[platform] = [f'Error: Failed to check ({str(e)})']
                time.sleep(2)
            else:
                break
    driver.quit()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
    info('Checking GitHub...')
    github_url = f'https://github.com/{clean_name}'
    try:
        r = requests.get(github_url, headers=headers)
        if r.status_code == 200:
            results['github'] = [github_url]
    except Exception as e:
        warn(f'Error checking GitHub: {str(e)}')
    return results

def print_results(discord_data, external_data):
    print()
    info('Discord Results')
    discord_info = discord_data.get('discord_info', {})
    if 'error' not in discord_info:
        info(f'Username: {discord_info.get("username")}')
        info(f'Cleaned Username: {discord_info.get("clean_username")}')
        info(f'ID: {discord_info.get("id")}')
        info(f'Avatar: {discord_info.get("avatar")}')
        info(f'Creation Date: {discord_info.get("created_at")}')
        servers = ', '.join(discord_info.get('servers') or []) or 'None'
        info(f'Common Servers: {servers}')
    else:
        warn(f'Error: {discord_info.get("error")}')
    
    print()
    info('External Results')
    for platform, links in external_data.items():
        platform_name = platform.capitalize()
        info(f'{platform_name}:')
        for link in links:
            info(f'  - URL: {link}')
    print()

async def main():
    clear_screen()
    
    # ASCII Art avec Fore.GREEN
    print(f'''
{Fore.GREEN}
    ▓█████▄  ▒█████  ▒██   ██▒    ▄▄▄█████▓ ▒█████   ▒█████    ██▓   
    ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒ ▓██▒   
    ░██   █▌▒██░  ██▒░░  █   ░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒ ▒██░   
    ░▓█▄   ▌▒██   ██░ ░ █ █ ▒     ░ ▓██▓ ░ ▒██   ██░▒██   ██░ ▒██░   
    ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░▒░██████
     ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░░ ▒░▓  
     ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░░ ░ ▒  
     ░ ░  ░ ░ ░ ░ ▒   ░    ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒     ░ ░  
       ░        ░ ░   ░    ░                   ░ ░      ░ ░  ░    ░  
 
''')
    print(f'    {Fore.GREEN}- {Fore.WHITE}Uses headless Selenium to bypass protections')
    print(f'    {Fore.GREEN}- {Fore.WHITE}Clean formatting: fast/efficient results')
    print(f'    {Fore.GREEN}- {Fore.WHITE}Discord bot required, simple commands, secure token')
    print(f'    {Fore.GREEN}- {Fore.WHITE}No shared server? Manual bypass with username')
    print(f'    {Fore.GREEN}- {Fore.WHITE}Retrieves username, ID, creation date, and avatar via Discord ID')
    print(f'    {Fore.GREEN}- {Fore.WHITE}Scans YouTube, TikTok, Snapchat, Instagram, and GitHub in stealth')
    print()
    
    while True:
        DISCORD_TOKEN = get_input('Enter Discord bot token')
        
        try:
            await bot.start(DISCORD_TOKEN)
            break  # Si la connexion réussit, on sort de la boucle
        except discord.errors.LoginFailure:
            warn('Invalid token. Get it from https://discord.com/developers/applications > Bot tab.')
            print()
            continue
        except Exception as e:
            warn(f'Startup error: {str(e)}')
            print()
            continue

@bot.event
async def on_ready():
    success(f'Bot connected: {bot.user.name}')
    print()
    while True:
        target_id = input_prompt('Enter Discord ID (or "quit")')
        if target_id.lower() == 'quit':
            info('Shutting down...')
            await bot.close()
            return
        
        if not re.match(r'^\d{18,19}$', target_id):
            warn('Invalid ID: Must be 18-19 digits. Ex: 1424308189377331231')
            print()
            continue
        
        discord_data = await discord_dox(target_id)
        username = discord_data.get('discord_info', {}).get('clean_username', target_id)
        
        if 'error' in discord_data['discord_info']:
            warn('No Discord username found. Enter manually?')
            print()
            username = input_prompt('Username (or "skip")')
            if username.lower() == 'skip':
                username = target_id
            else:
                username = clean_username(username)
            print()
        
        external_data = external_dox(username)
        print_results(discord_data, external_data)
        print()
        input_prompt('Press Enter to continue')

def run():
    clear_screen()
    set_console_title('Dox Tool | Shrek Multi Tools')
    asyncio.run(main())

if __name__ == '__main__':
    run()