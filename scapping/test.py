from itertools import count
from bs4 import BeautifulSoup
import requests

vgm_url = 'https://thierryorru.com'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
  
if soup.find('footer'):
    if str('Fièrement réalisé avec Wordpress') in str(soup.find('footer').text):
        print('oui')
    else:
        print('non')
else:
    print('pas de footer')