# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

global _AVAILABLE_VOICE_SHORTNAMES
import os
import sys
import hashlib
import asyncio
import time
from pathlib import Path
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def success(text):
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def info(text):
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')

def warn(text):
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')

try:
    import edge_tts
except ImportError:
    warn('edge-tts non installé. Installe avec: pip install edge-tts')
    exit(1)

root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from utilities.core.shrek_ui import set_console_title

OUTPUT_DIR = Path(os.path.join(root_path, 'output'))
OUTPUT_DIR.mkdir(exist_ok=True)
VOIX_FEMMES = {'fr_eloise': 'fr-FR-EloiseNeural', 'fr_denise': 'fr-FR-DeniseNeural', 'fr_claire': 'fr-CA-SylvieNeural', 'fr_sexy': 'fr-FR-DeniseNeural'}
_AVAILABLE_VOICE_SHORTNAMES = None

async def _get_available_voice_shortnames():
    global _AVAILABLE_VOICE_SHORTNAMES
    if _AVAILABLE_VOICE_SHORTNAMES is not None:
        return _AVAILABLE_VOICE_SHORTNAMES
    else:
        try:
            voices = await edge_tts.list_voices()
            _AVAILABLE_VOICE_SHORTNAMES = {v.get('ShortName') for v in voices if v.get('ShortName')}
        except Exception:
            _AVAILABLE_VOICE_SHORTNAMES = set()
        return _AVAILABLE_VOICE_SHORTNAMES

def play_audio(filepath):
    """Joue un fichier audio avec le lecteur par défaut Windows"""
    try:
        os.startfile(filepath)
    except Exception as e:
        warn(f'Impossible de jouer : {e}')

async def generate_femme_voice(text, voix='fr_eloise'):
    """Génère une voix de femme naturelle et crédible avec meilleure qualité"""
    try:
        info(f'Synthesizing female voice: "{text}"')
        voice = VOIX_FEMMES.get(voix, VOIX_FEMMES['fr_eloise'])
        available = await _get_available_voice_shortnames()
        if available and voice not in available:
            warn(f"Voice '{voice}' not available. Falling back to fr-FR-EloiseNeural.")
            voice = 'fr-FR-EloiseNeural'
        filename = OUTPUT_DIR / f'femme_troll_{int(time.time())}.mp3'
        if voix == 'fr_sexy':
            rate = '-15%'
            pitch = '-2Hz'
            info('Voix adulte sensuelle activée...')
        elif voix == 'fr_denise':
            rate = '-5%'
            pitch = '+2Hz'
        else:
            rate = '-10%'
            pitch = '+8Hz'
        communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)
        await communicate.save(str(filename))
        success(f'File generated: {filename}')
        info('Playing...')
        play_audio(str(filename))
    except Exception as e:
        msg = str(e)
        if 'No audio was received' in msg and voice != 'fr-FR-EloiseNeural':
            warn('No audio received, retry with fr-FR-EloiseNeural...')
            try:
                fallback = edge_tts.Communicate(text=text, voice='fr-FR-EloiseNeural', rate='-5%', pitch='+2Hz')
                await fallback.save(str(filename))
                success(f'File generated: {filename}')
                info('Playing...')
                play_audio(str(filename))
            except Exception as e2:
                warn(f'Error: {e2}')
                return None
        else:
            warn(f'Error: {e}')
            return None

def main():
    print(f'''
{Fore.GREEN}
       █████ ▄▄▄      ▀██ ▄█▀▓█████     ██▒   █▓ ▒█████    ██ ▄████▄ ▓█████
     ▓██    ▒████▄     ██▄█▒ ▓█   ▀    ▓██░   █▒▒██▒  ██▒▒▓██▒██▀ ▀█ ▓█   ▀
     ▒████  ▒██  ▀█▄  ▓███▄░ ▒███       ▓██  █▒░▒██░  ██▒░▒██▒▓█    ▄▒███  
     ░▓█▒   ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄      ▒██ █░░▒██   ██░ ░██▒▓▓▄ ▄██▒▓█  ▄
    ▒░▒█░    ▓█   ▓██ ▒██▒ █▄░▒████       ▒▀█░  ░ ████▓▒░ ░██▒ ▓███▀ ░▒████
    ░ ▒ ░    ▒▒   ▓▒█ ▒ ▒▒ ▓▒░░ ▒░        ░ ▐░  ░ ▒░▒░▒░  ░▓ ░ ░▒ ▒  ░░ ▒░ 
    ░ ░       ░   ▒▒  ░ ░▒ ▒░ ░ ░         ░ ░░    ░ ▒ ▒░   ▒   ░  ▒   ░ ░  
      ░ ░     ░   ▒   ░ ░░ ░    ░           ░░  ░ ░ ░ ▒    ▒ ░          ░  
    ░             ░   ░  ░      ░            ░      ░ ░    ░ ░ ░        ░  

''')

    print(f'    {Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] {Fore.WHITE}Natural Young Voice (Eloise) - RECOMMENDED')
    print(f'    {Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] {Fore.WHITE}Natural Voice (Denise)')
    print(f'    {Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] {Fore.WHITE}Quebec Voice (Sylvie) - Very Natural')
    print(f'    {Fore.GREEN}[{Fore.WHITE}4{Fore.GREEN}] {Fore.WHITE}SEXY Adult Voice')
    print(f'    {Fore.GREEN}[{Fore.WHITE}0{Fore.GREEN}] {Fore.WHITE}Quit')
    
    voix_choice = input(f'\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Choose voice: ').strip() or '1'
    voix_map = {'1': 'fr_eloise', '2': 'fr_denise', '3': 'fr_claire', '4': 'fr_sexy'}
    voix = voix_map.get(voix_choice, 'fr_eloise')

    if voix_choice == '0':
        return

    text = input(f'\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Fake Voice: {Style.RESET_ALL}').strip()

    if not text:
        warn('Text cannot be empty!')
    else:
        asyncio.run(generate_femme_voice(text, voix))
        retry = input(f'\n    {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} Generate another voice? (y/n) [n] → {Style.RESET_ALL}').lower().strip()
        if retry == 'y':
            main()
        else:
            info('Exiting...')

def run():
    root_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    from utilities.core.shrek_ui import set_console_title
    set_console_title('Fake Voice | Shrek Multi Tools')
    try:
        main()
    except KeyboardInterrupt:
        print()
        info('Stopped')
    except Exception as e:
        warn(f'Error: {e}')

if __name__ == '__main__':
    run()