
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def getLinks(query):
    results = []
    for j in search(query, tld="co.in", num=5, stop=3, pause=5):
        print(j)
        results.append(j)
    return results

import requests
from bs4 import BeautifulSoup

links = getLinks("Explain GSM architecture mcc bsc msc ques10")
for link in links:
    URL = link
    result = requests.get(URL)

    soup = BeautifulSoup(result.content, 'html5lib')
    div = soup.find("span", itemprop="text")

    print(answer)
    #print(soup.prettify())
