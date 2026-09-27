# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].
# Copyright © Shrek Multi Tools

import random
import datetime
from colorama import Fore, Style, init
init(autoreset=True)

def success(text):
    print(f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def info(text):
    print(f'{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] {Fore.WHITE}{text}{Style.RESET_ALL}')
def warn(text):
    print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.WHITE}{text}{Style.RESET_ALL}')
from keyauth import api
import sys
import time
import platform
import os
import hashlib
from time import sleep
city_zip_codes = {
    'France': {
        'Paris': [
            '75001',
            '75002',
            '75003',
            '75004',
            '75005',
            '75006',
            '75007',
            '75008',
            '75009',
            '75010',
            '75011',
            '75012',
            '75013',
            '75014',
            '75015',
            '75016',
            '75017',
            '75018',
            '75019',
            '75020',
            '75116'],
        'Marseille': [
            '13001',
            '13002',
            '13003',
            '13004',
            '13005',
            '13006',
            '13007',
            '13008',
            '13009',
            '13010',
            '13011',
            '13012',
            '13013',
            '13014',
            '13015',
            '13016'],
        'Lyon': [
            '69001',
            '69002',
            '69003',
            '69004',
            '69005',
            '69006',
            '69007',
            '69008',
            '69009'] },
    'USA': {
        'New York': [
            '10001',
            '10002',
            '10003',
            '10004',
            '10005',
            '10006',
            '10007',
            '10008',
            '10009',
            '10010',
            '10011',
            '10012',
            '10013',
            '10014',
            '10015',
            '10016',
            '10017',
            '10018',
            '10019',
            '10020'],
        'Los Angeles': [
            '90001',
            '90002',
            '90003',
            '90004',
            '90005',
            '90006',
            '90007',
            '90008',
            '90009',
            '90010',
            '90011',
            '90012',
            '90013',
            '90014',
            '90015',
            '90016',
            '90017',
            '90018',
            '90019',
            '90020'],
        'Chicago': [
            '60601',
            '60602',
            '60603',
            '60604',
            '60605',
            '60606',
            '60607',
            '60608',
            '60609',
            '60610',
            '60611',
            '60612',
            '60613',
            '60614',
            '60615',
            '60616',
            '60617',
            '60618',
            '60619',
            '60620'] },
    'Germany': {
        'Berlin': [
            '10115',
            '10117',
            '10119',
            '10178',
            '10179',
            '10243',
            '10245',
            '10247',
            '10249',
            '10315',
            '10317',
            '10318',
            '10319',
            '10365',
            '10367',
            '10369',
            '10405',
            '10407',
            '10409',
            '10435'],
        'Munich': [
            '80331',
            '80333',
            '80335',
            '80336',
            '80337',
            '80339',
            '80469',
            '80471',
            '80473',
            '80475',
            '80479',
            '80538',
            '80539',
            '80634',
            '80636',
            '80637',
            '80639',
            '80796',
            '80797',
            '80798'],
        'Hamburg': [
            '20095',
            '20097',
            '20099',
            '20144',
            '20146',
            '20148',
            '20149',
            '20251',
            '20253',
            '20255',
            '20257',
            '20259',
            '20354',
            '20355',
            '20357',
            '20359',
            '20457',
            '20459',
            '20535',
            '20537'] },
    'Belgium': {
        'Brussels': [
            '1000',
            '1020',
            '1030',
            '1040',
            '1050',
            '1060',
            '1070',
            '1080',
            '1081',
            '1082',
            '1083',
            '1084',
            '1085',
            '1086',
            '1087',
            '1088',
            '1089',
            '1090',
            '1099',
            '1100'],
        'Antwerp': [
            '2000',
            '2018',
            '2020',
            '2030',
            '2040',
            '2050',
            '2060',
            '2070',
            '2080',
            '2090',
            '2100',
            '2110',
            '2120',
            '2130',
            '2140',
            '2150',
            '2160',
            '2170',
            '2180',
            '2190'],
        'Ghent': [
            '9000',
            '9001',
            '9002',
            '9003',
            '9004',
            '9005',
            '9006',
            '9007',
            '9008',
            '9009',
            '9010',
            '9011',
            '9012',
            '9013',
            '9014',
            '9015',
            '9016',
            '9017',
            '9018',
            '9019'] },
    'Norway': {
        'Oslo': [
            '0001',
            '0002',
            '0003',
            '0004',
            '0005',
            '0006',
            '0007',
            '0008',
            '0009',
            '0010',
            '0011',
            '0012',
            '0013',
            '0014',
            '0015',
            '0016',
            '0017',
            '0018',
            '0019',
            '0020'],
        'Bergen': [
            '5000',
            '5001',
            '5002',
            '5003',
            '5004',
            '5005',
            '5006',
            '5007',
            '5008',
            '5009',
            '5010',
            '5011',
            '5012',
            '5013',
            '5014',
            '5015',
            '5016',
            '5017',
            '5018',
            '5019'],
        'Stavanger': [
            '4000',
            '4001',
            '4002',
            '4003',
            '4004',
            '4005',
            '4006',
            '4007',
            '4008',
            '4009',
            '4010',
            '4011',
            '4012',
            '4013',
            '4014',
            '4015',
            '4016',
            '4017',
            '4018',
            '4019'] } }
city_streets = {
    'France': {
        'Paris': [
            'Rue de la Paix',
            'Avenue des Champs-Élysées',
            'Boulevard Saint-Germain'],
        'Marseille': [
            'Rue Saint-Ferréol',
            'Cours Julien',
            'Rue de la République'],
        'Lyon': [
            'Rue de la République',
            'Rue Mercière',
            'Cours Vitton'] },
    'USA': {
        'New York': [
            'Broadway',
            'Wall Street',
            'Fifth Avenue'],
        'Los Angeles': [
            'Sunset Boulevard',
            'Hollywood Boulevard',
            'Rodeo Drive'],
        'Chicago': [
            'Michigan Avenue',
            'State Street',
            'Lake Shore Drive'] },
    'Germany': {
        'Berlin': [
            'Unter den Linden',
            'Friedrichstrasse',
            'Kurfürstendamm'],
        'Munich': [
            'Maximilianstrasse',
            'Leopoldstrasse',
            'Sendlinger Strasse'],
        'Hamburg': [
            'Reeperbahn',
            'Mönckebergstrasse',
            'Spitalerstrasse'] },
    'Belgium': {
        'Brussels': [
            'Rue Neuve',
            'Avenue Louise',
            'Boulevard Anspach'],
        'Antwerp': [
            'Meir',
            'Handelsstraat',
            'Pelgrimstraat'],
        'Ghent': [
            'Veldstraat',
            'Korenmarkt',
            'Sint-Baafsplein'] },
    'Norway': {
        'Oslo': [
            'Karl Johans gate',
            'Bogstadveien',
            'Grünerløkka'],
        'Bergen': [
            'Bryggen',
            'Torgallmenningen',
            'Strømgaten'],
        'Stavanger': [
            'Øvre Holmegate',
            'Vågen',
            'Løkkeveien'] } }
city_coordinates = {
    'Paris': (48.8566, 2.3522),
    'Marseille': (43.2965, 5.3698),
    'Lyon': (45.764, 4.8357),
    'New York': (40.7128, -74.006),
    'Los Angeles': (34.0522, -118.244),
    'Chicago': (41.8781, -87.6298),
    'Berlin': (52.52, 13.405),
    'Munich': (48.1351, 11.582),
    'Hamburg': (53.5511, 9.9937),
    'Brussels': (50.8503, 4.3517),
    'Antwerp': (51.2194, 4.4025),
    'Ghent': (51.0543, 3.7174),
    'Oslo': (59.9139, 10.7522),
    'Bergen': (60.3913, 5.3221),
    'Stavanger': (58.97, 5.73311) }
def generate_street_number():
    # ***<module>.generate_street_number: Failure: Different bytecode
    return random.randint(1, 99)
def generate_first_name(gender):
    # ***<module>.generate_first_name: Failure: Different bytecode
    male_names = ['John', 'Michael', 'Robert', 'David', 'William']
    female_names = ['Alice', 'Diana', 'Eva', 'Grace', 'Ivy']
    return random.choice(male_names if gender == 'male' else female_names)
def generate_last_name():
    # ***<module>.generate_last_name: Failure: Different bytecode
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    return random.choice(last_names)
def generate_birthday():
    # ***<module>.generate_birthday: Failure: Different bytecode
    start, end = (datetime.date(1950, 1, 1), datetime.date(2005, 12, 31))
    delta_days = (end - start).days
    return start + datetime.timedelta(days=random.randrange(delta_days))
def generate_ssn():
    # ***<module>.generate_ssn: Failure: Different bytecode
    return f'{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}'
def generate_credit_card():
    # ***<module>.generate_credit_card: Failure: Different bytecode
    brands = ['Visa', 'MasterCard', 'American Express', 'Discover', 'Voyager']
    brand = random.choice(brands)
    number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
    expire_month = random.randint(1, 12)
    expire_year = random.randint(datetime.datetime.now().year, datetime.datetime.now().year + 5)
    cvv = random.randint(100, 999)
    return {'brand': brand, 'number': number, 'expire': f'{expire_year}/{expire_month}', 'cvv': cvv}
def generate_phone_number(country='France'):
    # ***<module>.generate_phone_number: Failure: Different control flow
    return f'0{random.randint(1, 9)}{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}'
def generate_address(country):
    # ***<module>.generate_address: Failure: Different bytecode
    city = random.choice(list(city_zip_codes[country].keys()))
    street_name, zip_code = (random.choice(city_zip_codes[country][city]), random.choice(city_streets[country][city]))
    street_number = generate_street_number()
    phone = generate_phone_number(country)
    state = ''
    if country == 'USA':
        states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
        state = random.choice(states)
    lat, lng = city_coordinates.get(city, (0.0, 0.0))
    region = state if country == 'USA' else 'N/A' if country in ['France', 'Germany', 'Belgium', 'Norway'] else state
    return {'Street': f'{street_number} {street_name}', 'City/Town': city, 'State/Province/Region': region, 'Zip/Postal Code': zip_code, 'Phone Number': phone, 'Country': country, 'Latitude': lat, 'Longitude': lng}
def generate_random_profile(country='France'):
    gender = random.choice(['male', 'female'])
    first_name = generate_first_name(gender)
    last_name = generate_last_name()
    birthday = generate_birthday()
    ssn = generate_ssn()
    credit_card = generate_credit_card()
    address = generate_address(country)
    return {
        'Full Name': f'{first_name} {last_name}',
        'Gender': gender,
        'Birthday': birthday.strftime('%Y-%m-%d'),
        'Social Security Number': ssn,
        'Credit card brand': credit_card['brand'],
        'Credit card number': credit_card['number'],
        'Expire': credit_card['expire'],
        'CVV': credit_card['cvv'],
        **address,
    }


def main():
    root_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    from utilities.core.shrek_ui import shrek_input, pause

    print(f'''
{Fore.GREEN}
       █████ ▄▄▄      ▀██ ▄█▀▓█████     ▄▄▄      ▓█████▄  ▓█████▄  ██▀███  ▓█████  ██████   ██████ 
     ▓██    ▒████▄     ██▄█▒ ▓█   ▀    ▒████▄    ▒██▀ ██▌ ▒██▀ ██▌▓██ ▒ ██▒▓█   ▀▒██    ▒ ▒██    ▒ 
     ▒████  ▒██  ▀█▄  ▓███▄░ ▒███      ▒██  ▀█▄  ░██   █▌ ░██   █▌▓██ ░▄█ ▒▒███  ░ ▓██▄   ░ ▓██▄   
     ░▓█▒   ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄    ░██▄▄▄▄██▒░▓█▄   ▌▒░▓█▄   ▌▒██▀▀█▄  ▒▓█  ▄  ▒   ██▒  ▒   ██▒
    ▒░▒█░    ▓█   ▓██ ▒██▒ █▄░▒████     ▓█   ▓██░░▒████▓ ░░▒████▓ ░██▓ ▒██▒░▒████▒██████▒▒▒██████▒▒
    ░ ▒ ░    ▒▒   ▓▒█ ▒ ▒▒ ▓▒░░ ▒░      ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒▒▓  ▒ ░ ▒▓ ░▒▓░░░ ▒░ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
    ░ ░       ░   ▒▒  ░ ░▒ ▒░ ░ ░        ░   ▒▒   ░ ▒  ▒   ░ ▒  ▒   ░▒ ░ ▒░ ░ ░  ░ ░▒  ░  ░ ░▒  ░  
      ░ ░     ░   ▒   ░ ░░ ░    ░        ░   ▒    ░ ░  ░   ░ ░  ░    ░   ░    ░  ░  ░  ░  ░  ░  ░  
    ░             ░   ░  ░      ░            ░      ░        ░       ░        ░        ░        ░  
{Fore.RESET}
    ''')
    choice = shrek_input('Country (France, USA, Germany, Belgium, Norway)')
    if choice not in ['France', 'USA', 'Germany', 'Belgium', 'Norway']:
        warn('Invalid choice. Defaulting to France.')
        country = 'France'
    else:
        country = choice
    profile = generate_random_profile(country)
    print()
    success(f'Profile generated — {country}')
    print()
    for key, value in profile.items():
        info(f'{key}: {value}')
    pause()


def run():
    main()
if __name__ == '__main__':
    def clear_screen():
        # ***<module>.clear_screen: Failure: Missing bytecode
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
    clear_screen()
    main()
    input()