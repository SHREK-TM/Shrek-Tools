# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].

import ctypes
import re
import shutil
import sys
import time
import socket
from colorama import Fore, init
from pystyle import Center, Anime, Colors, Colorate, System

from utilities.core.common import counttokens, cls
from utilities.core.context import get_user_name
from utilities.core.themes import (
    SHREK_BANNER,
    apply_theme_text,
    get_theme,
    get_theme_colors,
    reset,
)

_startup_done = False
_ANSI_RE = re.compile(r"\033\[[0-9;]*m")
_COL_WIDTHS = (26, 26, 26)  

def _visible_len(text: str) -> int:
    return len(_ANSI_RE.sub("", text))


def _pad_visible(text: str, width: int) -> str:
    return text + (" " * max(0, width - _visible_len(text)))


def _terminal_width() -> int:
    try:
        return shutil.get_terminal_size((120, 30)).columns
    except Exception:
        return 120


def center_line(line: str) -> str:
    visible = _visible_len(line)
    pad = max(0, (_terminal_width() - visible) // 2)
    return " " * pad + line


def print_centered(line: str):
    print(center_line(line))


def run_startup_animation():
    """Shrek ASCII animation — runs once at application launch only."""
    global _startup_done
    if _startup_done:
        return
    _startup_done = True
    try:
        System.Size(120, 30)
        System.Clear()
        Anime.Fade(
            Center.Center(SHREK_BANNER),
            Colors.green_to_white,
            Colorate.Vertical,
            interval=0.030,
            enter=True,
        )
    except Exception:
        cls()
        t = get_theme_colors()
        print(t["primary"] + SHREK_BANNER + reset())


def loading_effect(tool_name: str, steps=None):
    t = get_theme_colors()
    cls()
    if steps is None:
        steps = ["Initialisation", "Chargement modules", "Préparation interface"]

    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    bar_width = 28

    print()
    print_centered(f"{t['accent']}{'━' * 40}{reset()}")
    print_centered(f"{t['primary']}▸ {t['highlight']}{tool_name}{reset()}")
    print()

    for i, step in enumerate(steps):
        progress = int((i + 1) / len(steps) * bar_width)
        bar = (
            f"{t['primary']}{'█' * progress}{t['muted']}{'░' * (bar_width - progress)}{reset()}"
        )
        for j in range(3):
            frame = frames[(i * 3 + j) % len(frames)]
            pct = int((i + (j + 1) / 3) / len(steps) * 100)
            line = (
                f"{t['accent']}{frame}{reset()} {step}... {bar} "
                f"{t['muted']}{pct:>3}%{reset()}"
            )
            sys.stdout.write("\r" + center_line(line))
            sys.stdout.flush()
            time.sleep(0.06)

    done = f"{t['primary']}✓{reset()} Prêt ! {' ' * (bar_width + 24)}"
    sys.stdout.write("\r" + center_line(done) + "\n")
    sys.stdout.flush()
    time.sleep(0.25)
    cls()


def tool_open_transition(tool_name: str):
    loading_effect(tool_name)


def render_menu_header(page: int = 1):
    init()
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools | Made by Shrek™")
    t = get_theme_colors()
    r = reset()
    p, a, h = t["primary"], t["accent"], t["highlight"]

    print(
        f"  {Fore.LIGHTBLACK_EX}discord.gg/JKsRYZ244U{Fore.RESET}                                                                                    Tokens: {a}[{h}{counttokens}{a}]"
    )
    print()
    print(f"{p}                                           ██████   ██░ ██  ██▀███  ▓█████ ▀██ ▄█▀ {r}")
    print(f"{p}                                         ▒██    ▒ ▒▓██░ ██ ▓██ ▒ ██▒▓█   ▀  ██▄█▒ {r}")
    print(f"{p}                                         ░ ▓██▄   ░▒██▀▀██ ▓██ ░▄█ ▒▒███   ▓███▄░ {r}")
    print(f"{p}                                           ▒   ██▒ ░▓█ ░██ ▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄ {r}")
    print(f"{p}                                         ▒██████▒▒ ░▓█▒░██▓░██▓ ▒██▒░▒████ ▒██▒ █▄{r}")
    print(f"{p}                                         ▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒▓ ░▒▓░░░ ▒░   ▒ ▒▒ ▓▒{r}")
    print(
        f"{h}› {a}[{h}TM{a}] {h}Made by Shrek™{p}                    ░ ░▒  ░    ▒ ░▒░ ░  ░▒ ░ ▒░ ░ ░   ░ ░▒ ▒░                  {h}Setting & Help {a}[{h}!{a}] {h}‹{r}"
    )
    print(
        f"{h}› {a}[{h}00{a}] {h}Exit{p}                               ░  ░  ░    ░  ░░ ░   ░   ░    ░   ░ ░░ ░                       {h}PREMIUM {a}[{h}BUY{a}] {h}‹{r}"
    )
    print(f"{p}                                                ░    ░  ░  ░   ░        ░   ░  ░    {r}")


def format_menu_entry(tool: dict, t: dict = None) -> str:
    t = t or get_theme_colors()
    r = reset()
    prefix = tool.get("prefix") or ""
    tid = tool["id"]
    name = tool["name"]
    prefix_slot = f"{t['highlight']}{prefix}{r}" if prefix else " "
    return (
        f"{prefix_slot}{t['accent']}[{t['highlight']}{tid}{t['accent']}] "
        f"{t['highlight']}{name}{r}"
    )


def render_menu_grid(tools_page: list, page: int, total_pages: int = 1):
    t = get_theme_colors()
    r = reset()
    a = t["accent"]
    h = t["highlight"]

    cols = [[], [], []]
    sorted_tools = sorted(
        tools_page,
        key=lambda x: (
            x.get("order") if x.get("order") is not None else 9999,
            int(x["id"]) if str(x.get("id", "")).isdigit() else 9999,
        ),
    )
    for idx, tool in enumerate(sorted_tools):
        col_idx = min(idx // 9, 2)
        cols[col_idx].append(format_menu_entry(tool, t))

    max_rows = 9
    na = f" {a}({h}N{a}/{h}A{a})"
    for col in cols:
        while len(col) < max_rows:
            col.append(na)


    border_top = (
        f"{a}              ╔══════════════════════════════╦══════════════════════════════╦══════════════════════════════╗{r}"
    )
    border_mid = (
        f"{a}              ║                              ║                              ║                              ║{r}"
    )
    border_bot = (
        f"{a}              ╚══════════════════════════════╩══════════════════════════════╩══════════════════════════════╝{r}"
    )

    print()
    print(border_top)
    print(border_mid)
    for row in range(max_rows):
        c0 = cols[0][row] if row < len(cols[0]) else ""
        c1 = cols[1][row] if row < len(cols[1]) else ""
        c2 = cols[2][row] if row < len(cols[2]) else ""
        
        line = (
            f"{a}              ║    "
            f"{_pad_visible(c0, _COL_WIDTHS[0])}{a}║    "
            f"{_pad_visible(c1, _COL_WIDTHS[1])}{a}║    "
            f"{_pad_visible(c2, _COL_WIDTHS[2])}{a}║{r}"
        )
        print(line)
    print(border_mid)
    print(border_bot)

    TABLE_TOTAL_WIDTH = 108 

    nav_parts = []
    if page > 1:
        nav_parts.append(f"{a}[{h}P{a}] {h}ᐊ PREVIOUS PAGE")
    if page < total_pages:
        nav_parts.append(f"{a}[{h}N{a}] {h}NEXT PAGE ᐅ")
    nav = "   ".join(nav_parts)
    
    page_info = f"{a}PAGE {h}{page}{a}/{h}{total_pages}{r}"
    
    full_text = f"{page_info}   {nav}".strip() if nav else page_info
    
    visible_len = _visible_len(full_text)
    spaces_needed = max(0, TABLE_TOTAL_WIDTH - visible_len)
    
    print(f"{' ' * spaces_needed}{full_text}")
    print()


def prompt_choice() -> str:
    t = get_theme_colors()
    r = reset()
    user = get_user_name()
    print(f"  {t['highlight']}┌──<{user}{t['accent']}@{t['highlight']}Shrek>─{t['accent']}[{t['highlight']}+{t['accent']}]{r}")
    return input(f"  {t['highlight']}└───{t['accent']}➤{t['highlight']} {r}").strip()