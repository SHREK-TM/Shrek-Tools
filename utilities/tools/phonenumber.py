import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime, UTC

init(autoreset=True)

def success(text): 
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def info(text):    
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def warn(text):    
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            status = 'Valid'
        else:
            warn('Invalid Phone Number!')
            input()
            return
        
        country_code = f'+{parsed_number.country_code}' if parsed_number.country_code else 'None'
        operator = carrier.name_for_number(parsed_number, 'fr') or 'None'
        number_type = phonenumbers.number_type(parsed_number)
        type_number = 'Mobile' if number_type == phonenumbers.PhoneNumberType.MOBILE else 'Fixe'
        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_info = timezones[0] if timezones else 'None'
        country = phonenumbers.region_code_for_number(parsed_number) or 'None'
        region = geocoder.description_for_number(parsed_number, 'fr') or 'None'
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL) or 'None'

        print()
        success(f'Status       : {status}')
        success(f'Formatted    : {formatted_number}')
        success(f'Country Code : {country_code}')
        success(f'Country      : {country}')
        success(f'Region       : {region}')
        success(f'Timezone     : {timezone_info}')
        success(f'Operator     : {operator}')
        success(f'Type Number  : {type_number}')
        print(f'\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        input()
        return
    except Exception:
        warn('Invalid format !')
        input()

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def run():
    root_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    from utilities.core.shrek_ui import set_console_title
    set_console_title('Phone Info | Shrek Multi Tools')
    
    clear_screen()
    print(f"""
{Fore.GREEN}
     ██▓███    ██░ ██  ▒█████   ███▄    █  ▓█████      ██ ███▄    █  ▒ ████▒ ▒█████  
    ▓██░  ██ ▒▓██░ ██ ▒██▒  ██▒ ██ ▀█   █  ▓█   ▀    ▒▓██ ██ ▀█   █ ▒▓██    ▒██▒  ██▒
    ▓██░ ██▓▒░▒██▀▀██ ▒██░  ██▒▓██  ▀█ ██▒ ▒███      ░▒██▓██  ▀█ ██▒░▒████  ▒██░  ██▒
    ▒██▄█▓▒ ▒ ░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒ ▒▓█  ▄     ░██▓██▒  ▐▌██▒░░▓█▒   ▒██   ██░
    ▒██▒ ░  ░ ░▓█▒░██▓░ ████▓▒░▒██░   ▓██░▒░▒████     ░██▒██░   ▓██░ ░▒█░   ░ ████▓▒░
    ▒▓▒░ ░  ░  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░░ ▒░      ░▓ ░ ▒░   ▒ ▒   ▒ ░   ░ ▒░▒░▒░ 
    ░▒ ░       ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░ ░        ▒ ░ ░░   ░ ▒░  ░       ░ ▒ ▒░ 
    ░░         ░  ░░ ░░ ░ ░ ▒     ░   ░ ░     ░        ▒    ░   ░ ░   ░ ░   ░ ░ ░ ▒  
               ░  ░  ░    ░ ░           ░ ░   ░        ░          ░             ░ ░  

""")
    
    tel = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Phone Number: {Style.RESET_ALL}')
    get_phone_info(tel)

if __name__ == "__main__":
    run()