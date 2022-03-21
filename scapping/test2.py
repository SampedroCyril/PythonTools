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
    httpsurl = "https://" + url[0]
    resp = requests.get(httpsurl, allow_redirects=True)
    if resp :
        if resp.status_code >= 200 or resp.status_code < 400:
            
            finalfile.writerow(['url OK ', httpsurl])
        else: finalfile.writerow(['url KO ', httpsurl])
    else:
        httpsurl = "https://www." + url[0]
        resp = requests.get(httpsurl, allow_redirects=True, verify=False)
        if resp.status_code >= 200 or resp.status_code < 400:
                finalfile.writerow(['url OK ', httpsurl])
        else: finalfile.writerow(['url KO ', httpsurl])