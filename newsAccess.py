import requests
from bs4 import BeautifulSoup

def spider():
    news = []
    url = "https://news.google.com/search?q=COVID%2019&hl=en-CA&gl=CA&ceid=CA%3Aen"
    source = requests.get(url)
    text = source.text
    soup = BeautifulSoup(text, "lxml")
    for link in soup.select("div > article > h3 > a"):
        href = "https://news.google.com" + link.get("href")[1:]
        title = link.string
        t = {}
        t["title"] = title
        t["link"] = href
        news.append(t)
    
    return(news)