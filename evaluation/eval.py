from googlesearch import search
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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


def checkSimilairty(userAnswer,modelAnswer):
    X =userAnswer
    Y =modelAnswer


    # tokenization
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    sw = stopwords.words('english')
    l1 =[];l2 =[]

    # remove stop words from string
    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    return round(cosine*100,2)
