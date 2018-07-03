#User class with constructor method taking self, name and email
class User(object):
    def __init__(self, name, email):
#name is a string
        self.name = name
#email is a string
        self.email = email
#books is a dict - will map Book object to User's rating
        self.books = {}

#Method to get user's mail - returns user's email
    def get_email(self):
        return self.email

#Method to change email - prints message when email changed
    def change_email(self, address):
        self.email = address
        print("The email for " + self.name + " has been changed to " + self.email)

#Method returns string to print out the user object
    def __repr__(self):
        return("User " + str(self.name) + ", email: " + str(self.email) + ", books read: " + str(len(self.books))) 
		
#Method for comparing users - compares names and emails
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.emai
		
#Method for collecting book ratings - set key to book
    def read_book(self, book, rating=None):
        self.books[book] = rating
		
#Method for calculating average rating - iterates through all book ratings for a particular user
    def get_average_rating(self):
        score = 0
        for value in self.books.values():
            if value:
                score += value
        avg = score / len(self.books)
        return avg
		
#Book class with constructor method taking self, title and isbn - works for all book instances
class Book(object):
    def __init__(self, title, isbn):
#title is a string
        self.title = title
#isbn is a number
        self.isbn = isbn
#ratings is an empty list
        self.ratings = []
		
#Method returning book's title
    def get_title(self):
        return self.title
		
#Method returning book's isbn
    def get_isbn(self):
        return self.isbn
		
#Method changing book's isbn
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN for " + self.title + " has been changed to " + str(self.isbn))
		
#Method to add rating - if rating outside range, then print warning
    def add_rating(self, rating):
#Check if rating is valid 	
        if rating and rating >= 1 and rating <= 4:
            self.ratings.append(rating)
        else:
#Rating outside the expected bounds
            print('Invalid Rating')
			
#Method compares books by checking title and isbn
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn
		
#Method returns (string) title
    def __repr__(self):
        return self.title
		
#Method calculate average rating for a book
    def get_average_rating(self):
        book_score = 0
        for rating in self.ratings:
            book_score += rating
        try:
            avg = book_score / len(self.ratings)  
        except ZeroDivisionError:
            print('ratings list is empty')    
        return avg
		
#Method to make Book hashable per instructions - allows book object t be used as key on user class
    def __hash__(self):
        return hash((self.title, self.isbn))

		
#Class Fiction - inherits from Book
class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author
		
#Method returns (string) 'author'
    def get_author(self):
        return self.author
		
#Method returns string {title} by {author}
    def __repr__(self):
        return self.title + " by " + self.author

		
#Class Non-Fiction - inherits from Book
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level
		
#Method returns subject
    def get_subject(self):
        return self.subject
		
#Method returns level
    def get_level(self):
        return self.level
		
#Method returns string {title} a {level} manual on {subject}
    def __repr__(self):
        return self.title + ', a ' + self.level + ' manual on ' + self.subject

		
#Class TomeRater
class TomeRater:
#Method to map user's email to name and book (that's been read)to user
    def __init__(self):
        self.users = {}
        self.books = {}
		
#Method to create a book
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book
		
#Method to create a new fiction book
    def create_novel(self, title, author, isbn):
        new_book = Fiction(title, author, isbn)
        return new_book
		
#Method to create a new non-fiction book
    def create_non_fiction(self, title, subject, level, isbn):
        new_book = Non_Fiction(title, subject, level, isbn)
        return new_book
		
#Method to link book to user
    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email " + email)
			
#Method to add user
    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
#Iterate over books
            for book in user_books:
                self.add_book_to_user(book, email)
				
#Method to print all keys in self.books
    def print_catalog(self):
        for item in self.books.keys():
            print(item)
			
#Method to print all isbn in self.books
#	def print_isbn(self):
#       for isbn in self.isbn:
#          print(isbn)
			
#Method to print all users
    def print_users(self):
        for user in self.users.values():
            print(user)
			
#Method to identify the most read book
    def get_most_read_book(self):
        max_reads = float("-inf")
        most_read = None
#Iterate through all books to fnd the one with greatest read frequency
        for book in self.books:
            number_of_reads = self.books[book]
            if number_of_reads > max_reads:
                max_reads = number_of_reads
                most_read = book
        return most_read
		
#Method to identfy the higehst rated book
    def highest_rated_book(self):
        highest_rating = float("-inf")
        best_book = None
#Iterate through books to find highest rating
        for book in self.books:
            avg = book.get_average_rating()
            if avg > highest_rating:
                highest_rating = avg
                best_book = book
        return best_book
		
#Method to find user who gives the highest average rating
    def most_positive_user(self):
        highest_rating = float("-inf")
        easy_scoring_user = None
#Iterate through all users
        for user in self.users.values():
            avg = user.get_average_rating()
            if avg > highest_rating:
                highest_rating = avg
                easy_scoring_user = user
        return easy_scoring_user
		
