# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import requests
import threading
import time
import random
import json
import os
import concurrent.futures
from PIL import Image, ImageTk, ImageDraw
import io
import urllib.parse
import base64
import math
import hashlib
import sys

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
  sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title

API_BASE = 'https://discord.com/api/v9'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0.0.0'}

# ---- Thème Hacker Shrek (Vert & Noir) ----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

SHREK_COLORS = {
    "bg": "#0a0a0a",
    "frame": "#111111",
    "frame_light": "#1a1a1a",
    "green_dark": "#00aa00",
    "green_bright": "#00ff00",
    "green_hover": "#00cc00",
    "red": "#ff0033",
    "red_hover": "#cc0028",
    "text": "#00ff00",
    "text_secondary": "#33ff33",
    "border": "#00ff00",
    "white": "#ffffff",
}

TRANSLATIONS = {
    'fr': {
        'app_title': 'Shrek Selfbot',
        'dashboard': 'Tableau de bord',
        'auto_reply': 'Réponse Auto',
        'status_rpc': 'Statut & RPC',
        'dm_friends': 'MP & Amis',
        'scripts': 'Scripts',
        'settings': 'Paramètres',
        'tools': 'Outils',
        'tools_desc': 'Outils avancés pour votre compte Discord',
        'connect_token': 'Connecter Token',
        'token_empty': 'Token vide',
        'token_invalid': 'Token invalide',
        'connected': 'Connecté avec succès',
        'error_connect': 'Erreur de connexion',
        'status_connected': 'Statut actuel',
        'change_status': 'Changer Statut',
        'rotator': 'Rotateur',
        'uptime': 'Temps actif',
        'refresh_dms': 'Rafraîchir DMs',
        'triggers': 'Déclencheurs (un par ligne)',
        'response': 'Réponse automatique',
        'delay': 'Délai (secondes)',
        'enable_auto': 'Activer Auto-Reply',
        'open_dms': 'DMs Ouverts',
        'friends_list': 'Liste d\'amis',
        'refresh_list': 'Rafraîchir la liste',
        'refresh_friends': 'Rafraîchir amis',
        'open_chat': 'Ouvrir Chat',
        'language': 'Langue',
        'theme_custom': 'Personnalisation du thème',
        'bg_color': 'Couleur de fond',
        'fg_color': 'Couleur de texte',
        'accent_color': 'Couleur d\'accent',
        'sidebar_color': 'Couleur de la barre latérale',
        'border_color_label': 'Couleur de bordure',
        'text_color_label': 'Couleur de texte principal',
        'secondary_text_color_label': 'Couleur de texte secondaire',
        'save_theme': 'Sauvegarder le thème',
        'reset_theme': 'Réinitialiser le thème',
        'colors_saved': 'Couleurs sauvegardées !',
        'rotate_speed': 'Vitesse (secondes)',
        'start_rotate': 'Démarrer Rotation',
        'stop_rotate': 'Arrêter Rotation',
        'clear_dms': 'Fermer tous les DMs',
        'cleanup_tools': 'Outils de nettoyage',
        'mass_leave': 'Quitter tous serveurs',
        'leave_groups': 'Quitter tous groupes',
        'token_info': 'Info Token'
    },
    'en': {
        'app_title': 'Shrek Selfbot',
        'dashboard': 'Dashboard',
        'auto_reply': 'Auto Reply',
        'status_rpc': 'Status & RPC',
        'dm_friends': 'DM & Friends',
        'scripts': 'Scripts',
        'settings': 'Settings',
        'tools': 'Tools',
        'tools_desc': 'Advanced tools for your Discord account',
        'connect_token': 'Connect Token',
        'token_empty': 'Token empty',
        'token_invalid': 'Token invalid',
        'connected': 'Connected successfully',
        'error_connect': 'Connection error',
        'status_connected': 'Current status',
        'change_status': 'Change Status',
        'rotator': 'Rotator',
        'uptime': 'Uptime',
        'refresh_dms': 'Refresh DMs',
        'triggers': 'Triggers (one per line)',
        'response': 'Auto response',
        'delay': 'Delay (seconds)',
        'enable_auto': 'Enable Auto-Reply',
        'open_dms': 'Open DMs',
        'friends_list': 'Friends List',
        'refresh_list': 'Refresh list',
        'refresh_friends': 'Refresh friends',
        'open_chat': 'Open Chat',
        'language': 'Language',
        'theme_custom': 'Theme customization',
        'bg_color': 'Background color',
        'fg_color': 'Text color',
        'accent_color': 'Accent color',
        'sidebar_color': 'Sidebar color',
        'border_color_label': 'Border color',
        'text_color_label': 'Primary text color',
        'secondary_text_color_label': 'Secondary text color',
        'save_theme': 'Save theme',
        'reset_theme': 'Reset theme',
        'colors_saved': 'Colors saved!',
        'rotate_speed': 'Speed (seconds)',
        'start_rotate': 'Start Rotation',
        'stop_rotate': 'Stop Rotation',
        'clear_dms': 'Close all DMs',
        'cleanup_tools': 'Cleanup tools',
        'mass_leave': 'Leave all servers',
        'leave_groups': 'Leave all groups',
        'token_info': 'Token Info'
    }
}

PRESET_COLORS = {
    'Rouge Vif': '#ef4444',
    'Orange Solaire': '#f97316',
    'Jaune Or': '#eab308',
    'Vert Émeraude': '#10b981',
    'Bleu Ciel': '#0ea5e9',
    'Bleu Roi': '#3b82f6',
    'Indigo Profond': '#6366f1',
    'Violet Mystique': '#8b5cf6',
    'Rose Bonbon': '#ec4899',
    'Cyan Futuriste': '#06b6d4',
    'Blanc Pur': '#ffffff',
    'Gris Anthracite': '#1f2937',
    'Noir Profond': '#000000',
    'Nuit Sombre': '#0d001a',
    'Violet Nuit': '#050010',
    'Lavande': '#a78bfa',
    'Pourpre': '#4c1d95'
}

class NightyUltimateSelfBot(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.load_config()
        self.title('Shrek Selfbot | Shrek Multi Tools')
        self.geometry('1100x700')
        self.resizable(False, False)
        self.token = ''
        self.headers = HEADERS.copy()
        self.user_data = {}
        self.my_id = None
        self.username = 'Shrek'
        self.discriminator = '0001'
        self.avatar_url = 'https://cdn.discordapp.com/embed/avatars/0.png'
        self.nitro = False
        self.servers_count = 0
        self.friends_count = 0
        self.uptime_start = time.time()
        self.commands_used = 0
        self.configure(fg_color=SHREK_COLORS["bg"])
        self.ensure_logo()
        self.triggers = self.config.get('auto_reply', {}).get('triggers', ['salut', 'cc', 'yo'])
        self.responses = ['yo bg ça va ?', 'cc enculé', 'quoi de neuf batard']
        self.auto_response_text = self.config.get('auto_reply', {}).get('response', 'yo bg ça va ?')
        self.reply_rules = self.config.get('auto_reply', {}).get('reply_rules', [])
        self.auto_sets = self.config.get('auto_reply', {}).get('auto_sets', [])
        self.active_auto_set_index = self.config.get('auto_reply', {}).get('active_set_index', 0)
        self.active_sets = self.config.get('auto_reply', {}).get('active_sets', None)
        if not isinstance(self.auto_sets, list) or len(self.auto_sets) == 0:
            base = {'triggers': self.triggers, 'response': self.auto_response_text}
            self.auto_sets = [base] + [{'triggers': [], 'response': ''} for _ in range(4)]
        else:
            if len(self.auto_sets) < 5:
                self.auto_sets += [{'triggers': [], 'response': ''} for _ in range(5 - len(self.auto_sets))]
        self.active_auto_set_index = max(0, min(4, int(self.active_auto_set_index)))
        if self.active_sets is None or not isinstance(self.active_sets, list):
            self.active_sets = [False] * 5
            self.active_sets[self.active_auto_set_index] = True
        if len(self.active_sets) < 5:
            self.active_sets += [False] * (5 - len(self.active_sets))
        self.polling_delay = self.config.get('auto_reply', {}).get('delay', 8.0)
        self.auto_reply_active = False
        self.monitored_channels = []
        self.guild_channels = []
        self.last_seen = {}
        self.joined_message_ids = set()
        self.processed_message_ids = set()
        self.session_id = os.urandom(16).hex()
        self.dm_refresh_interval = 60
        self.last_dm_refresh = 0
        self.nitro_sniper_active = False
        self.nitro_seen_message_ids = set()
        self.nitro_code_length = 16
        self.profiles = self.config.get('profiles', [])
        self.profile_rotator_running = False
        self.profile_rotation_interval = self.config.get('profile_rotation_interval', 3600)
        self.profile_rotation_range = self.config.get('profile_rotation_range', [0, max(0, len(self.profiles) - 1)])
        self.selected_profile_index = 0
        self.profile_variant_running = False
        self.sched_from_index_var = tk.IntVar(value=0)
        self.sched_to_index_var = tk.IntVar(value=max(0, len(self.profiles) - 1))
        self.sched_delay_min_var = tk.IntVar(value=10)
        try:
            self.rot_delay_label_var = tk.StringVar(value=f'{int(self.profile_rotation_interval / 60)} min')
        except:
            self.rot_delay_label_var = tk.StringVar(value='30 min')
        self.profile_interval_var = tk.IntVar(value=max(1, int(self.profile_rotation_interval / 60)))
        self.rotation_start_index_var = tk.IntVar(value=0)
        self.rotation_end_index_var = tk.IntVar(value=max(0, len(self.profiles) - 1))
        self.sched_delay_label_var = tk.StringVar(value=f'{int(self.sched_delay_min_var.get())} min')
        self.current_profile_index = 0
        self.profile_schedule = self.config.get('profile_schedule', [])
        self.message_schedule = self.config.get('message_schedule', [])
        self.msg_sched_delay_min_var = tk.IntVar(value=10)
        self.msg_sched_label_var = tk.StringVar(value=f'{int(self.msg_sched_delay_min_var.get())} min')
        self.msg_target_id_var = tk.StringVar()
        self.scheduler_running = False
        self.response_var = tk.StringVar(value=self.auto_response_text)
        self.interval_var = tk.DoubleVar(value=self.polling_delay)
        self.messages_received = 0
        self.responses_sent = 0
        self.running = False
        self.notifications = []
        self.stats_card = None
        self.delay_label_var = tk.StringVar(value=f'{self.interval_var.get():.1f}s')
        self.build_ui()
        self.protocol('WM_DELETE_WINDOW', self.on_close)
        threading.Thread(target=self.update_uptime, daemon=True).start()

    def ensure_logo(self):
        user_ico = os.path.join(root_path, 'utilities', 'tools', 'input', 'logo.ico')
        user_png = os.path.join(root_path, 'utilities', 'tools', 'input', 'logo.png')

        if os.path.exists(user_ico) or os.path.exists(user_png):
            if os.path.exists(user_ico):
                try:
                    self.iconbitmap(user_ico)
                except Exception:
                    pass
            im_src = user_png if os.path.exists(user_png) else user_ico
            try:
                self.iconphoto(True, tk.PhotoImage(file=im_src))
            except Exception:
                pass
            im_src = user_png if os.path.exists(user_png) else user_ico
            try:
                im = Image.open(im_src).resize((96, 96), Image.LANCZOS)
                self.blucore_logo_ctk = ctk.CTkImage(light_image=im, dark_image=im, size=(96, 96))
            except Exception:
                return None

    def load_config(self):
        self.config_file = os.path.join(root_path, 'input', 'config.json')
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            except:
                self.config = {}
        else:
            self.config = {}
        self.lang = self.config.get('language', 'fr')
        # Utiliser SHREK_COLORS au lieu de default_theme
        self.colors = self.config.get('theme', {})
        # Mapper les couleurs du fichier config vers SHREK_COLORS
        for k, v in SHREK_COLORS.items():
            if k not in self.colors:
                self.colors[k] = v

    def save_config(self):
        self.config['language'] = self.lang
        self.config['theme'] = self.colors
        self.config['auto_reply'] = {
            'active': self.running,
            'delay': self.interval_var.get(),
            'triggers': self.triggers,
            'response': self.response_var.get(),
            'reply_rules': self.reply_rules,
            'auto_sets': self.auto_sets,
            'active_set_index': self.active_auto_set_index,
            'active_sets': self.active_sets
        }
        self.config['profiles'] = self.profiles
        self.config['profile_rotation_interval'] = self.profile_rotation_interval
        self.config['profile_rotation_range'] = self.profile_rotation_range
        self.config['profile_schedule'] = self.profile_schedule
        self.config['message_schedule'] = self.message_schedule
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4)

    def t(self, key):
        return TRANSLATIONS.get(self.lang, TRANSLATIONS['fr']).get(key, key)

    def build_ui(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.canvas = tk.Canvas(self, highlightthickness=0, bg=SHREK_COLORS["bg"])
        self.canvas.pack(fill='both', expand=True)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.main_frame = ctk.CTkFrame(self, fg_color=SHREK_COLORS["bg"])
        self.main_frame.pack(fill='both', expand=True)
        self.sidebar = ctk.CTkFrame(self.main_frame, fg_color=SHREK_COLORS["frame"], width=280, corner_radius=0)
        self.sidebar.pack(side='left', fill='y')
        if hasattr(self, 'blucore_logo_ctk'):
            logo = ctk.CTkLabel(self.sidebar, text='', image=self.blucore_logo_ctk)
        else:
            logo = ctk.CTkLabel(self.sidebar, text='Shrek', font=('Montserrat', 42, 'bold'), text_color=SHREK_COLORS["green_bright"])
        logo.pack(pady=(60, 5))
        version = ctk.CTkLabel(self.sidebar, text='v1.0 Shrek Edition', font=('Roboto', 12), text_color=SHREK_COLORS["text_secondary"])
        version.pack(pady=(0, 40))
        menu = [
            ('📊 ' + self.t('dashboard'), self.show_dashboard),
            ('🤖 ' + self.t('auto_reply'), self.show_auto_reply),
            ('🎮 ' + self.t('status_rpc'), self.show_status_rpc),
            ('🛠️ ' + self.t('tools'), self.show_tools),
            ('👥 ' + self.t('dm_friends'), self.show_dm_friends),
            ('📜 ' + self.t('scripts'), self.show_scripts),
        ]
        for text, cmd in menu:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                font=('Roboto Medium', 14),
                fg_color='transparent',
                hover_color=SHREK_COLORS["border"],
                text_color=SHREK_COLORS["text"],
                anchor='w',
                corner_radius=25,
                height=50,
                command=cmd
            )
            btn.pack(fill='x', padx=15, pady=5)
        self.content = ctk.CTkFrame(self.main_frame, fg_color='transparent')
        self.content.pack(side='left', fill='both', expand=True, padx=40, pady=30)
        self.show_dashboard()

    def draw_gradient(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        for i in range(height):
            ratio = i / height
            r = int(13 + 35 * ratio)
            g = int(8 + 25 * ratio)
            b = int(35 + 90 * ratio)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, width, i, fill=color)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_columnconfigure(1, weight=1)
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_rowconfigure(1, weight=1)
        left_col = ctk.CTkFrame(self.content, fg_color='transparent')
        left_col.grid(row=0, column=0, rowspan=2, sticky='nsew', padx=20, pady=20)
        user_card = ctk.CTkFrame(left_col, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=1, border_color=SHREK_COLORS["border"])
        user_card.pack(fill='x', pady=(0, 20))
        self.header = ctk.CTkFrame(user_card, height=100, fg_color=SHREK_COLORS["green_dark"], corner_radius=20)
        self.header.pack(fill='x', padx=2, pady=2)
        self.avatar_label = ctk.CTkLabel(self.header, text='', width=100, height=100, fg_color='transparent')
        self.avatar_label.place(relx=0.12, rely=0.5, anchor='w')
        try:
            if hasattr(self, 'avatar_ctk'):
                self.avatar_label.configure(image=self.avatar_ctk)
            self.update_banner()
        except Exception:
            pass
        info_frame = ctk.CTkFrame(user_card, fg_color='transparent')
        info_frame.pack(fill='x', padx=20, pady=(40, 20))
        self.username_label = ctk.CTkLabel(info_frame, text=f'{self.username}#{self.discriminator}', font=('Arial', 22, 'bold'), text_color=SHREK_COLORS["text"])
        self.username_label.pack(anchor='w')
        self.id_label = ctk.CTkLabel(info_frame, text=f"User ID: {self.my_id or 'Not Connected'}", font=('Arial', 12), text_color=SHREK_COLORS["text_secondary"])
        self.id_label.pack(anchor='w')
        self.nitro_label = ctk.CTkLabel(info_frame, text='Nitro Status: Unknown', font=('Arial', 12), text_color=SHREK_COLORS["text_secondary"])
        self.nitro_label.pack(anchor='w', pady=(5, 0))
        stats_frame = ctk.CTkFrame(user_card, fg_color='transparent')
        stats_frame.pack(fill='x', padx=20, pady=20)
        
        def create_stat_bubble(parent, title, value):
            f = ctk.CTkFrame(parent, fg_color=SHREK_COLORS["bg"], corner_radius=15, border_width=1, border_color=SHREK_COLORS["border"])
            f.pack(side='left', fill='x', expand=True, padx=5)
            ctk.CTkLabel(f, text=value, font=('Arial', 20, 'bold'), text_color=SHREK_COLORS["green_bright"]).pack(pady=(10, 0))
            ctk.CTkLabel(f, text=title, font=('Arial', 10, 'bold'), text_color=SHREK_COLORS["text_secondary"]).pack(pady=(0, 10))
            return f
        
        self.stat_servers = create_stat_bubble(stats_frame, 'SERVERS', str(self.servers_count))
        self.stat_friends = create_stat_bubble(stats_frame, 'FRIENDS', str(self.friends_count))
        token_frame = ctk.CTkFrame(left_col, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=1, border_color=SHREK_COLORS["border"])
        token_frame.pack(fill='x', pady=0)
        ctk.CTkLabel(token_frame, text='Quick Connect', font=('Arial', 14, 'bold'), text_color=SHREK_COLORS["text"]).pack(anchor='w', padx=20, pady=(15, 5))
        self.token_entry = ctk.CTkEntry(token_frame, show='•', placeholder_text='Token here...', height=35, fg_color=SHREK_COLORS["bg"], border_color=SHREK_COLORS["border"])
        self.token_entry.pack(fill='x', padx=20, pady=5)
        ctk.CTkButton(token_frame, text='Connect', command=self.connect_token, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], corner_radius=20).pack(fill='x', padx=20, pady=(5, 15))
        right_col = ctk.CTkFrame(self.content, fg_color='transparent')
        right_col.grid(row=0, column=1, rowspan=2, sticky='nsew', padx=(0, 20), pady=20)
        notif_card = ctk.CTkFrame(right_col, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=1, border_color=SHREK_COLORS["border"])
        notif_card.pack(fill='both', expand=True, pady=(0, 20))
        ctk.CTkLabel(notif_card, text='🔔 Notification Center', font=('Arial', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=15)
        self.notif_list = ctk.CTkScrollableFrame(notif_card, fg_color='transparent')
        self.notif_list.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        self.refresh_notif_list()
        modules_card = ctk.CTkFrame(right_col, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=1, border_color=SHREK_COLORS["border"])
        modules_card.pack(fill='x')
        ctk.CTkLabel(modules_card, text='🧩 Modules Controls', font=('Arial', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=15)
        mods_frame = ctk.CTkFrame(modules_card, fg_color='transparent')
        mods_frame.pack(fill='x', padx=20, pady=(0, 20))
        self.switch_giveaway = ctk.CTkSwitch(mods_frame, text='Giveaway Joiner', command=self.toggle_giveaway, fg_color=SHREK_COLORS["bg"], progress_color=SHREK_COLORS["green_dark"])
        self.switch_giveaway.pack(pady=5, anchor='w')
        if getattr(self, 'giveaway_active', False):
            self.switch_giveaway.select()
        self.switch_nitro = ctk.CTkSwitch(mods_frame, text='Nitro Sniper (Beta)', command=self.toggle_nitro, fg_color=SHREK_COLORS["bg"], progress_color=SHREK_COLORS["green_dark"])
        self.switch_nitro.pack(pady=5, anchor='w')
        self.uptime_label = ctk.CTkLabel(right_col, text='Uptime: 00:00:00', font=('Consolas', 12), text_color=SHREK_COLORS["text_secondary"])
        self.uptime_label.pack(anchor='e')

    def refresh_notif_list(self):
        for w in self.notif_list.winfo_children():
            w.destroy()
        for msg in reversed(self.notifications[-15:]):
            row = ctk.CTkFrame(self.notif_list, fg_color=SHREK_COLORS["bg"], corner_radius=8)
            row.pack(fill='x', pady=4)
            ctk.CTkLabel(row, text=msg, font=('Consolas', 11), text_color=SHREK_COLORS["text"], anchor='w', justify='left').pack(side='left', padx=10, pady=5, fill='x')
            url = None
            if 'https://discord.com/gifts/' in msg:
                start = msg.find('https://discord.com/gifts/')
                end = msg.find(' ', start)
                url = msg[start:end] if end != -1 else msg[start:]
            elif 'https://discord.gift/' in msg:
                start = msg.find('https://discord.gift/')
                end = msg.find(' ', start)
                url = msg[start:end] if end != -1 else msg[start:]
            if url:
                ctk.CTkButton(row, text='Copier', width=70, height=24, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], corner_radius=12, command=lambda u=url: self.copy_to_clipboard(u)).pack(side='right', padx=8, pady=5)

    def toggle_giveaway(self):
        if self.switch_giveaway.get():
            self.giveaway_active = True
            self.log_msg('Giveaway Joiner: ON', 'success')
            threading.Thread(target=self.fetch_guild_channels, daemon=True).start()
            if not getattr(self, 'giveaway_thread_started', False):
                threading.Thread(target=self.giveaway_loop, daemon=True).start()
                self.giveaway_thread_started = True
        else:
            self.giveaway_active = False
            self.log_msg('Giveaway Joiner: OFF', 'info')

    def fetch_guild_channels(self):
        if not self.token:
            return None
        self.log_msg('🔍 Scan approfondi des serveurs...', 'info')
        r = requests.get(f'{API_BASE}/users/@me/guilds', headers=self.headers, timeout=10)
        if r.status_code == 200:
            guilds = r.json()
            all_channels = []
            
            def scan_guild(guild):
                if not getattr(self, 'giveaway_active', False) and not getattr(self, 'nitro_sniper_active', False):
                    return []
                rg = requests.get(f"{API_BASE}/guilds/{guild['id']}/channels", headers=self.headers, timeout=5)
                if rg.status_code == 200:
                    chans = rg.json()
                    text_chans = [c for c in chans if c.get('type') in [0, 5]]
                    gway = [c['id'] for c in text_chans if any(x in c['name'].lower() for x in ['give', 'event', 'drop', 'cadeau', 'gift', 'prix', 'win', 'gagne'])]
                    general = [c['id'] for c in text_chans if any(x in c['name'].lower() for x in ['general', 'chat', 'discutt', 'parle']) and c['id'] not in gway]
                    others = [c['id'] for c in text_chans if c['id'] not in gway and c['id'] not in general]
                    selection = gway + general + others
                    return selection
                return []
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                results = executor.map(scan_guild, guilds)
                for res in results:
                    all_channels.extend(res)
            
            self.guild_channels = list(set(all_channels))
            self.log_msg(f'✅ Giveaway Joiner: {len(self.guild_channels)} salons surveillés sur {len(guilds)} serveurs', 'success')
            if self.guild_channels:
                self.log_msg(f"ℹ️ Exemples: {', '.join(self.guild_channels[:5])}...", 'info')
        else:
            self.log_msg('❌ Erreur scan serveurs', 'error')

    def toggle_nitro(self):
        if self.switch_nitro.get():
            self.nitro_sniper_active = True
            self.log_msg('Nitro Sniper: ON', 'success')
            threading.Thread(target=self.refresh_dms, daemon=True).start()
            threading.Thread(target=self.fetch_guild_channels, daemon=True).start()
            if not getattr(self, 'nitro_thread_started', False):
                threading.Thread(target=self.nitro_sniper_loop, daemon=True).start()
                self.nitro_thread_started = True
        else:
            self.nitro_sniper_active = False
            self.log_msg('Nitro Sniper: OFF', 'info')

    def nitro_sniper_loop(self):
        while True:
            targets = (self.monitored_channels or []) + (getattr(self, 'guild_channels', []) or [])
            targets = list(set(targets))
            if getattr(self, 'nitro_sniper_active', False) and self.token and targets:
                with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                    executor.map(self.check_channel_gifts, targets)
                time.sleep(10)
                if random.random() < 0.1:
                    threading.Thread(target=self.fetch_guild_channels, daemon=True).start()
                    threading.Thread(target=self.refresh_dms, daemon=True).start()
            else:
                time.sleep(5)

    def extract_gift_link(self, text):
        if not text:
            return None
        for base in ['https://discord.com/gifts/', 'https://discord.gift/']:
            if base in text:
                s = text.find(base)
                e = text.find(' ', s)
                link = text[s:e] if e != -1 else text[s:]
                code = link.split('/')[-1].strip()
                if len(code) == self.nitro_code_length:
                    return link
        return None
    
    def check_channel_gifts(self, channel_id):
        try:
            r = requests.get(f'{API_BASE}/channels/{channel_id}/messages?limit=8', headers=self.headers, timeout=6)
            if r.status_code != 200:
                return
            messages = r.json()
            for msg in messages:
                mid = msg.get('id')
                if mid in self.nitro_seen_message_ids:
                    continue
                content = msg.get('content') or ''
                link = self.extract_gift_link(content)
                if not link:
                    embeds = msg.get('embeds') or []
                    for e in embeds:
                        text = (e.get('title') or '') + ' ' + (e.get('description') or '')
                        link = self.extract_gift_link(text)
                        if link:
                            break
                if link:
                    self.notifications.append(f'🎁 Nitro Gift: {link}')
                    if hasattr(self, 'notif_list') and self.notif_list.winfo_exists():
                        self.refresh_notif_list()
                    self.log_msg(f'Nitro Gift détecté: {link}', 'success')
                    self.nitro_seen_message_ids.add(mid)
        except Exception:
            return None

    def check_channel_giveaway(self, channel_id):
        if not getattr(self, 'giveaway_active', False):
            return None
        try:
            r = requests.get(f'{API_BASE}/channels/{channel_id}/messages?limit=10', headers=self.headers, timeout=5)
            if r.status_code == 200:
                messages = r.json()
                for msg in messages:
                    mid = msg.get('id')
                    if mid in self.processed_message_ids:
                        continue
                    
                    is_ongoing = False
                    content = (msg.get('content') or '').lower()
                    embeds = msg.get('embeds') or []
                    text = content
                    for e in embeds:
                        text += ' ' + (e.get('title') or '').lower() + ' ' + (e.get('description') or '').lower()
                    
                    if ('giveaway' in text or 'cadeau' in text or 'win' in text or 'gift' in text or '🎉' in text) and ('ended' not in text and 'terminé' not in text and 'no valid entrants' not in text):
                        if 'ends' in text or 'se termine' in text or 'fin' in text:
                            is_ongoing = True
                        else:
                            is_ongoing = True
                    
                    reacted = False
                    if 'reactions' in msg:
                        for reaction in msg['reactions']:
                            emoji_name = (reaction.get('emoji') or {}).get('name') or ''
                            if emoji_name.lower() in ['🎉', 'tada']:
                                if is_ongoing and not reaction.get('me') and mid not in self.joined_message_ids:
                                    self.join_giveaway(channel_id, mid, reaction['emoji'])
                                    self.joined_message_ids.add(mid)
                                    reacted = True
                                break
                    
                    if reacted:
                        self.log_msg(f'🎉 Giveaway rejoint via réaction (Salon: {channel_id})', 'success')
                    self.processed_message_ids.add(mid)
        except Exception:
            return None

    def click_giveaway_button(self, channel_id, message, button):
        try:
            payload = {
                'type': 3,
                'guild_id': message.get('guild_id'),
                'channel_id': channel_id,
                'message_id': message.get('id'),
                'application_id': message.get('application_id') or (message.get('author') or {}).get('id'),
                'session_id': self.session_id,
                'nonce': str(random.randint(100000000000000000, 999999999999999999)),
                'data': {'component_type': 2, 'custom_id': button.get('custom_id')}
            }
            ref = f"https://discord.com/channels/{message.get('guild_id') or '@me'}/{channel_id}"
            super_props = {
                'os': 'Windows', 'browser': 'Chrome', 'device': '',
                'system_locale': 'fr-FR', 'browser_user_agent': self.headers.get('User-Agent'),
                'browser_version': '131.0.0.0', 'os_version': '10',
                'referrer': 'https://discord.com/', 'referring_domain': 'discord.com',
                'referrer_current': ref, 'referring_domain_current': 'discord.com',
                'release_channel': 'stable', 'client_build_number': 0,
                'client_event_source': None
            }
            headers_local = self.headers.copy()
            headers_local.update({
                'Origin': 'https://discord.com',
                'Referer': ref,
                'X-Discord-Locale': self.lang if hasattr(self, 'lang') else 'fr',
                'X-Super-Properties': base64.b64encode(json.dumps(super_props).encode()).decode()
            })
            r = requests.post(f'{API_BASE}/interactions', headers=headers_local, json=payload, timeout=8)
            if r.status_code in [200, 204]:
                self.log_msg(f'Joined via button in {channel_id}', 'success')
                self.notifications.append(f'🎉 Joined via button in {channel_id}')
                if hasattr(self, 'notif_list') and self.notif_list.winfo_exists():
                    self.refresh_notif_list()
        except Exception:
            return None

    def giveaway_loop(self):
        self.log_msg('🚀 Giveaway Joiner: Mode Turbo Activé', 'success')
        while True:
            targets = (self.monitored_channels or []) + (getattr(self, 'guild_channels', []) or [])
            targets = list(set(targets))
            if getattr(self, 'giveaway_active', False) and self.token and targets:
                with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                    executor.map(self.check_channel_giveaway, targets)
                time.sleep(15)
                if random.random() < 0.1:
                    threading.Thread(target=self.fetch_guild_channels, daemon=True).start()
            else:
                time.sleep(5)

    def join_giveaway(self, channel_id, message_id, emoji):
        try:
            import urllib.parse
            if emoji['id']:
                emoji_str = f"{emoji['name']}:{emoji['id']}"
            else:
                emoji_str = emoji['name']
            emoji_encoded = urllib.parse.quote(emoji_str)
            r = requests.put(f'{API_BASE}/channels/{channel_id}/messages/{message_id}/reactions/{emoji_encoded}/@me', headers=self.headers, timeout=5)
            if r.status_code in [200, 204]:
                self.log_msg(f'Joined Giveaway in {channel_id}', 'success')
                self.notifications.append(f'🎉 Joined giveaway in {channel_id}')
                if hasattr(self, 'notif_list') and self.notif_list.winfo_exists():
                    self.refresh_notif_list()
        except Exception:
            return None

    def update_uptime(self):
        while True:
            try:
                elapsed = int(time.time() - self.uptime_start)
                days = elapsed // 86400
                hours = elapsed % 86400 // 3600
                mins = elapsed % 3600 // 60
                secs = elapsed % 60
                self.uptime_label.configure(text=f"{self.t('uptime')}: {days:02d}:{hours:02d}:{mins:02d}:{secs:02d}")
            except Exception:
                pass
            time.sleep(1)

    def update_avatar(self):
        if not self.user_data.get('avatar'):
            return None
        url = f"https://cdn.discordapp.com/avatars/{self.my_id}/{self.user_data['avatar']}.png?size=128"
        try:
            r = requests.get(url)
            img = Image.open(io.BytesIO(r.content)).convert('RGBA')
            size = 140
            img = img.resize((size, size), Image.LANCZOS)
            mask = Image.new('L', (size, size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, size, size), fill=255)
            circ = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            circ.paste(img, (0, 0), mask)
            try:
                hexc = SHREK_COLORS.get('green_bright', '#00ff00').lstrip('#')
                col = (int(hexc[0:2], 16), int(hexc[2:4], 16), int(hexc[4:6], 16), 255)
                ring = ImageDraw.Draw(circ)
                ring.ellipse((2, 2, size - 2, size - 2), outline=col, width=3)
            except Exception:
                pass
            self.avatar_ctk = ctk.CTkImage(light_image=circ, dark_image=circ, size=(size, size))
            self.avatar_label.configure(image=self.avatar_ctk)
        except Exception:
            return None

    def update_banner(self):
        try:
            if hasattr(self, 'header') and self.header.winfo_exists():
                banner_hash = self.user_data.get('banner')
                banner_color = self.user_data.get('banner_color')
                if banner_hash:
                    url = f'https://cdn.discordapp.com/banners/{self.my_id}/{banner_hash}.png?size=512'
                    r = requests.get(url, timeout=6)
                    img = Image.open(io.BytesIO(r.content))
                    w = max(600, self.header.winfo_width() or 1000)
                    h = 100
                    img = img.resize((w, h), Image.LANCZOS)
                    self.banner_ctk = ctk.CTkImage(light_image=img, dark_image=img, size=(w, h))
                    if not hasattr(self, 'banner_label') or not getattr(self, 'banner_label').winfo_exists():
                        self.banner_label = ctk.CTkLabel(self.header, text='', image=self.banner_ctk)
                        self.banner_label.pack(fill='both', expand=True)
                    else:
                        self.banner_label.configure(image=self.banner_ctk)
                elif banner_color:
                    self.header.configure(fg_color=banner_color)
        except Exception:
            if hasattr(self, 'user_data'):
                banner_color = self.user_data.get('banner_color')
                if banner_color and hasattr(self, 'header') and self.header.winfo_exists():
                    self.header.configure(fg_color=banner_color)

    def connect_token(self):
        self.token = self.token_entry.get().strip()
        if not self.token:
            messagebox.showerror('Erreur', self.t('token_empty'))
            return None
        self.headers['Authorization'] = self.token
        try:
            r = requests.get(f'{API_BASE}/users/@me', headers=self.headers, timeout=6)
            if r.status_code == 200:
                data = r.json()
                self.my_id = data['id']
                self.username = data['username']
                self.discriminator = data['discriminator']
                self.user_data = data
                self.nitro = data.get('premium_type', 0) > 0
                self.username_label.configure(text=f'{self.username}#{self.discriminator}')
                self.id_label.configure(text=f'User ID: {self.my_id}')
                self.nitro_label.configure(text=f"Nitro status: {'Nitro Boost' if self.nitro else 'Inactive'}", text_color='#00ff9d' if self.nitro else '#ff5555')
                self.update_avatar()
                self.update_banner()
                self.log_msg(self.t('connected'), 'success')
                self.load_guilds_and_friends()
            else:
                self.log_msg(f"{self.t('token_invalid')} : {r.status_code}", 'error')
        except Exception as e:
            self.log_msg(f"{self.t('error_connect')} : {e}", 'error')

    def load_guilds_and_friends(self):
        try:
            r = requests.get(f'{API_BASE}/users/@me/guilds', headers=self.headers, timeout=6)
            if r.status_code == 200:
                self.servers_count = len(r.json())
            r = requests.get(f'{API_BASE}/users/@me/relationships', headers=self.headers, timeout=6)
            if r.status_code == 200:
                friends = [rel for rel in r.json() if rel['type'] == 1]
                self.friends_count = len(friends)
            if self.stats_card is not None:
                self.stats_card.configure(text=f"{self.t('status_connected')}\nServers: {self.servers_count} | Friends: {self.friends_count}")
        except Exception:
            return None

    def show_auto_reply(self):
        self.clear_content()
        card = ctk.CTkFrame(self.content, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=2, border_color=SHREK_COLORS["border"])
        card.pack(fill='both', expand=True, pady=20, padx=20)
        title = ctk.CTkLabel(card, text=self.t('auto_reply'), font=('Consolas', 24, 'bold'), text_color=SHREK_COLORS["text"])
        title.pack(pady=15)
        refresh_frame = ctk.CTkFrame(card, fg_color='transparent')
        refresh_frame.pack(pady=(0, 10), padx=30, fill='x')
        ctk.CTkButton(refresh_frame, text=self.t('refresh_dms'), fg_color=SHREK_COLORS["border"], hover_color=SHREK_COLORS["green_dark"], corner_radius=20, command=self.refresh_dms).pack(anchor='w')
        triggers_frame = ctk.CTkFrame(card, fg_color='transparent')
        triggers_frame.pack(pady=10, padx=30, fill='x')
        ctk.CTkLabel(triggers_frame, text=self.t('triggers'), text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w')
        self.triggers_list = ctk.CTkTextbox(triggers_frame, height=80, text_color=SHREK_COLORS["text"])
        self.triggers_list.pack(pady=5, fill='x')
        self.triggers_list.delete('0.0', 'end')
        self.triggers_list.insert('0.0', '\n'.join(self.triggers))
        resp_frame = ctk.CTkFrame(card, fg_color='transparent')
        resp_frame.pack(pady=10, padx=30, fill='x')
        ctk.CTkLabel(resp_frame, text=self.t('response'), text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w')
        resp_entry = ctk.CTkEntry(resp_frame, textvariable=self.response_var, height=36, text_color=SHREK_COLORS["text"])
        resp_entry.pack(pady=5, fill='x')
        delay_frame = ctk.CTkFrame(card, fg_color='transparent')
        delay_frame.pack(pady=10, padx=30, fill='x')
        ctk.CTkLabel(delay_frame, text=self.t('delay'), text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=10)
        
        def on_delay_change(value):
            self.delay_label_var.set(f'{float(value):.1f}s')
        
        slider = ctk.CTkSlider(delay_frame, from_=5, to=30, variable=self.interval_var, command=on_delay_change, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"])
        slider.pack(side='left', padx=10, fill='x', expand=True)
        lbl_delay = ctk.CTkLabel(delay_frame, textvariable=self.delay_label_var, text_color=SHREK_COLORS["text"])
        lbl_delay.pack(side='left', padx=10)
        switch_frame = ctk.CTkFrame(card, fg_color='transparent')
        switch_frame.pack(pady=20)
        self.auto_reply_switch = ctk.CTkSwitch(switch_frame, text=self.t('enable_auto'), command=self.toggle_auto_reply, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"])
        self.auto_reply_switch.pack(pady=10)
        self.auto_stats = ctk.CTkLabel(switch_frame, text='Reçus: 0 | Répondu: 0', font=('Consolas', 14), text_color=SHREK_COLORS["text_secondary"])
        self.auto_stats.pack(pady=10)

    def refresh_dms(self):
        if not self.token:
            messagebox.showerror('Erreur', 'Connecte ton token d\'abord')
            return None
        try:
            r = requests.get(f'{API_BASE}/users/@me/channels', headers=self.headers, timeout=6)
            if r.status_code == 200:
                chans = r.json()
                self.monitored_channels = [c['id'] for c in chans if c.get('type') in [1, 3]]
                if self.running:
                    for channel_id in self.monitored_channels:
                        if channel_id not in self.last_seen:
                            try:
                                r2 = requests.get(f'{API_BASE}/channels/{channel_id}/messages?limit=1', headers=self.headers, timeout=5)
                                if r2.status_code == 200:
                                    msgs = r2.json()
                                    if msgs:
                                        self.last_seen[channel_id] = msgs[0]['id']
                            except Exception:
                                pass
                self.log_msg(f'DMs rafraîchis : {len(self.monitored_channels)} salons', 'success')
            else:
                self.log_msg(f'Échec refresh DMs : {r.status_code}', 'error')
        except Exception as e:
            self.log_msg(f'Erreur refresh DMs : {e}', 'error')

    def toggle_auto_reply(self):
        if self.auto_reply_switch.get():
            if not self.monitored_channels:
                try:
                    self.refresh_dms()
                except Exception:
                    pass
                if not self.monitored_channels:
                    messagebox.showwarning('Attention', 'Rafraîchis DMs d\'abord')
                    self.auto_reply_switch.deselect()
                    return None
            self.running = True
            self.log_msg('Auto-reply activé', 'success')
            self.triggers = [line.strip() for line in self.triggers_list.get('0.0', 'end').splitlines() if line.strip()]
            try:
                self.last_seen = {}
                for channel_id in self.monitored_channels:
                    try:
                        r = requests.get(f'{API_BASE}/channels/{channel_id}/messages?limit=1', headers=self.headers, timeout=5)
                        if r.status_code == 200:
                            msgs = r.json()
                            if msgs:
                                self.last_seen[channel_id] = msgs[0]['id']
                    except Exception:
                        continue
            except Exception:
                pass
            threading.Thread(target=self.auto_reply_loop, daemon=True).start()
        else:
            self.running = False
            self.log_msg('Auto-reply désactivé', 'info')

    def auto_reply_loop(self):
        while self.running:
            try:
                if time.time() - self.last_dm_refresh > self.dm_refresh_interval:
                    self.refresh_dms()
                    self.last_dm_refresh = time.time()
            except Exception:
                pass
            for channel_id in self.monitored_channels:
                try:
                    r = requests.get(f'{API_BASE}/channels/{channel_id}/messages?limit=5', headers=self.headers, timeout=5)
                    if r.status_code != 200:
                        continue
                    msgs = r.json()
                    for msg in reversed(msgs):
                        msg_id = msg['id']
                        if channel_id not in self.last_seen or msg_id > self.last_seen[channel_id]:
                            self.last_seen[channel_id] = msg_id
                            if msg['author']['id'] == self.my_id:
                                continue
                            content = msg.get('content', '').strip()
                            if content.lower() in [t.lower() for t in self.triggers]:
                                self.messages_received += 1
                                self.log_msg(f'Trigger : \'{content}\'', 'trigger')
                                send_r = requests.post(f'{API_BASE}/channels/{channel_id}/messages', headers=self.headers, json={'content': self.response_var.get()})
                                if send_r.status_code in [200, 201]:
                                    self.responses_sent += 1
                                    self.log_msg(f'Répondu : {self.response_var.get()}', 'success')
                                    self.update_auto_stats()
                                else:
                                    self.log_msg(f'Échec : {send_r.status_code}', 'error')
                                break
                except Exception:
                    continue
            time.sleep(self.interval_var.get())

    def update_auto_stats(self):
        self.auto_stats.configure(text=f'Reçus: {self.messages_received} | Répondu: {self.responses_sent}')

    def save_current_auto_set(self):
        idx = max(0, min(4, int(self.auto_set_index.get())))
        trigs = [line.strip() for line in self.triggers_list.get('0.0', 'end').splitlines() if line.strip()]
        resp = self.response_var.get().strip()
        self.auto_sets[idx] = {'triggers': trigs, 'response': resp}
        self.save_config()
        self.log_msg(f'Set {idx + 1} sauvegardé', 'success')

    def activate_current_auto_set(self):
        idx = max(0, min(4, int(self.auto_set_index.get())))
        self.active_auto_set_index = idx
        self.active_sets[idx] = True
        self.save_config()
        self.log_msg(f'Set {idx + 1} activé', 'success')

    def activate_selected_auto_sets(self):
        self.active_sets = [bool(v.get()) for v in self.set_check_vars]
        self.save_config()
        self.log_msg('Sélection de sets activée', 'success')

    def show_status_rpc(self):
        self.show_status_changer()

    def show_status_hub(self):
        self.clear_content()
        card = ctk.CTkFrame(self.content, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=2, border_color=SHREK_COLORS["border"])
        card.pack(fill='both', expand=True, pady=20, padx=20)
        title = ctk.CTkLabel(card, text=self.t('status_rpc'), font=('Consolas', 26, 'bold'), text_color=SHREK_COLORS["text"])
        title.pack(pady=12)
        tv = ctk.CTkTabview(card, width=900, height=480, fg_color=SHREK_COLORS["bg"], segmented_button_fg_color=SHREK_COLORS["frame"], segmented_button_selected_color=SHREK_COLORS["green_dark"], segmented_button_selected_hover_color=SHREK_COLORS["border"], segmented_button_unselected_color=SHREK_COLORS["bg"], segmented_button_unselected_hover_color=SHREK_COLORS["frame"], text_color=SHREK_COLORS["text"])
        tv.pack(fill='both', expand=True, padx=20, pady=10)
        tab_overview = tv.add('Aperçu')
        tab_profiles = tv.add('Profils')
        tab_scheduler = tv.add('Planificateur')
        overview = ctk.CTkFrame(tab_overview, fg_color='transparent')
        overview.pack(fill='both', expand=True, padx=20, pady=20)
        status_frame = ctk.CTkFrame(overview, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        status_frame.pack(fill='x', padx=10, pady=10)
        ctk.CTkLabel(status_frame, text=self.t('status_connected'), text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=10)
        self.status_var = tk.StringVar(value='online')
        status_combo = ctk.CTkComboBox(status_frame, values=['online', 'idle', 'dnd', 'invisible'], variable=self.status_var, width=150, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        status_combo.pack(side='left', padx=10)
        ctk.CTkButton(status_frame, text=self.t('change_status'), fg_color=SHREK_COLORS["border"], hover_color=SHREK_COLORS["green_dark"], corner_radius=20, command=self.change_status).pack(side='left', padx=12)
        ctk.CTkSwitch(status_frame, text=self.t('rotator'), command=self.toggle_status_rotator, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"]).pack(side='left', padx=12)
        custom_frame = ctk.CTkFrame(overview, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        custom_frame.pack(fill='x', padx=10, pady=10)
        ctk.CTkLabel(custom_frame, text='Custom Status', text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w', padx=10, pady=6)
        self.custom_status_text = tk.StringVar()
        self.custom_status_emoji = tk.StringVar()
        ctk.CTkEntry(custom_frame, textvariable=self.custom_status_text, height=36, placeholder_text='Texte', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=10, fill='x', expand=True)
        ctk.CTkEntry(custom_frame, textvariable=self.custom_status_emoji, height=36, width=140, placeholder_text='Emoji', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=10)
        ctk.CTkButton(custom_frame, text='Appliquer', width=120, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], corner_radius=20, command=self.apply_custom_status).pack(side='left', padx=10)
        ctk.CTkButton(custom_frame, text='Effacer', width=120, fg_color=SHREK_COLORS["bg"], hover_color=SHREK_COLORS["border"], corner_radius=20, command=self.clear_custom_status).pack(side='left', padx=10)
        profile_frame = ctk.CTkFrame(overview, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        profile_frame.pack(fill='x', padx=10, pady=10)
        ctk.CTkLabel(profile_frame, text='Profil', text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w', padx=10, pady=6)
        self.bio_var = tk.StringVar()
        self.accent_var = tk.StringVar()
        ctk.CTkEntry(profile_frame, textvariable=self.bio_var, height=36, placeholder_text='Bio (About Me)', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=10, fill='x', expand=True)
        ctk.CTkEntry(profile_frame, textvariable=self.accent_var, height=36, width=160, placeholder_text='#RRGGBB', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=10)
        ctk.CTkButton(profile_frame, text='Sauvegarder Profil', width=160, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], corner_radius=20, command=self.save_profile).pack(side='left', padx=10)
        profiles_card = ctk.CTkFrame(tab_profiles, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        profiles_card.pack(fill='both', expand=True, padx=20, pady=20)
        ctk.CTkLabel(profiles_card, text='Profils Multiples', font=('Consolas', 18, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=8)
        self.profiles_scroll = ctk.CTkScrollableFrame(profiles_card, fg_color='transparent', height=200)
        self.profiles_scroll.pack(fill='x', padx=10, pady=10)
        self.render_profiles_list()
        add_row = ctk.CTkFrame(profiles_card, fg_color='transparent')
        add_row.pack(fill='x', padx=10, pady=10)
        self.new_profile_name = tk.StringVar()
        self.new_profile_status = tk.StringVar(value='online')
        self.new_profile_text = tk.StringVar()
        self.new_profile_emoji = tk.StringVar()
        self.new_profile_bio = tk.StringVar()
        self.new_profile_accent = tk.StringVar()
        ctk.CTkEntry(add_row, textvariable=self.new_profile_name, placeholder_text='Nom profil', height=32, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=4)
        ctk.CTkComboBox(add_row, values=['online', 'idle', 'dnd', 'invisible'], variable=self.new_profile_status, width=120, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"]).pack(side='left', padx=4)
        ctk.CTkEntry(add_row, textvariable=self.new_profile_text, placeholder_text='Custom text', height=32, width=140, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=4)
        ctk.CTkEntry(add_row, textvariable=self.new_profile_emoji, placeholder_text='Emoji', height=32, width=100, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=4)
        ctk.CTkEntry(add_row, textvariable=self.new_profile_bio, placeholder_text='Bio', height=32, width=200, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=4)
        ctk.CTkEntry(add_row, textvariable=self.new_profile_accent, placeholder_text='#RRGGBB', height=32, width=110, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=4)
        ctk.CTkButton(add_row, text='Ajouter', width=90, command=self.add_profile, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        rotator_row = ctk.CTkFrame(profiles_card, fg_color='transparent')
        rotator_row.pack(fill='x', padx=10, pady=(0, 10))
        ctk.CTkLabel(rotator_row, text='Rotateur profils (sec):', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        self.profile_interval_var = tk.IntVar(value=int(self.profile_rotation_interval))
        
        def on_rot_delay_change(value):
            try:
                self.rot_delay_label_var.set(f'{int(float(value))} min')
            except:
                self.rot_delay_label_var.set('min')
        
        rot_slider = ctk.CTkSlider(rotator_row, from_=1, to=1440, variable=self.profile_interval_var, command=on_rot_delay_change, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"])
        rot_slider.pack(side='left', padx=5, fill='x', expand=True)
        ctk.CTkLabel(rotator_row, textvariable=self.rot_delay_label_var, text_color=SHREK_COLORS["text"]).pack(side='left', padx=6)
        ctk.CTkButton(rotator_row, text='Démarrer', width=100, command=self.toggle_profile_rotator, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=5)
        ctk.CTkButton(rotator_row, text='Arrêter', width=100, command=self.stop_profile_rotator, fg_color=SHREK_COLORS["bg"], hover_color=SHREK_COLORS["border"]).pack(side='left', padx=5)
        sched_card = ctk.CTkFrame(tab_scheduler, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        sched_card.pack(fill='both', expand=True, padx=20, pady=20)
        ctk.CTkLabel(sched_card, text='Planificateur de profils', font=('Consolas', 18, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=8)
        ctrl_row = ctk.CTkFrame(sched_card, fg_color='transparent')
        ctrl_row.pack(fill='x', padx=10, pady=10)
        self.schedule_profile_index = tk.IntVar(value=0)
        profile_names = [p.get('name', 'Profil') for p in self.profiles] or ['Profil 1']
        ctk.CTkComboBox(ctrl_row, values=profile_names, width=200, command=lambda v: self.schedule_profile_index.set(max(0, profile_names.index(v))), fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"]).pack(side='left', padx=6)
        self.schedule_delay_min = tk.IntVar(value=60)
        ctk.CTkLabel(ctrl_row, text='Dans (min):', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        ctk.CTkEntry(ctrl_row, textvariable=self.schedule_delay_min, width=80, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=6)
        ctk.CTkButton(ctrl_row, text='Planifier (relatif)', width=160, command=self.add_schedule_relative, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        abs_row = ctk.CTkFrame(sched_card, fg_color='transparent')
        abs_row.pack(fill='x', padx=10, pady=10)
        ctk.CTkLabel(abs_row, text='À heure (HH:MM):', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        self.schedule_clock = tk.StringVar()
        ctk.CTkEntry(abs_row, textvariable=self.schedule_clock, width=100, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=6)
        ctk.CTkButton(abs_row, text='Planifier (absolu)', width=160, command=self.add_schedule_absolute, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        self.schedule_switch = ctk.CTkSwitch(abs_row, text='Activer', command=self.toggle_scheduler, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"])
        self.schedule_switch.pack(side='left', padx=10)
        self.schedule_scroll = ctk.CTkScrollableFrame(sched_card, fg_color='transparent', height=220)
        self.schedule_scroll.pack(fill='x', padx=10, pady=10)
        self.render_schedule_list()

    def show_status_changer(self):
        self.clear_content()
        card = ctk.CTkFrame(self.content, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=2, border_color=SHREK_COLORS["border"])
        card.pack(fill='both', expand=True, pady=20, padx=20)
        title = ctk.CTkLabel(card, text=self.t('status_rpc'), font=('Consolas', 24, 'bold'), text_color=SHREK_COLORS["text"])
        title.pack(pady=15)
        status_frame = ctk.CTkFrame(card, fg_color='transparent')
        status_frame.pack(pady=20, padx=30, fill='x')
        ctk.CTkLabel(status_frame, text=self.t('status_connected'), text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=10)
        self.status_var = tk.StringVar(value='online')
        status_combo = ctk.CTkComboBox(status_frame, values=['online', 'idle', 'dnd', 'invisible'], variable=self.status_var, width=150, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        status_combo.pack(side='left', padx=10)
        change_btn = ctk.CTkButton(status_frame, text=self.t('change_status'), fg_color=SHREK_COLORS["border"], hover_color=SHREK_COLORS["green_dark"], corner_radius=20, command=self.change_status)
        change_btn.pack(side='left', padx=20)
        rotator_switch = ctk.CTkSwitch(status_frame, text=self.t('rotator'), command=self.toggle_status_rotator, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"])
        rotator_switch.pack(side='left', padx=20)
        custom_frame = ctk.CTkFrame(card, fg_color='transparent')
        custom_frame.pack(pady=10, padx=30, fill='x')
        ctk.CTkLabel(custom_frame, text='Custom Status', text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w')
        self.custom_status_text = tk.StringVar()
        self.custom_status_emoji = tk.StringVar()
        ctk.CTkEntry(custom_frame, textvariable=self.custom_status_text, height=36, placeholder_text='Texte', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=5, fill='x', expand=True)
        ctk.CTkEntry(custom_frame, textvariable=self.custom_status_emoji, height=36, width=140, placeholder_text='Emoji', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=5)
        profile_frame = ctk.CTkFrame(card, fg_color='transparent')
        profile_frame.pack(pady=10, padx=30, fill='x')
        ctk.CTkLabel(profile_frame, text='Profil', text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w')
        self.bio_var = tk.StringVar()
        self.accent_var = tk.StringVar()
        ctk.CTkEntry(profile_frame, textvariable=self.bio_var, height=36, placeholder_text='Bio (About Me)', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=5, fill='x', expand=True)
        ctk.CTkEntry(profile_frame, textvariable=self.accent_var, height=36, width=160, placeholder_text='#RRGGBB', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=5)
        ctk.CTkButton(profile_frame, text='Sauvegarder Profil', width=160, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], corner_radius=20, command=self.save_current_as_profile).pack(side='left', padx=5)
        apply_panel = ctk.CTkFrame(card, fg_color='transparent')
        apply_panel.pack(pady=4, padx=24, fill='x')
        ctk.CTkLabel(apply_panel, text='Appliquer:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        names_apply = [p.get('name', 'Profil') for p in self.profiles] or ['Profil 1']
        self.apply_profile_index_var = tk.IntVar(value=0)
        
        def on_apply_select(v):
            try:
                self.apply_profile_index_var.set(names_apply.index(v))
            except:
                self.apply_profile_index_var.set(0)
        
        self.apply_profile_combo = ctk.CTkComboBox(apply_panel, values=names_apply, width=160, command=on_apply_select, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        self.apply_profile_combo.set(names_apply[0])
        self.apply_profile_combo.pack(side='left', padx=6)
        ctk.CTkButton(apply_panel, text='Activer', width=100, command=lambda: self.apply_profile_index(int(self.apply_profile_index_var.get())), fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        rot_panel = ctk.CTkFrame(card, fg_color='transparent')
        rot_panel.pack(pady=4, padx=24, fill='x')
        ctk.CTkLabel(rot_panel, text='Rotation (min):', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        
        def on_rot_delay_change_top(value):
            try:
                self.rot_delay_label_var.set(f'{int(float(value))} min')
            except:
                self.rot_delay_label_var.set('min')
        
        rot_slider_top = ctk.CTkSlider(rot_panel, from_=1, to=1440, variable=self.profile_interval_var, command=on_rot_delay_change_top, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"])
        rot_slider_top.pack(side='left', padx=6, fill='x', expand=True)
        ctk.CTkLabel(rot_panel, textvariable=self.rot_delay_label_var, text_color=SHREK_COLORS["text"]).pack(side='left', padx=6)
        ctk.CTkLabel(rot_panel, text='De:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=(8, 2))
        names_rot_top = [p.get('name', 'Profil') for p in self.profiles] or ['Profil 1']
        self.rot_start_combo_top = ctk.CTkComboBox(rot_panel, values=names_rot_top, width=120, command=lambda v: self.rotation_start_index_var.set(names_rot_top.index(v) if v in names_rot_top else 0), fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        self.rot_start_combo_top.set(names_rot_top[min(self.rotation_start_index_var.get(), len(names_rot_top) - 1)])
        self.rot_start_combo_top.pack(side='left', padx=4)
        ctk.CTkLabel(rot_panel, text='À:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=(8, 2))
        self.rot_end_combo_top = ctk.CTkComboBox(rot_panel, values=names_rot_top, width=120, command=lambda v: self.rotation_end_index_var.set(names_rot_top.index(v) if v in names_rot_top else max(0, len(names_rot_top) - 1)), fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        self.rot_end_combo_top.set(names_rot_top[min(self.rotation_end_index_var.get(), len(names_rot_top) - 1)])
        self.rot_end_combo_top.pack(side='left', padx=4)
        ctk.CTkSwitch(rot_panel, text='Activer rotation', command=self.toggle_profile_rotator, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"]).pack(side='left', padx=8)
        sched_panel = ctk.CTkFrame(card, fg_color='transparent')
        sched_panel.pack(pady=4, padx=24, fill='x')
        ctk.CTkLabel(sched_panel, text='Planifier:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        names_sched_top = [p.get('name', 'Profil') for p in self.profiles] or ['Profil 1']
        self.sched_from_combo_top = ctk.CTkComboBox(sched_panel, values=names_sched_top, width=120, command=lambda v: self.sched_from_index_var.set(names_sched_top.index(v) if v in names_sched_top else 0), fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        self.sched_from_combo_top.set(names_sched_top[min(self.sched_from_index_var.get(), len(names_sched_top) - 1)])
        self.sched_from_combo_top.pack(side='left', padx=4)
        ctk.CTkLabel(sched_panel, text='→', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        self.sched_to_combo_top = ctk.CTkComboBox(sched_panel, values=names_sched_top, width=120, command=lambda v: self.sched_to_index_var.set(names_sched_top.index(v) if v in names_sched_top else max(0, len(names_sched_top) - 1)), fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        self.sched_to_combo_top.set(names_sched_top[min(self.sched_to_index_var.get(), len(names_sched_top) - 1)])
        self.sched_to_combo_top.pack(side='left', padx=4)
        ctk.CTkLabel(sched_panel, text='Dans (min):', text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=(8, 2))
        
        def on_sched_delay_change_top(value):
            try:
                self.sched_delay_label_var.set(f'{int(float(value))} min')
            except:
                self.sched_delay_label_var.set('min')
        
        sched_slider_top = ctk.CTkSlider(sched_panel, from_=1, to=1440, variable=self.sched_delay_min_var, command=on_sched_delay_change_top, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"])
        sched_slider_top.pack(side='left', padx=4, fill='x', expand=True)
        ctk.CTkLabel(sched_panel, textvariable=self.sched_delay_label_var, text_color=SHREK_COLORS["text"]).pack(side='left', padx=4)
        ctk.CTkButton(sched_panel, text='Valider', width=100, command=self.plan_scheduled_change, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        profiles_card = ctk.CTkFrame(card, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        profiles_card.pack(pady=15, padx=30, fill='x')
        ctk.CTkLabel(profiles_card, text='Profils Multiples', font=('Consolas', 18, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=8)
        self.profiles_scroll = ctk.CTkScrollableFrame(profiles_card, fg_color='transparent', height=180)
        self.profiles_scroll.pack(fill='x', padx=10, pady=10)
        self.render_profiles_list()
        sched_row = ctk.CTkFrame(profiles_card, fg_color='transparent')
        sched_row.pack(fill='x', padx=10, pady=10)
        ctk.CTkLabel(sched_row, text='Planifier:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        sched_names = [p.get('name', 'Profil') for p in self.profiles] or ['Profil 1']
        
        def set_sched_from(v):
            try:
                self.sched_from_index_var.set(sched_names.index(v))
            except:
                self.sched_from_index_var.set(0)
        
        def set_sched_to(v):
            try:
                self.sched_to_index_var.set(sched_names.index(v))
            except:
                self.sched_to_index_var.set(max(0, len(sched_names) - 1))
        
        ctk.CTkLabel(sched_row, text='De:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=(10, 2))
        self.sched_from_combo = ctk.CTkComboBox(sched_row, values=sched_names, width=160, command=set_sched_from, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        self.sched_from_combo.set(sched_names[min(self.sched_from_index_var.get(), len(sched_names) - 1)])
        self.sched_from_combo.pack(side='left', padx=4)
        ctk.CTkLabel(sched_row, text='À:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=(10, 2))
        self.sched_to_combo = ctk.CTkComboBox(sched_row, values=sched_names, width=160, command=set_sched_to, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        self.sched_to_combo.set(sched_names[min(self.sched_to_index_var.get(), len(sched_names) - 1)])
        self.sched_to_combo.pack(side='left', padx=4)
        ctk.CTkLabel(sched_row, text='Dans (min):', text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=(10, 2))
        
        def on_sched_delay_change(value):
            try:
                self.sched_delay_label_var.set(f'{int(float(value))} min')
            except:
                self.sched_delay_label_var.set('min')
        
        sched_slider = ctk.CTkSlider(sched_row, from_=1, to=1440, variable=self.sched_delay_min_var, command=on_sched_delay_change, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"])
        sched_slider.pack(side='left', padx=4, fill='x', expand=True)
        ctk.CTkLabel(sched_row, textvariable=self.sched_delay_label_var, text_color=SHREK_COLORS["text"]).pack(side='left', padx=6)
        ctk.CTkButton(sched_row, text='Valider', width=120, command=self.plan_scheduled_change, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        selected_row = ctk.CTkFrame(profiles_card, fg_color='transparent')
        selected_row.pack(fill='x', padx=10, pady=10)
        ctk.CTkLabel(selected_row, text='Profil sélectionné:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        selected_names = [p.get('name', 'Profil') for p in self.profiles] or ['Profil 1']
        
        def on_select_profile(v):
            try:
                self.selected_profile_index = selected_names.index(v)
                self.render_profile_variants_list()
            except:
                self.selected_profile_index = 0
        
        self.selected_profile_combo = ctk.CTkComboBox(selected_row, values=selected_names, width=200, command=on_select_profile, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"])
        self.selected_profile_combo.set(selected_names[0])
        self.selected_profile_combo.pack(side='left', padx=6)
        variants_card = ctk.CTkFrame(profiles_card, fg_color=SHREK_COLORS["bg"], corner_radius=12)
        variants_card.pack(fill='x', padx=10, pady=10)
        ctk.CTkLabel(variants_card, text='Variantes du profil', font=('Consolas', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=8)
        variant_row = ctk.CTkFrame(variants_card, fg_color='transparent')
        variant_row.pack(fill='x', padx=10, pady=6)
        self.variant_text_var = tk.StringVar()
        self.variant_emoji_var = tk.StringVar()
        self.variant_status_var = tk.StringVar(value='online')
        self.variant_delay_sec = tk.IntVar(value=5)
        ctk.CTkEntry(variant_row, textvariable=self.variant_text_var, placeholder_text='Texte', height=32, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=4, fill='x', expand=True)
        ctk.CTkEntry(variant_row, textvariable=self.variant_emoji_var, placeholder_text='Emoji', height=32, width=120, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=4)
        ctk.CTkComboBox(variant_row, values=['online', 'idle', 'dnd', 'invisible'], variable=self.variant_status_var, width=120, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], dropdown_fg_color=SHREK_COLORS["frame"]).pack(side='left', padx=4)
        ctk.CTkLabel(variant_row, text='Attendre (s):', text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=4)
        ctk.CTkEntry(variant_row, textvariable=self.variant_delay_sec, width=80, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=4)
        ctk.CTkButton(variant_row, text='Ajouter Variante', width=150, command=self.add_profile_variant, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        ctrl_row = ctk.CTkFrame(variants_card, fg_color='transparent')
        ctrl_row.pack(fill='x', padx=10, pady=6)
        ctk.CTkSwitch(ctrl_row, text='Prévisualiser', command=self.toggle_profile_variant_runner, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"]).pack(side='left', padx=6)
        self.variants_scroll = ctk.CTkScrollableFrame(variants_card, fg_color='transparent', height=180)
        self.variants_scroll.pack(fill='x', padx=10, pady=6)
        self.render_profile_variants_list()

    def save_current_as_profile(self):
        name = f'Profil {len(self.profiles) + 1}'
        status = getattr(self, 'status_var', tk.StringVar(value='online')).get()
        custom_text = getattr(self, 'custom_status_text', tk.StringVar()).get().strip()
        custom_emoji = getattr(self, 'custom_status_emoji', tk.StringVar()).get().strip()
        bio = getattr(self, 'bio_var', tk.StringVar()).get().strip()
        accent = getattr(self, 'accent_var', tk.StringVar()).get().strip()
        p = {'name': name, 'status': status, 'custom_text': custom_text, 'custom_emoji': custom_emoji, 'bio': bio, 'accent': accent}
        self.profiles.append(p)
        self.save_config()
        self.render_profiles_list()
        try:
            profile_names = [x.get('name', 'Profil') for x in self.profiles]
            names_for_combo = profile_names
            if hasattr(self, 'rot_start_combo'):
                self.rot_start_combo.configure(values=names_for_combo)
            if hasattr(self, 'rot_end_combo'):
                self.rot_end_combo.configure(values=names_for_combo)
            if hasattr(self, 'rot_start_combo_top'):
                self.rot_start_combo_top.configure(values=names_for_combo)
                self.rot_start_combo_top.set(names_for_combo[min(self.rotation_start_index_var.get(), len(names_for_combo) - 1)])
            if hasattr(self, 'rot_end_combo_top'):
                self.rot_end_combo_top.configure(values=names_for_combo)
                self.rot_end_combo_top.set(names_for_combo[min(self.rotation_end_index_var.get(), len(names_for_combo) - 1)])
            if hasattr(self, 'selected_profile_combo'):
                self.selected_profile_combo.configure(values=names_for_combo)
                self.selected_profile_combo.set(names_for_combo[-1])
                self.selected_profile_index = len(self.profiles) - 1
            if hasattr(self, 'rotation_end_index_var'):
                self.rotation_end_index_var.set(len(self.profiles) - 1)
                self.profile_rotation_range = [int(self.rotation_start_index_var.get()), int(self.rotation_end_index_var.get())]
            if hasattr(self, 'apply_profile_combo'):
                self.apply_profile_combo.configure(values=names_for_combo)
                self.apply_profile_combo.set(names_for_combo[-1])
                self.apply_profile_index_var.set(len(self.profiles) - 1)
            self.save_config()
        except Exception:
            pass
        self.log_msg('Profil sauvegardé dans la liste', 'success')
        self.render_profile_variants_list()
        vals = [x.get('name', 'Profil') for x in self.profiles] or ['Profil 1']
        if hasattr(self, 'sched_from_combo'):
            self.sched_from_combo.configure(values=vals)
            self.sched_from_combo.set(vals[min(self.sched_from_index_var.get(), len(vals) - 1)])
        if hasattr(self, 'sched_to_combo'):
            self.sched_to_combo.configure(values=vals)
            self.sched_to_combo.set(vals[min(self.sched_to_index_var.get(), len(vals) - 1)])
        if hasattr(self, 'sched_from_combo_top'):
            self.sched_from_combo_top.configure(values=vals)
            self.sched_from_combo_top.set(vals[min(self.sched_from_index_var.get(), len(vals) - 1)])
        if hasattr(self, 'sched_to_combo_top'):
            self.sched_to_combo_top.configure(values=vals)
            self.sched_to_combo_top.set(vals[min(self.sched_to_index_var.get(), len(vals) - 1)])
        return None

    def plan_message_schedule(self):
        try:
            chan = str(self.msg_target_id_var.get()).strip()
            delay = max(1, int(self.msg_sched_delay_min_var.get()))
            content = self.msg_content_box.get('1.0', 'end').strip()
        except:
            chan = ''
            delay = 10
            content = ''
        if not chan or not content:
            self.log_msg('ID ou message manquant', 'error')
            return None
        at = time.time() + delay * 60
        self.message_schedule.append({'at': at, 'channel_id': chan, 'content': content})
        self.save_config()
        if not self.scheduler_running:
            self.toggle_scheduler()
        self.render_msg_schedule_list()
        self.notifications.append(f'⏳ Message programmé: {chan} dans {delay} min')
        if hasattr(self, 'notif_list') and self.notif_list.winfo_exists():
            self.refresh_notif_list()

    def render_msg_schedule_list(self):
        if not hasattr(self, 'msg_sched_scroll'):
            return None
        for w in self.msg_sched_scroll.winfo_children():
            w.destroy()
        arr = sorted(self.message_schedule, key=lambda x: x.get('at', 0))
        for it in arr:
            row = ctk.CTkFrame(self.msg_sched_scroll, fg_color='transparent')
            row.pack(fill='x', padx=6, pady=4)
            eta = time.strftime('%H:%M', time.localtime(it.get('at', time.time())))
            chan = it.get('channel_id', '')
            ctk.CTkLabel(row, text=f'{eta} → {chan}', text_color=SHREK_COLORS["text"]).pack(side='left')
            ctk.CTkButton(row, text='Supprimer', width=100, fg_color=SHREK_COLORS["bg"], hover_color=SHREK_COLORS["border"], command=lambda ts=it.get('at'): self.delete_msg_schedule(ts)).pack(side='right')

    def delete_msg_schedule(self, at_ts):
        self.message_schedule = [x for x in self.message_schedule if x.get('at') != at_ts]
        self.save_config()
        self.render_msg_schedule_list()

    def change_status(self):
        if not self.token:
            messagebox.showerror('Erreur', self.t('token_empty'))
            return None
        payload = {'status': self.status_var.get()}
        try:
            r = requests.patch(f'{API_BASE}/users/@me/settings', headers=self.headers, json=payload, timeout=6)
            if r.status_code in (200, 204):
                self.log_msg(f'Statut → {self.status_var.get()}', 'success')
            else:
                self.log_msg(f'Échec : {r.status_code}', 'error')
        except Exception as e:
            self.log_msg(f'Erreur : {e}', 'error')

    def apply_custom_status(self):
        if not self.token:
            messagebox.showerror('Erreur', self.t('token_empty'))
            return None
        text = self.custom_status_text.get().strip()
        emoji = self.custom_status_emoji.get().strip()
        payload = {'custom_status': {'text': text or None, 'emoji_name': emoji or None}}
        try:
            r = requests.patch(f'{API_BASE}/users/@me/settings', headers=self.headers, json=payload, timeout=6)
            if r.status_code in (200, 204):
                self.log_msg('Custom status appliqué', 'success')
            else:
                self.log_msg(f'Échec custom status : {r.status_code}', 'error')
        except Exception as e:
            self.log_msg(f'Erreur : {e}', 'error')

    def clear_custom_status(self):
        if not self.token:
            messagebox.showerror('Erreur', self.t('token_empty'))
            return None
        payload = {'custom_status': None}
        try:
            r = requests.patch(f'{API_BASE}/users/@me/settings', headers=self.headers, json=payload, timeout=6)
            if r.status_code in (200, 204):
                self.log_msg('Custom status effacé', 'success')
            else:
                self.log_msg(f'Échec effacer : {r.status_code}', 'error')
        except Exception as e:
            self.log_msg(f'Erreur : {e}', 'error')

    def save_profile(self):
        if not self.token:
            messagebox.showerror('Erreur', self.t('token_empty'))
            return None
        bio = self.bio_var.get().strip()
        accent = self.accent_var.get().strip()
        color_int = None
        try:
            if accent.startswith('#') and len(accent) == 7:
                color_int = int(accent[1:], 16)
        except:
            color_int = None
        payload = {'bio': bio or '', 'accent_color': color_int}
        try:
            r = requests.patch(f'{API_BASE}/users/@me/profile', headers=self.headers, json=payload, timeout=6)
            if r.status_code in (200, 204):
                self.log_msg('Profil sauvegardé', 'success')
            else:
                self.log_msg(f'Échec profil : {r.status_code}', 'error')
        except Exception as e:
            self.log_msg(f'Erreur : {e}', 'error')

    def render_profiles_list(self):
        for w in self.profiles_scroll.winfo_children():
            w.destroy()
        for idx, p in enumerate(self.profiles):
            row = ctk.CTkFrame(self.profiles_scroll, fg_color='transparent')
            row.pack(fill='x', pady=4)
            name = p.get('name', 'Profil')
            status = p.get('status', 'online')
            ctk.CTkLabel(row, text=f'{name} [{status}]', text_color=SHREK_COLORS["text"]).pack(side='left', padx=6)
            ctk.CTkButton(row, text='Supprimer', width=90, fg_color=SHREK_COLORS["bg"], hover_color=SHREK_COLORS["border"], command=lambda i=idx: self.delete_profile_index(i)).pack(side='right', padx=4)
        if hasattr(self, 'selected_profile_combo'):
            try:
                vals = [p.get('name', 'Profil') for p in self.profiles] or ['Profil 1']
                self.selected_profile_combo.configure(values=vals)
                if self.selected_profile_index >= len(vals):
                    self.selected_profile_index = max(0, len(vals) - 1)
                self.selected_profile_combo.set(vals[self.selected_profile_index])
            except:
                return None
            
    def add_profile(self):
        p = {
            'name': self.new_profile_name.get().strip() or f'Profil {len(self.profiles) + 1}',
            'status': self.new_profile_status.get(),
            'custom_text': self.new_profile_text.get().strip(),
            'custom_emoji': self.new_profile_emoji.get().strip(),
            'bio': self.new_profile_bio.get().strip(),
            'accent': self.new_profile_accent.get().strip()
        }
        self.profiles.append(p)
        self.save_config()
        self.render_profiles_list()
        self.log_msg('Profil ajouté', 'success')

    def delete_profile_index(self, idx):
        if 0 <= idx < len(self.profiles):
            del self.profiles[idx]
            self.save_config()
            self.render_profiles_list()
            self.log_msg('Profil supprimé', 'info')

    def apply_profile_index(self, idx):
        if not self.token:
            messagebox.showerror('Erreur', self.t('token_empty'))
            return None
        if 0 <= idx < len(self.profiles):
            p = self.profiles[idx]
            self.current_profile_index = idx
            try:
                requests.patch(f'{API_BASE}/users/@me/settings', headers=self.headers, json={'status': p.get('status')}, timeout=6)
                requests.patch(f'{API_BASE}/users/@me/settings', headers=self.headers, json={'custom_status': {'text': p.get('custom_text') or None, 'emoji_name': p.get('custom_emoji') or None}}, timeout=6)
                color_int = None
                accent = p.get('accent', '')
                try:
                    if accent.startswith('#') and len(accent) == 7:
                        color_int = int(accent[1:], 16)
                except:
                    color_int = None
                requests.patch(f'{API_BASE}/users/@me/profile', headers=self.headers, json={'bio': p.get('bio', ''), 'accent_color': color_int}, timeout=6)
                self.log_msg(f"Profil appliqué: {p.get('name')}", 'success')
            except Exception as e:
                self.log_msg(f'Erreur appliquer profil: {e}', 'error')

    def toggle_profile_rotator(self):
        try:
            minutes = max(1, int(self.profile_interval_var.get()))
        except:
            minutes = 30
        self.profile_rotation_interval = minutes * 60
        start = int(getattr(self, 'rotation_start_index_var', tk.IntVar(value=0)).get())
        end = int(getattr(self, 'rotation_end_index_var', tk.IntVar(value=max(0, len(self.profiles) - 1))).get())
        start = max(0, min(start, len(self.profiles) - 1))
        end = max(0, min(end, len(self.profiles) - 1))
        if start > end:
            start, end = end, start
        self.profile_rotation_range = [start, end]
        self.current_profile_index = start
        if not self.profile_rotator_running:
            self.profile_rotator_running = True
            threading.Thread(target=self.profile_rotator_loop, daemon=True).start()
            self.log_msg('Rotateur profils démarré', 'success')
        else:
            self.profile_rotator_running = False
            self.log_msg('Rotateur profils arrêté', 'info')
        self.save_config()

    def plan_scheduled_change(self):
        try:
            from_idx = int(self.sched_from_index_var.get())
            to_idx = int(self.sched_to_index_var.get())
            delay_min = max(1, int(self.sched_delay_min_var.get()))
        except:
            from_idx = 0
            to_idx = max(0, len(self.profiles) - 1)
            delay_min = 10
        if self.profiles:
            self.apply_profile_index(from_idx)
            at = time.time() + delay_min * 60
            self.profile_schedule.append({'at': at, 'profile_index': to_idx})
            self.save_config()
            if not self.scheduler_running:
                self.toggle_scheduler()
            name_to = self.profiles[to_idx].get('name', 'Profil')
            self.notifications.append(f'⏳ Changement programmé: → {name_to} dans {delay_min} min')
            if hasattr(self, 'notif_list') and self.notif_list.winfo_exists():
                self.refresh_notif_list()

    def add_profile_variant(self):
        if not self.profiles:
            return None
        idx = int(self.selected_profile_index)
        if idx < 0 or idx >= len(self.profiles):
            idx = 0
        p = self.profiles[idx]
        if 'variants' not in p or not isinstance(p.get('variants'), list):
            p['variants'] = []
        try:
            delay = max(1, int(self.variant_delay_sec.get()))
        except:
            delay = 5
        v = {
            'text': (self.variant_text_var.get() or '').strip(),
            'emoji': (self.variant_emoji_var.get() or '').strip(),
            'status': self.variant_status_var.get(),
            'delay': delay
        }
        p['variants'].append(v)
        self.save_config()
        self.render_profile_variants_list()
        self.log_msg('Variante ajoutée', 'success')

    def render_profile_variants_list(self):
        if not hasattr(self, 'variants_scroll'):
            return None
        for w in self.variants_scroll.winfo_children():
            w.destroy()
        if not self.profiles:
            return None
        idx = int(self.selected_profile_index)
        if idx < 0 or idx >= len(self.profiles):
            idx = 0
        p = self.profiles[idx]
        items = p.get('variants', [])
        for i, it in enumerate(items):
            row = ctk.CTkFrame(self.variants_scroll, fg_color='transparent')
            row.pack(fill='x', pady=3)
            txt = it.get('text', '')
            em = it.get('emoji', '')
            st = it.get('status', 'online')
            dl = it.get('delay', 5)
            ctk.CTkLabel(row, text=f'[{i + 1}] {st} • {txt} {em} • {dl}s', text_color=SHREK_COLORS["text"]).pack(side='left', padx=6)
            ctk.CTkButton(row, text='Supprimer', width=90, fg_color=SHREK_COLORS["bg"], hover_color=SHREK_COLORS["border"], command=lambda k=i: self.delete_profile_variant(k)).pack(side='right', padx=4)

    def delete_profile_variant(self, i):
        if not self.profiles:
            return None
        idx = int(self.selected_profile_index)
        if idx < 0 or idx >= len(self.profiles):
            idx = 0
        p = self.profiles[idx]
        items = p.get('variants', [])
        if 0 <= i < len(items):
            del items[i]
            p['variants'] = items
            self.save_config()
            self.render_profile_variants_list()
            self.log_msg('Variante supprimée', 'info')

    def toggle_profile_variant_runner(self):
        self.profile_variant_running = not self.profile_variant_running
        if self.profile_variant_running:
            threading.Thread(target=self.profile_variant_loop, daemon=True).start()
            self.log_msg('Prévisualisation démarrée', 'success')
        else:
            self.log_msg('Prévisualisation arrêtée', 'info')

    def profile_variant_loop(self):
        while self.profile_variant_running:
            while True:
                if not self.profiles:
                    time.sleep(1)
                    continue
                idx = int(self.selected_profile_index)
                if idx < 0 or idx >= len(self.profiles):
                    idx = 0
                items = self.profiles[idx].get('variants', [])
                for it in items:
                    if not self.profile_variant_running:
                        break
                    try:
                        st = it.get('status', 'online')
                        tx = it.get('text', '')
                        em = it.get('emoji', '')
                        requests.patch(f'{API_BASE}/users/@me/settings', headers=self.headers, json={'status': st}, timeout=6)
                        requests.patch(f'{API_BASE}/users/@me/settings', headers=self.headers, json={'custom_status': {'text': tx or None, 'emoji_name': em or None}}, timeout=6)
                    except Exception:
                        pass
                    time.sleep(max(1, int(it.get('delay', 5))))

    def stop_profile_rotator(self):
        self.profile_rotator_running = False
        self.log_msg('Rotateur profils arrêté', 'info')

    def profile_rotator_loop(self):
        while self.profile_rotator_running:
            if self.profiles:
                start = self.profile_rotation_range[0] if isinstance(self.profile_rotation_range, list) else 0
                end = self.profile_rotation_range[1] if isinstance(self.profile_rotation_range, list) else max(0, len(self.profiles) - 1)
                start = max(0, min(start, len(self.profiles) - 1))
                end = max(0, min(end, len(self.profiles) - 1))
                if start > end:
                    start, end = end, start
                if self.current_profile_index < start or self.current_profile_index > end:
                    self.current_profile_index = start
                self.apply_profile_index(self.current_profile_index)
                if self.current_profile_index >= end:
                    self.current_profile_index = start
                else:
                    self.current_profile_index += 1
            time.sleep(self.profile_rotation_interval)

    def render_schedule_list(self):
        if not hasattr(self, 'schedule_scroll'):
            return None
        for w in self.schedule_scroll.winfo_children():
            w.destroy()
        items = sorted(self.profile_schedule, key=lambda x: x.get('at', 0))
        for i, it in enumerate(items):
            row = ctk.CTkFrame(self.schedule_scroll, fg_color='transparent')
            row.pack(fill='x', pady=4)
            ts = time.strftime('%H:%M', time.localtime(it.get('at', 0)))
            name = self.profiles[it.get('profile_index', 0)].get('name', 'Profil') if self.profiles else f"Profil {it.get('profile_index', 0) + 1}"
            ctk.CTkLabel(row, text=f'{ts} → {name}', text_color=SHREK_COLORS["text"]).pack(side='left', padx=6)
            ctk.CTkButton(row, text='Appliquer', width=90, command=lambda idx=it.get('profile_index', 0): self.apply_profile_index(idx), fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='right', padx=4)
            ctk.CTkButton(row, text='Supprimer', width=90, fg_color=SHREK_COLORS["bg"], hover_color=SHREK_COLORS["border"], command=lambda k=it.get('at'): self.delete_schedule(k)).pack(side='right', padx=4)

    def add_schedule_relative(self):
        idx = int(self.schedule_profile_index.get())
        delay = max(1, int(self.schedule_delay_min.get()))
        at = time.time() + delay * 60
        self.profile_schedule.append({'at': at, 'profile_index': idx})
        self.save_config()
        self.render_schedule_list()
        if not self.scheduler_running:
            self.toggle_scheduler()

    def add_schedule_absolute(self):
        idx = int(self.schedule_profile_index.get())
        val = (self.schedule_clock.get() or '').strip()
        try:
            hh, mm = map(int, val.split(':'))
            now = time.localtime()
            target = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, hh, mm, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
            if target <= time.time():
                target += 86400
            self.profile_schedule.append({'at': target, 'profile_index': idx})
            self.save_config()
            self.render_schedule_list()
            if not self.scheduler_running:
                self.toggle_scheduler()
        except:
            self.log_msg('Heure invalide (HH:MM)', 'error')

    def delete_schedule(self, at_ts):
        self.profile_schedule = [x for x in self.profile_schedule if x.get('at') != at_ts]
        self.save_config()
        self.render_schedule_list()

    def toggle_scheduler(self):
        self.scheduler_running = not self.scheduler_running
        if self.scheduler_running:
            threading.Thread(target=self.scheduler_loop, daemon=True).start()
            self.log_msg('Planificateur activé', 'success')
        else:
            self.log_msg('Planificateur désactivé', 'info')

    def scheduler_loop(self):
        while self.scheduler_running:
            now = time.time()
            due = [x for x in self.profile_schedule if x.get('at', 0) <= now]
            for it in due:
                self.apply_profile_index(it.get('profile_index', 0))
                self.profile_schedule.remove(it)
                self.save_config()
                try:
                    idx = it.get('profile_index', 0)
                    name = self.profiles[idx].get('name', 'Profil') if self.profiles else f'Profil {idx + 1}'
                    self.notifications.append(f'🔁 Changement exécuté: {name}')
                    if hasattr(self, 'notif_list') and self.notif_list.winfo_exists():
                        self.refresh_notif_list()
                except:
                    continue
            msg_due = [m for m in self.message_schedule if m.get('at', 0) <= now]
            for it in msg_due:
                try:
                    chan = str(it.get('channel_id', '')).strip()
                    content = str(it.get('content', '')).strip()
                    if chan and content:
                        requests.post(f'{API_BASE}/channels/{chan}/messages', headers=self.headers, json={'content': content}, timeout=8)
                        self.notifications.append(f'📨 Message envoyé: {chan}')
                        if hasattr(self, 'notif_list') and self.notif_list.winfo_exists():
                            self.refresh_notif_list()
                except:
                    pass
                self.message_schedule.remove(it)
                self.save_config()
            if due or msg_due:
                self.render_schedule_list()
            time.sleep(5)

    def toggle_status_rotator(self):
        if getattr(self, 'status_rotator_running', False):
            self.status_rotator_running = False
            self.log_msg('Rotator arrêté', 'info')
            return None
        self.status_rotator_running = True
        self.log_msg('Rotator démarré', 'success')
        threading.Thread(target=self.status_rotator_loop, daemon=True).start()

    def status_rotator_loop(self):
        statuses = ['online', 'idle', 'dnd', 'invisible']
        while getattr(self, 'status_rotator_running', False):
            status = random.choice(statuses)
            payload = {'status': status}
            try:
                requests.patch(f'{API_BASE}/users/@me/settings', headers=self.headers, json=payload, timeout=6)
                self.log_msg(f'Rotator → {status}', 'info')
            except Exception:
                pass
            time.sleep(random.uniform(30, 120))

    def show_tools(self):
        self.clear_content()
        title_frame = ctk.CTkFrame(self.content, fg_color='transparent')
        title_frame.pack(fill='x', pady=(0, 20))
        ctk.CTkLabel(title_frame, text=self.t('tools'), font=('Montserrat', 24, 'bold'), text_color=SHREK_COLORS["green_bright"]).pack(anchor='w')
        ctk.CTkLabel(title_frame, text=self.t('tools_desc'), font=('Roboto', 12), text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w')
        grid = ctk.CTkFrame(self.content, fg_color='transparent')
        grid.pack(fill='both', expand=True)
        grid.grid_columnconfigure(0, weight=1)
        grid.grid_columnconfigure(1, weight=1)
        rotator_frame = ctk.CTkFrame(grid, fg_color=SHREK_COLORS["frame"], corner_radius=15, border_width=1, border_color=SHREK_COLORS["border"])
        rotator_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        ctk.CTkLabel(rotator_frame, text='💫 ' + self.t('rotator'), font=('Roboto', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=10)
        self.rotator_text = ctk.CTkTextbox(rotator_frame, height=100, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"])
        self.rotator_text.pack(fill='x', padx=10, pady=5)
        self.rotator_text.insert('0.0', 'Playing GTA VI\nWatching You\nShrek on Top')
        speed_frame = ctk.CTkFrame(rotator_frame, fg_color='transparent')
        speed_frame.pack(fill='x', padx=10, pady=5)
        ctk.CTkLabel(speed_frame, text=self.t('rotate_speed'), text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        self.rotator_speed = ctk.CTkEntry(speed_frame, width=50, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"])
        self.rotator_speed.insert(0, '5')
        self.rotator_speed.pack(side='right')
        self.btn_rotate = ctk.CTkButton(rotator_frame, text=self.t('start_rotate'), fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], command=self.toggle_rotator)
        self.btn_rotate.pack(pady=10, padx=10, fill='x')
        acc_frame = ctk.CTkFrame(grid, fg_color=SHREK_COLORS["frame"], corner_radius=15, border_width=1, border_color=SHREK_COLORS["border"])
        acc_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        ctk.CTkLabel(acc_frame, text='🛡️ Account Tools', font=('Roboto', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=10)
        ctk.CTkButton(acc_frame, text='🗑️ ' + self.t('clear_dms'), fg_color='#ef4444', hover_color='#b91c1c', command=self.run_clear_dms).pack(pady=10, padx=20, fill='x')
        hs_frame = ctk.CTkFrame(acc_frame, fg_color='transparent')
        hs_frame.pack(fill='x', padx=10, pady=10)
        ctk.CTkLabel(hs_frame, text='HypeSquad:', text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w')
        row_hs = ctk.CTkFrame(hs_frame, fg_color='transparent')
        row_hs.pack(fill='x', pady=5)
        ctk.CTkButton(row_hs, text='Bravery', width=60, fg_color='#9c88ff', command=lambda: self.set_hypesquad(1)).pack(side='left', padx=2)
        ctk.CTkButton(row_hs, text='Brilliance', width=60, fg_color='#f47fff', command=lambda: self.set_hypesquad(2)).pack(side='left', padx=2)
        ctk.CTkButton(row_hs, text='Balance', width=60, fg_color='#1abc9c', command=lambda: self.set_hypesquad(3)).pack(side='left', padx=2)
        clean_frame = ctk.CTkFrame(grid, fg_color=SHREK_COLORS["frame"], corner_radius=15, border_width=1, border_color=SHREK_COLORS["border"])
        clean_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
        ctk.CTkLabel(clean_frame, text='🧹 ' + self.t('cleanup_tools'), font=('Roboto', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=10)
        btn_row = ctk.CTkFrame(clean_frame, fg_color='transparent')
        btn_row.pack(fill='x', padx=20, pady=10)
        ctk.CTkButton(btn_row, text='🚪 ' + self.t('mass_leave'), fg_color='#ef4444', hover_color='#b91c1c', command=self.run_mass_leave).pack(side='left', fill='x', expand=True, padx=5)
        ctk.CTkButton(btn_row, text='🚪 ' + self.t('leave_groups'), fg_color='#ef4444', hover_color='#b91c1c', command=self.run_leave_groups).pack(side='left', fill='x', expand=True, padx=5)
        ctk.CTkButton(btn_row, text='ℹ️ ' + self.t('token_info'), fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], command=self.show_token_info_popup).pack(side='left', fill='x', expand=True, padx=5)

    def toggle_rotator(self):
        if not hasattr(self, 'rotator_active'):
            self.rotator_active = False
        if self.rotator_active:
            self.rotator_active = False
            self.btn_rotate.configure(text=self.t('start_rotate'), fg_color=SHREK_COLORS["green_dark"])
        else:
            self.rotator_active = True
            self.btn_rotate.configure(text=self.t('stop_rotate'), fg_color='#ef4444')
            threading.Thread(target=self.loop_rotator, daemon=True).start()

    def loop_rotator(self):
        statuses = self.rotator_text.get('0.0', 'end').strip().split('\n')
        statuses = [s for s in statuses if s.strip()]
        if not statuses:
            return None
        try:
            delay = float(self.rotator_speed.get())
        except:
            delay = 5.0
        i = 0
        while self.rotator_active:
            status = statuses[i % len(statuses)]
            self.change_custom_status(status)
            i += 1
            time.sleep(delay)

    def change_custom_status(self, text):
        if not self.token:
            return None
        data = {'custom_status': {'text': text}}
        try:
            requests.patch(API_BASE + '/users/@me/settings', headers=self.headers, json=data)
        except:
            return None

    def run_clear_dms(self):
        if not messagebox.askyesno('Confirmation', 'Are you sure you want to close ALL DMs?'):
            return None
        threading.Thread(target=self.worker_clear_dms, daemon=True).start()

    def worker_clear_dms(self):
        try:
            r = requests.get(API_BASE + '/users/@me/channels', headers=self.headers)
            if r.status_code == 200:
                channels = r.json()
                for c in channels:
                    requests.delete(API_BASE + f"/channels/{c['id']}", headers=self.headers)
                    time.sleep(0.5)
                messagebox.showinfo('Success', 'All DMs closed!')
        except Exception as e:
            print(e)
            
    def set_hypesquad(self, house_id):
        threading.Thread(target=lambda: requests.post(API_BASE + '/hypesquad/online', headers=self.headers, json={'house_id': house_id}), daemon=True).start()
    
    def run_mass_leave(self):
        if not messagebox.askyesno('Confirmation', 'Are you sure you want to LEAVE ALL SERVERS?'):
            return None
        threading.Thread(target=self.worker_mass_leave, daemon=True).start()
    
    def worker_mass_leave(self):
        try:
            r = requests.get(API_BASE + '/users/@me/guilds', headers=self.headers)
            if r.status_code == 200:
                guilds = r.json()
                for g in guilds:
                    if not g.get('owner'):
                        requests.delete(API_BASE + f"/users/@me/guilds/{g['id']}", headers=self.headers)
                        time.sleep(0.5)
                messagebox.showinfo('Success', 'Left all servers (except owned)!')
        except Exception as e:
            print(e)

    def run_leave_groups(self):
        if not messagebox.askyesno('Confirmation', 'Are you sure you want to LEAVE ALL GROUPS?'):
            return None
        threading.Thread(target=self.worker_leave_groups, daemon=True).start()

    def worker_leave_groups(self):
        try:
            r = requests.get(API_BASE + '/users/@me/channels', headers=self.headers)
            if r.status_code == 200:
                channels = r.json()
                for c in channels:
                    if c['type'] == 3:
                        requests.delete(API_BASE + f"/channels/{c['id']}", headers=self.headers)
                        time.sleep(0.5)
                messagebox.showinfo('Success', 'Left all Group DMs!')
        except Exception as e:
            print(e)

    def show_token_info_popup(self):
        threading.Thread(target=self.worker_token_info, daemon=True).start()

    def worker_token_info(self):
        try:
            r = requests.get(API_BASE + '/users/@me', headers=self.headers)
            if r.status_code == 200:
                data = r.json()
                info = f"\nID: {data.get('id')}\nUsername: {data.get('username')}#{data.get('discriminator')}\nEmail: {data.get('email')}\nPhone: {data.get('phone')}\nMFA Enabled: {data.get('mfa_enabled')}\nVerified: {data.get('verified')}\nLocale: {data.get('locale')}\nNSFW Allowed: {data.get('nsfw_allowed')}\nFlags: {data.get('flags')}\nBio: {data.get('bio')}\n                "
                messagebox.showinfo('Token Info', info)
            else:
                messagebox.showerror('Error', 'Could not fetch info')
        except Exception as e:
            print(e)

    def show_dm_friends(self):
        self.clear_content()
        card = ctk.CTkFrame(self.content, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=2, border_color=SHREK_COLORS["border"])
        card.pack(fill='both', expand=True, pady=20, padx=20)
        self.dm_card = card
        title = ctk.CTkLabel(card, text=self.t('dm_friends'), font=('Consolas', 24, 'bold'), text_color=SHREK_COLORS["text"])
        title.pack(pady=15)
        self.dm_container = ctk.CTkFrame(card, fg_color='transparent')
        self.dm_container.pack(fill='both', expand=True)
        self.dm_tabview = ctk.CTkTabview(self.dm_container, width=800, height=500, fg_color=SHREK_COLORS["bg"], segmented_button_fg_color=SHREK_COLORS["frame"], segmented_button_selected_color=SHREK_COLORS["green_dark"], segmented_button_selected_hover_color=SHREK_COLORS["border"], segmented_button_unselected_color=SHREK_COLORS["bg"], segmented_button_unselected_hover_color=SHREK_COLORS["frame"], text_color=SHREK_COLORS["text"])
        self.dm_tabview.pack(fill='both', expand=True, padx=20, pady=10)
        tab_dms = self.dm_tabview.add(self.t('open_dms'))
        tab_friends = self.dm_tabview.add(self.t('friends_list'))
        self.dm_scroll = ctk.CTkScrollableFrame(tab_dms, fg_color='transparent')
        self.dm_scroll.pack(fill='both', expand=True, padx=10, pady=10)
        btn_refresh_dms = ctk.CTkButton(tab_dms, text=self.t('refresh_list'), command=self.load_open_dms, fg_color=SHREK_COLORS["border"], hover_color=SHREK_COLORS["green_dark"], corner_radius=20)
        btn_refresh_dms.pack(pady=10)
        friends_top = ctk.CTkFrame(tab_friends, fg_color='transparent')
        friends_top.pack(fill='x', pady=5)
        ctk.CTkButton(friends_top, text=self.t('refresh_friends'), command=self.refresh_friends, fg_color=SHREK_COLORS["border"], hover_color=SHREK_COLORS["green_dark"], corner_radius=20, width=120).pack(side='left', padx=10)
        ctk.CTkButton(friends_top, text='✉️ DM ALL', command=self.show_dm_all_dialog, fg_color='#ef4444', hover_color='#dc2626', corner_radius=20, width=100).pack(side='right', padx=10)
        self.friends_scroll = ctk.CTkScrollableFrame(tab_friends, fg_color='transparent')
        self.friends_scroll.pack(fill='both', expand=True, padx=10, pady=10)
        self.load_open_dms()
        self.refresh_friends()

    def load_open_dms(self):
        for widget in self.dm_scroll.winfo_children():
            widget.destroy()
        if not self.token:
            ctk.CTkLabel(self.dm_scroll, text=self.t('token_empty'), text_color='red').pack()
            return None
        
        def fetch_dms_thread():
            try:
                r = requests.get(f'{API_BASE}/users/@me/channels', headers=self.headers, timeout=10)
                if r.status_code == 200:
                    dms = r.json()
                    dms.sort(key=lambda x: x.get('last_message_id') or '0', reverse=True)
                    dms = [d for d in dms if d.get('type') in [1, 3]]
                    self.after(0, lambda: self.display_dms(dms))
                else:
                    self.log_msg(f'Erreur load DMs: {r.status_code}', 'error')
            except Exception as e:
                self.log_msg(f'Erreur load DMs: {e}', 'error')
        
        threading.Thread(target=fetch_dms_thread, daemon=True).start()

    def display_dms(self, dms):
        if not dms:
            ctk.CTkLabel(self.dm_scroll, text='Aucun DM ouvert.', text_color=SHREK_COLORS["text_secondary"]).pack(pady=20)
            return None
        for dm in dms:
            dm_id = dm['id']
            recipients = dm.get('recipients', [])
            if dm['type'] == 1 and recipients:
                name = f"{recipients[0]['username']}#{recipients[0].get('discriminator', '0')}"
            else:
                if dm['type'] == 3:
                    name = dm.get('name') or ', '.join([u['username'] for u in recipients])
                    if not name:
                        name = 'Groupe Inconnu'
                else:
                    name = 'Inconnu'
            row = ctk.CTkFrame(self.dm_scroll, fg_color=SHREK_COLORS["frame"], corner_radius=10)
            row.pack(fill='x', pady=5, padx=5)
            info_frame = ctk.CTkFrame(row, fg_color='transparent')
            info_frame.pack(side='left', padx=10, pady=10, fill='x', expand=True)
            ctk.CTkLabel(info_frame, text=name, font=('Arial', 14, 'bold'), text_color=SHREK_COLORS["text"]).pack(anchor='w')
            last_msg_lbl = ctk.CTkLabel(info_frame, text=f"ID: {dm.get('last_message_id', 'N/A')}", text_color=SHREK_COLORS["text_secondary"], font=('Arial', 10))
            last_msg_lbl.pack(anchor='w')
            action_frame = ctk.CTkFrame(row, fg_color='transparent')
            action_frame.pack(side='right', padx=10)
            self.check_last_msg(dm_id, last_msg_lbl)
            ctk.CTkButton(action_frame, text=self.t('open_chat'), width=100, height=30, fg_color=SHREK_COLORS["bg"], hover_color=SHREK_COLORS["green_dark"], corner_radius=20, command=lambda i, n=dm_id, name=name: self.open_dm_panel(i, n)).pack(side='right', padx=5)

    def check_last_msg(self, channel_id, label_widget):
        def _check():
            try:
                r = requests.get(f'{API_BASE}/channels/{channel_id}/messages?limit=1', headers=self.headers, timeout=5)
                if r.status_code == 200:
                    msgs = r.json()
                    if msgs:
                        last_msg = msgs[0]
                        author = last_msg.get('author', {})
                        content = last_msg.get('content', '')
                        if len(content) > 20:
                            content = content[:20] + '...'
                        is_me = author.get('id') == self.my_id
                        prefix = 'Moi' if is_me else f"{author.get('username')}"
                        color = SHREK_COLORS["text_secondary"] if is_me else '#ef4444'
                        text = f'{prefix}: {content}'
                        
                        def _safe():
                            try:
                                if label_widget.winfo_exists():
                                    label_widget.configure(text=text, text_color=color)
                            except Exception:
                                pass
                        
                        self.after(0, _safe)
            except Exception:
                pass
        
        threading.Thread(target=_check, daemon=True).start()

    def open_dm_panel(self, channel_id, name):
        self.dm_tabview.pack_forget()
        self.chat_frame = ctk.CTkFrame(self.dm_container, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        self.chat_frame.pack(fill='both', expand=True, padx=10, pady=10)
        head = ctk.CTkFrame(self.chat_frame, height=50, fg_color='transparent')
        head.pack(fill='x', pady=5)
        ctk.CTkButton(head, text='< Retour', width=80, corner_radius=20, fg_color=SHREK_COLORS["border"], command=self.close_chat_panel).pack(side='left', padx=10)
        ctk.CTkLabel(head, text=f'Chat: {name}', font=('Arial', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(side='left', padx=10)
        chat_scroll = ctk.CTkTextbox(self.chat_frame, fg_color=SHREK_COLORS["frame"], text_color=SHREK_COLORS["text"])
        chat_scroll.pack(fill='both', expand=True, padx=10, pady=10)
        input_frame = ctk.CTkFrame(self.chat_frame, fg_color='transparent')
        input_frame.pack(fill='x', padx=10, pady=10)
        entry = ctk.CTkEntry(input_frame, placeholder_text='Message...', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"])
        entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        def send_msg(event=None):
            content = entry.get()
            if not content:
                return None
            threading.Thread(target=lambda: self.send_dm_msg(channel_id, content, chat_scroll), daemon=True).start()
            entry.delete(0, 'end')
        
        entry.bind('<Return>', send_msg)
        btn_send = ctk.CTkButton(input_frame, text='Envoyer', width=80, command=send_msg, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], corner_radius=20)
        btn_send.pack(side='right')
        threading.Thread(target=lambda: self.load_chat_history(channel_id, chat_scroll), daemon=True).start()

    def close_chat_panel(self):
        if hasattr(self, 'chat_frame') and self.chat_frame.winfo_exists():
            self.chat_frame.destroy()
        self.dm_tabview.pack(fill='both', expand=True, padx=20, pady=10)

    def load_chat_history(self, channel_id, widget):
        try:
            r = requests.get(f'{API_BASE}/channels/{channel_id}/messages?limit=20', headers=self.headers, timeout=10)
            if r.status_code == 200:
                msgs = r.json()
                text = ''
                for msg in reversed(msgs):
                    author = msg['author']['username']
                    content = msg.get('content', '')
                    timestamp = msg['timestamp'].split('T')[1][:5]
                    text += f'[{timestamp}] {author}: {content}\n\n'
                self.after(0, lambda: widget.insert('0.0', text))
                self.after(0, lambda: widget.see('end'))
        except Exception as e:
            return None
    
    def send_dm_msg(self, channel_id, content, widget):
        try:
            r = requests.post(f'{API_BASE}/channels/{channel_id}/messages', headers=self.headers, json={'content': content})
            if r.status_code in [200, 201]:
                timestamp = time.strftime('%H:%M')
                widget.insert('end', f'[{timestamp}] Moi: {content}\n\n')
                widget.see('end')
        except Exception as e:
            return None

    def refresh_friends(self):
        if not self.token:
            messagebox.showerror('Erreur', self.t('token_empty'))
            return None
        try:
            r = requests.get(f'{API_BASE}/users/@me/relationships', headers=self.headers, timeout=6)
            if r.status_code == 200:
                self.friends_cache = r.json()
                for w in self.friends_scroll.winfo_children():
                    w.destroy()
                count = 0
                for rel in self.friends_cache:
                    if rel.get('type') == 1:
                        count += 1
                        u = rel['user']
                        username = u['username']
                        discrim = u.get('discriminator', '0')
                        user_id = u['id']
                        f_card = ctk.CTkFrame(self.friends_scroll, fg_color=SHREK_COLORS["frame"], corner_radius=10)
                        f_card.pack(fill='x', pady=5, padx=5)
                        info_frame = ctk.CTkFrame(f_card, fg_color='transparent')
                        info_frame.pack(side='left', padx=10, pady=10)
                        ctk.CTkLabel(info_frame, text=f'{username}#{discrim}', font=('Arial', 14, 'bold'), text_color=SHREK_COLORS["text"]).pack(anchor='w')
                        ctk.CTkLabel(info_frame, text=f'ID: {user_id}', font=('Arial', 10), text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w')
                        action_frame = ctk.CTkFrame(f_card, fg_color='transparent')
                        action_frame.pack(side='right', padx=10)
                        ctk.CTkButton(action_frame, text='Copier', width=60, height=30, fg_color=SHREK_COLORS["bg"], hover_color=SHREK_COLORS["border"], corner_radius=15, command=lambda n=f'{username}#{discrim}': self.copy_to_clipboard(n)).pack(side='right', padx=5)
                        ctk.CTkButton(action_frame, text='Chat', width=60, height=30, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"], corner_radius=15, command=lambda uid=user_id, n=username: self.open_dm_from_friend(uid, n)).pack(side='right', padx=5)
                if count == 0:
                    ctk.CTkLabel(self.friends_scroll, text='Aucun ami trouvé.', text_color=SHREK_COLORS["text_secondary"]).pack(pady=20)
            else:
                self.log_msg(f'Échec refresh friends : {r.status_code}', 'error')
        except Exception as e:
            self.log_msg(f'Erreur refresh friends : {e}', 'error')

    def copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()
        self.log_msg(f'Copié: {text}', 'info')

    def open_dm_from_friend(self, user_id, name):
        threading.Thread(target=self.create_dm_and_open, args=(user_id, name), daemon=True).start()

    def create_dm_and_open(self, user_id, name):
        try:
            r = requests.post(f'{API_BASE}/users/@me/channels', headers=self.headers, json={'recipient_id': user_id})
            if r.status_code in (200, 201):
                chan = r.json()
                self.after(0, lambda: self.open_dm_panel(chan['id'], name))
            else:
                self.log_msg(f'Erreur création DM: {r.status_code}', 'error')
        except Exception as e:
            self.log_msg(f'Erreur création DM: {e}', 'error')

    def show_dm_all_dialog(self):
        dialog = ctk.CTkInputDialog(text='Message pour DM ALL (Tous les amis):', title='DM ALL')
        msg = dialog.get_input()
        if msg and messagebox.askyesno('Confirmation', f'Envoyer à TOUS les amis ?\nMessage: {msg}'):
            threading.Thread(target=self.start_dm_all, args=(msg,), daemon=True).start()

    def start_dm_all(self, message):
        if not hasattr(self, 'friends_cache') or not self.friends_cache:
            self.log_msg('Aucun ami chargé. Rafraîchissez la liste.', 'error')
            return None
        count = 0
        self.log_msg('Démarrage DM ALL...', 'info')
        for rel in self.friends_cache:
            if rel.get('type') == 1:
                user_id = rel['user']['id']
                try:
                    r = requests.post(f'{API_BASE}/users/@me/channels', headers=self.headers, json={'recipient_id': user_id})
                    if r.status_code in [200, 201]:
                        chan_id = r.json()['id']
                        r2 = requests.post(f'{API_BASE}/channels/{chan_id}/messages', headers=self.headers, json={'content': message})
                        if r2.status_code in [200, 201]:
                            count += 1
                            time.sleep(1.5)
                except:
                    pass
        self.log_msg(f'DM ALL terminé. Envoyé à {count} amis.', 'success')

    def show_scripts(self):
        self.clear_content()
        card = ctk.CTkFrame(self.content, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=2, border_color=SHREK_COLORS["border"])
        card.pack(fill='both', expand=True, pady=20, padx=20)
        title = ctk.CTkLabel(card, text='Planificateur de messages', font=('Consolas', 24, 'bold'), text_color=SHREK_COLORS["text"])
        title.pack(pady=15)
        sched = ctk.CTkFrame(card, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        sched.pack(fill='x', padx=20, pady=10)
        top = ctk.CTkFrame(sched, fg_color='transparent')
        top.pack(fill='x', padx=12, pady=10)
        ctk.CTkLabel(top, text='Channel/DM ID:', text_color=SHREK_COLORS["text_secondary"]).pack(side='left')
        ctk.CTkEntry(top, textvariable=self.msg_target_id_var, width=200, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=8)
        ctk.CTkLabel(top, text='Dans (min):', text_color=SHREK_COLORS["text_secondary"]).pack(side='left', padx=(10, 2))
        
        def on_msg_delay(value):
            try:
                self.msg_sched_label_var.set(f'{int(float(value))} min')
            except:
                self.msg_sched_label_var.set('min')
        
        ctk.CTkSlider(top, from_=1, to=1440, variable=self.msg_sched_delay_min_var, command=on_msg_delay, fg_color=SHREK_COLORS["frame"], progress_color=SHREK_COLORS["green_dark"]).pack(side='left', padx=6, fill='x', expand=True)
        ctk.CTkLabel(top, textvariable=self.msg_sched_label_var, text_color=SHREK_COLORS["text"]).pack(side='left', padx=6)
        ctk.CTkButton(top, text='Programmer', width=120, command=self.plan_message_schedule, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        ctk.CTkLabel(sched, text='Contenu du message:', text_color=SHREK_COLORS["text_secondary"]).pack(anchor='w', padx=12)
        self.msg_content_box = ctk.CTkTextbox(sched, height=120, text_color=SHREK_COLORS["text"], fg_color=SHREK_COLORS["bg"])
        self.msg_content_box.pack(fill='x', padx=12, pady=8)
        list_card = ctk.CTkFrame(card, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        list_card.pack(fill='x', padx=20, pady=10)
        ctk.CTkLabel(list_card, text='Messages programmés', font=('Arial', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=10)
        self.msg_sched_scroll = ctk.CTkScrollableFrame(list_card, fg_color='transparent', height=200)
        self.msg_sched_scroll.pack(fill='x', padx=10, pady=10)
        self.render_msg_schedule_list()
        dm_all_card = ctk.CTkFrame(card, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        dm_all_card.pack(fill='x', padx=20, pady=10)
        ctk.CTkLabel(dm_all_card, text='Diffusion aux amis (DM ALL)', font=('Arial', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=10)
        dm_row = ctk.CTkFrame(dm_all_card, fg_color='transparent')
        dm_row.pack(fill='x', padx=12, pady=8)
        self.dm_all_text = tk.StringVar()
        ctk.CTkEntry(dm_row, textvariable=self.dm_all_text, placeholder_text='Message à envoyer à tous les amis', fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', fill='x', expand=True, padx=6)
        ctk.CTkButton(dm_row, text='Envoyer', width=120, command=lambda: threading.Thread(target=self.start_dm_all, args=(self.dm_all_text.get(),), daemon=True).start(), fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)
        
        # Server Cloner
        cloner = ctk.CTkFrame(card, fg_color=SHREK_COLORS["bg"], corner_radius=15)
        cloner.pack(fill='x', padx=20, pady=10)
        ctk.CTkLabel(cloner, text='Server Cloner', font=('Consolas', 18, 'bold'), text_color=SHREK_COLORS["text"]).pack(pady=10)
        row = ctk.CTkFrame(cloner, fg_color='transparent')
        row.pack(fill='x', padx=10, pady=10)
        self.clone_source_guild = tk.StringVar()
        self.clone_new_name = tk.StringVar()
        ctk.CTkEntry(row, textvariable=self.clone_source_guild, placeholder_text='Source Guild ID', height=34, width=220, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=6)
        ctk.CTkEntry(row, textvariable=self.clone_new_name, placeholder_text='Nouveau nom', height=34, width=220, fg_color=SHREK_COLORS["bg"], text_color=SHREK_COLORS["text"], border_color=SHREK_COLORS["border"]).pack(side='left', padx=6)
        ctk.CTkButton(row, text='Cloner', width=100, command=self.clone_server_ui, fg_color=SHREK_COLORS["green_dark"], hover_color=SHREK_COLORS["green_hover"]).pack(side='left', padx=6)

    def clone_server_ui(self):
        src = self.clone_source_guild.get().strip()
        name = self.clone_new_name.get().strip() or 'Clone'
        if not self.token or not src:
            self.log_msg('Token ou Guild ID manquant', 'error')
            return None
        threading.Thread(target=lambda: self.clone_server(src, name), daemon=True).start()

    def clone_server(self, source_guild_id, new_name):
        try:
            r_new = requests.post(f'{API_BASE}/guilds', headers=self.headers, json={'name': new_name}, timeout=8)
            if r_new.status_code not in [200, 201]:
                self.log_msg(f'Échec création serveur : {r_new.status_code}', 'error')
                return
            new_guild = r_new.json()
            new_gid = new_guild.get('id')
            self.log_msg(f'Serveur créé: {new_name} ({new_gid})', 'success')
            r_ch = requests.get(f'{API_BASE}/guilds/{source_guild_id}/channels', headers=self.headers, timeout=8)
            if r_ch.status_code != 200:
                self.log_msg(f'Échec lecture canaux source : {r_ch.status_code}', 'error')
                return
            chans = r_ch.json()
            categories = [c for c in chans if c.get('type') == 4]
            text_and_others = [c for c in chans if c.get('type') in [0, 2, 5]]
            cat_map = {}
            pos = 0
            for cat in sorted(categories, key=lambda x: x.get('position', 0)):
                payload = {'name': cat.get('name', 'cat'), 'type': 4, 'position': pos}
                rc = requests.post(f'{API_BASE}/guilds/{new_gid}/channels', headers=self.headers, json=payload, timeout=8)
                if rc.status_code in [200, 201]:
                    cat_id = rc.json().get('id')
                    cat_map[cat.get('id')] = cat_id
                pos += 1
            for ch in sorted(text_and_others, key=lambda x: x.get('position', 0)):
                payload = {'name': ch.get('name', 'chan'), 'type': ch.get('type', 0), 'position': ch.get('position', 0)}
                pid = ch.get('parent_id')
                if pid and pid in cat_map:
                    payload['parent_id'] = cat_map[pid]
                rc = requests.post(f'{API_BASE}/guilds/{new_gid}/channels', headers=self.headers, json=payload, timeout=8)
            self.log_msg('Clone terminé (structure canaux)', 'success')
        except Exception as e:
            self.log_msg(f'Erreur clone: {e}', 'error')

    def show_settings(self):
        self.clear_content()
        card = ctk.CTkFrame(self.content, fg_color=SHREK_COLORS["frame"], corner_radius=20, border_width=2, border_color=SHREK_COLORS["border"])
        card.pack(fill='both', expand=True, pady=20, padx=20)
        title = ctk.CTkLabel(card, text=self.t('settings'), font=('Consolas', 24, 'bold'), text_color=SHREK_COLORS["text"])
        title.pack(pady=15)
        scroll = ctk.CTkScrollableFrame(card, fg_color='transparent')
        scroll.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Language
        ctk.CTkLabel(scroll, text=self.t('language'), font=('Arial', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(anchor='w', pady=(10, 5))
        lang_var = tk.StringVar(value=self.lang)
        
        def change_lang(val):
            self.lang = val
            self.save_config()
            self.build_ui()
        
        seg_lang = ctk.CTkSegmentedButton(
            scroll, 
            values=['fr', 'en'], 
            variable=lang_var, 
            command=change_lang, 
            selected_color=SHREK_COLORS["green_dark"], 
            unselected_color=SHREK_COLORS["bg"],
            text_color=SHREK_COLORS["text"]
        )
        seg_lang.pack(anchor='w', pady=5)
        
        # Theme customization
        ctk.CTkLabel(scroll, text=self.t('theme_custom'), font=('Arial', 16, 'bold'), text_color=SHREK_COLORS["text"]).pack(anchor='w', pady=(20, 5))
        
        colors_to_edit = [
            ('bg_color', self.t('bg_color')),
            ('fg_color', self.t('fg_color')),
            ('accent_color', self.t('accent_color')),
            ('sidebar_color', self.t('sidebar_color')),
            ('border_color', self.t('border_color_label')),
            ('text_color', self.t('text_color_label')),
            ('secondary_text_color', self.t('secondary_text_color_label'))
        ]
        
        for key, label_text in colors_to_edit:
            row = ctk.CTkFrame(scroll, fg_color='transparent')
            row.pack(fill='x', pady=5)
            ctk.CTkLabel(row, text=label_text, text_color=SHREK_COLORS["text"]).pack(side='left', padx=10)
            preview = ctk.CTkLabel(row, text='   ', fg_color=self.colors[key], width=30, corner_radius=5)
            preview.pack(side='right', padx=10)
            current_hex = self.colors[key].lower()
            current_name = 'Personnalisé'
            for name, hex_code in PRESET_COLORS.items():
                if hex_code.lower() == current_hex:
                    current_name = name
                    break
            
            def on_color_change(choice, k=key, p=preview):
                if choice in PRESET_COLORS:
                    new_color = PRESET_COLORS[choice]
                    self.colors[k] = new_color
                    p.configure(fg_color=new_color)
            
            combo = ctk.CTkComboBox(
                row, 
                values=list(PRESET_COLORS.keys()), 
                command=on_color_change, 
                width=180, 
                fg_color=SHREK_COLORS["bg"], 
                text_color=SHREK_COLORS["text"], 
                dropdown_fg_color=SHREK_COLORS["frame"], 
                dropdown_text_color=SHREK_COLORS["text"], 
                button_color=SHREK_COLORS["green_dark"], 
                button_hover_color=SHREK_COLORS["green_hover"]
            )
            combo.set(current_name)
            combo.pack(side='right')
        
        btn_frame = ctk.CTkFrame(scroll, fg_color='transparent')
        btn_frame.pack(pady=30, fill='x')
        ctk.CTkButton(
            btn_frame, 
            text=self.t('save_theme'), 
            fg_color=SHREK_COLORS["green_dark"], 
            hover_color=SHREK_COLORS["green_hover"], 
            corner_radius=20, 
            command=self.save_and_refresh
        ).pack(side='left', padx=10, expand=True)
        ctk.CTkButton(
            btn_frame, 
            text=self.t('reset_theme'), 
            fg_color='#ef4444', 
            hover_color='#dc2626', 
            corner_radius=20, 
            command=self.reset_theme
        ).pack(side='right', padx=10, expand=True)

    def save_and_refresh(self):
        self.save_config()
        self.build_ui()
        messagebox.showinfo('Info', self.t('colors_saved'))

    def reset_theme(self):
        # Réinitialiser avec les couleurs Shrek par défaut
        default_theme = {
            'bg_color': SHREK_COLORS["bg"],
            'fg_color': SHREK_COLORS["text"],
            'sidebar_color': SHREK_COLORS["frame"],
            'accent_color': SHREK_COLORS["green_dark"],
            'border_color': SHREK_COLORS["border"],
            'text_color': SHREK_COLORS["text"],
            'secondary_text_color': SHREK_COLORS["text_secondary"]
        }
        self.colors = default_theme
        self.save_config()
        self.build_ui()

    def log_msg(self, msg: str, level: str='info'):
        print(f'[{level.upper()}] {msg}')

    def on_close(self):
        self.save_config()
        self.destroy()


def main():
    app = NightyUltimateSelfBot()
    app.mainloop()


def run():
    from utilities.core.shrek_ui import set_console_title
    set_console_title('Shrek Selfbot | Shrek Multi Tools')
    os.system('cls' if os.name == 'nt' else 'clear')
    main()


if __name__ == '__main__':
    run()