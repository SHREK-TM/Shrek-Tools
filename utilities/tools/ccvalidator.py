# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Fixed from V5.5 decompiled ccvalidator.py

import os
import random
import re
import sys
import requests
from colorama import Fore, Style, init

init(autoreset=True)

from utilities.core.paths import USERAGENTS_FILE

USER_AGENT_FILE = USERAGENTS_FILE
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
)


def success(text):
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def info(text):
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def warn(text):
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')


def load_user_agents():
    if not os.path.exists(USER_AGENT_FILE):
        info(f"{USER_AGENT_FILE} missing — using default user-agent.")
        return [DEFAULT_USER_AGENT]
    with open(USER_AGENT_FILE, "r", encoding="utf-8") as f:
        agents = [line.strip() for line in f if line.strip()]
    return agents or [DEFAULT_USER_AGENT]


def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)]
    checksum = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0


def get_card_brand(card_number):
    brands = {
        r"^4[0-9]{12}(?:[0-9]{3})?$": "Visa",
        r"^5[1-5][0-9]{14}$": "MasterCard",
        r"^3[47][0-9]{13}$": "American Express",
        r"^6(?:011|5[0-9]{2})[0-9]{12}$": "Discover",
        r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$": "Diners Club",
        r"^(?:2131|1800|35\d{3})\d{11}$": "JCB",
    }
    for pattern, brand in brands.items():
        if re.match(pattern, card_number):
            return brand
    return "Unknown"


def get_bin_info(card_number):
    bin_number = card_number[:6]
    url = f"https://lookup.binlist.net/{bin_number}"
    user_agent = random.choice(load_user_agents())
    try:
        response = requests.get(url, headers={"User-Agent": user_agent}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "Bank": data.get("bank", {}).get("name", "Unknown"),
                "Country": data.get("country", {}).get("name", "Unknown"),
                "Type": data.get("type", "Unknown"),
                "Brand": data.get("scheme", "Unknown").capitalize(),
            }
    except requests.RequestException:
        pass
    return {"Error": "cc invalid"}


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(f'''{Fore.GREEN}
     ▄████▄  ▄████▄  ██▒   █▓ ▄▄▄       ██▓     ██▓▓█████▄  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
    ▒██▀ ▀█ ▒██▀ ▀█ ▓██░   █▒▒████▄    ▓██▒   ▒▓██▒▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
    ▒▓█    ▄▒▓█    ▄ ▓██  █▒░▒██  ▀█▄  ▒██░   ▒▒██▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
    ▒▓▓▄ ▄██▒▓▓▄ ▄██  ▒██ █░░░██▄▄▄▄██ ▒██░   ░░██░░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
    ▒ ▓███▀ ▒ ▓███▀    ▒▀█░  ▒▓█   ▓██▒░██████░░██░░▒████▓ ▒▓█   ▓██  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
    ░ ░▒ ▒  ░ ░▒ ▒     ░ ▐░  ░▒▒   ▓▒█░░ ▒░▓   ░▓   ▒▒▓  ▒ ░▒▒   ▓▒█  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
      ░  ▒    ░  ▒     ░ ░░  ░ ░   ▒▒ ░░ ░ ▒  ░ ▒ ░ ░ ▒  ▒ ░ ░   ▒▒     ░      ░ ▒ ▒░   ░▒ ░ ▒ 
    ░       ░            ░░    ░   ▒     ░ ░  ░ ▒ ░ ░ ░  ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░ ░     ░ ░           ░        ░  ░    ░    ░     ░          ░               ░ ░     ░     
{Style.RESET_ALL}''')
    card_number = input(f'\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Card number: {Style.RESET_ALL}').strip()
    card_number = card_number.replace(" ", "").replace("\t", "").replace("\n", "")
    print()
    if not card_number.isdigit():
        warn('Invalid card number — digits only.')
    elif luhn_check(card_number):
        success('Valid card — Luhn check passed.')
        success(f'Brand: {get_card_brand(card_number)}')
        for key, value in get_bin_info(card_number).items():
            info(f'{key}: {value}')
    else:
        warn('Invalid card — Luhn check failed.')
    print()
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to exit.{Style.RESET_ALL}')


def run():
    root_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    if root_path not in sys.path:
        sys.path.insert(0, root_path)   
    from utilities.core.shrek_ui import set_console_title
    set_console_title('CC Validator | Shrek Multi Tools')
    main()


if __name__ == "__main__":
    main()