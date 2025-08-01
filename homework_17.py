### Task 1 ###

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("woof woof")

class Cat(Animal):
    def talk(self):
        print("meow")

def make_animal_talk(animal):
    animal.talk()


### Task 2 ###

class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"Author: '{self.name}', country: '{self.country}', birthday: '{self.birthday}'"

class Book:
    total_books = 0

    def __init__(self, name: str, year: int, author: Author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __str__(self):
        return f"Book: '{self.name}', year:{self.year}, author:{self.author})"

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")

        book = Book(name, year, author)
        self.books.append(book)

        if author not in self.authors:
            self.authors.append(author)

        return book

    def group_by_author(self, author: Author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books and {len(self.authors)} authors"


if __name__ == "__main__":

    lib = Library("My Library")

    author1 = Author("Taras Koval", "Ukraine", "1980-01-01")
    author2 = Author("Peter Nord", "USA", "2000-06-06")

    book1 = lib.new_book("Kvitka", 1997, author1)
    book2 = lib.new_book("History", 1997, author2)
    book3 = lib.new_book("Tomorrow", 2025, author1)

    print(lib)
    print(f"Total books created: {Book.total_books}")


### Task 3 ###
import math

class Fraction:

    def __init__(self, up, down):
        if down == 0:
            raise ValueError("Down cannot be zero")
        if not isinstance(up, int) or not isinstance(down, int):
            raise TypeError("Up and Down must be integers")

        negativity = -1 if up * down < 0 else 1
        up, down = abs(up), abs(down)
        gcd = math.gcd(up, down)

        self.up = negativity * (up // gcd)
        self.down = down // gcd

    def __str__(self):
        return f"{self.up}/{self.down}"

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.up == other.up and self.down == other.down

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return self.up * other.down < other.up * self.down

    def __le__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return self.up * other.down <= other.up * self.down

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return self.up * other.down > other.up * self.down

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return self.up * other.down >= other.up * self.down

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return True
        return not self.__eq__(other)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only add Fraction to Fraction")
        new_up = self.up * other.down + other.up * self.down
        new_down = self.down * other.down
        return Fraction(new_up, new_down)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract Fraction from Fraction")
        new_up = self.up * other.down - other.up * self.down
        new_down = self.down * other.down
        return Fraction(new_up, new_down)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply Fraction with Fraction")
        new_up = self.up * other.up
        new_down = self.down * other.down
        return Fraction(new_up, new_down)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide Fraction by Fraction")
        if other.up == 0:
            raise ValueError("Division by zero")
        new_up = self.up * other.down
        new_down = self.down * other.up
        return Fraction(new_up, new_down)

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    assert (x + y) == Fraction(3, 4)
    assert str(x - y) == "1/4"
    assert str(x * y) == "1/8"
    assert str(x / y) == "2/1"
    assert (x < y) == False
    assert (x > y) == True