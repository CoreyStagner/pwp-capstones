class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        old = self.email
        self.email = address
        print("Your email has been changed from {} to {}".format(old, self.email))

    def __repr__(self):
        return "Welcome:\n\tUser {}\n\tEmail: {}\n\tBooks Read:{}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        self.books[book] = rating
        print(self.books)

    def get_average_rating(self):
        total = 0
        count = 0
        for el in self.books.values():
            total += 1
            if type(el) != int:
                count += 0
            else:
                count += el
        avg = float(1.0 * count / total)
        return avg
        

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new):
        old = self.isbn
        self.isbn = new
        print("Your email has been changed from {o} to {n}".format(o = old, n = new))
    
    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    
    def __repr__(self):
        return "This book is {}, and the ISBN number is: {}".format(self.title, self.isbn)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        total = 0
        count = 0
        print(len(self.ratings))
        if len(self.ratings) > 0:
            for el in self.ratings:
                total += 1
                count += el
                print(count)
            avg = 1.0 * float(count/total)
            return avg
        else:
            return "oops no ratings"

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, isbn, author):
        super(Fiction, self).__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super(Non_Fiction, self).__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, isbn, author)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, isbn, subject, level)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {e}").format(e=email)

    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        win_book = ""
        win_count = 0
        for book in self.books.keys():
            if self.books[book].get() > win_count:
                win_book = self.books[book]
                win_count = self.books[book].get()
        print("The most read book was {b} and has been read {c} times").format(b = win_book, c = win_count)

    def highest_rated_book(self):
        win_book = ""
        win_rating = 0
        for book in self.books.keys():
            if book.get_average_rating > win_rating:
                win_book = book.title
                win_rating = book.get_average_rating
        print("The highest rated book was {b} and has was rated a {r} out of four").format(b = win_book, r = win_rating)

    def most_positive_user(self):
        win_avg = 0
        win_user = ""
        for user in self.users.values():
            if user.get_average_rating() > win_avg:
                win_avg = user.get_average_rating()
                win_user = user.name

        print("The most positive reviewer was {n} and has an average rating {r} out of four").format(n = win_user, r = win_avg)
        











# # Users
# stephen = User("Stephen Hawking", "hawking@universe.edu")

# # Books
# alice_in_wonderland = Fiction("Alice In Wonderland", 1234, "Lewis Carroll")
# society_of_mind = Non_Fiction("Society of Mind", 7538, "Artificial Intelligence", "beginner")
# bible = Non_Fiction("Holy Bible", 1, "Life", "beginner")
# # print(stephen)
# # print(alice_in_wonderland)
# # print(society_of_mind)
# bible.add_rating(4)
# bible.add_rating(3)
# stephen.read_book(alice_in_wonderland, 2)
# stephen.read_book(society_of_mind, 3)
# # stephen.read_book(bible)
# # print(stephen.get_average_rating())

# print(bible.get_average_rating())