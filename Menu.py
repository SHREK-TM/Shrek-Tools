# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import ctypes
import os
import sys

import colorama
from colorama import Fore
colorama.init(autoreset=False)

from utilities.core.common import cls
from utilities.core.context import (
    load_user_name,
    save_user_name,
    register_menu_callback,
)
from utilities.core.paths import USER_NAME_FILE, chdir_to_root
from utilities.core.display import (
    run_startup_animation,
    tool_open_transition,
    render_menu_header,
    render_menu_grid,
    prompt_choice,
)
from utilities.core.loader import (
    get_tools_by_page,
    get_tool_by_id,
    get_special_tool,
    get_page_count,
)

from utilities.core.premium import buy_premium

USER_NAME_PATH = USER_NAME_FILE


def prompt_username():
    ctypes.windll.kernel32.SetConsoleTitleW("Welcome to Shrek Multi Tools | Made by Shrek™")
    name = input(f"""
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
    save_user_name(name.strip() or "User")
    return name.strip() or "User"


def run_tool(tool):
    if not tool:
        return
    tool_open_transition(tool["name"])
    try:
        tool["run"]()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Interrupted.{Fore.RESET}")
    except Exception as exc:
        print(f"\n{Fore.RED}Error running {tool['name']}: {exc}{Fore.RESET}")
        import traceback
        traceback.print_exc()


def show_page(page: int, total_pages: int):
    render_menu_header(page)
    tools = get_tools_by_page(page)
    render_menu_grid(tools, page, total_pages)
    return prompt_choice()


def main_menu():
    current_page = 1
    while True:
        total_pages = get_page_count()
        if current_page > total_pages:
            current_page = total_pages
        choice = show_page(current_page, total_pages)
        normalized = choice.upper()

        if normalized in ("0", "00"):
            sys.exit(0)
        if normalized == "N" and current_page < total_pages:
            current_page += 1
            continue
        if normalized == "P" and current_page > 1:
            current_page -= 1
            continue
        if normalized == "BUY":
            buy_premium()
            continue
        if normalized == "!":
            tool = get_special_tool("!")
            run_tool(tool)
            continue
        if normalized == "TM":
            tool = get_special_tool("TM")
            run_tool(tool)
            continue

        tool = get_tool_by_id(choice)
        if tool:
            run_tool(tool)
            continue

        print(f"{Fore.RED}Error, Invalid Option{Fore.RESET}")
        input("Press ENTER...")


def main():
    chdir_to_root()
    os.makedirs(os.path.dirname(USER_NAME_PATH), exist_ok=True)
    if not os.path.exists(USER_NAME_PATH):
        prompt_username()
    else:
        load_user_name()

    register_menu_callback(main_menu)
    run_startup_animation()
    main_menu()


if __name__ == "__main__":
    while True:
        try:
            main()
        except SystemExit:
            break
        except Exception as exc:
            print(f"{Fore.RED}Fatal error: {exc}{Fore.RESET}")
            input("Press ENTER to restart...")
        else:
            break