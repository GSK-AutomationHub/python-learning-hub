
class Book:

    # CLASS OBJECT ATTRIBUTE
    store = "The Magic Book Store"

    def __init__(self,name,author,pages):
        print(f"The new book got added in '{Book.store}'")
        # USER DEFINED ATTRIBUTES
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        # STRING REPRESENTATION OF THE BOOK OBJECT
        return f"The Book '{self.name}' written by Author '{self.author}'"

    def __len__(self):
        # LENGTH OF THE BOOK OBJECT
        return self.pages

    def __del__(self):
        # DELETE SUCCESS MESSAGE FOR THE BOOK OBJECT
        print("the book object has been deleted")

b = Book('python rocks', 'jose', 300)
print(b)
print(f"the book length is {len(b)}")
del b
