import sqlite3


def create_database():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Phone TEXT NOT NULL)''')
    conn.commit()
    conn.close()


def add_entry():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Entries (Name, Phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()
    print("Entry added")


def lookup_phone():
    name = input("Enter name to look up: ")

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute("SELECT Phone FROM Entries WHERE Name = ?", (name,))
    result = cur.fetchone()
    conn.close()

    if result:
        print(f"Phone number for {name}: {result[0]}")
    else:
        print(f"No entry found for {name}.")


def update_phone():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute("UPDATE Entries SET Phone = ? WHERE Name = ?", (new_phone, name))
    conn.commit()
    conn.close()

    print("Phone number updated")


def delete_entry():
    name = input("Enter name to delete: ")

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
    conn.commit()
    conn.close()

    print(f"Entry for {name} deleted")


def main():
    create_database()

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Entry")
        print("2. Look Up Phone Number")
        print("3. Update Phone Number")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            lookup_phone()
        elif choice == "3":
            update_phone()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()