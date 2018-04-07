#!/usr/bin/python
import requests
import sys
try: 
        from BeautifulSoup import BeautifulSoup
except ImportError:
        from bs4 import BeautifulSoup

url = 'http://www.morfix.co.il/'

try:
    r = requests.get(url+sys.argv[1]) 
except IndexError:
    print("No term specified")
    sys.exit(1)

html = r.content
parsed_html = BeautifulSoup(html, "lxml")
try:
    print parsed_html.body.find('div', attrs={'class':'default_trans'}).text
except AttributeError:
    print parsed_html.body.find('div', attrs={'class':'translation translation_he heTrans'}).text
