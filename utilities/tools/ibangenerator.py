import os
import random
import sys
import hashlib
from time import sleep
from datetime import datetime, UTC
from colorama import Fore, Style, init

init(autoreset=True)

def success(text): print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def info(text):    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def warn(text):    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')

iban_formats = {
    'FR': {'length': 27, 'bban': 'BBBBBGSSSCCCCCCCCCCCCCCC', 'name': 'France'},
    'DE': {'length': 22, 'bban': 'BBBBBBBBCCCCCCCCCC', 'name': 'Germany'},
    'ES': {'length': 24, 'bban': 'BBBBGSSSCCCCCCCCCCCC', 'name': 'Spain'},
    'IT': {'length': 27, 'bban': 'KBBBBBBSSSSSCCCCCCCCCCCC', 'name': 'Italy'},
    'GB': {'length': 22, 'bban': 'BBBBSSSSSSCCCCCCCCCC', 'name': 'United Kingdom'},
    'BE': {'length': 16, 'bban': 'BBBCCCCCCCCCC', 'name': 'Belgium'},
    'NL': {'length': 18, 'bban': 'BBBBCCCCCCCCCC', 'name': 'Netherlands'},
    'CH': {'length': 21, 'bban': 'BBBBBKCCCCCCCCCCC', 'name': 'Switzerland'},
    'LU': {'length': 20, 'bban': 'BBBCCCCCCCCCCCCC', 'name': 'Luxembourg'},
    'PT': {'length': 25, 'bban': 'BBBBSSSSCCCCCCCCCCCBB', 'name': 'Portugal'},
    'AT': {'length': 20, 'bban': 'BBBBBCCCCCCCCCCCC', 'name': 'Austria'},
    'IE': {'length': 22, 'bban': 'BBBBSSSSSSCCCCCCCCCC', 'name': 'Ireland'}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_bban(country_code):
    format_str = iban_formats[country_code]['bban']
    return ''.join((str(random.randint(0, 9)) for _ in format_str))

def calculate_check_digits(country_code, bban):
    temp = bban + country_code + '00'
    numeric = ''.join((str(ord(c) - 55) if c.isalpha() else c for c in temp))
    return f'{98 - int(numeric) % 97:02d}'

def generate_iban(country_code):
    bban = generate_bban(country_code)
    check_digits = calculate_check_digits(country_code, bban)
    return f'{country_code}{check_digits}{bban}'

def generate_multiple_ibans(country_code, count=1):
    return [generate_iban(country_code) for _ in range(count)]

def menu():
    clear()
    print(f'''
{Fore.GREEN} 
      ██  ▄▄▄▄    ▄▄▄      ███▄    █      ▄████  ▓█████ ███▄    █ 
    ▒▓██▒▒█████▄ ▒████▄    ██ ▀█   █      ██▒ ▀█ ▓█   ▀ ██ ▀█   █ 
    ▒▒██▒▒██▒ ▄██▒██  ▀█▄ ▓██  ▀█ ██▒    ▒██░▄▄▄ ▒███  ▓██  ▀█ ██▒
    ░░██░▒██░█▀  ░██▄▄▄▄██▓██▒  ▐▌██▒    ░▓█  ██ ▒▓█  ▄▓██▒  ▐▌██▒
    ░░██░░▓█  ▀█▓▒▓█   ▓██▒██░   ▓██░    ▒▓███▀▒▒░▒████▒██░   ▓██░
     ░▓  ░▒▓███▀▒░▒▒   ▓▒█░ ▒░   ▒ ▒     ░▒   ▒ ░░░ ▒░ ░ ▒░   ▒ ▒ 
    ░ ▒ ░▒░▒   ░ ░ ░   ▒▒ ░ ░░   ░ ▒░     ░   ░ ░ ░ ░  ░ ░░   ░ ▒░
    ░ ▒ ░ ░    ░   ░   ▒     ░   ░ ░      ░   ░     ░     ░   ░ ░ 
      ░   ░            ░           ░          ░ ░   ░           ░ 
    ''')
    items = list(iban_formats.items())
    col_count = 2
    rows = -(-len(items) // col_count)
    for r in range(rows):
        line_parts = []
        for c in range(col_count):
            i = r + c * rows
            if i < len(items):
                num = f'{i + 1:02}'
                code, data = items[i]
                entry = f'    {Fore.GREEN}[{Fore.WHITE}{num}{Fore.GREEN}] {Fore.WHITE}{data["name"]:<22}'
                line_parts.append(entry)
        print(' '.join(line_parts) + Style.RESET_ALL)
    
    choice = input(f'\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Country (0 to quit): {Style.RESET_ALL}').strip('[]')
    if choice == '0':
        info('Closing generator...')
    else:
        try:
            country_code = list(iban_formats.keys())[int(choice) - 1]
        except Exception:
            warn('Invalid input.')
            return None
        
        count_input = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} How many IBANs to generate? (default=1): {Style.RESET_ALL}') or '1'
        try:
            count = max(1, int(count_input))
        except ValueError:
            count = 1
            
        clear()
        info(f' IBANs generated for {iban_formats[country_code]["name"]} \n')
        for iban in generate_multiple_ibans(country_code, count):
            success(iban)

def run():
    root_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    from utilities.core.shrek_ui import set_console_title
    set_console_title('IBAN Generator | Shrek Multi Tools')
    menu()
    input(f'\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to continue... {Style.RESET_ALL}')

if __name__ == '__main__':
    run()