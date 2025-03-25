
# ================================
#  كلاس الكتاب Book
# ================================
class Book:
    def _init_(self, book_id, title, author, subject, publication_date, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.subject = subject
        self.publication_date = publication_date
        self.copies = copies

    def _str_(self):
        return f"{self.title} by {self.author} ({self.publication_date}) - Copies: {self.copies}"


# ================================
#  كلاس المستخدم User (العضو)
# ================================
class User:
    def _init_(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
        self.reserved_books = []

    def borrow_book(self, library, book_id):
        book = library.search_book_by_id(book_id)
        if book and book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book)
            print(f"✅ {self.name} borrowed '{book.title}'.")
        else:
            print(f"❌ Sorry, '{book.title}' is not available.")

    def return_book(self, library, book_id):
        for book in self.borrowed_books:
            if book.book_id == book_id:
                book.copies += 1
                self.borrowed_books.remove(book)
                print(f"🔄 {self.name} returned '{book.title}'.")
                return
        print(f"❌ {self.name} doesn't have this book.")

    def reserve_book(self, library, book_id):
        book = library.search_book_by_id(book_id)
        if book:
            self.reserved_books.append(book)
            print(f"🔖 {self.name} reserved '{book.title}'.")
        else:
            print(f"❌ Book not found.")

    def renew_book(self, book_id):
        for book in self.borrowed_books:
            if book.book_id == book_id:
                print(f"🔄 {self.name} renewed '{book.title}'.")
                return
        print(f"❌ {self.name} doesn't have this book to renew.")

    def _str_(self):
        return f"User: {self.name} | Borrowed Books: {[book.title for book in self.borrowed_books]}"


# ================================
#  كلاس المكتبة Library
# ================================
class Library:
    def _init_(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"📚 Book '{book.title}' added to the library.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"❌ Book '{book.title}' removed from the library.")
                return
        print("❗ Book not found.")

    def update_book(self, book_id, title=None, author=None, subject=None, publication_date=None, copies=None):
        book = self.search_book_by_id(book_id)
        if book:
            book.title = title or book.title
            book.author = author or book.author
            book.subject = subject or book.subject
            book.publication_date = publication_date or book.publication_date
            book.copies = copies if copies is not None else book.copies
            print(f"🔄 Book '{book.title}' updated successfully.")
        else:
            print("❗ Book not found.")

    def search_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        return results

    def display_books(self):
        if not self.books:
            print("📭 No books in the library.")
        for book in self.books:
            print(book)

    def add_user(self, user):
        self.users.append(user)
        print(f"👤 User '{user.name}' added.")

    def _str_(self):
        return f"Library with {len(self.books)} books and {len(self.users)} users."


# ================================
#  كلاس المكتبي Librarian
# ================================
class Librarian:
    def _init_(self, name):
        self.name = name

    def add_book_to_library(self, library, book):
        library.add_book(book)

    def remove_book_from_library(self, library, book_id):
        library.remove_book(book_id)

    def edit_book_info(self, library, book_id, title=None, author=None, subject=None, publication_date=None, copies=None):
        library.update_book(book_id, title, author, subject, publication_date, copies)

    def issue_library_card(self, library, user):
        library.add_user(user)
        print(f"📄 Library card issued for {user.name}.")


# ================================
#  اختبار المشروع
# ================================

# إنشاء المكتبة
library = Library()

# إنشاء المكتبي
librarian = Librarian("Mr. Ahmed")

# إضافة كتب للمكتبة
book1 = Book(1, "Python Crash Course", "Eric Matthes", "Programming", "2019", 3)
book2 = Book(2, "Clean Code", "Robert C. Martin", "Software Engineering", "2008", 2)
librarian.add_book_to_library(library, book1)
librarian.add_book_to_library(library, book2)

# عرض الكتب المتاحة
print("\n📌 Available Books in Library:")
library.display_books()

# إنشاء مستخدم
user1 = User(101, "Ali")
librarian.issue_library_card(library, user1)

# المستخدم يستعير كتاب
print("\n📌 Borrowing Books:")
user1.borrow_book(library, 1)

# المستخدم يحجز كتاب
print("\n📌 Reserving a Book:")
user1.reserve_book(library, 2)

# عرض الكتب بعد الاستعارة
print("\n📌 Books after Borrowing:")
library.display_books()

# المستخدم يرجع كتاب
print("\n📌 Returning a Book:")
user1.return_book(library, 1)

# المستخدم يجدد الاستعارة
print("\n📌 Renewing a Book:")
user1.renew_book(2)

# عرض الكتب بعد الإرجاع
print("\n📌 Books after Returning:")
library.display_books()
