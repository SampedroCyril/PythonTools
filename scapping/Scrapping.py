from itertools import count
from bs4 import BeautifulSoup
import requests
import csv
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

# urls = []
# i[0] => url
for url in file:
    
    # vgm_url = url
    # html_text = requests.get(vgm_url).text
    # soup = BeautifulSoup(html_text, 'html.parser')
    print(url[0])
    # if '<p>' in soup:
    #     print()
