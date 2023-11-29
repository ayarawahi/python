class library:
    def __init__(self):
        self.library=[]
    def add_book(self,title,author,copies):
        book={"title":title,"author":author,"copies":copies}
        self.library.append(book)
    def display_books(self):
        for i in self.library:
            print(i)
    def search_book(self,title):
        for  i in  self.library:
            if (i["title"]==title):
                print(i["author"])
    
lb1=library()
lb1.add_book("ayhkuha","ali",4)
lb1.add_book("aya","omn",8)
lb1.display_books()
lb1.search_book("aya")