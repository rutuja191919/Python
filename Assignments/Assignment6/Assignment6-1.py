class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print("Name : ",self.Name,"Author : ",self.Author," NoOfBooks : ",BookStore.NoOfBooks, end = "\n")

def main():
    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming", "Dennis Richie")
    Obj2.Display()

if __name__ == "__main__":
    main()