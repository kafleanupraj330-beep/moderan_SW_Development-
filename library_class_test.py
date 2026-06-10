class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if not self.available:
            return False
        self.available = False
        return True

    def return_book(self):
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def is_available(self, title):
        for book in self.books:
            if book.title == title:
                return book.available
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.borrow()
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return True
        return False

# Pytest Test Functions

# --- Library Class Tests ---

def test_library_initialization():
    """1. Library Initialization: books list is empty"""
    lib = Library()
    assert lib.books == []


def test_library_add_book():
    """2. Add book: Adds Book instance to list with correct title, author, and available=True"""
    lib = Library()
    lib.add_book("Foundation", "Isaac Asimov")

    assert len(lib.books) == 1
    assert lib.books[0].title == "Foundation"
    assert lib.books[0].author == "Isaac Asimov"
    assert lib.books[0].available is True


def test_library_is_available_exists():
    """3. Check availability - exists: is_available(title) returns True"""
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    assert lib.is_available("Dune") is True


def test_library_is_available_not_exists():
    """4. Check availability - doesn’t exist: is_available(title) returns False"""
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    assert lib.is_available("The Hobbit") is False


def test_borrow_book_available():
    """5. Borrow book - available: borrow_book(title) returns True and sets available to False"""
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    result = lib.borrow_book("Dune")
    assert result is True
    assert lib.books[0].available is False


def test_borrow_book_already_borrowed():
    """6. Borrow book - already borrowed: borrow_book(title) returns False"""
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    lib.borrow_book("Dune")  # First borrow

    result = lib.borrow_book("Dune")  # Second borrow attempt
    assert result is False


def test_borrow_book_not_in_library():
    """7. Borrow book - not in library: borrow_book(title) returns False"""
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    result = lib.borrow_book("Neuromancer")
    assert result is False


def test_return_book_valid():
    """8. Return book - valid: return_book(title) returns True and sets available to True"""
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    lib.borrow_book("Dune")  # Borrow it first

    result = lib.return_book("Dune")
    assert result is True
    assert lib.books[0].available is True


def test_return_book_not_exists():
    """9. Return book - doesn’t exist: return_book(title) returns False"""
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    result = lib.return_book("The Matrix")
    assert result is False


def test_return_book_already_available():
    """10. Return book - already available: Still returns True, doesn’t break logic"""
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    # "Dune" starts off available

    result = lib.return_book("Dune")
    assert result is True
    assert lib.books[0].available is True