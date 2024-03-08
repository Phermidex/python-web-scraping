from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import datetime
#import random

#print(random.seed(datetime.datetime.now()))

class content:

    def __init__(self, url):
        self.url = url

    def getHtml(self):
        try:
            html = urlopen(self.url)
        except HTTPError as e:
            return False
        try:
            soup = BeautifulSoup(html.read(), "html.parser")
        except AttributeError as e:
            return False
        
        return "title:{0}\n\ncontent: {1}\
                ".format(soup.title.string, soup.body.get_text())