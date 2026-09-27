# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import ctypes
import os
import webbrowser
import sys
import time
from colorama import Fore, Style

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.common import *
from utilities.core.context import save_user_name, return_to_menu
from utilities.core.themes import THEMES, get_theme, set_theme
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
    set_console_title('Settings | Shrek Multi Tools')
    
    print(f"""
{Fore.GREEN}
      ██████  ▓█████▄▄▄█████▓▄▄▄█████▓  ██▓ ███▄    █  ▄████   ██████ 
    ▒██    ▒  ▓█   ▀▓  ██▒ ▓▒▓  ██▒ ▓▒▒▓██▒ ██ ▀█   █  ██▒ ▀█▒██    ▒ 
    ░ ▓██▄    ▒███  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░ ▓██▄   
      ▒   ██▒ ▒▓█  ▄░ ▓██▓ ░ ░ ▓██▓ ░ ░░██░▓██▒  ▐▌██▒░▓█  ██  ▒   ██▒
    ▒██████▒▒▒░▒████  ▒██▒ ░   ▒██▒ ░ ░░██░▒██░   ▓██░▒▓███▀▒▒██████▒▒
    ▒ ▒▓▒ ▒ ░░░░ ▒░   ▒ ░░     ▒ ░░    ░▓  ░ ▒░   ▒ ▒ ░▒   ▒ ▒ ▒▓▒ ▒ ░
    ░ ░▒  ░  ░ ░ ░      ░        ░    ░ ▒ ░░ ░░   ░ ▒░ ░   ░ ░ ░▒  ░ ░
    ░  ░  ░      ░    ░        ░      ░ ▒ ░   ░   ░ ░  ░   ░ ░  ░  ░  
          ░  ░   ░                      ░           ░      ░       ░  
""")
    print()
    print(f'    {Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}] {Fore.WHITE}Change user name')
    print(f'    {Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}] {Fore.WHITE}Help channel (discord)')
    print(f'    {Fore.GREEN}[{Fore.WHITE}03{Fore.GREEN}] {Fore.WHITE}Meaning of commands')
    print(f'    {Fore.GREEN}[{Fore.WHITE}04{Fore.GREEN}] {Fore.WHITE}Change theme {Fore.GREEN}[{Fore.WHITE}{get_theme()}{Fore.GREEN}]')
    print(f'    {Fore.GREEN}[{Fore.WHITE}00{Fore.GREEN}] {Fore.WHITE}Exit')
    print()

    choice = input_prompt('Choice')

    if choice in ("1", "01"):
        clear_screen()
        new_name = input_prompt('Enter your new username')
        if new_name:
            save_user_name(new_name)
            success('Username updated — restart to see it in the menu')
        else:
            warn('Username cannot be empty!')
        time.sleep(1)
        run()
        return

    elif choice in ("2", "02"):
        webbrowser.open("https://discord.gg/mQVvRGfs46")
        time.sleep(1)
        run()
        return

    elif choice in ("3", "03"):
        clear_screen()
        print(f"""
{Fore.GREEN}> {Fore.WHITE}Tools load from utilities/core/tool_order.py
{Fore.GREEN}> {Fore.WHITE}Each tool exposes run() in utilities/tools/
{Fore.GREEN}> {Fore.WHITE}Token tools are grouped in TOKEN PANEL (option 13)
{Fore.GREEN}> {Fore.WHITE}Menu order is managed in utilities/core/tool_order.py
{Fore.GREEN}> {Fore.WHITE}No need to edit Menu.py anymore.
""")
        input_prompt('Press Enter to return')
        run()
        return

    elif choice in ("4", "04"):
        clear_screen()
        print(f"\n{Fore.GREEN}Available themes:{Fore.WHITE}")
        for i, theme in enumerate(THEMES, 1):
            active = f" {Fore.YELLOW}(active){Fore.WHITE}" if theme == get_theme() else ""
            print(f'    {Fore.GREEN}[{Fore.WHITE}{i:02}{Fore.GREEN}] {Fore.WHITE}{theme}{active}')
        print()
        pick = input_prompt(f'Choose (1-{len(THEMES)})')
        if pick.isdigit() and 1 <= int(pick) <= len(THEMES):
            set_theme(THEMES[int(pick) - 1])
            success('Theme updated!')
        else:
            warn('Invalid choice!')
        time.sleep(1)
        run()
        return

    elif choice in ("0", "00"):
        return_to_menu()
        return

    else:
        warn('Invalid option')
        time.sleep(1)
        run()
        return

if __name__ == '__main__':
    run()