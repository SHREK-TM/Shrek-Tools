# Shrek was proudly coded by Shrek™ [https://github.com/blackray207].
# Copyright © Shrek Multi Tools

########################################

import os
import re
import sys
import shutil
import requests
from time import sleep
from colorama import Fore
from zipfile import ZipFile
from bs4 import BeautifulSoup

from utilities.Settings.common import *

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

#########################################

def search_for_updates():
    clear()
    setTitle("New Update Found | Made by Shrek™")
    r = requests.get("https://github.com/blackray207/Shrek-Tools/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        print(
            f"""{Fore.YELLOW}
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.RED}Looks like this Shrek-Tools {THIS_VERSION} is outdated """.replace(
                "█", f"{Fore.WHITE}█{Fore.GREEN}"
            ),
            end="\n\n",
        )
        soup = BeautifulSoup(requests.get("https://github.com/blackray207/Shrek-Tools/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        print(f'                               {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Would You Like To Update To The Latest Version?')
        choice = input(f'                               {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}(Y/N)?: ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"\n                               {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE} Updating Shrek-Tools...")

            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("Shrek-Tools.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("Shrek-Tools.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Shrek-Tools.zip")
                cwd = os.getcwd()+'\\Shrek-Tools\\'
                shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'Shrek-Tools.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('Shrek-Tools')
                input(f"                               {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE} Update Successfully Finished!", end="")
                os.startfile("Shrek-Tools.exe")
                os._exit(0)

            else:
                new_version_source = requests.get("https://github.com/blackray207/Shrek-Tools/archive/refs/heads/master.zip")
                with open("Shrek-Tools-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Shrek-Tools-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Shrek-Tools-main.zip")
                cwd = os.getcwd()+'\\Shrek-Tools-main'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                input(f"                               {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE} Update Successfully Finished!")
                print(f'                               {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE} Press ENTER to View New Update!')
                if os.path.exists(os.getcwd()+'Setup.bat'):
                    os.startfile("Setup.bat")
                elif os.path.exists(os.getcwd()+'Start.bat'):
                    os.startfile("Start.bat")
                os._exit(0)
