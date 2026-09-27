# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import os
import sys
import time
import ctypes
import msvcrt
import hashlib
from colorama import Fore, Style, init

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)

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


# ---- Admin Functions ----
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def relaunch_as_admin():
    params = ' '.join([f'\"{arg}\"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, params, None, 1)
    sys.exit(0)

def ensure_admin():
    if not is_admin():
        info('Administrator privileges required, relaunching...')
        relaunch_as_admin()


# ---- Lock File Functions ----
locked_files = []

def lock_file(path):
    try:
        f = open(path, 'rb')
        msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, os.path.getsize(path))
        locked_files.append(f)
    except:
        return None


# ---- Protect Functions ----
def protect_discord():
    base = os.getenv('APPDATA')
    leveldb = os.path.join(base, 'discord', 'Local Storage', 'leveldb')
    if os.path.exists(leveldb):
        for file in os.listdir(leveldb):
            if file.endswith('.ldb') or file.endswith('.log'):
                lock_file(os.path.join(leveldb, file))
    print()
    success('Anti-Grabb Discord enabled')

def protect_telegram():
    base = os.getenv('APPDATA')
    tdata = os.path.join(base, 'Telegram Desktop', 'tdata')
    if os.path.exists(tdata):
        for root, _, files in os.walk(tdata):
            for f in files:
                lock_file(os.path.join(root, f))
    print()
    success('Anti-Grabb Telegram enabled')

def protect_browsers():
    paths = [
        os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default'),
        os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Edge', 'User Data', 'Default'),
        os.path.join(os.getenv('LOCALAPPDATA'), 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default')
    ]
    targets = ['Login Data', 'History', 'Cookies', 'Web Data']
    for path in paths:
        if os.path.exists(path):
            for t in targets:
                lock_file(os.path.join(path, t))
    print()
    success('Anti-Grabb Browsers enabled')


# ---- Menu ----
def menu():
    print(f'''
{Fore.GREEN}
     ▄▄▄      ███▄    █ ▄▄▄█████▓  ██▓     ▄████  ██▀███   ▄▄▄      ▄▄▄▄    ▄▄▄▄   
    ▒████▄    ██ ▀█   █ ▓  ██▒ ▓▒▒▓██▒     ██▒ ▀█▓██ ▒ ██▒▒████▄   ▓█████▄ ▓█████▄ 
    ▒██  ▀█▄ ▓██  ▀█ ██▒▒ ▓██░ ▒░▒▒██▒    ▒██░▄▄▄▓██ ░▄█ ▒▒██  ▀█▄ ▒██▒ ▄██▒██▒ ▄██
    ░██▄▄▄▄██▓██▒  ▐▌██▒░ ▓██▓ ░ ░░██░    ░▓█  ██▒██▀▀█▄  ░██▄▄▄▄██▒██░█▀  ▒██░█▀  
    ▒▓█   ▓██▒██░   ▓██░  ▒██▒ ░ ░░██░    ▒▓███▀▒░██▓ ▒██▒▒▓█   ▓██░▓█  ▀█▓░▓█  ▀█▓
    ░▒▒   ▓▒█░ ▒░   ▒ ▒   ▒ ░░    ░▓      ░▒   ▒ ░ ▒▓ ░▒▓░░▒▒   ▓▒█░▒▓███▀▒░▒▓███▀▒
    ░ ░   ▒▒ ░ ░░   ░ ▒░    ░    ░ ▒ ░     ░   ░   ░▒ ░ ▒ ░ ░   ▒▒ ▒░▒   ░ ▒░▒   ░ 
      ░   ▒     ░   ░ ░   ░      ░ ▒ ░     ░   ░   ░░   ░   ░   ▒   ░    ░  ░    ░ 
          ░           ░            ░           ░    ░           ░   ░       ░      
''')
    print()
    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Anti-Grabb Discord')
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Anti-Grabb Telegram')
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Anti-Grabb Browsers')
    print(f'    {Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}Anti-Grabb ALL')
    print(f'    {Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] {Fore.WHITE}Quit')
    print()
    return input_prompt('Choice')


# ---- Main ----
def main():
    clear_screen()
    choice = menu()
    
    if choice == '1':
        protect_discord()
    elif choice == '2':
        protect_telegram()
    elif choice == '3':
        protect_browsers()
    elif choice == '4':
        protect_discord()
        protect_telegram()
        protect_browsers()
        print()
        success('ANTI-GRABB ALL ENABLED')
    elif choice == '0':
        return_to_menu()
        return
    else:
        warn('Invalid option')
        time.sleep(1)
        main()
        return

    print()
    info('Anti-Grabb active - Close the tool to restore system')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        warn('Anti-Grabb disabled, system restored')
        return_to_menu()


# ---- Run ----
def run():
    set_console_title('Anti Grab | Shrek Multi Tools')
    ensure_admin()
    clear_screen()
    main()

if __name__ == '__main__':
    run()