import streamlit as st
import json
import os

LIBRARY_FILE = "library.txt"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

library = load_library()

st.title("📚 Personal Library Manager")

menu = [
    "➕ Add a Book",
    "🗑️ Remove a Book",
    "🔍 Search for a Book",
    "📚 Display All Books",
    "📊 Display Statistics",
    "🚪 Exit"
]

choice = st.sidebar.selectbox("Choose an action", menu)

if choice == "➕ Add a Book":
    st.subheader("➕ Add a New Book")

    with st.form("add_book_form"):
        title = st.text_input("Title of the Book")
        author = st.text_input("Author of the Book")
        year = st.number_input("Publication Year", min_value=0, step=1, format="%d")
        genre = st.text_input("Category of the Book")
        read_status = st.checkbox("Are you Read it?")
        submitted = st.form_submit_button("Add Book ")

        if submitted:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read_status
            }
            library.append(book)
            save_library(library)
            st.success(f"Book added: {title} by {author} ({year}), Genre: {genre}, Read: {read_status}")

elif choice == "🗑️ Remove a Book":
    st.subheader("🗑️ Remove a Book")
    titles = [book["title"] for book in library]
    if titles:
        book_to_remove = st.selectbox("Select a book to remove", titles)
        if st.button("Remove"):
            library = [book for book in library if book["title"] != book_to_remove]
            save_library(library)
            st.success(f"Book removed: {book_to_remove}")
    else:
        st.info("Library is empty.")

elif choice == "🔍 Search for a Book":
    st.subheader("🔍 Search for a Book")
    query = st.text_input("Enter title or author to search:")
    if query:
        found_books = [
            book for book in library
            if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()
        ]
        if found_books:
            for book in found_books:
                st.write(f"{book['title']} by {book['author']} ({book['year']}), Genre: {book['genre']}, Read: {book['read']}")
        else:
            st.warning("No matching books found.")

elif choice == "📚 Display All Books":
    st.subheader("📚 All Books in Library")
    if library:
        for book in library:
            st.write(f"{book['title']} by {book['author']} ({book['year']}), Genre: {book['genre']}, Read: {book['read']}")
    else:
        st.info("Library is empty.")

elif choice == "📊 Display Statistics":
    st.subheader("📊 Library Statistics")
    if library:
        total = len(library)
        read = sum(book["read"] for book in library)
        percent = (read / total) * 100
        st.write(f"Total books: {total}")
        st.write(f"Books read: {read}")
        st.write(f"Percentage read: {percent:.2f}%")
    else:
        st.info("Library is empty.")

elif choice == "🚪 Exit":
    save_library(library)
    st.success("Library saved. You may close the app.")

# Footer on every page
st.markdown("---")
st.markdown(
    """
    <div style="
        text-align: center;
        margin-top: 20px;
        font-size: 1.1rem;
        color: #444;
    ">
        ✨ App made by <strong>Muhammad Awais 🖤</strong> ✨<br>
        🔗 <a href="https://github.com/mhdawaisrajput" target="_blank" style="color: #3366cc; text-decoration: none;">
            Visit my GitHub
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


