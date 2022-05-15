import os
import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--url', type=str, required=True, help='Url to iterate')
parser.add_argument('--start', type=int, required=True, help='Page to start on')
parser.add_argument('--end', type=int, required=True, help='Page to end with')
parser.add_argument('--attack', type=str, required=True, help='Select attack type')

args = parser.parse_args()

links = []

page = args.start

if args.attack == 'ftpanon':
    while page <= args.end:
        lk_split = args.url.split('=')
        lk_split[1] = '&category'
        lk_split.insert(1, f'={page}')
        full_lk = ''.join(lk_split)
        soup = BeautifulSoup(requests.get(full_lk).content, 'html.parser')
        for class_find in soup.find_all(class_="sabai-directory-contact-website"):
            for a in class_find.find_all('a'):
                if a['href'] not in links:
                    if "NULL" not in a['href'] and 'https' not in a['href']:
                        links.append(a['href'])
                        print(a['href'])
                        if 'www' in a['href']:
                            link = a['href'].split('www.')[1].strip()
                            if '/' in link:
                                clean_link = link.replace('/', '')
                                os.system(f'sudo nmap -sS -sV --script=ftp-anon {clean_link} -p 21 > results.txt')
                                with open('results.txt', 'r') as f:
                                    lines = f.read()
                                    if 'Anonymous' in lines:
                                        print(lines)
                                os.system('sudo rm results.txt')
                            else:
                                os.system(f'sudo nmap -sS -sV --script=ftp-anon {link} -p 21 > results.txt')
                                with open('results.txt', 'r') as f:
                                    lines = f.read()
                                    if 'Anonymous' in lines:
                                        print(lines)
                                os.system('sudo rm results.txt')
                            pass
                        else:
                            link = a['href'].split('//')[1].strip()
                            if '/' in link:
                                clean_link = link.replace('/', '')
                                os.system(f'sudo nmap -sS -sV --script=ftp-anon {clean_link} -p 21 > results.txt')
                                with open('results.txt', 'r') as f:
                                    lines = f.read()
                                    if 'Anonymous' in lines:
                                        print(lines)
                                os.system('sudo rm results.txt')
                            else:
                                os.system(f'sudo nmap -sS -sV --script=ftp-anon {link} -p 21 > results.txt')
                                with open('results.txt', 'r') as f:
                                    lines = f.read()
                                    if 'Anonymous' in lines:
                                        print(lines)
                                os.system('sudo rm results.txt')
                    else:
                        pass
                else:
                    pass
        page += 1

elif args.attack == 'general':
    while page <= args.end:
        lk_split = args.url.split('=')
        lk_split[1] = '&category'
        lk_split.insert(1, f'={page}')
        full_lk = ''.join(lk_split)
        soup = BeautifulSoup(requests.get(full_lk).content, 'html.parser')
        for class_find in soup.find_all(class_="sabai-directory-contact-website"):
            for a in class_find.find_all('a'):
                if a['href'] not in links:
                    if "NULL" not in a['href'] and 'https' not in a['href']:
                        links.append(a['href'])
                        print(a['href'])
                        if 'www' in a['href']:
                            link = a['href'].split('www.')[1].strip()
                            if '/' in link:
                                clean_link = link.replace('/', '')
                                os.system(f'sudo nmap -sS -F -T4 {clean_link}')
                            else:
                                os.system(f'sudo nmap -sS -F -T4 {link}')
                            pass
                        else:
                            link = a['href'].split('//')[1].strip()
                            if '/' in link:
                                clean_link = link.replace('/', '')
                                os.system(f'sudo nmap -sS -F -T4 {clean_link}')
                            else:
                                os.system(f'sudo nmap -sS -F -T4 {link}')
                    else:
                        pass
                else:
                    pass
        page += 1
