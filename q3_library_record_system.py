# Q3. Library Record System

books = {
    "B1": {
        "title": "Python Basics",
        "author": "Rao",
        "copies": 2,
        "issued_to": []
    },
    "B2": {
        "title": "Data Structures",
        "author": "Iyer",
        "copies": 1,
        "issued_to": []
    },
    "B3": {
        "title": "Algorithms",
        "author": "Rao",
        "copies": 1,
        "issued_to": []
    }
}

ever_issued = set()

while True:

    print("\n--- LIBRARY RECORD SYSTEM ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        isbn = input("Enter ISBN: ")

        if isbn in books:
            copies = int(input("Enter additional copies: "))
            if copies > 0:
                books[isbn]["copies"] += copies
                print("Copies added successfully!")
            else:
                print("Invalid number of copies!")

        else:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            copies = int(input("Enter number of copies: "))

            if copies > 0:
                books[isbn] = {
                    "title": title,
                    "author": author,
                    "copies": copies,
                    "issued_to": []
                }