import json

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.load_books()

    def add_book(self, title, author):
        """Adds a new book using a (title, author) approach."""
        book = (title, author, True)  # Tuple: (title, author, available)
        self.books.append(book)
        print(f'Book "{title}" by {author} added.')

    def borrow_book(self, title):
        """Borrows a book if available."""
        for i, book in enumerate(self.books):
            if book[0].lower() == title.lower() and book[2]:  # Book is available
                self.books[i] = (book[0], book[1], False)  # Update tuple to unavailable
                print(f'You borrowed "{title}".')
                return
        print(f'Sorry, "{title}" is not available.')

    def return_book(self, title):
        """Returns a borrowed book."""
        for i, book in enumerate(self.books):
            if book[0].lower() == title.lower() and not book[2]:
                self.books[i] = (book[0], book[1], True)  # Mark as available
                print(f'You returned "{title}".')
                return
        print(f'Error: "{title}" was not borrowed.')

    def view_books(self):
        """Displays all available books."""
        available_books = [book for book in self.books if book[2]]
        if available_books:
            print("\nAvailable Books:")
            for title, author, _ in available_books:
                print(f"- {title} by {author}")
        else:
            print("No books available.")

    def save_books(self):
        """Saves books to a file."""
        with open("library.json", "w") as f:
            json.dump(self.books, f)
        print("Library data saved.")

    def load_books(self):
        """Loads books from a file."""
        try:
            with open("library.json", "r") as f:
                self.books = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

def main():
    library = Library("City Library")

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)

        elif choice == "2":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == "3":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "4":
            library.view_books()

        elif choice == "5":
            library.save_books()
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
