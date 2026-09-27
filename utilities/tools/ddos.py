# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].

import os
import sys 
import webbrowser
from colorama import Fore, init

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import pause

init(autoreset=True)


def run():
    print(f"""
{Fore.GREEN}
    ▓█████▄ ▓█████▄  ▒█████    ██████ 
    ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
    ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
    ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
    ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
     ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
     ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
     ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
       ░       ░        ░ ░        ░  

""")
    input(f'''  {Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Press Enter to open the DDOS panel{Fore.RESET}''')
    webbrowser.open("https://stresserai.ru/hub")
    pause()
