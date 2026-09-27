# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import os
import sys
import json
import shutil
import threading
import subprocess
from pathlib import Path
from send2trash import send2trash
import customtkinter as ctk
import tkinter as tk
import hashlib
import time

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title

# ---- Thème Hacker (Vert & Noir) ----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

COLORS = {
    "bg": "#0a0a0a",
    "frame": "#111111",
    "frame_light": "#1a1a1a",
    "green_dark": "#00aa00",
    "green_bright": "#00ff00",
    "green_hover": "#00cc00",
    "red": "#ff0000",
    "text": "#00ff00",
    "text_secondary": "#33ff33",
    "border": "#00ff00"
}

APP_NAME = 'CC Cleaner | Shrek Multi Tools'
# Correction: utiliser root_path pour pointer vers data/ (selon la table)
DATA_DIR = Path(os.path.join(root_path, 'data'))
SPACE_FILE = DATA_DIR / 'space_freed.txt'
STARTUP_CFG = DATA_DIR / 'startup_config.json'
DATA_DIR.mkdir(exist_ok=True)

if not SPACE_FILE.exists():
    SPACE_FILE.write_text('0')

BROWSERS = {
    'Chrome': Path(os.getenv('LOCALAPPDATA')) / 'Google/Chrome/User Data',
    'Edge': Path(os.getenv('LOCALAPPDATA')) / 'Microsoft/Edge/User Data',
    'Brave': Path(os.getenv('LOCALAPPDATA')) / 'BraveSoftware/Brave-Browser/User Data',
    'Firefox': Path(os.getenv('APPDATA')) / 'Mozilla/Firefox/Profiles'
}

CACHE_DIRS = ['Cache', 'Code Cache', 'GPUCache']
SITE_DATA_DIRS = ['Cookies', 'Local Storage', 'Session Storage', 'Network/Cookies']
SESSION_FILES = ['Current Session', 'Current Tabs', 'Last Session', 'Last Tabs']
TEMP_PATHS = [os.getenv('TEMP'), 'C:\\Windows\\Temp']
RECENT = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Recent')
CRASH = os.path.join(os.getenv('LOCALAPPDATA'), 'CrashDumps')
PREFETCH = 'C:\\Windows\\Prefetch'

APPS = {
    'discord': [
        os.path.join(os.getenv('APPDATA'), 'discord', 'Cache'),
        os.path.join(os.getenv('APPDATA'), 'discord', 'Code Cache'),
        os.path.join(os.getenv('APPDATA'), 'discord', 'GPUCache')
    ],
    'steam': ['C:\\Program Files (x86)\\Steam\\appcache'],
    'spotify': [os.path.join(os.getenv('LOCALAPPDATA'), 'Spotify', 'Storage')],
    'epic': [os.path.join(os.getenv('LOCALAPPDATA'), 'EpicGamesLauncher', 'Saved', 'webcache')]
}

def get_size(path: Path) -> int:
    total = 0
    if path.is_file():
        return path.stat().st_size
    else:
        for p in path.rglob('*'):
            if p.is_file():
                try:
                    total += p.stat().st_size
                except:
                    pass
        return total

def delete_path(path: Path) -> int:
    if not path.exists():
        return 0
    else:
        try:
            size = get_size(path)
            if path.is_file():
                path.unlink(missing_ok=True)
                return size
            else:
                shutil.rmtree(path, ignore_errors=True)
                return size
        except:
            return 0

def clean_folder(path, filter_ext=None, log=None):
    freed = 0
    if not path or not os.path.exists(path):
        return 0
    else:
        for root, _, files in os.walk(path):
            for f in files:
                if filter_ext and (not f.endswith(filter_ext)):
                    continue
                try:
                    fp = os.path.join(root, f)
                    freed += os.path.getsize(fp)
                    send2trash(fp)
                    if log:
                        log(f'[DEL] {fp}')
                except:
                    pass
        return freed

def delete_file(path, log=None):
    try:
        size = os.path.getsize(path)
        send2trash(path)
        if log:
            log(f'[DEL] {path}')
        return size
    except:
        return 0

def load_total_freed() -> int:
    try:
        return int(SPACE_FILE.read_text())
    except:
        return 0

def save_total_freed(value: int):
    SPACE_FILE.write_text(str(value))

def fmt(size):
    for u in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f'{size:.2f} {u}'
        else:
            size /= 1024
    return f'{size:.2f} TB'

def close_browsers(log=None):
    processes = ['chrome.exe', 'msedge.exe', 'brave.exe', 'firefox.exe']
    for p in processes:
        subprocess.run(f'taskkill /f /im {p}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if log:
            log(f'[INFO] Closed {p}')

def clean_browser_cache(log=None):
    close_browsers(log)
    freed = 0
    for name, base in BROWSERS.items():
        if base.exists():
            for d in CACHE_DIRS:
                freed += delete_path(base / d)
    return freed

def clean_browser_history(log=None):
    close_browsers(log)
    freed = 0
    for name, base in BROWSERS.items():
        if name in ['Chrome', 'Edge', 'Brave']:
            freed += delete_path(base / 'History')
        else:
            if name == 'Firefox':
                for profile in base.glob('*.default*'):
                    freed += delete_path(profile / 'places.sqlite')
    return freed

def clean_browser_site_data(log=None):
    close_browsers(log)
    freed = 0
    for name, base in BROWSERS.items():
        if base.exists():
            for d in SITE_DATA_DIRS:
                freed += delete_path(base / d)
    return freed

def clean_browser_sessions(log=None):
    close_browsers(log)
    freed = 0
    for name, base in BROWSERS.items():
        if name in ['Chrome', 'Edge', 'Brave']:
            for f in ['Current Session', 'Current Tabs', 'Last Session', 'Last Tabs']:
                freed += delete_path(base / f)
        else:
            if name == 'Firefox':
                for profile in base.glob('*.default*'):
                    freed += delete_path(profile / 'recovery.jsonlz4')
    return freed

def clean_browser_max(log=None):
    close_browsers(log)
    freed = 0
    for name, base in BROWSERS.items():
        if not base.exists():
            continue
        else:
            if name in ['Chrome', 'Edge', 'Brave']:
                for profile_dir in base.glob('*'):
                    freed += delete_path(profile_dir)
                    if log:
                        log(f'[DEL] {profile_dir}')
            else:
                if name == 'Firefox':
                    for profile in base.glob('*.default*'):
                        freed += delete_path(profile)
                        if log:
                            log(f'[DEL] {profile}')
    return freed

def clean_windows_system(log=None):
    freed = 0
    for p in TEMP_PATHS + [RECENT, CRASH, PREFETCH]:
        freed += clean_folder(p, log=log)
    subprocess.run('ipconfig /flushdns', shell=True)
    subprocess.run('PowerShell -Command "Clear-RecycleBin -Force"', shell=True)
    return freed

def clean_apps(log=None):
    freed = 0
    for app in APPS.values():
        for p in app:
            freed += clean_folder(p, log=log)
    return freed

def load_startup():
    if not STARTUP_CFG.exists():
        return {}
    else:
        return json.load(open(STARTUP_CFG))

def save_startup(cfg):
    json.dump(cfg, open(STARTUP_CFG, 'w'), indent=2)

def install_startup():
    cmd = f'"{sys.executable}" "{os.path.abspath(__file__)}" --startup'
    subprocess.run(f'schtasks /create /f /sc onlogon /rl highest /tn BlueCleaner /tr {cmd}', shell=True, stdout=subprocess.DEVNULL)

# ---- Thème Hacker pour l'application ----
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

class BlueCleanerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry('900x700')
        self.configure(fg_color=COLORS["bg"])
        self.total_freed = load_total_freed()
        self.build_ui()
    
    def build_ui(self):
        # Title
        ctk.CTkLabel(
            self, 
            text='[ CC CLEANER ]', 
            font=('Consolas', 28, 'bold'), 
            text_color=COLORS["green_bright"]
        ).pack(pady=(15, 5))
        
        ctk.CTkLabel(
            self, 
            text='Shrek Multi Tools — System & Browser Cleaner', 
            font=('Consolas', 13), 
            text_color=COLORS["text_secondary"]
        ).pack(pady=(0, 10))
        
        # Tabs
        self.tabs = ctk.CTkTabview(
            self, 
            width=860, 
            height=350, 
            fg_color=COLORS["frame"], 
            corner_radius=10,
            segmented_button_selected_color=COLORS["green_dark"],
            segmented_button_selected_hover_color=COLORS["green_hover"],
            segmented_button_unselected_color=COLORS["frame_light"],
            segmented_button_unselected_hover_color=COLORS["frame_light"],
            text_color=COLORS["text"]
        )
        self.tabs.pack(padx=20, pady=(0, 10))
        
        for t in ['WINDOWS', 'ADVANCED', 'BROWSERS', 'APPLICATIONS', 'STARTUP']:
            self.tabs.add(t)
            self.tabs.tab(t).configure(fg_color=COLORS["frame"])
        
        tab_padx, tab_pady = (12, 6)
        
        # ---- Windows Tab ----
        self.w_temp_var = tk.BooleanVar()
        self.w_temp = ctk.CTkCheckBox(
            self.tabs.tab('WINDOWS'), 
            text='Temporary files', 
            text_color=COLORS["text"], 
            variable=self.w_temp_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.w_recent_var = tk.BooleanVar()
        self.w_recent = ctk.CTkCheckBox(
            self.tabs.tab('WINDOWS'), 
            text='Recent files', 
            text_color=COLORS["text"], 
            variable=self.w_recent_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.w_dns_var = tk.BooleanVar()
        self.w_dns = ctk.CTkCheckBox(
            self.tabs.tab('WINDOWS'), 
            text='Flush DNS cache', 
            text_color=COLORS["text"], 
            variable=self.w_dns_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.w_bin_var = tk.BooleanVar()
        self.w_bin = ctk.CTkCheckBox(
            self.tabs.tab('WINDOWS'), 
            text='Recycle bin', 
            text_color=COLORS["text"], 
            variable=self.w_bin_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        for cb in [self.w_temp, self.w_recent, self.w_dns, self.w_bin]:
            cb.pack(anchor='w', padx=tab_padx, pady=tab_pady)
        
        # ---- Advanced Tab ----
        self.a_crash_var = tk.BooleanVar()
        self.a_crash = ctk.CTkCheckBox(
            self.tabs.tab('ADVANCED'), 
            text='Crash dumps', 
            text_color=COLORS["text"], 
            variable=self.a_crash_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.a_prefetch_var = tk.BooleanVar()
        self.a_prefetch = ctk.CTkCheckBox(
            self.tabs.tab('ADVANCED'), 
            text='Prefetch (pro)', 
            text_color=COLORS["text"], 
            variable=self.a_prefetch_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        for cb in [self.a_crash, self.a_prefetch]:
            cb.pack(anchor='w', padx=tab_padx, pady=tab_pady)
        
        # ---- Browsers Tab ----
        self.b_cache_var = tk.BooleanVar()
        self.b_cache = ctk.CTkCheckBox(
            self.tabs.tab('BROWSERS'), 
            text='Browser cache', 
            text_color=COLORS["text"], 
            variable=self.b_cache_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.b_history_var = tk.BooleanVar()
        self.b_history = ctk.CTkCheckBox(
            self.tabs.tab('BROWSERS'), 
            text='Browser history', 
            text_color=COLORS["text"], 
            variable=self.b_history_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.b_cookies_var = tk.BooleanVar()
        self.b_cookies = ctk.CTkCheckBox(
            self.tabs.tab('BROWSERS'), 
            text='Cookies & Site Data', 
            text_color=COLORS["text"], 
            variable=self.b_cookies_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.b_super_var = tk.BooleanVar()
        self.b_super = ctk.CTkCheckBox(
            self.tabs.tab('BROWSERS'), 
            text='Super Clean (Reset Browsers)', 
            text_color=COLORS["text"], 
            variable=self.b_super_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        for cb in [self.b_cache, self.b_history, self.b_cookies, self.b_super]:
            cb.pack(anchor='w', padx=tab_padx, pady=tab_pady)
        
        # ---- Applications Tab ----
        self.app_discord_var = tk.BooleanVar()
        self.app_discord = ctk.CTkCheckBox(
            self.tabs.tab('APPLICATIONS'), 
            text='Discord cache', 
            text_color=COLORS["text"], 
            variable=self.app_discord_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.app_steam_var = tk.BooleanVar()
        self.app_steam = ctk.CTkCheckBox(
            self.tabs.tab('APPLICATIONS'), 
            text='Steam cache', 
            text_color=COLORS["text"], 
            variable=self.app_steam_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.app_spotify_var = tk.BooleanVar()
        self.app_spotify = ctk.CTkCheckBox(
            self.tabs.tab('APPLICATIONS'), 
            text='Spotify cache', 
            text_color=COLORS["text"], 
            variable=self.app_spotify_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        self.app_epic_var = tk.BooleanVar()
        self.app_epic = ctk.CTkCheckBox(
            self.tabs.tab('APPLICATIONS'), 
            text='Epic Games cache', 
            text_color=COLORS["text"], 
            variable=self.app_epic_var,
            border_color=COLORS["green_dark"],
            border_width=2,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            font=('Consolas', 12)
        )
        
        for cb in [self.app_discord, self.app_steam, self.app_spotify, self.app_epic]:
            cb.pack(anchor='w', padx=tab_padx, pady=tab_pady)
        
        # ---- Startup Tab ----
        cfg = load_startup()
        self.s_opts = {}
        for key in ['temp', 'browser_cache', 'browser_history', 'apps', 'recent', 'bin']:
            var = tk.BooleanVar(value=cfg.get(key, False))
            chk = ctk.CTkCheckBox(
                self.tabs.tab('STARTUP'), 
                text=f"{key.replace('_', ' ').capitalize()} at startup", 
                text_color=COLORS["text"], 
                variable=var,
                border_color=COLORS["green_dark"],
                border_width=2,
                fg_color=COLORS["green_dark"],
                hover_color=COLORS["green_hover"],
                font=('Consolas', 12)
            )
            chk.pack(anchor='w', padx=tab_padx, pady=tab_pady)
            self.s_opts[key] = var
        
        ctk.CTkButton(
            self.tabs.tab('STARTUP'), 
            text='▶ APPLY STARTUP SETTINGS', 
            command=self.save_startup, 
            fg_color=COLORS["green_dark"], 
            hover_color=COLORS["green_hover"], 
            text_color=COLORS["text"],
            font=('Consolas', 11, 'bold'),
            border_color=COLORS["border"],
            border_width=1
        ).pack(pady=8)
        
        # ---- Log Box ----
        self.logbox = ctk.CTkTextbox(
            self, 
            height=150, 
            fg_color=COLORS["frame"], 
            text_color=COLORS["text"], 
            corner_radius=8,
            font=('Consolas', 10),
            border_color=COLORS["border"],
            border_width=1
        )
        self.logbox.pack(padx=20, pady=(0, 10), fill='both', expand=True)
        
        # ---- Footer ----
        footer = ctk.CTkFrame(self, fg_color=COLORS["frame"], height=60)
        footer.pack(side='bottom', fill='x', padx=20, pady=(0, 10))
        footer.pack_propagate(False)
        
        self.space_label = ctk.CTkLabel(
            footer, 
            text=f'Storage Recover: {fmt(self.total_freed)}', 
            text_color=COLORS["green_bright"], 
            font=('Consolas', 13, 'bold')
        )
        self.space_label.pack(side='left', padx=15)
        
        ctk.CTkButton(
            footer, 
            text='▶ CLEAN ALL', 
            command=self.clean_all, 
            fg_color=COLORS["green_dark"], 
            hover_color=COLORS["green_hover"], 
            text_color=COLORS["text"],
            font=('Consolas', 11, 'bold'),
            border_color=COLORS["border"],
            border_width=1
        ).pack(side='right', padx=15, pady=10)
        
        ctk.CTkButton(
            footer, 
            text='▶ CLEAN', 
            command=self.start_clean, 
            fg_color=COLORS["green_dark"], 
            hover_color=COLORS["green_hover"], 
            text_color=COLORS["text"],
            font=('Consolas', 11, 'bold'),
            border_color=COLORS["border"],
            border_width=1
        ).pack(side='right', padx=15, pady=10)
        
        # Startup message
        self.log('[+] CC Cleaner v1.0 loaded')
        self.log('[*] Select cleaning options and click CLEAN')
    
    def log(self, m):
        self.logbox.insert('end', m + '\n')
        self.logbox.see('end')
    
    def start_clean(self):
        threading.Thread(target=self.clean, daemon=True).start()
    
    def clean_all(self):
        for var in [self.w_temp_var, self.w_recent_var, self.w_dns_var, self.w_bin_var,
                    self.a_crash_var, self.a_prefetch_var, self.b_cache_var, self.b_history_var,
                    self.b_cookies_var, self.b_super_var, self.app_discord_var, self.app_steam_var,
                    self.app_spotify_var, self.app_epic_var]:
            var.set(True)
        self.start_clean()
    
    def clean(self):
        freed = 0
        self.log('[*] Cleaning started...')
        
        if self.w_temp_var.get():
            for p in TEMP_PATHS:
                freed += clean_folder(p, log=self.log)
        
        if self.w_recent_var.get():
            freed += clean_folder(RECENT, log=self.log)
        
        if self.w_dns_var.get():
            subprocess.run('ipconfig /flushdns', shell=True)
            self.log('[+] DNS cache flushed')
        
        if self.w_bin_var.get():
            subprocess.run('PowerShell -Command "Clear-RecycleBin -Force"', shell=True)
            self.log('[+] Recycle bin cleared')
        
        if self.a_crash_var.get():
            freed += clean_folder(CRASH, log=self.log)
        
        if self.a_prefetch_var.get():
            freed += clean_folder(PREFETCH, log=self.log)
        
        if self.b_cache_var.get():
            freed += clean_browser_cache(log=self.log)
        
        if self.b_history_var.get():
            freed += clean_browser_history(log=self.log)
            freed += clean_browser_sessions(log=self.log)
        
        if self.b_cookies_var.get():
            freed += clean_browser_site_data(log=self.log)
        
        if self.b_super_var.get():
            freed += clean_browser_max(log=self.log)
        
        if self.app_discord_var.get():
            for p in APPS['discord']:
                freed += clean_folder(p, log=self.log)
        
        if self.app_steam_var.get():
            for p in APPS['steam']:
                freed += clean_folder(p, log=self.log)
        
        if self.app_spotify_var.get():
            for p in APPS['spotify']:
                freed += clean_folder(p, log=self.log)
        
        if self.app_epic_var.get():
            for p in APPS['epic']:
                freed += clean_folder(p, log=self.log)
        
        self.total_freed += freed
        save_total_freed(self.total_freed)
        self.space_label.configure(text=f'Storage Recover: {fmt(self.total_freed)}')
        self.log(f'[+] Freed this session: {fmt(freed)}')
    
    def save_startup(self):
        cfg = {k: v.get() for k, v in self.s_opts.items()}
        save_startup(cfg)
        install_startup()
        self.log('[*] Startup options saved')

def startup_clean():
    total = load_total_freed()
    freed = 0
    freed += clean_browser_max()
    freed += clean_windows_system()
    freed += clean_apps()
    save_total_freed(total + freed)

def run():
    set_console_title('CC Cleaner | Shrek Multi Tools')
    os.system('cls' if os.name == 'nt' else 'clear')
    if '--startup' in sys.argv:
        startup_clean()
    else:
        app = BlueCleanerApp()
        app.mainloop()

if __name__ == '__main__':
    run()