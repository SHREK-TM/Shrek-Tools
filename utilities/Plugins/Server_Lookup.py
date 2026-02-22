import os
import requests
import colorama
from time import sleep
from colorama import Fore, init

init(autoreset=True)

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cls()
    print(f"""{Fore.GREEN}
          
   ██▓    ▒█████   ▒█████   ▀██ ▄█▀ █    ██  ██▓███  
  ▓██▒   ▒██▒  ██▒▒██▒  ██▒  ██▄█▒  ██  ▓██▒▓██░  ██ 
  ▒██░   ▒██░  ██▒▒██░  ██▒ ▓███▄░ ▓██  ▒██░▓██░ ██▓▒
  ▒██░   ▒██   ██░▒██   ██░ ▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
  ░██████░ ████▓▒░░ ████▓▒░ ▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
  ░ ▒░▓  ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒ ▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
  ░ ░ ▒    ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░ ░▒░ ░ ░ ░▒ ░     
    ░ ░  ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░   ░░ ░ ░ ░░       
      ░      ░ ░      ░ ░   ░  ░      ░                      
    """)
    
    token = input(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Token: ")
    guild_id = input(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Server ID: ")

    headers = {
        'Authorization': token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    print(f"\n{Fore.YELLOW}Fetching data...{Fore.RESET}")
    sleep(1)

    res = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}?with_counts=true", headers=headers)
    
    if res.status_code != 200:
        print(f"{Fore.RED}Error: Could not find server. Check your Token and ID.")
        return

    data = res.json()
    owner_id = data.get('owner_id')
    owner_res = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/members/{owner_id}", headers=headers)
    
    owner_name = "Unknown"
    if owner_res.status_code == 200:
        owner_data = owner_res.json()
        user = owner_data.get('user', {})
        owner_name = f"{user.get('username')}#{user.get('discriminator', '0000')}"

    print(f"""
{Fore.GREEN}--------< Server Information >--------{Fore.RESET}

[{Fore.GREEN}Name{Fore.RESET}]      :   {data.get('name')} 
[{Fore.GREEN}ID{Fore.RESET}]        :   {data.get('id')}
[{Fore.GREEN}Owner{Fore.RESET}]     :   {owner_name} 
[{Fore.GREEN}Owner ID{Fore.RESET}]  :   {owner_id}
[{Fore.GREEN}Members{Fore.RESET}]   :   {data.get('approximate_member_count')}
[{Fore.GREEN}Region{Fore.RESET}]    :   {data.get('region')}
[{Fore.GREEN}Icon URL{Fore.RESET}]  :   https://cdn.discordapp.com/icons/{guild_id}/{data.get('icon')}.webp?size=256
""")

if __name__ == '__main__':
    main()
