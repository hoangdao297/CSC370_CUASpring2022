class phonebook:
    def __init__(self) -> None:
        book={}
        phonebooksize=0
    def add(self,name,number):
        self.book[name]=number
        self.phonebooksize+=1
    def delete(self,name):
        if (name in self.book):
            del(self.book[name])
            self.phonebooksize-=1
            print("Deleted")
        else:
            print("Name does not exist in phone book")
    def lookforcontact(self,name):
        if (name in self.book):
            print("Name: "+name)
            print("Number: "+str(self.book[name]))
        else:
            print("Name does not exist in phone book")
    def returnsize(self):
        return self.phonebooksize
    
        