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
writedfile = open('urls.csv', 'w')
finalfile = csv.writer(writedfile)

for url in file:
    
    try :
        httpsurl = "https://" + url[0]
        resp = requests.get(httpsurl.replace('\u200b', ''), allow_redirects=True).text
        httpcode = requests.get(httpsurl.replace('\u200b', ''), allow_redirects=True)
        soup = BeautifulSoup(resp, 'html.parser')
        if resp:
            if httpcode.status_code >= 200 or httpcode.status_code < 400:
                if 'Wordpress' in soup.find('body').text or 'Lorem ipsum' in soup.find('body').text or 'Prestashop' in soup.find('body').text or 'Mug The best is yet to come' in soup.find('body').text:
                    finalfile.writerow({'url KO' : httpsurl})
                else: finalfile.writerow({'url OK' : httpsurl})
            else: finalfile.writerow({'url KO' : httpsurl})
            
    except :
        httpsurl = "https://www." + url[0]
        resp = requests.get(httpsurl.replace('\u200b', ''), allow_redirects=True).text
        httpcode = requests.get(httpsurl.replace('\u200b', ''), allow_redirects=True)
        soup = BeautifulSoup(resp, 'html.parser')
        if resp:
            if httpcode.status_code >= 200 or httpcode.status_code < 400:
                if 'Wordpress' in soup.find('body').text or 'Lorem ipsum' in soup.find('body').text or 'Prestashop' in soup.find('body').text or 'Mug The best is yet to come' in soup.find('body').text:
                    finalfile.writerow({'url KO' : httpsurl})
                else: finalfile.writerow({'url OK' : httpsurl})
            else: finalfile.writerow({'url KO' : httpsurl})