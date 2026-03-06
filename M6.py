# --------------------------
# 1. Book Class (Custom Class 1: Encapsulate book attributes and behaviors)
# --------------------------
class Book:
    def __init__(self, book_id, title, author):
        """
        Book class constructor: Initialize book attributes
        Args:
            book_id (str): Unique book ID (e.g., "B001")
            title (str): Book title
            author (str): Book author
        """
        # Encapsulation: Mark private attributes with single underscore (not for direct external modification)
        self._book_id = book_id
        self.title = title
        self.author = author
        self._is_borrowed = False  # Book borrowing status (private, modified only via methods)

    def borrow_book(self):
        """Borrow a book: Modify private attribute _is_borrowed (demonstrates encapsulation)"""
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False

    def return_book(self):
        """Return a book: Modify private attribute _is_borrowed"""
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False

    def get_status(self):
        """Get book status (encapsulation: provide external access interface for private attribute)"""
        return "Borrowed" if self._is_borrowed else "Available"

    def __str__(self):
        """Special method: Return user-friendly string representation of the book"""
        return f"Book[{self._book_id}]: 《{self.title}》 - {self.author} (Status: {self.get_status()})"

# --------------------------
# 2. LibraryUser Parent Class (Custom Class 2: Base class for library users)
# --------------------------
class LibraryUser:
    def __init__(self, user_id, name):
        """
        Library user constructor: Initialize basic user attributes
        Args:
            user_id (str): Unique user ID (e.g., "U001")
            name (str): User name
        """
        self.user_id = user_id
        self.name = name

    def __str__(self):
        """Special method: Return basic user information"""
        return f"Library User[{self.user_id}]: {self.name}"

# --------------------------
# 3. Patron Subclass (Inherits from LibraryUser, extends borrowing functionality)
# --------------------------
class Patron(LibraryUser):
    def __init__(self, user_id, name):
        """
        Patron subclass constructor: Inherit parent class attributes, add borrowed books list
        Args:
            user_id (str): User ID
            name (str): User name
        """
        # Call parent class constructor (core of inheritance)
        super().__init__(user_id, name)
        self.borrowed_books = []  # Subclass new attribute: list of borrowed books

    def borrow(self, book):
        """
        Subclass extended method: Borrow a book (interact with Book object)
        Args:
            book (Book): Book object to borrow
        """
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"✔ {self.name} successfully borrowed 《{book.title}》")
        else:
            print(f"✘ 《{book.title}》is already borrowed. {self.name} failed to borrow it.")

    def return_book(self, book):
        """
        Subclass extended method: Return a book (interact with Book object)
        Args:
            book (Book): Book object to return
        """
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            print(f"✔ {self.name} successfully returned 《{book.title}》")
        else:
            print(f"✘ {self.name} did not borrow 《{book.title}》. Return failed.")

    def list_borrowed_books(self):
        """Subclass extended method: List all borrowed books"""
        if not self.borrowed_books:
            return f"{self.name} has no borrowed books"
        book_list = "\n  - ".join([f"{b.title} ({b._book_id})" for b in self.borrowed_books])
        return f"{self.name}'s borrowed books:\n  - {book_list}"

    def __str__(self):
        """Special method: Override parent class method to return detailed patron information"""
        base_info = super().__str__()
        return f"{base_info} | Number of borrowed books: {len(self.borrowed_books)}"

# --------------------------
# 4. Main Program: Instantiate objects and demonstrate interaction
# --------------------------
def main():
    print("===== Library Management System =====")
    
    # 1. Create book objects
    book1 = Book("B001", "Python Crash Course", "Eric Matthes")
    book2 = Book("B002", "Data Structures and Algorithm Analysis in Python", "Mark Allen Weiss")
    book3 = Book("B003", "Design Patterns: Elements of Reusable Object-Oriented Software", "Gamma et al.")
    
    # Print book information (call __str__ method)
    print("\n--- Library Collection ---")
    print(book1)
    print(book2)
    print(book3)
    
    # 2. Create patron objects (subclass instances)
    patron1 = Patron("U001", "Wei Zhang")
    patron2 = Patron("U002", "Jinglu Yang")
    
    # Print patron information (call overridden __str__ method)
    print("\n--- Patron Information ---")
    print(patron1)
    print(patron2)
    
    # 3. Demonstrate borrow/return interaction
    print("\n--- Borrow Operations ---")
    patron1.borrow(book1)  # Wei Zhang borrows B001
    patron1.borrow(book2)  # Wei Zhang borrows B002
    patron2.borrow(book1)  # Jinglu Yang tries to borrow B001 (already borrowed)
    
    print("\n--- Status After Borrowing ---")
    print(patron1.list_borrowed_books())
    print(book1)  # Check status of B001
    
    print("\n--- Return Operations ---")
    patron1.return_book(book1)  # Wei Zhang returns B001
    patron1.return_book(book3)  # Wei Zhang tries to return B003 (not borrowed)
    
    print("\n--- Final Status ---")
    print(patron1)
    print(book1)

if __name__ == "__main__":
    main()