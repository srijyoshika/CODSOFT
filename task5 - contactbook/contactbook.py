#Contact book
import sys
contacts = {}

def add():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("saved successfully.")

def view():
    if len(contacts) == 0:
        print("Not found.")
    else:
        print("\n------ SAVED CONTACTS ------")
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")


def search():
    search_name = input("Enter the name to search: ")
    if search_name in contacts:
        details = contacts[search_name]
        print("\nContact Found:")
        print(f"Name: {search_name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
        print(f"Address: {details['Address']}")
    else:
        print("not found.")

def update():
    update_name = input("Enter the name to update: ")

    if update_name in contacts:

        while True:
            print("\nWhat do you want to update?")
            print("1. Update Name")
            print("2. Update Phone Number")
            print("3. Update Email")
            print("4. Update Address")
            print("5. Update All Details")
            print("6. Back to Main Menu")

            ch = int(input("Enter your choice: "))
            match ch:
                case 1:
                    new_name = input("Enter new name: ")
                    contacts[new_name] = contacts.pop(update_name)
                    update_name = new_name
                    print("Name updated successfully.")

                case 2:
                    new_phone = input("Enter new phone number: ")
                    contacts[update_name]["Phone"] = new_phone
                    print("Phone number updated successfully.")

                case 3:
                    new_email = input("Enter new email: ")
                    contacts[update_name]["Email"] = new_email
                    print("Email updated successfully.")

                case 4:
                    new_address = input("Enter new address: ")
                    contacts[update_name]["Address"] = new_address
                    print("Address updated successfully.")

                case 5:
                    new_name = input("Enter new name: ")
                    new_phone = input("Enter new phone number: ")
                    new_email = input("Enter new email: ")
                    new_address = input("Enter new address: ")

                    contacts.pop(update_name)
                    contacts[new_name] = {
                        "Phone": new_phone,
                        "Email": new_email,
                        "Address": new_address
                    }
                    update_name = new_name

                    print("All details updated successfully.")

                case 6:
                    break

                case _:
                    print("Invalid choice")

    else:
        print("Contact not found.")

def delete():
    delete_name = input("Enter name to delete: ")
    if delete_name in contacts:
        del contacts[delete_name]
        print("deleted successfully.")
    else:
        print("not found.")

while True:
    print("\n========== PERSONAL CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    ch= int(input("Select an option (1-6): "))
    match ch:
        case 1:
            add()
        case 2:
            view()
        case 3: 
            search()
        case 4:
            update()
        case 5:
            delete()
        case 6:
            print("Closing Contact Book. Thank you!")
            sys.exit()
        case _: 
            print("Invalid choice")
