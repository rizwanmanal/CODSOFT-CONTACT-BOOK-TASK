
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name}: {contact.phone}")

    def search_contact(self, query):
        matching_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query.lower() in contact.phone]
        if matching_contacts:
            print(f"Search results for '{query}':")
            for contact in matching_contacts:
                print(f"{contact.name}: {contact.phone}")
        else:
            print(f"No contacts found with name or phone containing '{query}'.")

    def update_contact(self, index):
        old_contact = self.contacts[index]
        name = input("Enter new name: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        new_contact = Contact(name, phone, email, address)
        self.contacts[index] = new_contact
        print(f"Contact updated: {new_contact.name} - {new_contact.phone}")

    def delete_contact(self, index):
        self.contacts.pop(index)
        print("Contact deleted.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")

            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

            print(f"Contact added: {name} - {phone}")

        elif choice == 2:
            contact_book.display_contacts()

        elif choice == 3:
            query = input("Enter name or phone to search for: ")
            contact_book.search_contact(query)

        elif choice == 4:
            index = int(input("Enter index of contact to update: "))
            if 0 <= index < len(contact_book.contacts):
                contact_book.update_contact(index)
            else:
                print("Invalid index.")

        elif choice == 5:
            index = int(input("Enter index of contact to delete: "))
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
            else:
                print("Invalid index.")

        elif choice == 6:
            break

        else:
            print("Error: Invalid choice. Please try again.")


if __name__ == "__main__":
    main()