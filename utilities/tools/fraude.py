# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import qrcode
import random
import os
import sys
import platform
import hashlib
from datetime import datetime, timedelta
import json
import string
import re

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

COLORS = {
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
    "white": "#ffffff"
}

class IDCardCreator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('ID Card Generator | Shrek Multi Tools')
        self.geometry('1400x780')
        self.minsize(1200, 650)
        self.configure(fg_color=COLORS["bg"])
        
        icon_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'shrek.ico')
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except:
                pass
        
        # ---- Détection de police ----
        self.font_path = None
        if platform.system() == "Windows":
            font_candidates = [
                "C:/Windows/Fonts/OCR-B.ttf",
                "C:/Windows/Fonts/ocrb10.ttf",
                "C:/Windows/Fonts/consola.ttf",
                "C:/Windows/Fonts/arial.ttf",
            ]
        elif platform.system() == "Linux":
            font_candidates = [
                "/usr/share/fonts/truetype/ocr-b/OCR-B.ttf",
                "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            ]
        elif platform.system() == "Darwin":
            font_candidates = [
                "/System/Library/Fonts/Helvetica.ttf",
                "/Library/Fonts/Arial.ttf",
            ]
        else:
            font_candidates = []
        
        for path in font_candidates:
            if os.path.exists(path):
                self.font_path = path
                print(f"✅ Police trouvée: {path}")
                break
        
        if self.font_path is None:
            self.font_path = 'arial.ttf'
            print("⚠️ Aucune police système trouvée")
        
        # ---- Variables ----
        self.use_qr = ctk.BooleanVar(value=False)
        self.qr_url = ctk.StringVar(value='')
        self.preview_image = None
        self.photo_tk = None
        self.update_timer = None
        self.photo_path = None
        self.user_photo = None
        self.signature_path = None
        self.user_signature = None
        self.template_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'template_id.png')
        self.custom_template_path = None
        self.custom_template = None
        
        # ---- Taille globale des textes ----
        self.text_size = 0.9
        self.mrz_size = 1.5
        
        # ---- Génération aléatoire ----
        self.doc_number = self.generate_doc_number()
        self.birth_date = self.generate_birth_date()
        self.issue_date = self.generate_issue_date()
        self.sex = random.choice(["M", "F"])
        self.place_of_birth = random.choice(["PARIS", "LYON", "MARSEILLE", "BORDEAUX", "LILLE", "TOULOUSE", "NICE", "NANTES"])
        self.height = random.randint(150, 200)
        self.department = random.choice(["75", "69", "13", "33", "59", "31", "06", "44"])
        self.admin_code = ''.join(random.choices(string.digits, k=6))
        
        # ---- Positions textes (Initiales juste au-dessus du nom, bien à droite de la photo) ----
        self.pos = {
            'surname': [0.32, 0.28],
            'given_names': [0.32, 0.36],
            'sex': [0.32, 0.44],
            'dob': [0.32, 0.52],
            'pob': [0.32, 0.60],
            'height': [0.32, 0.68],
            'doc_no': [0.55, 0.28],
            'initials': [0.32, 0.15],
            'mrz_part1': [0.05, 0.88],
            'mrz_part2': [0.05, 0.92],
        }
        
        # ---- Positions photo, QR et signature ----
        self.photo_pos = [0.03, 0.08]
        self.qr_pos = [0.88, 0.78]
        self.signature_pos = [0.55, 0.70]
        
        # ---- Tailles (Photo à 1.2 par défaut) ----
        self.photo_scale = 1.2
        self.qr_scale = 1.0
        self.signature_scale = 1.0
        
        # ---- Champs personnalisés ----
        self.custom_fields = {}
        self.custom_field_keys = []
        self.custom_counter = 1
        
        # ---- Présélections ----
        self.presets = {
            'France': {
                'fields': ['NOM', 'Prénoms', 'Sexe', 'Date de naiss.', 'Lieu de naiss.', 'Taille', 'N° Document', "Date d'émission", 'Département'],
                'template': 'template_france.png'
            }
        }
        self.current_preset = 'France'
        self.custom_preset_names = []
        
        # ---- Fichier de sauvegarde des positions ----
        self.pos_file = os.path.join(root_path, 'utilities', 'tools', 'input', 'positions.json')
        
        # ---- Drag & Drop ----
        self.dragging = False
        self.drag_key = None
        self.drag_type = None
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.pos_start_x = 0
        self.pos_start_y = 0
        
        # ---- Chargement des positions sauvegardées ----
        self.load_positions()
        
        self.build_ui()
        self.after(100, self.update_preview)
    
    def load_positions(self):
        if os.path.exists(self.pos_file):
            try:
                with open(self.pos_file, 'r') as f:
                    loaded = json.load(f)
                    
                    # IGNORE le fichier s'il contient des positions incorrectes ou obsolètes
                    # Le fichier est réinitialisé pour toujours utiliser les nouvelles positions parfaites
                    if 'initials' not in self.pos:
                        loaded = {} # On reset tout
                    
                    for key, value in loaded.items():
                        if key in self.pos:
                            self.pos[key] = value
                            
                print(f"✅ Positions chargées depuis {self.pos_file}")
            except Exception as e:
                print(f"⚠️ Erreur chargement: {e}")
    
    def save_positions(self):
        try:
            with open(self.pos_file, 'w') as f:
                json.dump(self.pos, f, indent=4)
            self.status_label.configure(text='[+] Positions saved!')
            print(f"✅ Positions sauvegardées dans {self.pos_file}")
            return True
        except Exception as e:
            self.status_label.configure(text=f'[!] Save error: {str(e)[:30]}')
            print(f"⚠️ Erreur sauvegarde: {e}")
            return False
    
    def generate_doc_number(self):
        return ''.join(random.choices(string.digits, k=12))
    
    def generate_birth_date(self):
        start = datetime(1950, 1, 1)
        end = datetime(2005, 12, 31)
        delta = end - start
        random_date = start + timedelta(days=random.randint(0, delta.days))
        return random_date.strftime('%d.%m.%Y')
    
    def generate_issue_date(self):
        start = datetime(2010, 1, 1)
        end = datetime(2026, 12, 31)
        delta = end - start
        random_date = start + timedelta(days=random.randint(0, delta.days))
        return random_date.strftime('%d.%m.%Y')
    
    def date_to_mrz_ym(self, date_str):
        try:
            parts = date_str.split('.')
            if len(parts) == 3:
                return parts[2][-2:] + parts[1]
            return '2401'
        except:
            return '2401'
    
    def date_to_mrz(self, date_str):
        try:
            parts = date_str.split('.')
            if len(parts) == 3:
                return parts[2][-2:] + parts[1] + parts[0]
            return '010101'
        except:
            return '010101'
    
    def date_to_mrz_expiry(self, birth_date):
        try:
            birth_dt = datetime.strptime(birth_date, '%d.%m.%Y')
            exp_dt = birth_dt.replace(year=birth_dt.year + 10)
            return exp_dt.strftime('%y%m%d')
        except:
            return '300101'
    
    def get_initials(self, surname, given_names):
        initials = ""
        if surname:
            initials += surname[0].upper()
        if given_names:
            initials += given_names[0].upper()
        return initials
    
    def calculate_check_digit(self, string_to_check):
        """Calcule le chiffre de contrôle avec l'algorithme MRZ (poids 7,3,1)"""
        weights = [7, 3, 1]
        total = 0
        
        for i, char in enumerate(string_to_check):
            if char.isdigit():
                value = int(char)
            elif char.isalpha():
                value = ord(char.upper()) - 55
            elif char == '<':
                value = 0
            else:
                value = 0
            
            weight = weights[i % 3]
            total += value * weight
        
        return total % 10
    
    def generate_mrz(self, surname, given_names, doc_number, birth_date, sex, department, admin_code):
        """Génère les 2 lignes MRZ complètes (44 caractères chacune) selon la norme ICAO 9303"""
        
        surname_clean = ''.join(c.upper() for c in surname if c.isalpha() or c == ' ')
        given_clean = ''.join(c.upper() for c in given_names if c.isalpha() or c == ' ')
        
        surname_mrz = surname_clean.replace(' ', '<')
        given_mrz = given_clean.replace(' ', '<')
        
        surname_mrz = surname_mrz[:36]
        given_mrz = given_mrz[:30]
        
        doc_clean = doc_number[:12]
        
        birth_mrz = self.date_to_mrz(birth_date)
        exp_mrz = self.date_to_mrz_expiry(birth_date)
        
        sex_mrz = 'M' if sex.upper() == 'M' else 'F'
        
        part1_base = f"IDFRA{surname_mrz}<<{given_mrz}"
        part1 = (part1_base + "<" * 44)[:44]
        
        check_doc = self.calculate_check_digit(doc_clean + "<" + "FRA" + birth_mrz)
        check_birth = self.calculate_check_digit(birth_mrz)
        check_exp = self.calculate_check_digit(exp_mrz)
        
        opt_data = f"{department.zfill(2)}{admin_code}"
        check_opt = self.calculate_check_digit(opt_data)
        
        part2_base = f"{doc_clean}{check_doc}FRA{birth_mrz}{check_birth}{sex_mrz}{exp_mrz}{check_exp}{opt_data}{check_opt}"
        part2 = (part2_base + "<" * 44)[:44]
        
        return part1, part2
    
    def build_ui(self):
        main_frame = ctk.CTkFrame(
            self, 
            fg_color=COLORS["frame"], 
            corner_radius=12,
            border_color=COLORS["green_dark"],
            border_width=2
        )
        main_frame.pack(padx=10, pady=10, fill='both', expand=True)
        
        title_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["bg"], corner_radius=5)
        title_frame.pack(pady=(8, 5), padx=15, fill='x')
        
        title = ctk.CTkLabel(
            title_frame, 
            text='[ ID CARD GENERATOR ]', 
            font=ctk.CTkFont(family='Consolas', size=18, weight='bold'), 
            text_color=COLORS["green_bright"]
        )
        title.pack(pady=5)
        
        subtitle = ctk.CTkLabel(
            title_frame,
            text='Drag text/photo/QR/signature/MRZ to move | Text Size slider | MRZ Size slider',
            font=ctk.CTkFont(family='Consolas', size=11),
            text_color=COLORS["text_secondary"]
        )
        subtitle.pack(pady=(0, 5))
        
        container = ctk.CTkFrame(main_frame, fg_color=COLORS["frame"])
        container.pack(padx=5, pady=5, fill='both', expand=True)
        
        left_frame = ctk.CTkFrame(
            container,
            fg_color=COLORS["frame_light"],
            corner_radius=8,
            border_color=COLORS["green_dark"],
            border_width=1
        )
        left_frame.pack(side='left', padx=5, pady=5, fill='y')
        
        scroll_frame = ctk.CTkScrollableFrame(
            left_frame,
            fg_color=COLORS["frame_light"],
            width=420,
            height=650
        )
        scroll_frame.pack(padx=5, pady=5, fill='both', expand=True)
        
        # TAILLE GLOBALE DES TEXTES
        text_size_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        text_size_frame.pack(padx=5, pady=5, fill='x')
        
        ctk.CTkLabel(
            text_size_frame,
            text='Text Size:',
            font=ctk.CTkFont(family='Consolas', size=11, weight='bold'),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=5)
        
        self.text_size_slider = ctk.CTkSlider(
            text_size_frame,
            from_=0.3,
            to=2.5,
            number_of_steps=44,
            command=self.change_text_size,
            width=120
        )
        self.text_size_slider.set(self.text_size)
        self.text_size_slider.pack(side='left', padx=5, fill='x', expand=True)
        
        self.text_size_label = ctk.CTkLabel(
            text_size_frame,
            text='0.9x',
            font=ctk.CTkFont(family='Consolas', size=11, weight='bold'),
            text_color=COLORS["green_bright"],
            width=40
        )
        self.text_size_label.pack(side='left', padx=5)
        
        # TAILLE MRZ
        mrz_size_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        mrz_size_frame.pack(padx=5, pady=5, fill='x')
        
        ctk.CTkLabel(
            mrz_size_frame,
            text='MRZ Size:',
            font=ctk.CTkFont(family='Consolas', size=11, weight='bold'),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=5)
        
        self.mrz_size_slider = ctk.CTkSlider(
            mrz_size_frame,
            from_=0.3,
            to=2.5,
            number_of_steps=44,
            command=self.change_mrz_size,
            width=120
        )
        self.mrz_size_slider.set(self.mrz_size)
        self.mrz_size_slider.pack(side='left', padx=5, fill='x', expand=True)
        
        self.mrz_size_label = ctk.CTkLabel(
            mrz_size_frame,
            text='1.5x',
            font=ctk.CTkFont(family='Consolas', size=11, weight='bold'),
            text_color=COLORS["green_bright"],
            width=40
        )
        self.mrz_size_label.pack(side='left', padx=5)
        
        # BOUTON RANDOM
        random_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        random_frame.pack(padx=5, pady=5, fill='x')
        
        ctk.CTkButton(
            random_frame,
            text='🎲 Randomize All',
            command=self.randomize_all,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=11, weight='bold'),
            border_color=COLORS["border"],
            border_width=1
        ).pack(fill='x', pady=5, padx=5)
        
        # PRESETS
        preset_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        preset_frame.pack(padx=5, pady=5, fill='x')
        
        ctk.CTkLabel(
            preset_frame,
            text='Preset:',
            font=ctk.CTkFont(family='Consolas', size=11, weight='bold'),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=5)
        
        preset_list = ['France'] + self.custom_preset_names + ['--- Create New ---']
        self.preset_var = ctk.StringVar(value='France')
        self.preset_menu = ctk.CTkOptionMenu(
            preset_frame,
            values=preset_list,
            variable=self.preset_var,
            command=self.on_preset_change,
            fg_color=COLORS["bg"],
            button_color=COLORS["green_dark"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=11)
        )
        self.preset_menu.pack(side='left', padx=5, fill='x', expand=True)
        
        ctk.CTkButton(
            preset_frame,
            text='💾 Save',
            command=self.save_preset,
            fg_color=COLORS["frame_light"],
            hover_color=COLORS["green_dark"],
            text_color='#ffffff',
            font=ctk.CTkFont(family='Consolas', size=10),
            width=60,
            height=30,
            border_color=COLORS["green_dark"],
            border_width=1
        ).pack(side='right', padx=3)
        
        ctk.CTkButton(
            preset_frame,
            text='🗑️ Del',
            command=self.delete_preset,
            fg_color=COLORS["frame_light"],
            hover_color=COLORS["red"],
            text_color='#ffffff',
            font=ctk.CTkFont(family='Consolas', size=10),
            width=40,
            height=30,
            border_color=COLORS["green_dark"],
            border_width=1
        ).pack(side='right', padx=3)
        
        # BOUTON SAVE POSITIONS
        save_pos_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        save_pos_frame.pack(padx=5, pady=3, fill='x')
        
        ctk.CTkButton(
            save_pos_frame,
            text='💾 Save Positions',
            command=self.save_positions,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=11, weight='bold'),
            border_color=COLORS["border"],
            border_width=1
        ).pack(fill='x', pady=3, padx=5)
        
        # Champs de base
        ctk.CTkLabel(
            scroll_frame,
            text='CARD DETAILS',
            font=ctk.CTkFont(family='Consolas', size=12, weight='bold'),
            text_color=COLORS["green_bright"]
        ).pack(pady=(5, 5))
        
        self.field_keys = ['surname', 'given_names', 'sex', 'dob', 'pob', 'height', 'doc_no']
        self.field_labels = ['NOM', 'Prénoms', 'Sexe', 'Date de naiss.', 'Lieu de naiss.', 'Taille (cm)', 'N° Document']
        
        self.entries = {}
        
        default_values = {
            'surname': 'MOUSE',
            'given_names': 'MICKEY',
            'sex': 'M',
            'dob': '01.01.1920',
            'pob': 'SAINT NAZAIRE',
            'height': '175',
            'doc_no': '201244110987'
        }
        
        for i, key in enumerate(self.field_keys):
            row = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"])
            row.pack(fill='x', pady=1, padx=5)
            
            label = ctk.CTkLabel(
                row, 
                text=self.field_labels[i], 
                font=ctk.CTkFont(family='Consolas', size=10),
                text_color=COLORS["green_bright"],
                width=100,
                anchor='w'
            )
            label.pack(side='left', padx=2)
            
            entry = ctk.CTkEntry(
                row, 
                font=ctk.CTkFont(family='Consolas', size=10),
                fg_color=COLORS["bg"], 
                text_color=COLORS["text"],
                border_color=COLORS["green_dark"],
                border_width=1,
                corner_radius=3,
                height=28
            )
            entry.pack(side='left', padx=2, fill='x', expand=True)
            entry.bind('<KeyRelease>', self.trigger_preview_update)
            
            if key in default_values:
                entry.insert(0, default_values[key])
            
            self.entries[key] = entry
        
        # CHAMPS PERSONNALISÉS
        custom_header = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"])
        custom_header.pack(padx=5, pady=(5, 3), fill='x')
        
        ctk.CTkLabel(
            custom_header,
            text='CUSTOM FIELDS',
            font=ctk.CTkFont(family='Consolas', size=12, weight='bold'),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=5)
        
        ctk.CTkButton(
            custom_header,
            text='➕ Add Field',
            command=self.add_custom_field,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10),
            width=80,
            height=30,
            border_color=COLORS["border"],
            border_width=1
        ).pack(side='right', padx=5)
        
        self.custom_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"])
        self.custom_frame.pack(padx=5, pady=0, fill='x')
        self.custom_frame.pack_forget()
        
        # TAILLE PHOTO
        photo_size_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        photo_size_frame.pack(padx=5, pady=2, fill='x')
        
        ctk.CTkLabel(
            photo_size_frame,
            text='Photo Size:',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=5)
        
        self.photo_size_slider = ctk.CTkSlider(
            photo_size_frame,
            from_=0.5,
            to=2.0,
            number_of_steps=30,
            command=self.change_photo_size,
            width=100
        )
        self.photo_size_slider.set(self.photo_scale)
        self.photo_size_slider.pack(side='left', padx=5, fill='x', expand=True)
        
        self.photo_size_label = ctk.CTkLabel(
            photo_size_frame,
            text='1.2x',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"],
            width=35
        )
        self.photo_size_label.pack(side='left', padx=5)
        
        # TAILLE QR
        qr_size_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        qr_size_frame.pack(padx=5, pady=2, fill='x')
        
        ctk.CTkLabel(
            qr_size_frame,
            text='QR Size:',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=5)
        
        self.qr_size_slider = ctk.CTkSlider(
            qr_size_frame,
            from_=0.5,
            to=2.0,
            number_of_steps=30,
            command=self.change_qr_size,
            width=100
        )
        self.qr_size_slider.set(1.0)
        self.qr_size_slider.pack(side='left', padx=5, fill='x', expand=True)
        
        self.qr_size_label = ctk.CTkLabel(
            qr_size_frame,
            text='1.0x',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"],
            width=35
        )
        self.qr_size_label.pack(side='left', padx=5)
        
        # TAILLE SIGNATURE
        signature_size_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        signature_size_frame.pack(padx=5, pady=2, fill='x')
        
        ctk.CTkLabel(
            signature_size_frame,
            text='Signature Size:',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=5)
        
        self.signature_size_slider = ctk.CTkSlider(
            signature_size_frame,
            from_=0.5,
            to=2.0,
            number_of_steps=30,
            command=self.change_signature_size,
            width=100
        )
        self.signature_size_slider.set(1.0)
        self.signature_size_slider.pack(side='left', padx=5, fill='x', expand=True)
        
        self.signature_size_label = ctk.CTkLabel(
            signature_size_frame,
            text='1.0x',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"],
            width=35
        )
        self.signature_size_label.pack(side='left', padx=5)
        
        # PHOTO
        photo_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        photo_frame.pack(padx=5, pady=2, fill='x')
        
        ctk.CTkLabel(
            photo_frame,
            text='Photo:',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=3)
        
        self.photo_label = ctk.CTkLabel(
            photo_frame,
            text='None',
            font=ctk.CTkFont(family='Consolas', size=9),
            text_color=COLORS["text_secondary"]
        )
        self.photo_label.pack(side='left', padx=5, fill='x', expand=True)
        
        ctk.CTkButton(
            photo_frame,
            text='📷 Import',
            command=self.load_photo,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10),
            width=50,
            height=30
        ).pack(side='right', padx=3)
        
        ctk.CTkButton(
            photo_frame,
            text='🗑️ Remove',
            command=self.remove_photo,
            fg_color=COLORS["red"],
            hover_color=COLORS["red_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10),
            width=50,
            height=30
        ).pack(side='right', padx=3)
        
        # SIGNATURE IMAGE
        signature_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        signature_frame.pack(padx=5, pady=2, fill='x')
        
        ctk.CTkLabel(
            signature_frame,
            text='Signature:',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=3)
        
        self.signature_label = ctk.CTkLabel(
            signature_frame,
            text='None',
            font=ctk.CTkFont(family='Consolas', size=9),
            text_color=COLORS["text_secondary"]
        )
        self.signature_label.pack(side='left', padx=5, fill='x', expand=True)
        
        ctk.CTkButton(
            signature_frame,
            text='✍️ Import',
            command=self.load_signature,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10),
            width=50,
            height=30
        ).pack(side='right', padx=3)
        
        ctk.CTkButton(
            signature_frame,
            text='🗑️ Remove',
            command=self.remove_signature,
            fg_color=COLORS["red"],
            hover_color=COLORS["red_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10),
            width=50,
            height=30
        ).pack(side='right', padx=3)
        
        # TEMPLATE
        template_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        template_frame.pack(padx=5, pady=2, fill='x')
        
        ctk.CTkLabel(
            template_frame,
            text='Template:',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"]
        ).pack(side='left', padx=3)
        
        self.template_label = ctk.CTkLabel(
            template_frame,
            text='Default',
            font=ctk.CTkFont(family='Consolas', size=9),
            text_color=COLORS["text_secondary"]
        )
        self.template_label.pack(side='left', padx=5, fill='x', expand=True)
        
        ctk.CTkButton(
            template_frame,
            text='🖼️ Import',
            command=self.load_template,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10),
            width=50,
            height=30
        ).pack(side='right', padx=3)
        
        ctk.CTkButton(
            template_frame,
            text='↺ Reset',
            command=self.reset_template,
            fg_color=COLORS["red"],
            hover_color=COLORS["red_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10),
            width=50,
            height=30
        ).pack(side='right', padx=3)
        
        # QR
        qr_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        qr_frame.pack(padx=5, pady=2, fill='x')
        
        ctk.CTkCheckBox(
            qr_frame,
            text='QR Code',
            variable=self.use_qr,
            command=self.trigger_preview_update,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            border_color=COLORS["green_dark"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10)
        ).pack(side='left', padx=3)
        
        ctk.CTkEntry(
            qr_frame,
            textvariable=self.qr_url,
            font=ctk.CTkFont(family='Consolas', size=9),
            fg_color=COLORS["bg"],
            text_color=COLORS["text"],
            border_color=COLORS["green_dark"],
            border_width=1,
            corner_radius=3,
            placeholder_text='URL (optional)'
        ).pack(side='left', padx=3, fill='x', expand=True)
        self.qr_url.trace('w', lambda *args: self.trigger_preview_update())
        
        # BOUTON GENERATE
        generate_frame = ctk.CTkFrame(scroll_frame, fg_color=COLORS["frame_light"], corner_radius=5)
        generate_frame.pack(padx=5, pady=10, fill='x')
        
        ctk.CTkButton(
            generate_frame,
            text='▶ GENERATE CARD',
            command=self.generate_card,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=14, weight='bold'),
            border_color=COLORS["border"],
            border_width=2,
            height=45
        ).pack(fill='x', pady=5, padx=5)
        
        # DROITE : PREVIEW
        preview_frame = ctk.CTkFrame(
            container,
            fg_color=COLORS["frame_light"],
            corner_radius=8,
            border_color=COLORS["green_dark"],
            border_width=1
        )
        preview_frame.pack(side='right', padx=5, pady=5, fill='both', expand=True)
        
        ctk.CTkLabel(
            preview_frame,
            text='LIVE PREVIEW (Drag text/photo/QR/signature/MRZ to move)',
            font=ctk.CTkFont(family='Consolas', size=13, weight='bold'),
            text_color=COLORS["green_bright"]
        ).pack(pady=5)
        
        self.canvas = ctk.CTkCanvas(
            preview_frame,
            bg=COLORS["bg"],
            highlightthickness=1,
            highlightcolor=COLORS["green_dark"],
            cursor='hand2'
        )
        self.canvas.pack(padx=10, pady=10, fill='both', expand=True)
        
        self.canvas.bind('<Button-1>', self.on_mouse_down)
        self.canvas.bind('<B1-Motion>', self.on_mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_mouse_up)
        self.canvas.bind('<Leave>', self.on_mouse_leave)
        
        self.status_label = ctk.CTkLabel(
            main_frame,
            text='Ready - Drag to reposition | Text Size & MRZ Size sliders | Add custom fields',
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["text_secondary"]
        )
        self.status_label.pack(pady=3)
        
        self.bind('<Configure>', self.on_resize)
    
    def change_mrz_size(self, value):
        self.mrz_size = round(float(value), 2)
        self.mrz_size_label.configure(text=f'{self.mrz_size:.1f}x')
        self.trigger_preview_update()
    
    def change_text_size(self, value):
        self.text_size = round(float(value), 2)
        self.text_size_label.configure(text=f'{self.text_size:.1f}x')
        self.trigger_preview_update()
    
    def change_photo_size(self, value):
        self.photo_scale = round(float(value), 2)
        self.photo_size_label.configure(text=f'{self.photo_scale:.1f}x')
        self.trigger_preview_update()
    
    def change_qr_size(self, value):
        self.qr_scale = round(float(value), 2)
        self.qr_size_label.configure(text=f'{self.qr_scale:.1f}x')
        self.trigger_preview_update()
    
    def change_signature_size(self, value):
        self.signature_scale = round(float(value), 2)
        self.signature_size_label.configure(text=f'{self.signature_scale:.1f}x')
        self.trigger_preview_update()
    
    def randomize_all(self):
        self.doc_number = self.generate_doc_number()
        self.birth_date = self.generate_birth_date()
        self.issue_date = self.generate_issue_date()
        self.sex = random.choice(["M", "F"])
        self.place_of_birth = random.choice(["PARIS", "LYON", "MARSEILLE", "BORDEAUX", "LILLE", "TOULOUSE", "NICE", "NANTES"])
        self.height = random.randint(150, 200)
        self.department = random.choice(["75", "69", "13", "33", "59", "31", "06", "44"])
        
        surnames = ["DUPONT", "MARTIN", "DURAND", "PETIT", "ROBERT", "RICHARD", "MOREAU", "LAURENT", "SIMON", "MICHEL", "LEFEBVRE", "LEROY", "MORIN", "BONNET"]
        given_names_list = ["JEAN", "PIERRE", "MARIE", "PAUL", "JACQUES", "ANNE", "LOUIS", "PHILIPPE", "FRANÇOIS", "CLAIRE", "NICOLAS", "JULIE", "SOPHIE", "THOMAS"]
        
        if 'surname' in self.entries:
            self.entries['surname'].delete(0, 'end')
            self.entries['surname'].insert(0, random.choice(surnames))
        
        if 'given_names' in self.entries:
            self.entries['given_names'].delete(0, 'end')
            self.entries['given_names'].insert(0, random.choice(given_names_list))
        
        if 'sex' in self.entries:
            self.entries['sex'].delete(0, 'end')
            self.entries['sex'].insert(0, self.sex)
        
        if 'dob' in self.entries:
            self.entries['dob'].delete(0, 'end')
            self.entries['dob'].insert(0, self.birth_date)
        
        if 'pob' in self.entries:
            self.entries['pob'].delete(0, 'end')
            self.entries['pob'].insert(0, self.place_of_birth)
        
        if 'height' in self.entries:
            self.entries['height'].delete(0, 'end')
            self.entries['height'].insert(0, str(self.height))
        
        if 'doc_no' in self.entries:
            self.entries['doc_no'].delete(0, 'end')
            self.entries['doc_no'].insert(0, self.doc_number)
        
        self.trigger_preview_update()
        self.status_label.configure(text='[+] Random data generated!')
    
    def generate_card(self):
        self.status_label.configure(text='[*] Generating card...')
        try:
            img = self.render_card(1200, 840)
            output_dir = os.path.join(root_path, 'output')
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = os.path.join(output_dir, f'id_card_{timestamp}.png')
            img.save(filename)
            self.status_label.configure(text=f'[+] Card saved: {filename}')
            messagebox.showinfo('Success', f'ID Card saved to:\n{filename}')
        except Exception as e:
            self.status_label.configure(text=f'[!] Error: {str(e)}')
            messagebox.showerror('Error', f'Generation failed: {str(e)}')
    
    def add_custom_field(self):
        if not self.custom_frame.winfo_ismapped():
            self.custom_frame.pack(padx=5, pady=0, fill='x')
        
        name = f"Text {self.custom_counter}"
        self.custom_counter += 1
        
        key = f"custom_{len(self.custom_fields)}"
        x_pos = 0.15
        y_pos = 0.76 + len(self.custom_fields) * 0.05
        self.pos[key] = [x_pos, y_pos]
        self.custom_fields[key] = [name, x_pos, y_pos]
        self.custom_field_keys.append(key)
        
        row = ctk.CTkFrame(self.custom_frame, fg_color=COLORS["frame_light"])
        row.pack(fill='x', pady=1, padx=5)
        
        label = ctk.CTkLabel(
            row, 
            text=name, 
            font=ctk.CTkFont(family='Consolas', size=10),
            text_color=COLORS["green_bright"],
            width=100,
            anchor='w'
        )
        label.pack(side='left', padx=2)
        
        entry = ctk.CTkEntry(
            row, 
            font=ctk.CTkFont(family='Consolas', size=10),
            fg_color=COLORS["bg"], 
            text_color=COLORS["text"],
            border_color=COLORS["green_dark"],
            border_width=1,
            corner_radius=3,
            height=28
        )
        entry.pack(side='left', padx=2, fill='x', expand=True)
        entry.bind('<KeyRelease>', self.trigger_preview_update)
        entry.insert(0, name.upper())
        
        self.entries[key] = entry
        
        ctk.CTkButton(
            row,
            text='✕',
            command=lambda k=key: self.remove_custom_field(k),
            fg_color=COLORS["red"],
            hover_color=COLORS["red_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=10, weight='bold'),
            width=25,
            height=25
        ).pack(side='right', padx=2)
        
        self.status_label.configure(text=f'Field added: {name}')
        self.trigger_preview_update()
    
    def remove_custom_field(self, key):
        if key in self.custom_fields:
            del self.custom_fields[key]
        if key in self.custom_field_keys:
            self.custom_field_keys.remove(key)
        if key in self.pos:
            del self.pos[key]
        if key in self.entries:
            self.entries[key].master.destroy()
            del self.entries[key]
        if len(self.custom_fields) == 0:
            self.custom_frame.pack_forget()
        self.status_label.configure(text='Field removed')
        self.trigger_preview_update()
    
    def remove_photo(self):
        self.user_photo = None
        self.photo_path = None
        self.photo_label.configure(text='None')
        self.status_label.configure(text='Photo removed')
        self.trigger_preview_update()
    
    def remove_signature(self):
        self.user_signature = None
        self.signature_path = None
        self.signature_label.configure(text='None')
        self.status_label.configure(text='Signature removed')
        self.trigger_preview_update()
    
    def load_signature(self):
        file_path = filedialog.askopenfilename(
            title='Select Signature Image',
            filetypes=[('Image files', '*.png *.jpg *.jpeg *.bmp *.gif')]
        )
        if file_path:
            self.signature_path = file_path
            self.user_signature = Image.open(file_path)
            self.signature_label.configure(text=os.path.basename(file_path)[:15])
            self.status_label.configure(text=f'Signature loaded: {os.path.basename(file_path)}')
            self.trigger_preview_update()
    
    def on_preset_change(self, choice):
        if choice == '--- Create New ---':
            self.create_new_preset()
        else:
            self.current_preset = choice
            preset = self.presets.get(choice)
            if preset:
                for i, key in enumerate(self.field_keys):
                    if i < len(preset['fields']):
                        self.field_labels[i] = preset['fields'][i]
                self.status_label.configure(text=f'Preset loaded: {choice}')
                self.update_preview()
    
    def create_new_preset(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title('Create New Preset')
        dialog.geometry('400x220')
        dialog.resizable(False, False)
        dialog.configure(fg_color=COLORS["bg"])
        dialog.transient(self)
        dialog.grab_set()
        
        icon_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'shrek.ico')
        if os.path.exists(icon_path):
            try:
                dialog.iconbitmap(icon_path)
            except:
                pass
        
        dialog.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - 400) // 2
        y = self.winfo_y() + (self.winfo_height() - 220) // 2
        dialog.geometry(f'+{x}+{y}')
        
        main_frame = ctk.CTkFrame(dialog, fg_color=COLORS["frame"], corner_radius=10)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ctk.CTkLabel(
            main_frame,
            text='[ NEW PRESET ]',
            font=ctk.CTkFont(family='Consolas', size=16, weight='bold'),
            text_color=COLORS["green_bright"]
        ).pack(pady=(15, 10))
        
        ctk.CTkLabel(
            main_frame,
            text='Preset name:',
            font=ctk.CTkFont(family='Consolas', size=12),
            text_color=COLORS["text_secondary"]
        ).pack(anchor='w', padx=20)
        
        entry = ctk.CTkEntry(
            main_frame,
            font=ctk.CTkFont(family='Consolas', size=12),
            fg_color=COLORS["bg"],
            text_color=COLORS["text"],
            border_color=COLORS["green_dark"],
            border_width=1,
            corner_radius=3,
            height=35
        )
        entry.pack(padx=20, pady=(5, 15), fill='x')
        entry.focus()
        
        btn_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["frame"])
        btn_frame.pack(pady=(0, 15))
        
        def on_confirm():
            name = entry.get().strip()
            if not name:
                return
            if name in self.presets:
                messagebox.showerror('Error', 'Preset already exists!')
                return
            self.presets[name] = {
                'fields': self.field_labels.copy(),
                'template': 'custom.png'
            }
            self.custom_preset_names.append(name)
            self.current_preset = name
            self.preset_var.set(name)
            self.update_preset_menu()
            self.status_label.configure(text=f'New preset created: {name}')
            dialog.destroy()
        
        ctk.CTkButton(
            btn_frame,
            text='[ CREATE ]',
            command=on_confirm,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=12, weight='bold'),
            border_color=COLORS["border"],
            border_width=1,
            width=100,
            height=40
        ).pack(side='left', padx=5)
        
        ctk.CTkButton(
            btn_frame,
            text='[ CANCEL ]',
            command=dialog.destroy,
            fg_color=COLORS["frame"],
            hover_color=COLORS["frame_light"],
            text_color=COLORS["text_secondary"],
            font=ctk.CTkFont(family='Consolas', size=12),
            border_color=COLORS["green_dark"],
            border_width=1,
            width=100,
            height=40
        ).pack(side='left', padx=5)
        
        entry.bind('<Return>', lambda e: on_confirm())
    
    def save_preset(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title('Save Preset')
        dialog.geometry('400x220')
        dialog.resizable(False, False)
        dialog.configure(fg_color=COLORS["bg"])
        dialog.transient(self)
        dialog.grab_set()
        
        icon_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'shrek.ico')
        if os.path.exists(icon_path):
            try:
                dialog.iconbitmap(icon_path)
            except:
                pass
        
        dialog.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - 400) // 2
        y = self.winfo_y() + (self.winfo_height() - 220) // 2
        dialog.geometry(f'+{x}+{y}')
        
        main_frame = ctk.CTkFrame(dialog, fg_color=COLORS["frame"], corner_radius=10)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ctk.CTkLabel(
            main_frame,
            text='[ SAVE PRESET ]',
            font=ctk.CTkFont(family='Consolas', size=16, weight='bold'),
            text_color=COLORS["green_bright"]
        ).pack(pady=(15, 10))
        
        ctk.CTkLabel(
            main_frame,
            text='Preset name:',
            font=ctk.CTkFont(family='Consolas', size=12),
            text_color=COLORS["text_secondary"]
        ).pack(anchor='w', padx=20)
        
        entry = ctk.CTkEntry(
            main_frame,
            font=ctk.CTkFont(family='Consolas', size=12),
            fg_color=COLORS["bg"],
            text_color=COLORS["text"],
            border_color=COLORS["green_dark"],
            border_width=1,
            corner_radius=3,
            height=35
        )
        entry.pack(padx=20, pady=(5, 15), fill='x')
        entry.focus()
        
        btn_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["frame"])
        btn_frame.pack(pady=(0, 15))
        
        def on_confirm():
            name = entry.get().strip()
            if not name:
                return
            if name in self.presets:
                messagebox.showerror('Error', 'Preset already exists!')
                return
            self.presets[name] = {
                'fields': self.field_labels.copy(),
                'template': 'custom.png'
            }
            if name not in ['France']:
                self.custom_preset_names.append(name)
            self.current_preset = name
            self.preset_var.set(name)
            self.update_preset_menu()
            self.status_label.configure(text=f'Preset saved: {name}')
            dialog.destroy()
        
        ctk.CTkButton(
            btn_frame,
            text='[ SAVE ]',
            command=on_confirm,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["text"],
            font=ctk.CTkFont(family='Consolas', size=12, weight='bold'),
            border_color=COLORS["border"],
            border_width=1,
            width=100,
            height=40
        ).pack(side='left', padx=5)
        
        ctk.CTkButton(
            btn_frame,
            text='[ CANCEL ]',
            command=dialog.destroy,
            fg_color=COLORS["frame"],
            hover_color=COLORS["frame_light"],
            text_color=COLORS["text_secondary"],
            font=ctk.CTkFont(family='Consolas', size=12),
            border_color=COLORS["green_dark"],
            border_width=1,
            width=100,
            height=40
        ).pack(side='left', padx=5)
        
        entry.bind('<Return>', lambda e: on_confirm())
    
    def delete_preset(self):
        if self.current_preset == 'France':
            messagebox.showerror('Error', 'Cannot delete default preset!')
            return
        if self.current_preset in self.custom_preset_names:
            self.custom_preset_names.remove(self.current_preset)
        del self.presets[self.current_preset]
        self.current_preset = 'France'
        self.preset_var.set('France')
        self.update_preset_menu()
        self.status_label.configure(text=f'Preset deleted')
    
    def update_preset_menu(self):
        preset_list = ['France'] + self.custom_preset_names + ['--- Create New ---']
        self.preset_menu.configure(values=preset_list)
        self.preset_var.set(self.current_preset)
    
    def load_template(self):
        file_path = filedialog.askopenfilename(
            title='Select Template Image',
            filetypes=[('Image files', '*.png *.jpg *.jpeg *.bmp *.gif')]
        )
        if file_path:
            self.custom_template_path = file_path
            self.custom_template = Image.open(file_path)
            self.template_label.configure(text=os.path.basename(file_path)[:20])
            self.status_label.configure(text=f'Template loaded: {os.path.basename(file_path)}')
            self.trigger_preview_update()
    
    def reset_template(self):
        self.custom_template_path = None
        self.custom_template = None
        self.template_label.configure(text='Default')
        self.status_label.configure(text='Template reset to default')
        self.trigger_preview_update()
    
    # ---- DRAG & DROP ----
    def on_mouse_down(self, event):
        canvas_x = event.x
        canvas_y = event.y
        
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        
        target_ratio = 900 / 630
        if canvas_w / canvas_h > target_ratio:
            img_h = canvas_h
            img_w = int(canvas_h * target_ratio)
        else:
            img_w = canvas_w
            img_h = int(canvas_w / target_ratio)
        
        offset_x = (canvas_w - img_w) // 2
        offset_y = (canvas_h - img_h) // 2
        
        rel_x = (canvas_x - offset_x) / img_w
        rel_y = (canvas_y - offset_y) / img_h
        
        for key, pos in self.pos.items():
            px, py = pos
            detection_range = 0.07 if key.startswith('mrz') else 0.04
            if abs(rel_x - px) < detection_range and abs(rel_y - py) < detection_range:
                self.dragging = True
                self.drag_key = key
                self.drag_type = 'text'
                self.pos_start_x = pos[0]
                self.pos_start_y = pos[1]
                self.drag_start_x = rel_x
                self.drag_start_y = rel_y
                self.status_label.configure(text=f'Dragging: {key}')
                self.canvas.configure(cursor='fleur')
                return
        
        if self.user_photo:
            px, py = self.photo_pos
            if abs(rel_x - px) < 0.10 and abs(rel_y - py) < 0.12:
                self.dragging = True
                self.drag_key = 'photo'
                self.drag_type = 'photo'
                self.pos_start_x = px
                self.pos_start_y = py
                self.drag_start_x = rel_x
                self.drag_start_y = rel_y
                self.status_label.configure(text='Dragging: Photo')
                self.canvas.configure(cursor='fleur')
                return
        
        if self.use_qr.get():
            px, py = self.qr_pos
            if abs(rel_x - px) < 0.06 and abs(rel_y - py) < 0.06:
                self.dragging = True
                self.drag_key = 'qr'
                self.drag_type = 'qr'
                self.pos_start_x = px
                self.pos_start_y = py
                self.drag_start_x = rel_x
                self.drag_start_y = rel_y
                self.status_label.configure(text='Dragging: QR Code')
                self.canvas.configure(cursor='fleur')
                return
        
        if self.user_signature:
            px, py = self.signature_pos
            if abs(rel_x - px) < 0.10 and abs(rel_y - py) < 0.08:
                self.dragging = True
                self.drag_key = 'signature'
                self.drag_type = 'signature'
                self.pos_start_x = px
                self.pos_start_y = py
                self.drag_start_x = rel_x
                self.drag_start_y = rel_y
                self.status_label.configure(text='Dragging: Signature')
                self.canvas.configure(cursor='fleur')
                return
        
        self.dragging = False
        self.canvas.configure(cursor='hand2')
    
    def on_mouse_drag(self, event):
        if not self.dragging:
            return
        
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        
        target_ratio = 900 / 630
        if canvas_w / canvas_h > target_ratio:
            img_h = canvas_h
            img_w = int(canvas_h * target_ratio)
        else:
            img_w = canvas_w
            img_h = int(canvas_w / target_ratio)
        
        offset_x = (canvas_w - img_w) // 2
        offset_y = (canvas_h - img_h) // 2
        
        rel_x = (event.x - offset_x) / img_w
        rel_y = (event.y - offset_y) / img_h
        
        dx = rel_x - self.drag_start_x
        dy = rel_y - self.drag_start_y
        
        new_x = max(0.0, min(1.0, self.pos_start_x + dx))
        new_y = max(0.0, min(1.0, self.pos_start_y + dy))
        
        if self.drag_type == 'text':
            self.pos[self.drag_key] = [new_x, new_y]
        elif self.drag_type == 'photo':
            self.photo_pos = [new_x, new_y]
        elif self.drag_type == 'qr':
            self.qr_pos = [new_x, new_y]
        elif self.drag_type == 'signature':
            self.signature_pos = [new_x, new_y]
        
        self.trigger_preview_update()
    
    def on_mouse_up(self, event):
        if self.dragging and self.drag_key:
            self.status_label.configure(text=f'Position saved for: {self.drag_key}')
        self.dragging = False
        self.drag_key = None
        self.drag_type = None
        self.canvas.configure(cursor='hand2')
    
    def on_mouse_leave(self, event):
        if self.dragging:
            self.dragging = False
            self.drag_key = None
            self.drag_type = None
            self.canvas.configure(cursor='hand2')
            self.status_label.configure(text='Drag cancelled')
    
    def load_photo(self):
        file_path = filedialog.askopenfilename(
            title='Select Photo',
            filetypes=[('Image files', '*.png *.jpg *.jpeg *.bmp *.gif')]
        )
        if file_path:
            self.photo_path = file_path
            self.user_photo = Image.open(file_path)
            self.photo_label.configure(text=os.path.basename(file_path)[:15])
            self.status_label.configure(text=f'Photo loaded: {os.path.basename(file_path)}')
            self.trigger_preview_update()
    
    def on_resize(self, event):
        if event.widget == self:
            self.trigger_preview_update()
    
    def render_card(self, width, height):
        data = {key: e.get().strip() for key, e in self.entries.items()}
        for k in data:
            if not data[k]:
                data[k] = ''
        
        # --- RATIO EXACT DE LA CNI FRANÇAISE (85.6mm x 54mm) ---
        target_ratio = 85.6 / 54.0
        if width / height > target_ratio:
            height = int(width / target_ratio)
        else:
            width = int(height * target_ratio)
        
        try:
            if self.custom_template is not None:
                img = self.custom_template.copy().convert('RGB')
                orig_w, orig_h = img.size
                ratio = min(width / orig_w, height / orig_h)
                new_w = int(orig_w * ratio)
                new_h = int(orig_h * ratio)
                img = img.resize((new_w, new_h), Image.LANCZOS)
                x_offset = (width - new_w) // 2
                y_offset = (height - new_h) // 2
                bg = Image.new('RGB', (width, height), '#1a1a2e')
                bg.paste(img, (x_offset, y_offset))
                img = bg
            elif os.path.exists(self.template_path):
                img = Image.open(self.template_path).convert('RGB')
                orig_w, orig_h = img.size
                ratio = min(width / orig_w, height / orig_h)
                new_w = int(orig_w * ratio)
                new_h = int(orig_h * ratio)
                img = img.resize((new_w, new_h), Image.LANCZOS)
                x_offset = (width - new_w) // 2
                y_offset = (height - new_h) // 2
                bg = Image.new('RGB', (width, height), '#1a1a2e')
                bg.paste(img, (x_offset, y_offset))
                img = bg
            else:
                img = Image.new('RGB', (width, height), (216, 236, 220))
                draw = ImageDraw.Draw(img)
                try:
                    font = ImageFont.truetype(self.font_path, int(height * 0.04))
                except:
                    font = ImageFont.load_default()
                draw.text((int(width*0.05), int(height*0.05)), 'TEMPLATE NOT FOUND', fill='#ff0000', font=font)
                draw.text((int(width*0.05), int(height*0.10)), 'Place your template at:', fill='#000000', font=font)
                draw.text((int(width*0.05), int(height*0.15)), self.template_path, fill='#000000', font=font)
        except Exception as e:
            img = Image.new('RGB', (width, height), '#ff0000')
            draw = ImageDraw.Draw(img)
            try:
                font = ImageFont.truetype(self.font_path, int(height * 0.03))
            except:
                font = ImageFont.load_default()
            draw.text((int(width*0.05), int(height*0.05)), f'Error: {str(e)}', fill='#ffffff', font=font)
        
        # ---- AJOUT DES FILIGRANES (Marianne et RF) ----
        try:
            marianne_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'marianne_watermark.png')
            if os.path.exists(marianne_path):
                marianne = Image.open(marianne_path).convert('RGBA')
                marianne = marianne.resize((width, height), Image.LANCZOS)
                img = Image.alpha_composite(img.convert('RGBA'), marianne).convert('RGB')
        except:
            pass
        
        # ---- AJOUT DES GUILLOCHES ----
        try:
            guilloche_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'guilloche.png')
            if os.path.exists(guilloche_path):
                guilloche = Image.open(guilloche_path).convert('RGBA')
                guilloche = guilloche.resize((width, height), Image.LANCZOS)
                img = Image.alpha_composite(img.convert('RGBA'), guilloche).convert('RGB')
        except:
            pass
        
        # ---- AJOUT DES RF PUNCHES ----
        try:
            rf_punch_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'rf_punch.png')
            if os.path.exists(rf_punch_path):
                rf_punch = Image.open(rf_punch_path).convert('RGBA')
                rf_punch = rf_punch.resize((width, height), Image.LANCZOS)
                img = Image.alpha_composite(img.convert('RGBA'), rf_punch).convert('RGB')
        except:
            pass
        
        # ---- AJOUT DES BANDELETTES DORÉES RF ----
        try:
            rf_stripe_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'rf_stripe.png')
            if os.path.exists(rf_stripe_path):
                rf_stripe = Image.open(rf_stripe_path).convert('RGBA')
                rf_stripe = rf_stripe.resize((width, height), Image.LANCZOS)
                img = Image.alpha_composite(img.convert('RGBA'), rf_stripe).convert('RGB')
        except:
            pass
        
        # ---- AJOUT DU FIL DE SÉCURITÉ ----
        try:
            security_thread_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'security_thread.png')
            if os.path.exists(security_thread_path):
                security_thread = Image.open(security_thread_path).convert('RGBA')
                security_thread = security_thread.resize((width, height), Image.LANCZOS)
                img = Image.alpha_composite(img.convert('RGBA'), security_thread).convert('RGB')
        except:
            pass
        
        draw = ImageDraw.Draw(img)
        
        # ---- TAILLE DES TEXTES (TOUS IDENTIQUES) ----
        TAILLE_TEXTE = int(26 * self.text_size)
        TAILLE_MRZ = int(18 * self.mrz_size)
        
        try:
            if self.font_path and os.path.exists(self.font_path):
                font_texte = ImageFont.truetype(self.font_path, TAILLE_TEXTE)
                font_mrz = ImageFont.truetype(self.font_path, TAILLE_MRZ)
            else:
                raise Exception("Police non trouvée")
        except:
            font_texte = ImageFont.load_default()
            font_mrz = ImageFont.load_default()
        
        color_text = '#1a1a2e'
        color_mrz = '#000000'
        
        def get_pos(key):
            x_percent, y_percent = self.pos[key]
            return (int(width * x_percent), int(height * y_percent))
        
        # ======== ÉTAPE 1 : ON DESSINE LA PHOTO EN PREMIER (EN ARRIÈRE-PLAN) ========
        if self.user_photo:
            try:
                photo_width = int(width * 0.20 * self.photo_scale)
                photo_height = int(photo_width / (35/45))
                
                photo_x = int(width * self.photo_pos[0])
                photo_y = int(height * self.photo_pos[1])
                
                if photo_y + photo_height > height * 0.80:
                    photo_height = int(height * 0.80) - photo_y
                    photo_width = int(photo_height * (35/45))
                
                # PAS DE cadre blanc
                photo = self.user_photo.copy().convert('L')
                photo = photo.convert('RGB')
                photo = photo.resize((photo_width, photo_height), Image.LANCZOS)
                img.paste(photo, (photo_x, photo_y))
            except:
                pass
        
        # ======== ÉTAPE 2 : ON DESSINE LES TEXTES ET LE RESTE PAR-DESSUS ========
        # ---- ÉCRIT LES TEXTES ----
        if data.get('surname'):
            x, y = get_pos('surname')
            draw.text((x, y), data['surname'].upper(), fill=color_text, font=font_texte)
        
        if data.get('given_names'):
            x, y = get_pos('given_names')
            draw.text((x, y), data['given_names'].upper(), fill=color_text, font=font_texte)
        
        if data.get('sex'):
            x, y = get_pos('sex')
            draw.text((x, y), data['sex'].upper(), fill=color_text, font=font_texte)
        
        if data.get('dob'):
            x, y = get_pos('dob')
            draw.text((x, y), data['dob'], fill=color_text, font=font_texte)
        
        if data.get('pob'):
            x, y = get_pos('pob')
            draw.text((x, y), data['pob'].upper(), fill=color_text, font=font_texte)
        
        if data.get('height'):
            x, y = get_pos('height')
            draw.text((x, y), f"{data['height']} cm", fill=color_text, font=font_texte)
        
        if data.get('doc_no'):
            x, y = get_pos('doc_no')
            draw.text((x, y), data['doc_no'], fill=color_text, font=font_texte)
        
        # ---- INITIALES ----
        initials = self.get_initials(data.get('surname', ''), data.get('given_names', ''))
        if initials:
            x, y = get_pos('initials')
            draw.text((x, y), initials, fill=color_text, font=font_texte)
        
        # ---- MRZ ----
        surname = data.get('surname', '')
        given_names = data.get('given_names', '')
        doc_no = data.get('doc_no', self.doc_number)
        birth_date = data.get('dob', '01.01.1990')
        sex = data.get('sex', 'M')
        department = "00"
        
        line1, line2 = self.generate_mrz(
            surname, given_names, doc_no, birth_date, sex, department, self.admin_code
        )
        
        x_mrz1, y_mrz1 = get_pos('mrz_part1')
        draw.text((x_mrz1, y_mrz1), line1, fill=color_mrz, font=font_mrz)
        
        x_mrz2, y_mrz2 = get_pos('mrz_part2')
        draw.text((x_mrz2, y_mrz2), line2, fill=color_mrz, font=font_mrz)
        
        # ---- CHAMPS PERSONNALISÉS ----
        for key in self.custom_field_keys:
            if data.get(key):
                x, y = get_pos(key)
                draw.text((x, y), data[key].upper(), fill=color_text, font=font_texte)
        
        # ---- SIGNATURE ----
        if self.user_signature:
            try:
                sig_width = int(width * 0.14 * self.signature_scale)
                sig_height = int(height * 0.04 * self.signature_scale)
                sig_x = int(width * self.signature_pos[0])
                sig_y = int(height * self.signature_pos[1])
                
                sig = self.user_signature.copy().convert('L')
                sig = sig.point(lambda x: 0 if x < 128 else 255, '1')
                sig = sig.convert('RGB')
                sig = sig.resize((sig_width, sig_height), Image.LANCZOS)
                img.paste(sig, (sig_x, sig_y))
            except:
                pass
        
        # ---- QR ----
        if self.use_qr.get():
            qr_data = self.qr_url.get().strip() or f"ID:{data.get('doc_no', '')}|NAME:{data.get('surname', '')}"
            try:
                qr_size = int(min(width, height) * 0.07 * self.qr_scale)
                qr = qrcode.make(qr_data).convert('RGB').resize((qr_size, qr_size))
                qr_x = int(width * self.qr_pos[0])
                qr_y = int(height * self.qr_pos[1])
                img.paste(qr, (qr_x, qr_y))
            except:
                pass
        
        return img
    
    def render_preview(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width < 10:
            canvas_width = 550
        if canvas_height < 10:
            canvas_height = 400
        
        target_ratio = 900 / 630
        if canvas_width / canvas_height > target_ratio:
            new_height = canvas_height
            new_width = int(canvas_height * target_ratio)
        else:
            new_width = canvas_width
            new_height = int(canvas_width / target_ratio)
        
        return self.render_card(new_width, new_height)
    
    def update_preview(self):
        try:
            if self.canvas.winfo_width() < 10:
                self.after(50, self.update_preview)
                return
            
            pil_img = self.render_preview()
            self.preview_image = pil_img
            self.photo_tk = ImageTk.PhotoImage(pil_img)
            self.canvas.delete('all')
            self.canvas.create_image(
                self.canvas.winfo_width() // 2,
                self.canvas.winfo_height() // 2,
                anchor='center',
                image=self.photo_tk
            )
        except Exception as e:
            self.status_label.configure(text=f'Error: {str(e)[:30]}')
    
    def trigger_preview_update(self, event=None):
        if self.update_timer:
            self.after_cancel(self.update_timer)
        self.update_timer = self.after(200, self.update_preview)

def run():
    set_console_title('ID Card Generator | Shrek Multi Tools')
    os.system('cls' if os.name == 'nt' else 'clear')
    app = IDCardCreator()
    app.mainloop()

if __name__ == '__main__':
    run()