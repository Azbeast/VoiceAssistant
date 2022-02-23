import requests
from bs4 import BeautifulSoup as soup
import re
import webbrowser

movies = {}
links = {}

def Search(input):
    movies.clear()
    name = input
    req = requests.get("https://yts.mx/browse-movies/" + name)
    s = soup(req.text, 'lxml')
    titles = s.select('.browse-movie-title')
    links = s.select('.browse-movie-link')

    if(len(titles) == 0):
        print("Name of movie is not correct, or movie is not available on YTS")
        return
    else:
        for i in range(len(titles)):
            print(str(i) + ". " + links[i].figure.img["alt"])
            movies[i] = titles[i]['href']


def Links(input):
    input = int(input)
    links.clear()
    id = movies[input]
    req = requests.get(id)
    s = soup(req.text, 'lxml')
    print(s)
    m = s.find_all("p", {"class":"hidden-md hidden-lg"})

    movie_links = re.compile('(https://yts.mx/torrent/download/[^"]+)')
    title = re.compile('(\"Download [^\"]*\")')
    titles = title.findall(str(m[0]))
    linkovi = movie_links.findall(str(m[0]))

    i = 0
    for link in linkovi:
        print(str(i)+ ". "+str(titles[i]))
        print("----- "+str(link))
        links[i] = link
        i += 1

def Download(input):
    input = int(input)
    webbrowser.open(links[input])

"""

text = input()
Search(text)
id = int(input())
Links(id)
link = int(input())
Download(link)
    """