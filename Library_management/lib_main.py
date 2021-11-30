

class Library:      #* Defining the library class
    
    def __init__(self, list, name):     #* Initializing the variables for the class
        
        self.booksList = list
        self.name = name
        self.lendDict = {}
        
    
    def displaybooks(self):     #* Display the list of books in the library
    
        print("\nFolllowing books are there in the", self.name, "Library")
    
        for book in self.booksList:     
    
            if book not in self.lendDict.keys():    #* If book has not been lent
                print(book)
    
            elif book in self.lendDict.keys():      #* If book has been lent by somenone
                print(book,"- already taken by",self.lendDict.get(book))

    
    def lendBook(self, user, book):         #* Lend book to the user
        
        if book in self.booksList:      #* Check if book is there in the library
        
            if book not in self.lendDict.keys():   #* Check if book has not already been lent
                self.lendDict.update({book:user})
                print("\nBook dictionary has been upadated")
        
            else:       #* If book already lent
                print("\nBook already taken by ", self.lendDict[book])
        
        else:       #* If book isnt in the library
            print("\nBook not in Library")
    
    
    def addBook(self, book):        #* Add books to library
        
        self.booksList.append(book)     #* Append books to booksList
        print('\nBook has been added to library!')

    def returnBook(self, book):     #* Return book to library
        self.lendDict.pop(book)
        print(book, "returned")


def main():
    jai = Library(["Python", "C++", "Java", "DS", "Ruby"], "Jai")   #*Books in library, name of library
    
    while True:

        print("\nWelcome to ", jai.name, "library.")
        print("1. Display")
        print("2. Lend")
        print("3. Add")
        print("4. Return\n")
        
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:    
            jai.displaybooks()

        elif user_choice == 2:
            name = input("\nEnter your name: ")
            book = input("Enter the name of the book you want to lend: ")
            jai.lendBook(name, book)

        elif user_choice == 3:
            book = input("\nEnter the name of the book you want to add: ")
            jai.addBook(book)

        elif user_choice == 4:
            book = input("\nEnter the name of the book you want to return: ")
            jai.returnBook(book)
        
        else:
            print("\nNot Valid option")
            continue
        
        print("\nPress q to quit and c to continue\n")
        
        user_ch = input().lower()
        
        if user_ch == 'q':
            exit()
        
        if user_ch=='c':
            continue