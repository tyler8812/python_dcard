import requests
from bs4 import BeautifulSoup
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction


temp = []





def bug1(a, b):
    url = "https://www.dcard.tw/f"
    resp = requests.get(url)

    
    soup = BeautifulSoup(resp.text, "html.parser")
    tag_name = 'div.PostList_entry_1rq5Lf a'
    articles = soup.select(tag_name)

    for art in articles:
        if art['href'][1] == 'f':  
            temp = art['href'].split('-', 1)
            a.append(temp[1][0:18])
            b.append(temp[0])

def bug2(a, b):
    url = "https://www.dcard.tw/f"
    resp = requests.get(url)

    
    soup = BeautifulSoup(resp.text, "html.parser")
    tag_name = 'ul.ForumEntryGroup_list_cdSR2f li a'
    articles = soup.select(tag_name)
    count = 0
    for art in articles:
        if count == 0:
            count += 1
        else:
            temp = art['href'].split('/',3)
            a.append(art.text)
            b.append(temp[2])

def bug3(a, b, c):
    url = "https://www.dcard.tw/f"
    url = url + "/" + c
    
    resp = requests.get(url)

    
    soup = BeautifulSoup(resp.text, "html.parser")
    tag_name = 'div.PostList_entry_1rq5Lf a'
    articles = soup.select(tag_name)

    for art in articles:
        if art['href'][1] == 'f':  
            temp = art['href'].split('-', 1)
            a.append(temp[1][0:18])
            b.append(temp[0])


def bug4(a, b):
    url = "https://www.dcard.tw/f?latest=true"
    resp = requests.get(url)

    
    soup = BeautifulSoup(resp.text, "html.parser")
    tag_name = 'div.PostList_entry_1rq5Lf a'
    articles = soup.select(tag_name)

    for art in articles:
        if art['href'][1] == 'f':  
            temp = art['href'].split('-', 1)
            a.append(temp[1][0:18])
            b.append(temp[0])


def bug5(a, b, c):
    url = "https://www.dcard.tw/search/general?query="
    url = url + c
    resp = requests.get(url)

    
    soup = BeautifulSoup(resp.text, "html.parser")
    tag_name = "div.PostWrap__Wrap-sc-1uitxs3-1.keZFtc a"
    articles = soup.select(tag_name)

    for art in articles:
        if art['href'][1] == 'f':  
            temp = art['href'].split('-', 1)
            a.append(temp[1][0:18])
            b.append(temp[0])
            
            


            
            


        






