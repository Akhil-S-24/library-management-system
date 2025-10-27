# ===== Library Management System =====

library = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "available": True, "borrowed_by": None},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True, "borrowed_by": None},
    {"title": "1984", "author": "George Orwell", "available": False, "borrowed_by": "Aarav"},
]


def display_books():
    """Show all books in the library."""
    if not library:
        print("\n📭 No books available in the library.")
    else:
        print("\n📚 List of Books:")
        for i, book in enumerate(library, start=1):
            status = (
                f"Available ✅"
                if book["available"]
                else f"Borrowed ❌ (by {book['borrowed_by']})"
            )
            print(f"{i}. {book['title']} by {book['author']} — [{status}]")


def add_book():
    """Add a new book to the library."""
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    library.append({"title": title, "author": author, "available": True, "borrowed_by": None})
    print(f"✅ Book '{title}' added successfully!")


def borrow_book():
    """Borrow a book if it is available, or offer to add it if not found."""
    student_name = input("Enter your name: ")
    title = input("Enter the title of the book to borrow: ")

    for book in library:
        if book["title"].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                book["borrowed_by"] = student_name
                print(f"📖 {student_name}, you borrowed '{book['title']}'. Enjoy reading!")
                return
            else:
                print(f"❌ Sorry, '{book['title']}' is already borrowed by {book['borrowed_by']}.")
                return

    # Book not found — suggest adding
    print(f"⚠️ The book '{title}' is not available in our library.")
    print("📬 You can request this book from the librarian or add it now.")
    request = input("Would you like to add this book to the library? (yes/no): ").lower()
    if request == "yes":
        author = input("Enter the author of this book: ")
        library.append({"title": title, "author": author, "available": True, "borrowed_by": None})
        print(f"✅ '{title}' by {author} has been added to the library!")
    else:
        print("👍 Okay, maybe next time.")


def return_book():
    """Return a borrowed book."""
    student_name = input("Enter your name: ")
    title = input("Enter the title of the book to return: ")

    for book in library:
        if book["title"].lower() == title.lower():
            if not book["available"]:
                if book["borrowed_by"].lower() == student_name.lower():
                    book["available"] = True
                    book["borrowed_by"] = None
                    print(f"🔙 Thank you, {student_name}, for returning '{book['title']}'!")
                    return
                else:
                    print(f"⚠️ Sorry, '{book['title']}' was borrowed by {book['borrowed_by']}, not you.")
                    return
            else:
                print("⚠️ This book wasn’t borrowed.")
                return
    print(f"❌ Book '{title}' not found in the library records.")


def main():
    """Main menu-driven loop."""
    while True:
        print("\n===== 📘 Library Management System =====")
        print("1. Display all books")
        print("2. Add a new book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("👋 Exiting Library System. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
