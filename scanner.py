import os
import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--url', type=str, required=True, help='Url to iterate')
parser.add_argument('--start', type=int, required=True, help='Page to start on')
parser.add_argument('--end', type=int, required=True, help='Page to end with')

args = parser.parse_args()

links = []

page = args.start

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

    page += 1
