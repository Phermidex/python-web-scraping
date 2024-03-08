
import contentHtml
import file
class App:

    def __init__(self, url):
        self.url = url
        self.html = ""

    def content_html(self):
        return contentHtml.content(self.url).getHtml()




## run script and enter name, url and press enter: python app.py
customFileName = input("Enter file name: ")
customUrl = input("Enter url: ")

file.manager("{0}.txt".format(customFileName)).write(App(customUrl).content_html())

read_file = file.manager("{0}.txt".format(customFileName)).read()

print("Done! our file are successfully created. Check your file is called '{0}.txt' and this is your content\n\n\n{1}.".format(customFileName,read_file))


