# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].

import os
import random
import threading

from utilities.core.paths import TOKENS_FILE, USERAGENTS_FILE, TOOLS_ASSETS_DIR

lock = threading.Lock()
threads = 3
ur = "https://discord.com/api/v9/channels/messages"

try:
    tokens = open(TOKENS_FILE, encoding="utf-8").read().splitlines()
except FileNotFoundError:
    tokens = []


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ""
    for _ in range(lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
    }


def secondHeader(token):
    return {
        ":authority": "discord.com",
        ":method": "PATCH",
        ":path": "/api/v9/users/@me",
        ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "authorization": token,
        "content-length": "124",
        "content-type": "application/json",
        "Cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://canary.discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    }


def useragent():
    file_path = USERAGENTS_FILE
    legacy_path = os.path.join(TOOLS_ASSETS_DIR, "user-agents.txt")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            useragents = [agent.strip() for agent in file.readlines() if agent.strip()]
            if useragents:
                return random.choice(useragents)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error reading user-agents file: {e}")
        return ""
    try:
        with open(legacy_path, "r", encoding="utf-8") as file:
            useragents = [agent.strip() for agent in file.readlines() if agent.strip()]
            return random.choice(useragents) if useragents else ""
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Error reading user-agents file: {e}")
        return ""
