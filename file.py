
class manager:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write(self, content):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def append(self, content):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(content)
    
    def delete(self):
        with open(self.filename, 'w') as f:
            f.write('')