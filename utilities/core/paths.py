# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import os
import sys

# ---- RACINE DU PROJET ----
root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# ---- CHEMINS DES FICHIERS DE DONNÉES ----
DATA_DIR = os.path.join(root_path, 'data')
INPUT_DIR = os.path.join(root_path, 'utilities', 'tools', 'input')
OUTPUT_DIR = os.path.join(root_path, 'output')
TOOLS_ASSETS_DIR = os.path.join(root_path, 'utilities', 'tools', 'input') 

# ---- FICHIERS DE DONNÉES ----
TOKENS_FILE = os.path.join(root_path, 'tokens.txt')
USERAGENTS_FILE = os.path.join(DATA_DIR, 'useragents.txt')
PROXY_FILE = os.path.join(DATA_DIR, 'proxy.txt')
GROUPS_FILE = os.path.join(DATA_DIR, 'groups.txt')
MEMBER_ID_FILE = os.path.join(DATA_DIR, 'Member_id.txt')
CHANNELS_FILE = os.path.join(DATA_DIR, 'channels.txt')
ROLES_FILE = os.path.join(DATA_DIR, 'roles.txt')
DIRB_WORDLIST_FILE = os.path.join(DATA_DIR, 'dirb_wordlist.txt')
KEY_FILE = os.path.join(DATA_DIR, 'key.txt')
KEYGPT_FILE = os.path.join(DATA_DIR, 'keygpt.txt')
SPACE_FREED_FILE = os.path.join(DATA_DIR, 'space_freed.txt')
CONFIG_FILE = os.path.join(INPUT_DIR, 'config.json')

# ---- IMAGES ET ICÔNES (dans tools/input/) ----
BACKGROUND_IMG = os.path.join(INPUT_DIR, 'background.png')
ICON_ICO = os.path.join(INPUT_DIR, 'icon.ico')
SHREK_ICO = os.path.join(INPUT_DIR, 'shrek.ico')
PAYPAL_PNG = os.path.join(INPUT_DIR, 'paypal.png')

# ---- OUTPUT FILES ----
NAMES_FILE = os.path.join(OUTPUT_DIR, 'names.txt')
AUDIT_LOG = os.path.join(OUTPUT_DIR, 'audit.log')
PASSWORDS_FILE = os.path.join(OUTPUT_DIR, 'passwords.txt')
SCAN_FILE = os.path.join(OUTPUT_DIR, 'scan.txt')

# ---- AUTRES ----
USER_SETTINGS_DIR = os.path.join(root_path, 'utilities', 'settings')
USER_NAME_FILE = os.path.join(USER_SETTINGS_DIR, 'user_name.txt')

# ---- FONCTIONS ----
def ensure_project_dirs():
    """Crée tous les dossiers nécessaires du projet"""
    for d in [DATA_DIR, INPUT_DIR, OUTPUT_DIR, USER_SETTINGS_DIR]:
        os.makedirs(d, exist_ok=True)
    return True

def chdir_to_root():
    """Change le répertoire de travail vers la racine du projet"""
    os.chdir(root_path)
    return root_path

# ---- EXPORTS ----
__all__ = [
    'root_path',
    'DATA_DIR',
    'INPUT_DIR',
    'OUTPUT_DIR',
    'TOKENS_FILE',
    'USERAGENTS_FILE',
    'PROXY_FILE',
    'GROUPS_FILE',
    'MEMBER_ID_FILE',
    'CHANNELS_FILE',
    'ROLES_FILE',
    'DIRB_WORDLIST_FILE',
    'KEY_FILE',
    'KEYGPT_FILE',
    'SPACE_FREED_FILE',
    'CONFIG_FILE',
    'BACKGROUND_IMG',
    'ICON_ICO',
    'SHREK_ICO',
    'PAYPAL_PNG',
    'NAMES_FILE',
    'AUDIT_LOG',
    'PASSWORDS_FILE',
    'SCAN_FILE',
    'USER_SETTINGS_DIR',
    'USER_NAME_FILE',
    'ensure_project_dirs',
    'chdir_to_root',
    'migrate_legacy_paths',
]