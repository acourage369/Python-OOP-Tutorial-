from book import Book

# Instances of books
book1 = Book("Python programing", "Brainy Yawson", 23 - 64 - 22 - 42, 2017, 600, 44)
book2 = Book("Java Programming in 30 days", "Normson Solomon", 12-34-35-21, 2015, 400, 90)

print("Book 1")
print(f"Title: {book1.set_title()}")
print(f"Author: {book1.set_author()}")
print(f"ISBN: {book1.set_isbn()}")
print(f"Publication date: {book1.set_publication_date()}")
print(f"Page: {book1.set_page()}")
print(f"Price: ${book1.set_price()}")
print(f"Book length: {book1.is_book_long()}")
print(f"Publication status: {book1.check_publication()}")

print("\n")

print("Book 2")
print(f"Title: {book2.set_title()}")
print(f"Author: {book2.set_author()}")
print(f"ISBN: {book2.set_isbn()}")
print(f"Publication date: {book2.set_publication_date()}")
print(f"Page: {book2.set_page()}")
print(f"Price: ${book2.set_price()}")
print(f"Book length: {book2.is_book_long()}")
print(f"Publication status: {book2.check_publication()}")



