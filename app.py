
import contentHtml
import file

""" App for web scraping """
class App:
    """ url is the url you want to scraping """    
    def __init__(self, url):
        self.url = url
        self.html = ""
    """ returns the content of the url """
    def content_html(self):
        return contentHtml.content(self.url).getHtml()




## run script and enter name, url and press enter: python app.py
customFileName = input("Enter file name: ")
customUrl = input("Enter url: ")

file.manager("%s.txt" % customFileName).write(App(customUrl).content_html())
read_file = file.manager("%s.txt" % customFileName).read()
print("Done! our file are successfully created. Check your file is called '%s.txt' and this is your content\n\n\n%s." % (customFileName, read_file))

