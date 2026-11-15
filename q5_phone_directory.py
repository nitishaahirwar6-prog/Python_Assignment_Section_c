# Q5: Phone Directory

phone_directory = {}

while True:
    print("\n--- Phone Directory ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phone_directory[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phone_directory:
            print("Phone Number:", phone_directory[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in phone_directory:
            phone = input("Enter new phone number: ")
            phone_directory[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in phone_directory:
            del phone_directory[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        if phone_directory:
            for name, phone in phone_directory.items():
                print(name, ":", phone)
        else:
            print("Phone Directory is empty!")

    elif choice == "6":
        print("Exiting Phone Directory...")
        break

    else:
        print("Invalid choice!")