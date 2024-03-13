from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


class content:

    def __init__(self, url):
        self.url = url

    def getHtml(self):
        try:
            html = urlopen(self.url)
        except HTTPError as e:
            return False
        try:
            soup = BeautifulSoup(html.read(), "html.parser", from_encoding="utf-8")
        except AttributeError as e:
            return False
        
        return "#title:%s\n\n###content: %s" % (soup.title.get_text(), soup.get_text().replace('\n', ' '))