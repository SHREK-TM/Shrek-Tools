# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].

import os

from colorama import Fore, Style
from utilities.core.common import getTempDir

THEMES = ["shrek", "dark", "fire", "water", "neon"]
THEME_FILE = os.path.join(getTempDir(), "shrek_theme")

THEME_PALETTES = {
    "shrek": {
        "primary": Fore.LIGHTGREEN_EX,
        "accent": Fore.GREEN,
        "highlight": Fore.WHITE,
        "muted": Fore.GREEN,
    },
    "dark": {
        "primary": Fore.WHITE,
        "accent": Fore.LIGHTBLACK_EX,
        "highlight": Fore.LIGHTWHITE_EX,
        "muted": Fore.LIGHTBLACK_EX,
    },
    "fire": {
        "primary": Fore.RED,
        "accent": Fore.YELLOW,
        "highlight": Fore.LIGHTYELLOW_EX,
        "muted": Fore.LIGHTRED_EX,
    },
    "water": {
        "primary": Fore.CYAN,
        "accent": Fore.BLUE,
        "highlight": Fore.LIGHTCYAN_EX,
        "muted": Fore.LIGHTBLUE_EX,
    },
    "neon": {
        "primary": Fore.MAGENTA,
        "accent": Fore.LIGHTMAGENTA_EX,
        "highlight": Fore.LIGHTWHITE_EX,
        "muted": Fore.LIGHTBLACK_EX,
    },
}


def _fade_blackwhite(text):
    faded = ""
    red = green = blue = 0
    for line in text.splitlines():
        faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
        if red < 255:
            red += 20
            green += 20
            blue += 20
            if red > 255:
                red = green = blue = 255
    return faded


def _fade_cyan(text):
    fade = ""
    blue = 100
    for line in text.splitlines():
        fade += f"\033[38;2;0;255;{blue}m{line}\033[0m\n"
        blue = min(blue + 15, 255)
    return fade


def _fade_neon(text):
    fade = ""
    for line in text.splitlines():
        red = 255
        for char in line:
            red = max(red - 2, 0)
            fade += f"\033[38;2;{red};0;255m{char}\033[0m"
        fade += "\n"
    return fade


def _fade_purple(text):
    fade = ""
    red = 255
    for line in text.splitlines():
        fade += f"\033[38;2;{red};0;180m{line}\033[0m\n"
        red = max(red - 20, 0)
    return fade


def _fade_water(text):
    fade = ""
    green = 10
    for line in text.splitlines():
        fade += f"\033[38;2;0;{green};255m{line}\033[0m\n"
        green = min(green + 15, 255)
    return fade


def _fade_fire(text):
    fade = ""
    green = 250
    for line in text.splitlines():
        fade += f"\033[38;2;255;{green};0m{line}\033[0m\n"
        green = max(green - 25, 0)
    return fade


FADE_MAP = {
    "dark": (_fade_blackwhite, _fade_blackwhite),
    "fire": (_fade_fire, _fade_fire),
    "water": (_fade_water, _fade_cyan),
    "neon": (_fade_purple, _fade_neon),
}


def _normalize_theme_name(name: str) -> str:
    if name == "hazardous":
        return "shrek"
    return name


def get_theme():
    try:
        with open(THEME_FILE, "r") as f:
            theme = _normalize_theme_name(f.read().strip())
        if theme in THEMES:
            return theme
    except FileNotFoundError:
        pass
    return "shrek"


def set_theme(name: str):
    name = _normalize_theme_name(name)
    if name not in THEMES:
        return False
    with open(THEME_FILE, "w") as f:
        f.write(name)
    return True


def get_theme_colors(theme: str = None) -> dict:
    name = _normalize_theme_name(theme or get_theme())
    return THEME_PALETTES.get(name, THEME_PALETTES["shrek"])


def reset():
    return Style.RESET_ALL


def apply_theme_text(text: str, theme: str = None) -> str:
    theme = _normalize_theme_name(theme or get_theme())
    if theme == "shrek":
        t = get_theme_colors("shrek")
        return t["primary"] + text + reset()
    t1, _ = FADE_MAP.get(theme, (None, None))
    if t1:
        return t1(text)
    return text


SHREK_BANNER = """

  ██████   ██░ ██  ██▀███  ▓█████ ▀██ ▄█▀
▒██    ▒ ▒▓██░ ██ ▓██ ▒ ██▒▓█   ▀  ██▄█▒ 
░ ▓██▄   ░▒██▀▀██ ▓██ ░▄█ ▒▒███   ▓███▄░ 
  ▒   ██▒ ░▓█ ░██ ▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄ 
▒██████▒▒ ░▓█▒░██▓░██▓ ▒██▒░▒████ ▒██▒ █▄
▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒▓ ░▒▓░░░ ▒░  ▒ ▒▒ ▓▒
░ ░▒  ░    ▒ ░▒░ ░  ░▒ ░ ▒░ ░ ░   ░ ░▒ ▒░
░  ░  ░    ░  ░░ ░   ░   ░    ░   ░ ░░ ░ 
      ░    ░  ░  ░   ░        ░   ░  ░   
      
          Github.com/SHREK-TM    
"""
