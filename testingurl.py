#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

unique_links = set()

def get_html_page(link):
    old_index=0
  

    response = requests.get(link,headers=headers)
    page = BeautifulSoup(response.content,"html.parser")
    tds = ""
    navlinks_with_text = [a['href'] for a in page.find_all('a',{"class": "page-link"}, href=True) if a.text]
    old_index = len(unique_links)
    unique_links.update(set(navlinks_with_text))
    
    divs = page.findAll("table", {"class": "table bordered"})
    for div in divs:
        rows = div.findAll('tr')
        for row in rows :
            td = row.findAll('td')
            for item in td:
                tds+=item.text
            tds+= "\n"
    unique_links_list = list(unique_links)
    for index in range(old_index,len(unique_links_list)) :
        link = unique_links_list[index]
        if(len(link)>0):
            tds+= get_html_page(link)
    return tds
 

csv=""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
url = ""
response = requests.get(url,headers=headers)

page = BeautifulSoup(response.content,"html.parser")


links_with_text = [a['href'] for a in page.find_all('a',{"class": "nav-link"}, href=True) if a.text]

data = ""

for link in links_with_text:
    data += get_html_page(link)

text_file = open("Output.csv", "w")
text_file.write(data)
text_file.close()



  