import os
import platform
import random
import socket
import subprocess
import sys
import ctypes

import requests
from colorama import Fore, Style, init

init(autoreset=True)

def success(text): print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def info(text):    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def warn(text):    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')


def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    except OSError:
        return False


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def pause():
    input(f"\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Press Enter to continue...{Style.RESET_ALL}")


def get_ip_info(ip):
    if not is_valid_ip(ip):
        warn(f"Invalid IP address: {ip}")
        pause()
        return
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url, timeout=5)
        if response.status_code == 404:
            info("Status: invalid")
        else:
            print('')
            success("Status: valid")
        data = response.json()
        info(f"Country: {data.get('country', 'None')}")
        info(f"Region: {data.get('region', 'None')}")
        info(f"City: {data.get('city', 'None')}")
        info(f"Coordinates: {data.get('loc', 'None')}")
        info(f"Timezone: {data.get('timezone', 'None')}")
        info(f"ISP: {data.get('org', 'None')}")
    except requests.RequestException as exc:
        warn(f"Error fetching IP info: {exc}")
    pause()


def ip_pinger(ip):
    if not is_valid_ip(ip):
        warn(f"Invalid IP address: {ip}")
        pause()
        return
    if not is_admin():
        warn("Admin privileges recommended for reliable ping. Run as administrator.")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", ip],
            capture_output=True,
            text=True,
            timeout=10,
            encoding="cp1252",
        )
        info(f"Ping output: {result.stdout.strip()}")
        if result.stderr:
            warn(f"Ping error: {result.stderr.strip()}")
        if result.returncode == 0:
            success(f"{ip} is reachable")
        else:
            warn(f"{ip} is unreachable")
    except subprocess.TimeoutExpired:
        warn("Ping timed out after 10 seconds")
    except subprocess.SubprocessError as exc:
        warn(f"Ping failed: {exc}")
    except UnicodeDecodeError:
        try:
            result = subprocess.run(
                ["ping", param, "1", ip],
                capture_output=True,
                text=True,
                timeout=10,
                encoding="utf-8",
            )
            info(f"Ping output (UTF-8): {result.stdout.strip()}")
            if result.stderr:
                warn(f"Ping error (UTF-8): {result.stderr.strip()}")
            if result.returncode == 0:
                success(f"{ip} is reachable")
            else:
                warn(f"{ip} is unreachable")
        except Exception as exc:
            warn(f"Ping failed with encoding fallback: {exc}")
    pause()


def port_scanner(ip, ports=(80, 443, 22, 21, 25, 8080, 3389)):
    if not is_valid_ip(ip):
        warn(f"Invalid IP address: {ip}")
        pause()
        return
    info(f"Scanning ports on {ip}...")
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0)
            result = sock.connect_ex((ip, port))
            if result == 0:
                success(f"Port {port} is OPEN")
                open_ports.append(port)
            else:
                warn(f"Port {port} is CLOSED")
            sock.close()
        except socket.error as exc:
            warn(f"Port {port} scan failed: {exc}")
    if not open_ports:
        warn(f"No open ports found on {ip}")
    pause()


def ip_generator():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    success(f"Generated IP: {ip}")
    pause()


def main():
    print(f'''
{Fore.GREEN}
      ██ ██▓███      ▄▄▄█████▓ ▒█████   ▒█████    ██▓   
    ▒▓██▓██░  ██     ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒ ▓██▒   
    ░▒██▓██░ ██▓▒    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒ ▒██░   
     ░██▒██▄█▓▒ ▒    ░ ▓██▓ ░ ▒██   ██░▒██   ██░ ▒██░   
     ░██▒██▒ ░  ░      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░▒░██████
     ░▓ ▒▓▒░ ░  ░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░░ ▒░▓  
      ▒ ░▒ ░             ░      ░ ▒ ▒░   ░ ▒ ▒░ ░░ ░ ▒  
      ▒ ░░             ░ ░    ░ ░ ░ ▒  ░ ░ ░ ▒     ░ ░  
      ░                           ░ ░      ░ ░  ░    ░  

''')
    options = [
        ("01", "IP Info"),
        ("02", "IP Pinger"),
        ("03", "Port Scanner"),
        ("04", "IP Generator"),
        ("05", "Exit"),
    ]
    for num, name in options:
        print(f"    {Fore.GREEN}[{Fore.WHITE}{num}{Fore.GREEN}] {Fore.WHITE}{name}")

    choice = input(f"\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Choose an option: {Style.RESET_ALL}").strip()
    if choice in ("1", "01"):
        ip = input(f"    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Enter IP: {Style.RESET_ALL}").strip()
        get_ip_info(ip)
    elif choice in ("2", "02"):
        ip = input(f"    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Enter IP to ping: {Style.RESET_ALL}").strip()
        ip_pinger(ip)
    elif choice in ("3", "03"):
        ip = input(f"    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Enter IP to scan ports: {Style.RESET_ALL}").strip()
        port_scanner(ip)
    elif choice in ("4", "04"):
        ip_generator()
    elif choice in ("5", "05"):
        info("Returning to Shrek menu...")
    else:
        warn("Invalid choice!")
        pause()


def run():
    root_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    from utilities.core.shrek_ui import set_console_title

    set_console_title("IP Tool | Shrek Multi Tools")
    main()


if __name__ == "__main__":
    run()