# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import smtplib
import os
import sys
import re
import random
import time
import hashlib
import requests
import dns.resolver
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colorama import init, Fore, Style
from time import sleep
from datetime import datetime, UTC

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title
from utilities.core.paths import USERAGENTS_FILE

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
            # Efface la ligne du prompt
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.flush()
            # Affiche l'erreur
            warn('Please enter a valid value')
            time.sleep(0.8)
            # Efface la ligne d'erreur
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.flush()
            # Le prompt sera réaffiché par le while

# ---- User-Agent loader ----
def _load_user_agent():
    path = USERAGENTS_FILE
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as handle:
            user_agents = [line.strip() for line in handle if line.strip()]
        if user_agents:
            return random.choice(user_agents)
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

user_agent = _load_user_agent()

# ---- Site check functions ----
def Instagram(email):
    session = requests.Session()
    headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.instagram.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.instagram.com/'
    }
    data = {'email': email}
    response = session.get('https://www.instagram.com/accounts/emailsignup/', headers=headers)
    if response.status_code != 200:
        return False
    token = session.cookies.get('csrftoken')
    if not token:
        return False
    headers['x-csrftoken'] = token
    headers['Referer'] = 'https://www.instagram.com/accounts/emailsignup/'
    response = session.post(url='https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', headers=headers, data=data)
    if response.status_code == 200:
        if 'Another account is using the same email.' in response.text or 'email_is_taken' in response.text:
            return True
        return False
    return False

def Twitter(email):
    response = requests.get('https://api.twitter.com/i/users/email_available.json', params={'email': email})
    if response.status_code == 200:
        return response.json()['taken']
    return False

def Pinterest(email):
    response = requests.get('https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get/', params={'source_url': '/', 'data': '{\"options\": {\"email\": \"' + email + '\"}, \"context\": {}}'})
    if response.status_code == 200:
        data = response.json()['resource_response']
        if data['message'] == 'Invalid email.':
            return False
        return data['data'] is not False
    return False

def Imgur(email):
    headers = {'User-Agent': user_agent}
    data = {'email': email}
    response = requests.post('https://imgur.com/signin/ajax_email_available', headers=headers, data=data)
    if response.status_code == 200:
        data = response.json()['data']
        if data['available']:
            return False
        return True
    return False

def Patreon(email):
    headers = {'User-Agent': user_agent}
    data = {'email': email}
    response = requests.post('https://www.plurk.com/Users/isEmailFound', headers=headers, data=data)
    if response.status_code == 200:
        return 'True' in response.text
    return False

def Spotify(email):
    headers = {'User-Agent': user_agent}
    params = {'validate': '1', 'email': email}
    response = requests.get('https://spclient.wg.spotify.com/signup/public/v1/account', headers=headers, params=params)
    if response.status_code == 200:
        status = response.json()['status']
        return status == 20
    return False

def FireFox(email):
    data = {'email': email}
    response = requests.post('https://api.accounts.firefox.com/v1/account/status', data=data)
    if response.status_code == 200:
        return 'false' not in response.text
    return False

def LastPass(email):
    response = requests.get('https://lastpass.com/create_account.php', params={'check': 'avail', 'username': email})
    if response.status_code == 200:
        return 'no' in response.text
    return False

def Archive(email):
    data = {'input_name': 'username', 'input_value': email, 'input_validator': 'true', 'submit_by_js': 'true'}
    response = requests.post('https://archive.org/account/signup', data=data)
    if response.status_code == 200:
        return 'is already taken.' in response.text
    return False

def ProtonMail(email):
    data = {'Address': email}
    response = requests.post('https://account.proton.me/api/users/exists', json=data)
    if response.status_code == 200:
        return response.json().get('Exists', False)
    return False

sites = [Instagram, Twitter, Pinterest, Imgur, Patreon, Spotify, FireFox, LastPass, Archive, ProtonMail]

# ---- Email Tracker ----
def email_tracker():
    email = get_input('Enter email')
    print()
    for site in sites:
        result = site(email)
        if result:
            success(f'{site.__name__}: Found')
        else:
            info(f'{site.__name__}: Not Found')
    info('Tracker finished')
    print()
    input_prompt('Press Enter to continue')
    start()

# ---- Email Lookup (DNS) ----
def run_email_lookup():
    email = get_input('Enter Email')
    print()
    info('Recovering information...')
    info_dict = {}
    try:
        domain_all = email.split('@')[-1]
    except:
        domain_all = None
    try:
        name = email.split('@')[0]
    except:
        name = None
    try:
        domain = re.search('@([^@.]+)\\.', email).group(1)
    except:
        domain = None
    try:
        tld = f".{email.split('.')[-1]}"
    except:
        tld = None

    try:
        mx_records = dns.resolver.resolve(domain_all, 'MX')
        mx_servers = [str(record.exchange) for record in mx_records]
        info_dict['mx_servers'] = mx_servers
    except:
        mx_servers = None
        info_dict['mx_servers'] = None

    try:
        spf_records_raw = dns.resolver.resolve(domain_all, 'TXT')
        spf_records = [str(r) for r in spf_records_raw if 'spf' in str(r).lower()]
        info_dict['spf_records'] = spf_records if spf_records else None
    except:
        spf_records = None
        info_dict['spf_records'] = None

    try:
        dmarc_records_raw = dns.resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
        dmarc_records = [r.strings[0].decode('utf-8') if r.strings else '' for r in dmarc_records_raw]
        info_dict['dmarc_records'] = dmarc_records
    except:
        dmarc_records = None
        info_dict['dmarc_records'] = None

    if mx_servers:
        info_dict['google_workspace'] = any('google.com' in s for s in mx_servers)
        info_dict['microsoft_365'] = any('outlook.com' in s for s in mx_servers)
    else:
        info_dict['google_workspace'] = None
        info_dict['microsoft_365'] = None

    print(f'''
────────────────────────────────────────────────────────────────────────────────
Email      : {email}
Name       : {name}
Domain     : {domain}
TLD        : {tld}
Domain All : {domain_all}
Servers    : {(' / '.join(mx_servers) if mx_servers else None)}
SPF        : {spf_records}
DMARC      : {(' / '.join(dmarc_records) if dmarc_records else None)}
Workspace  : {info_dict['google_workspace']}
Microsoft  : {info_dict['microsoft_365']}
────────────────────────────────────────────────────────────────────────────────
''')
    print()
    input_prompt('Press Enter to continue')
    start()

# ---- Main Start Function ----
def start():
    clear_screen()
    print(f'''
{Fore.GREEN}
     █████  ███▄ ▄███▓ ▄▄▄       ██ ██▓       ▄▄▄█████▓ ▒█████   ▒█████   ██▓   
    ▓█   ▀ ▓██▒▀█▀ ██▒▒████▄   ▒▓██▓██▒       ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒   
    ▒███   ▓██    ▓██░▒██  ▀█▄ ░▒██▒██░       ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░   
    ▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██▒██░       ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░   
    ░▒████▒▒██▒   ░██▒ ▓█   ▓██ ░██░██████      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████
    ░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█ ░▓ ░ ▒░▓        ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  
     ░ ░  ░░  ░      ░  ░   ▒▒   ▒ ░ ░ ▒          ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  
       ░   ░      ░     ░   ▒    ▒   ░ ░        ░ ░    ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░  
       ░  ░       ░         ░    ░     ░                   ░ ░      ░ ░      ░  
''')
    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Spoofer Email    ')     
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Personalized Email  ')      
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Tracker Email   ')
    print(f'    {Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}Lockup Email        ')                    
    print(f'    {Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] {Fore.WHITE}Quit      ')
    print()
    choice = input_prompt('Choice')
    print()

    if choice == '1':
        victim_email = get_input("victim's email")
        print()

        try:
            Valeur = input_prompt('number of messages sent')
            Valeur = int(Valeur)
            objet = get_input('Subject')
            e_mail_message = get_input('Message to send')

            config_email = 'shrekdiscord@gmail.com'
            config_password = 'vdiyamviyzooclcm'
            config_server = 'smtp.gmail.com'
            config_server_port = 587

            def send_email():
                try:
                    multipart_message = MIMEMultipart()
                    multipart_message['Subject'] = objet
                    multipart_message['From'] = config_email
                    multipart_message['To'] = victim_email
                    multipart_message.attach(MIMEText(e_mail_message, 'plain'))
                    serveur_mail = smtplib.SMTP(config_server, config_server_port)
                    serveur_mail.starttls()
                    serveur_mail.login(config_email, config_password)
                    serveur_mail.sendmail(config_email, victim_email, multipart_message.as_string())
                    serveur_mail.quit()
                    return True
                except smtplib.SMTPAuthenticationError:
                    warn('ERROR: the password app or email address is expired')
                    warn('Please contact the creator or too many messages at once, try again later')
                    print()
                    input_prompt('Press Enter to continue')
                    start()
                    return False
                except smtplib.SMTPRecipientsRefused:
                    warn("ERROR: the recipient's email is invalid")
                    print()
                    input_prompt('Press Enter to continue')
                    start()
                    return False

            counter = 0
            while counter < Valeur:
                if send_email():
                    success('email sent!')
                    time.sleep(3)
                    counter += 1
                else:
                    break

            print()
            start()

        except ValueError:
            warn('ERROR: enter a number')
            print()
            start()

    elif choice == '2':
        email_send = get_input('email address sending the message')
        print()

        while True:
            password_email = input_prompt('app password')
            if len(password_email) == 16:
                break
            else:
                warn('ERROR: the app password must contain 16 characters')
                time.sleep(1)

        victim_email = get_input("victim's email")
        print()

        try:
            Valeur = input_prompt('number of messages sent')
            Valeur = int(Valeur)
            objet = get_input('Subject')
            e_mail_message = get_input('Message to send')

            config_email = email_send
            config_password = password_email
            config_server = 'smtp.gmail.com'
            config_server_port = 587

            def send_email():
                try:
                    multipart_message = MIMEMultipart()
                    multipart_message['Subject'] = objet
                    multipart_message['From'] = config_email
                    multipart_message['To'] = victim_email
                    multipart_message.attach(MIMEText(e_mail_message, 'plain'))
                    serveur_mail = smtplib.SMTP(config_server, config_server_port)
                    serveur_mail.starttls()
                    serveur_mail.login(config_email, config_password)
                    serveur_mail.sendmail(config_email, victim_email, multipart_message.as_string())
                    serveur_mail.quit()
                    return True
                except smtplib.SMTPAuthenticationError:
                    warn('ERROR: the app password or email address is invalid')
                    print()
                    input_prompt('Press Enter to continue')
                    start()
                    return False
                except smtplib.SMTPRecipientsRefused:
                    warn("ERROR: the recipient's email is invalid")
                    print()
                    input_prompt('Press Enter to continue')
                    start()
                    return False

            counter = 0
            while counter < Valeur:
                if send_email():
                    success('email sent!')
                    time.sleep(3)
                    counter += 1
                else:
                    break

            print()
            start()

        except ValueError:
            warn('ERROR: enter a number')
            print()
            start()

    elif choice == '3':
        email_tracker()

    elif choice == '4':
        run_email_lookup()

    elif choice == '0':
        info('Exiting...')
        sys.exit()

    else:
        warn('Invalid choice. Exiting.')
        sys.exit()

# ---- Run function ----
def run():
    clear_screen()
    set_console_title('Email Toolkit | Shrek Multi Tools')
    start()

if __name__ == '__main__':
    run()