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
writedfile = open('urls.csv', 'w', newline='')
finalfile = csv.writer(writedfile)

for url in file:
    
    try :
        httpsurl = "https://" + url[0]
        # resp = requests.get(httpsurl.replace('\u200b', ''), allow_redirects=True).text
        httpcode = requests.get(httpsurl.replace('\u200b', ''), allow_redirects=True)
        if httpcode.status_code >= 200 or httpcode.status_code < 400:
                finalfile.writerow(['url OK', httpsurl])
        else: finalfile.writerow(['url KO', httpsurl])
            
    except :
        httpsurl = "https://www." + url[0]
        # resp = requests.get(httpsurl.replace('\u200b', ''), allow_redirects=True).text
        httpcode = requests.get(httpsurl.replace('\u200b', ''), allow_redirects=True)
        if httpcode.status_code >= 200 or httpcode.status_code < 400:
                finalfile.writerow(['url OK', httpsurl])
        else: finalfile.writerow(['url KO', httpsurl])