books = []
book_details = {}

def add_book(books, book_details, title, details):
    # Add the title to books list
    books.append(title)
    book_details[title] = details
    print("Book added successfully!")
    
def update_book(book_details, title, key, value):
    # If book exists, update the details
    if title in book_details:
        book_details[title][key] = value
        print(f"Updated {key} for book {title}")
    else:
        print(f"Book {title} not found")

def display_books(books, book_details):
    # Print all books and details nicely
    print("\nAll Books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")
        for key, value in book_details[book].items():
            print(f"   {key}: {value}")
        print()

def list_authors(book_details):
    # Collect and return a set of all unique authors
    authors = set()
    for book in book_details.values():
        author = book.get('Author', '').split(', ')
        book_list.update(author)
    return book_list

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Display Books")
    print("4. List Authors")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = input("Enter year published: ")
        genre = input("Enter genre (comma-separated): ")
        details = {
            "Author": author,
            "Year Published": year,
            "Genre": genre
        }
        add_book(books, book_details, title, details)

    elif choice == '2':
        title = input("Enter book title name to update: ")
        key = input("Enter detail to update (Author/Year Published/Genre): ")
        value = input(f"Enter new value for {key}: ")
        update_book(book_details, title, key, value)

    elif choice == '3':
        display_books(books, book_details)

    elif choice == '4':
        authors = list_authors(book_details)
        print("\nAll Authors:")
        for author in authors:
            print(f"- {author}")

    elif choice == '5':
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
