import pytest
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


# --- Book Class Tests ---


def test_book_initialization():
    """1. Initialization: Title, author, and availability set correctly"""
    book = Book("The Hobbit", "J.R.R. Tolkien")
    assert book.title == "The Hobbit"
    assert book.author == "J.R.R. Tolkien"
    assert book.available is True


def test_book_borrow_success():
    """2. Borrow when available: borrow() returns True, sets available to False"""
    book = Book("Clean Code", "Robert Cecil Martin")
    success = book.borrow()
    assert success is True
    assert book.available is False


def test_book_borrow_fail():
    """3. Borrow when not available: borrow() returns False, available remains False"""
    book = Book("1984", "George Orwell")
    book.borrow()  # Make it unavailable first

    success = book.borrow()  # Try to borrow again
    assert success is False
    assert book.available is False


def test_book_return():
    """4. Return book: return_book() sets available to True"""
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book.borrow()  # Make it unavailable first
    assert book.available is False

    book.return_book()
    assert book.available is True
