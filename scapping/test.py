from os import path
from bs4 import BeautifulSoup
import urllib3, csv
from tkinter import filedialog
from tkinter import *
import urllib3

# window = Tk()
# window.geometry("100x100")
# filename = filedialog.askopenfilename(initialdir="/",
#                                       title = "",
#                                       filetypes=())

# filename = filename.replace('/', '\\')

# openedfile = open(filename, encoding='utf-8')
# file = csv.reader(openedfile)
# urls = []
# for url in file:
    # httpsurl = "https://" + url[0]
#     # htmltext = requests.get(httpsurl).text
#     # soup = BeautifulSoup(htmltext, 'html.parser')
    # uri = 'https://' + str(url[0])
    # if '.fr' in uri or '.com' in uri:
    # print(url[0])
# for i in range(len(urls)):
    # http = urllib3.PoolManager()
    # r = http.request('GET', uri)
    # soup = BeautifulSoup(r, 'html.parser')
    # print(soup)
    
# print(len(urls)//5)