import json  # For saving and loading the library as JSON data
import os   # For checking file existence

LIBRARY_FILE = "library.txt"  # File to store the library data

# Function to load library from file if it exists, otherwise return an empty list.
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            try:
                # Load JSON data from the file.
                return json.load(file)
            except json.JSONDecodeError:
                # If file is corrupted or empty, return an empty library.
                return []
    return []

# Function to save the current library to a file.
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Load the library data when the program starts.
library = load_library()


# Welcome message for the library manager.
print("Welcome to Your Personal Library Manager!")

# Main loop to repeatedly prompt the user for actions.
while True:
    # Define the menu options.
    choices = [
        "1. Add a book",
        "2. Remove a book",
        "3. Search for a book",
        "4. Display all books",
        "5. Display statistics",
        "6. Exit"
    ]

    # Display each menu option.
    for choice in choices:
        print(choice)
    
    # Prompt the user to input their choice.
    user_input = input("Enter your choice: ")

    # Option 1: Add a new book to the library.
    if user_input == "1":
        # Prompt for book details.
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        # Convert publication year to integer; handle invalid input.
        try:
            year = int(input("Enter the publication year of the book: "))
        except ValueError:
            print("Invalid year. Please enter an integer value.")
            continue
        genre = input("Enter the genre of the book: ")
        # Ask if the book has been read (Yes/No). Normalize input to boolean.
        read_input = input("Have you read this book? (yes/no): ").strip().lower()
        read_status = True if read_input in ["yes", "y"] else False

        # Create a dictionary for the book.
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status
        }
        # Add the book to the library.
        library.append(book)
        print(f"Book added successfully: {title} by {author} ({year}), Genre: {genre}, Read: {read_status}")

    # Option 2: Remove a book from the library.
    elif user_input == "2":
        # Ask for the title of the book to remove.
        title = input("Enter the title of the book to remove: ")
        book_found = False  # Flag to check if the book is found.
        # Iterate through the library to find the matching book (case-insensitive).
        for book in library:
            if book["title"].lower() == title.lower():
                library.remove(book)
                book_found = True
                print(f"Book removed successfully: {title}")
                break  # Remove only the first occurrence.
        if not book_found:
            print(f"Book not found in the library: {title}")

    # Option 3: Search for a book by title or author.
    elif user_input == "3":
        query = input("Enter the title or author of the book to search for: ")
        found_books = []  # List to store matching books.
        # Search each book for a matching title or author (case-insensitive substring match).
        for book in library:
            if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
                found_books.append(book)
        # Display search results.
        if found_books:
            print("Book(s) found:")
            for book in found_books:
                print(f"{book['title']} by {book['author']} ({book['year']}), Genre: {book['genre']}, Read: {book['read']}")
        else:
            print(f"No books found matching: {query}")

    # Option 4: Display all books in the library.
    elif user_input == "4":
        if not library:
            print("The library is empty.")
        else:
            print("Library contents:")
            for book in library:
                # Print each book in a formatted way.
                print(f"{book['title']} by {book['author']} ({book['year']}), Genre: {book['genre']}, Read: {book['read']}")

    # Option 5: Display library statistics.
    elif user_input == "5":
        if not library:
            print("The library is empty.")
        else:
            total_books = len(library)
            # Count the books that have been read.
            read_books = sum(1 for book in library if book["read"])
            # Calculate the percentage of books read.
            percent_read = (read_books / total_books) * 100
            print("Library statistics:")
            print(f"Total books: {total_books}")
            print(f"Percentage of books read: {percent_read:.2f}%")

    # Option 6: Exit the program.
    elif user_input == "6":
        # Save the library data before exiting.
        save_library(library)
        print("Exiting the library manager. Your library data has been saved.")
        break  # End the loop to exit the program.

    # Handle invalid menu options.
    else:
        print("Invalid choice. Please try again.")