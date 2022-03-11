from bs4 import BeautifulSoup
import requests, csv
from tkinter import filedialog
from tkinter import *

window = Tk()
window.geometry("100x100")
filename = filedialog.askopenfilename(initialdir="/",
                                      title = "",
                                      filetypes=())

filename = filename.replace('/', '\\')

openedfile = open(filename, encoding='utf-8')
file = csv.reader(openedfile)

urlok = []
urlko = []
for url in file:
    # 20x & 30x donc 200 <= x > 400
    httpsurl = "https://" + url[0]
    resp = requests.get(httpsurl.replace('\u200b', '')).text
    soup = BeautifulSoup(resp, 'html.parser')
    
    if resp: 
        if 'Wordpress' in soup.find('body').text or 'Lorem ipsum' in soup.find('body').text or 'Prestashop' in soup.find('body').text or 'Mug The best is yet to come' in soup.find('body').text:
            urlko.append(resp.status_code)
        else: urlok.append(resp.status_code)
        
    else: print(resp.status_code)