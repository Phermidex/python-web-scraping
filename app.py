
from contentHtml import content
from file import manager

""" App for web scraping """
class App:
    """ url is the url you want to scraping """    
    def __init__(self, url):
        self.url = url
        
    """ returns the content of the url """
    def content_html(self):
        return content(self.url).getHtml()




## run script and enter name, url press enter
## commad to run script is: python app.py
customFileName = input("Enter file name: ")
customUrl = input("Enter url: ")

manager("%s.md" % customFileName).write(str(App(customUrl).content_html()))
read_file = manager("%s.md" % customFileName).read()
print("Done! our file are successfully created.\
       Check your file is called '%s.md' and this is your content\n\n\n\
      %s." % (customFileName, read_file))

