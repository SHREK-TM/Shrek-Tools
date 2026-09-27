# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import os
import sys
import random
import string
import winreg
import atexit
import signal
import subprocess
import shutil
from pathlib import Path
from colorama import init, Fore, Style
import ctypes
import time
import platform
import hashlib
from time import sleep
from datetime import datetime, UTC
root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title

init(autoreset=True)

global spoofed
global new_disk_serial
global original_hwids

original_hwids = {}
new_disk_serial = None
spoofed = False

def success(text): 
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def info(text):    
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def warn(text):    
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def print_centered(text, color=Fore.GREEN):
    """Centre un bloc de texte multi-lignes de manière uniforme pour préserver l'ASCII art."""
    term_width = shutil.get_terminal_size().columns
    lines = text.strip("\n").split("\n")
    
    # Calcul de la largeur maximale du bloc pour appliquer une marge uniforme à toutes les lignes
    max_len = max((len(line.rstrip()) for line in lines), default=0)
    padding = " " * max(0, (term_width - max_len) // 2)

    for line in lines:
        print(padding + color + line.rstrip() + Style.RESET_ALL)

def set_seed():
    """Set a random seed for reproducible HWID generation."""
    global SEED
    SEED = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
    random.seed(SEED)
    info(f'Seeding system initialized with seed: {SEED}')

def generate_cpu_id():
    """Generate a realistic CPU ID."""
    prefixes = ['AMD Ryzen 7 5800X', 'Intel Core i9-12900K', 'AMD Ryzen 5 5600X']
    return random.choice(prefixes)

def generate_gpu_id():
    """Generate a realistic GPU ID."""
    models = ['NVIDIA RTX 3080', 'AMD RX 6800', 'Intel Arc A770']
    return random.choice(models)

def generate_disk_serial():
    """Generate a realistic disk serial number."""
    manufacturers = ['WD', 'ST', 'SAMSUNG']
    prefix = random.choice(manufacturers)
    serial = ''.join((random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
    return f'{prefix}{serial}'

def get_current_cpu_id():
    """Get current CPU ID from registry."""
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0', 0, winreg.KEY_READ)
        cpu_id = winreg.QueryValueEx(key, 'Identifier')[0]
        winreg.CloseKey(key)
        return cpu_id if cpu_id else None
    except:
        return None

def get_current_gpu_id():
    """Get current GPU ID from registry."""
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000', 0, winreg.KEY_READ)
        gpu_id = winreg.QueryValueEx(key, 'DriverDesc')[0]
        winreg.CloseKey(key)
        return gpu_id if gpu_id else None
    except:
        return None

def get_current_disk_serial():
    """Get current disk serial number via vol or wmic."""
    try:
        output = subprocess.check_output('vol C:', shell=True, stderr=subprocess.DEVNULL).decode().strip()
        serial = output.split('Volume Serial Number is ')[1].strip()
        return serial if serial else None
    except:
        try:
            output = subprocess.check_output('wmic diskdrive get SerialNumber', shell=True, stderr=subprocess.DEVNULL).decode().strip()
            for line in output.splitlines()[1:]:
                serial = line.strip()
                if serial:
                    return serial
            return None
        except:
            return None

def clean_game_data():
    """Clean game tracking data for popular games."""
    paths = [
        Path(os.getenv('APPDATA')) / 'FortniteGame', 
        Path(os.getenv('APPDATA')) / 'EpicGamesLauncher', 
        Path(os.getenv('LOCALAPPDATA')) / 'Riot Games', 
        Path(os.getenv('APPDATA')) / 'Minecraft', 
        Path(os.getenv('LOCALAPPDATA')) / 'Valorant'
    ]
    cleaned = False
    for path in paths:
        try:
            if path.exists():
                for item in path.glob('**/*'):
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item, ignore_errors=True)
                info(f'Cleaned game data at {path}')
                cleaned = True
        except:
            pass
    if not cleaned:
        warn('No game data found to clean.')
    return None

def backup_hwids():
    """Backup all available HWIDs in memory."""
    original_hwids['cpu'] = get_current_cpu_id()
    original_hwids['gpu'] = get_current_gpu_id()
    original_hwids['disk'] = get_current_disk_serial()
    info('Backing up original HWIDs:')
    for key, value in original_hwids.items():
        if value:
            info(f'    - {key.upper()}: {value}')
        else:
            warn(f'    - {key.upper()}: Failed to retrieve, will skip spoofing.')
    if not any(original_hwids.values()):
        warn('Failed to backup any HWIDs. Aborting.')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
    return False

def is_admin():
    """Check if the script is running with admin privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def spoof_hwids(simulate: bool=True):
    """Spoof CPU, GPU, and Disk HWIDs temporarily."""
    global new_disk_serial
    global spoofed
    if not is_admin() and (not simulate):
        warn('Admin privileges required for live spoofing. Run as administrator.')
        warn('Use run_as_admin.bat in the Shrek Tools folder to launch with admin rights.')
        input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
    return False

def restore_hwids():
    """Restore all original HWIDs from memory."""
    global spoofed
    if not spoofed:
        pass
    return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal_handler(sig, frame):
    """Handle Ctrl+C to restore HWIDs and return to menu."""
    if spoofed:
        warn('Ctrl+C detected. Restoring original HWIDs...')
        restore_hwids()
    clear_screen()
    main()

def display_menu():
    clear_screen()

    print('')
    print('')
    ascii_art = """
 ▄████  ▒█████    ██████ ▄▄▄█████▓     ███▄ ▄███▓ ▒█████  ▓█████▄  ▓█████
 ██▒ ▀█▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒    ▓██▒▀█▀ ██▒▒██▒  ██▒▒██▀ ██▌ ▓█   ▀
▒██░▄▄▄▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░    ▓██    ▓██░▒██░  ██▒░██   █▌ ▒███  
░▓█  ██▒██   ██░  ▒   ██▒░ ▓██▓ ░     ▒██    ▒██ ▒██   ██░░▓█▄   ▌ ▒▓█  ▄
▒▓███▀▒░ ████▓▒░▒██████▒▒  ▒██▒ ░     ▒██▒   ░██▒░ ████▓▒░░▒████▓ ▒░▒████
░▒   ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░       ░ ▒░   ░  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░░ ▒░ 
 ░   ░   ░ ▒ ▒░ ░ ░▒  ░ ░    ░        ░  ░      ░  ░ ▒ ▒░  ░ ▒  ▒ ░ ░ ░  
 ░   ░ ░ ░ ░ ▒  ░  ░  ░    ░          ░      ░   ░ ░ ░ ▒   ░ ░  ░     ░  
     ░     ░ ░        ░                      ░       ░ ░     ░    ░   ░"""

    print_centered(ascii_art, color=Fore.GREEN)
    print_centered("Become a ghost. Spoof all HWIDs temporarily", color=Fore.WHITE)
    print('')
    warn('WARNING: Use in a VM for testing. Requires admin rights for live mode')
    warn('Check HWIDs: Run commands in CMD (admin)')
    print('')
    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Launch Spoofing (Simulation Mode)')
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Launch Spoofing (Live Mode - Admin Required)')
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Clean Game Data')
    print(f'    {Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}Exit')
    print('')

def main():
    """Main function for Phantom Veil Spoofer."""
    signal.signal(signal.SIGINT, signal_handler)
    atexit.register(lambda: restore_hwids() if spoofed else None)
    
    while True:
        display_menu()
        choice = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Select an option: {Style.RESET_ALL}').strip()
        
        if choice == '1':
            set_seed()
            backup_hwids()
            spoof_hwids(simulate=True)
            success('Simulation mode: HWIDs would be spoofed to:')
            info(f'    - CPU: {generate_cpu_id()}')
            info(f'    - GPU: {generate_gpu_id()}')
            info(f'    - Disk: {generate_disk_serial()}')
            input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
        elif choice == '2':
            if not is_admin():
                warn('Admin privileges required for live spoofing. Run as administrator.')
                input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
            else:
                set_seed()
                backup_hwids()
                spoof_hwids(simulate=False)
                input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
        elif choice == '3':
            clean_game_data()
            input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to return to menu... {Style.RESET_ALL}')
        elif choice == '4':
            info('Exiting Phantom Veil Spoofer...')
            restore_hwids()
            break
        else:
            warn('Invalid option. Please select 1-4.')
            time.sleep(1)

def run():
    set_console_title('Phantom Veil Spoofer | Shrek Multi Tools')
    clear_screen()
    main()

if __name__ == '__main__':
    run()