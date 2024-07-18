# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

####################################################################

import os
import sys
import os.path
import colorama
import requests
import webbrowser
from time import sleep
from colored import fg, attr
from requests.api import options
from colorama import Fore, Back, Style, init

colorama.init(autoreset=True)

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def menu():
    cls()
    print(f"""
{Fore.GREEN}
  
   ██▓    ▒█████   ▒█████   ▀██ ▄█▀ █    ██  ██▓███  
  ▓██▒   ▒██▒  ██▒▒██▒  ██▒  ██▄█▒  ██  ▓██▒▓██░  ██ 
  ▒██░   ▒██░  ██▒▒██░  ██▒ ▓███▄░ ▓██  ▒██░▓██░ ██▓▒
  ▒██░   ▒██   ██░▒██   ██░ ▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
  ░██████░ ████▓▒░░ ████▓▒░ ▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
  ░ ▒░▓  ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒ ▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
  ░ ░ ▒    ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░ ░▒░ ░ ░ ░▒ ░     
    ░ ░  ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░   ░░ ░ ░ ░░       
      ░      ░ ░      ░ ░   ░  ░      ░              

{Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Server Lookup
{Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] {Fore.WHITE}Exit
""")
menu()

option = input(f"""{Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE} """)

def fetch_data(option):
    if option == '1':
        cls()
        print(f"""
{Fore.GREEN}
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
        sleep(1)

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Token: """)
        }

        guildId = input(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Server ID: """)

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        print(f"""
{Fore.RESET}{Fore.GREEN}--------< Server Infomation >--------{Fore.RESET}

[{Fore.GREEN}Name{Fore.RESET}]      :   {response['name']} 
[{Fore.GREEN}ID{Fore.RESET}]        :   {response['id']}
[{Fore.GREEN}Owner{Fore.RESET}]     :   {owner['user']['username']}#{owner['user']['discriminator']} 
[{Fore.GREEN}Owner ID{Fore.RESET}]  :   {response['owner_id']}
[{Fore.GREEN}Members{Fore.RESET}]   :   {response['approximate_member_count']}
[{Fore.GREEN}Region{Fore.RESET}]    :   {response['region']}
[{Fore.GREEN}Icon URL{Fore.RESET}]  :   https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
""")
        os.system('pause')
        tool()

    elif option == '0':
        tool()

if __name__ == '__main__':
    fetch_data(option)
