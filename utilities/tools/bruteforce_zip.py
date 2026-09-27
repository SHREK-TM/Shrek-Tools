# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import zipfile
import os
import time
import psutil
from pystyle import *
from tqdm import tqdm
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime, UTC

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def success(text):
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def info(text):
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def warn(text):
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def select_file_dialog(title="Sélectionner un fichier", filetypes=None):
    """Ouvre une boîte de dialogue pour sélectionner un fichier."""
    if filetypes is None:
        filetypes = [("Tous les fichiers", "*.*")]
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        file_path = filedialog.askopenfilename(
            title=title,
            filetypes=filetypes
        )
        root.destroy()
        return file_path
    except Exception:
        return ""

def get_zip_info(zip_file_path):
    """Récupère des infos sur le fichier ZIP et vérifie le chiffrement."""
    try:
        with zipfile.ZipFile(zip_file_path) as zf:
            num_files = len(zf.namelist())
            if num_files == 0:
                return (0, 'Unknown', False, 'ZIP file is empty')
            
            compression_methods = {zf.getinfo(name).compress_type for name in zf.namelist()}
            if hasattr(zipfile, 'compressor_names'):
                main_method = zipfile.compressor_names.get(max(compression_methods, default=0), 'Unknown')
            else:
                compression_map = {0: 'Stored', 8: 'Deflated', 9: 'Deflate64', 12: 'BZIP2', 14: 'LZMA'}
                main_method = compression_map.get(max(compression_methods, default=0), 'Unknown')
            
            is_encrypted = any((zf.getinfo(name).flag_bits & 1 for name in zf.namelist()))
            
            if not is_encrypted and num_files > 0:
                try:
                    with zf.open(zf.namelist()[0], 'r'):
                        pass
                    is_encrypted = False
                except RuntimeError:
                    is_encrypted = True
            
            return (num_files, main_method, is_encrypted, None)
    except zipfile.BadZipFile:
        return (0, 'Unknown', False, 'Invalid ZIP file')

def estimate_max_time(total_words, words_per_sec=50000):
    """Estime le temps max pour le bruteforce."""
    return total_words / words_per_sec

def bruteforce(root_path):
    clear_screen()
    num_workers = 4
    ascii_art = (f'''{Fore.GREEN}
    ▓█████▄ ▓█████   ██████ ▄▄▄█████▓ ██▀███   ▒█████ ▓██   ██▓   ▒███████▒ ██▓ ██▓███
    ▒██▀ ██▌▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▒██  ██▒   ▒ ▒ ▒ ▄▀░▓██▒▓██░  ██▒
    ░██   █▌▒███   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒ ▒██ ██░   ░ ▒ ▄▀▒░ ▒██▒▓██░ ██▓▒
    ░▓█▄   ▌▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░ ░ ▐██▓░     ▄▀▒   ░░██░▒██▄█▓▒ ▒
    ░▒████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ ░ ██▒▓░   ▒███████▒░██░▒██▒ ░  ░
    ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░   ██▒▒▒    ░▒▒ ▓░▒░▒░▓  ▒▓▒░ ░  ░
    ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ▓██ ░▒░    ░░▒ ▒ ░ ▒ ▒ ░░▒ ░
    ░ ░  ░    ░   ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒  ▒ ▒ ░░     ░ ░ ░ ░ ░ ▒ ░░░
    ░       ░  ░      ░              ░         ░ ░  ░ ░          ░ ░     ░

    - {Fore.WHITE}ZIP Bruteforce Tool
    {Fore.GREEN}- {Fore.WHITE}Ultra-fast dictionary attack for password-protected ZIP files.
    {Fore.GREEN}- {Fore.WHITE}Multithreading with 4 workers for extreme performance.
    {Fore.GREEN}- {Fore.WHITE}Handles massive dictionaries and complex ZIPs with robust validation.
    {Fore.GREEN}- {Fore.WHITE}Tracks advanced stats: words tested, speed, per-thread efficiency, CPU/memory usage.
    {Fore.GREEN}- {Fore.WHITE}Saves comprehensive results to output\passwords.txt.
    {Fore.GREEN}- {Fore.WHITE}Press 'Q' to quit or 'R' to retry if the password is not found.
''')
    print(ascii_art)
    
    # --- Sélection du fichier ZIP ---
    zip_file_path = ''
    while not zip_file_path:
        print()
        choice = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Enter ZIP path (or press Enter to browse): {Style.RESET_ALL}').strip().strip('"\'')
        if not choice:
            zip_file_path = select_file_dialog("Sélectionner le fichier ZIP protégé", [("Fichiers ZIP", "*.zip"), ("Tous les fichiers", "*.*")])
            if zip_file_path:
                success(f'Selected ZIP: {zip_file_path}')
        else:
            zip_file_path = choice
        
        if not zip_file_path:
            warn('No file selected.')
            continue
        elif not os.path.exists(zip_file_path):
            warn('ZIP file not found.')
            zip_file_path = ''
        else:
            num_files, compression_method, is_encrypted, error = get_zip_info(zip_file_path)
            if error:
                warn(error)
                zip_file_path = ''
            elif not is_encrypted:
                warn('ZIP file is not password-protected.')
                zip_file_path = ''
            else:
                zip_size = os.path.getsize(zip_file_path) / 1048576
    
    # --- Sélection du dictionnaire ---
    dict_path = ''
    while not dict_path:
        print()
        choice = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Enter dictionary path (or press Enter to browse): {Style.RESET_ALL}').strip().strip('"\'')
        if not choice:
            dict_path = select_file_dialog("Sélectionner le fichier de dictionnaire", [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
            if dict_path:
                success(f'Selected dictionary: {dict_path}')
        else:
            dict_path = choice
        
        if not dict_path:
            warn('No file selected.')
        elif not os.path.exists(dict_path):
            warn('Dictionary file not found.')
            dict_path = ''
        else:
            break
    
    with open(dict_path, 'r', encoding='utf-8', errors='ignore') as f:
        total_lines = sum((1 for _ in f))
        dict_size = os.path.getsize(dict_path) / 1048576
        f.seek(0)
    
    est_time = estimate_max_time(total_lines)
    cpu_count = os.cpu_count() or 1
    print()
    info(f'ZIP file size: {zip_size:.2f} MB')
    info(f'Number of files in ZIP: {num_files}')
    info(f'ZIP compression method: {compression_method}')
    info(f'ZIP is encrypted: {is_encrypted}')
    info(f'Dictionary size: {dict_size:.2f} MB, {total_lines} words')
    info(f'Using {num_workers} threads (CPU cores available: {cpu_count})')
    info(f'Estimated max time: {est_time:.2f} seconds (at 50k words/sec)')
    print()
    
    start_time = time.time()
    words_tested = 0
    cpu_times_start = psutil.cpu_times_percent()
    output_dir = os.path.join(root_path, 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    def try_password(word, zip_file):
        try:
            zip_file.extractall(path=output_dir, pwd=word.encode())
            return word
        except RuntimeError:
            return
        except Exception as e:
            warn(f'Unexpected error: {e}')
    
    with zipfile.ZipFile(zip_file_path) as zip_file:
        pass
    
    with open(dict_path, 'r', encoding='utf-8', errors='ignore') as f:
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            for word in tqdm(f, desc='Bruteforcing ZIP', total=total_lines, unit='word'):
                word = word.strip()
                if not word:
                    continue
                words_tested += 1
                result = try_password(word, zip_file)
                if result:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    words_per_sec = words_tested / elapsed_time if elapsed_time > 0 else 0
                    words_per_thread = words_per_sec / num_workers if num_workers > 0 else 0
                    mem_usage = psutil.Process().memory_info().rss / 1048576
                    cpu_times_end = psutil.cpu_times_percent()
                    cpu_usage = (cpu_times_end.user - cpu_times_start.user) / elapsed_time * 100 if elapsed_time > 0 else 0
                    print()
                    success(f'Password found: {word}')
                    info(f'Time taken: {elapsed_time:.2f} seconds')
                    info(f'Words tested: {words_tested} ({words_tested / total_lines * 100:.2f}%)')
                    info(f'Average speed: {words_per_sec:.2f} words/sec')
                    info(f'Speed per thread: {words_per_thread:.2f} words/sec')
                    info(f'Approx. CPU usage: {cpu_usage:.2f}%')
                    info(f'Approx. memory usage: {mem_usage:.2f} MB')
                    info(f'ZIP files extracted: {num_files}')
                    info(f'ZIP compression method: {compression_method}')
                    with open(os.path.join(output_dir, 'passwords.txt'), 'w') as out_file:
                        out_file.write(f'Password: {word}\n')
                        out_file.write(f'Time taken: {elapsed_time:.2f} seconds\n')
                        out_file.write(f'Words tested: {words_tested} ({words_tested / total_lines * 100:.2f}%)\n')
                        out_file.write(f'Average speed: {words_per_sec:.2f} words/sec\n')
                        out_file.write(f'Speed per thread: {words_per_thread:.2f} words/sec\n')
                        out_file.write(f'Approx. CPU usage: {cpu_usage:.2f}%\n')
                        out_file.write(f'Approx. memory usage: {mem_usage:.2f} MB\n')
                        out_file.write(f'ZIP files extracted: {num_files}\n')
                        out_file.write(f'ZIP compression method: {compression_method}\n')
                    input(f"\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Data saved to {os.path.join(output_dir, 'passwords.txt')}. Press Enter to continue.{Style.RESET_ALL}")
                    return True
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    words_per_sec = words_tested / elapsed_time if elapsed_time > 0 else 0
    words_per_thread = words_per_sec / num_workers if num_workers > 0 else 0
    mem_usage = psutil.Process().memory_info().rss / 1048576
    cpu_times_end = psutil.cpu_times_percent()
    cpu_usage = (cpu_times_end.user - cpu_times_start.user) / elapsed_time * 100 if elapsed_time > 0 else 0
    print()
    warn('Password not found in the provided dictionary.')
    info(f'Words tested: {words_tested} ({words_tested / total_lines * 100:.2f}%)')
    info(f'Time taken: {elapsed_time:.2f} seconds')
    info(f'Average speed: {words_per_sec:.2f} words/sec')
    info(f'Speed per thread: {words_per_thread:.2f} words/sec')
    info(f'Approx. CPU usage: {cpu_usage:.2f}%')
    info(f'Approx. memory usage: {mem_usage:.2f} MB')
    print()
    choice = input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Retry [R] or Quit [Q]? {Style.RESET_ALL}').lower()
    if choice == 'q':
        info('Exiting program.')
        exit()
    return False

def main(root_path):
    while True:
        if bruteforce(root_path):
            return None

def run():
    root_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    from utilities.core.shrek_ui import set_console_title
    set_console_title('ZIP Bruteforce | Shrek Multi Tools')
    main(root_path)

if __name__ == '__main__':
    run()