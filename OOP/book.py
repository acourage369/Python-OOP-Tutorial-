class Book:

    def __init__(self, title, author, ISBN, publication_date, page, price):
        self.title = title
        self.author = author
        self.isbn = ISBN
        self.publication_date = publication_date
        self.page = page
        self.price = price

    def set_title(self):
        return self.title

    def set_author(self):
        return self.author

    def set_isbn(self):
        return self.isbn

    def set_publication_date(self):
        return self.publication_date

    def set_page(self):
        return self.page

    def set_price(self):
        return self.price

    def is_book_long(self):
        if self.page > 500:
            return "The book is long."
        else:
            return "The book is not long."

    def check_publication(self):
        if 2023 - self.publication_date <= 5:
            return f"{self.set_title()} is a recent publication."
        else:
            return f"{self.set_title()} is not a recent publication."
