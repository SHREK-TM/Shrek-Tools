# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].

import os

from utilities.core.common import yeslist, nolist
from utilities.core.paths import USER_NAME_FILE

_user_name = "User"
_menu_callback = None


def get_user_name():
    return _user_name


def set_user_name(name: str):
    global _user_name
    _user_name = name


def load_user_name():
    global _user_name
    try:
        with open(USER_NAME_FILE, "r", encoding="utf-8") as f:
            _user_name = f.read().strip() or "User"
    except FileNotFoundError:
        pass
    return _user_name


def save_user_name(name: str):
    os.makedirs(os.path.dirname(USER_NAME_FILE), exist_ok=True)
    with open(USER_NAME_FILE, "w", encoding="utf-8") as f:
        f.write(name)
    set_user_name(name)


def register_menu_callback(callback):
    global _menu_callback
    _menu_callback = callback


def return_to_menu():
    if _menu_callback:
        _menu_callback()
