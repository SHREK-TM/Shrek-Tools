import subprocess

packages = [
    "pylibcheck"
    "requests",
    "setuptools",
    "colorama",
    "bs4",
    "selenium",
    "discord",
    "discum",
    "pyinstaller",
    "qrcode",
    "python-http-client",
    "charset_normalizer",
    "2captcha-python",
    "beautifulsoup4",
    "pyperclip",
    "pypiwin32",
    "packaging",
    "keyboard",
    "colored",
    "PyNaCl",
    "easygui",
    "tasksio",
    "colour",
    "pillow",
    "psutil",
    "emoji",
    "httpx",
    "tqdm",
    "websocket",
    "Cipher",
    "Popen",
    "login",
    "pipe",
    "fore",
    "aes",
    "loads",
    "pystyle",
    "pyautogui",
    "pyfadecolor"
]

for package in packages:
    subprocess.run(["pip", "install", package])
