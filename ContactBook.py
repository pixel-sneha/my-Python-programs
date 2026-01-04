#Contact book application
def display_menu(): 
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input()
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input()
    email = input()
    address = input()

    contact_book[name] = {
        "phone" : phone,
        "email" : email,
        "address" : address
    }
    print("Contact added successfully!")

def view_contact(contact_book):
    contact = input()
    if contact in contact_book:
        print(f"Name: {contact}")
        print(f"Phone: {contact_book[contact]['phone']}")
        print(f"Email: {contact_book[contact]['email']}")
        print(f"Address: {contact_book[contact]['address']}")
    else:
        print("Contact not found!")
        return

def edit_contact(contact_book):
    user = input()
    if user in contact_book:
        new_phone = input()
        new_email = input()
        new_address = input()

        if new_phone:
            contact_book[user]['phone'] = new_phone
        if new_email:
            contact_book[user]['email'] = new_email
        if new_address:
            contact_book[user]['address'] = new_address
            
        print("Contact updated successfully!")
        
    else:
        print("Contact not found!")
        return

def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        update_dict = contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
