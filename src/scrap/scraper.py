# scraper.py

import mechanicalsoup
from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "https://ro.wikipedia.org/wiki/"

search = input()

try:
    page = urlopen(base_url + search)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    paras = soup.find_all('p', class_ = "")

    text_to_save = ""
    for p in paras[:3]:
        text = p.text.strip(" \r\n\t")
        if text == "":
             continue   
        text_to_save += text + '\n'
    print(text_to_save)
except Exception as e:
    print("pagina inexistenta")
    print(str(e))