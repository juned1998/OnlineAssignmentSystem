from googlesearch import search

def getLinks(query):
    results = []
    for j in search(query, tld="co.in", num=1, stop=1, pause=5):
        print(j)
        results.append(j)
    return results

import requests
from bs4 import BeautifulSoup

def getAnswer(question):
    links = getLinks(question + "ques10")
    for link in links:
        URL = link
        result = requests.get(URL)

        soup = BeautifulSoup(result.content, 'html5lib')
        #div = soup.find_all(['div.content span.clear-fix p', 'div.content span.clear-fix li'])
        div = soup.find_all("span", {"class": "clearfix"})

        for para in div:
            answer = ''.join(para.text)

        return answer    
#     print(answer)
# getAnswer("Explain Microprocessor")
