class Publication:

    def __init__(self,name):
        self.name = name
    
    def print_info(self):
        print(f"Name of print: {self.name}")

class Book(Publication):

    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Print type: Book\nAuthor: {self.author}\nPage count: {self.page_count}\n")

class Magazine(Publication):
    
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
    
    def print_info(self):
        super().print_info()

        print(f"Print type: Magazine\nEditor: {self.editor}\n")

publication = []

# Finnish instuctions has a different page count
publication.append(Book("Compartment No. 6", "Rosa Liksom", 192))
publication.append(Magazine("Donald Duck", "Aki Hyyppä"))

for p in publication:
    p.print_info()