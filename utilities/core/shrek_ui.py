# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].

import ctypes
import os

from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def set_console_title(title: str):
    if os.name == "nt":
        ctypes.windll.kernel32.SetConsoleTitleW(title)


def show_banner(title: str = "Shrek Multi Tools"):
    clear_screen()
    set_console_title(f"{title} | Shrek Multi Tools")
    print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{title}{Fore.RESET}\n")


def shrek_input(prompt: str) -> str:
    return input(
        f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{prompt}{Fore.RESET}"
    ).strip()


def pause(message: str = "Press Enter to return to menu..."):
    input(f"\n{Fore.YELLOW}{message}{Fore.RESET}")
