contacts = {}
def add_contact():
  name = input("Enter contact name: ")
  phone_number = input("Enter phone number: ")
  email = input("Enter email (optional): ")
  address = input("Enter address (optional): ")
  contact_details = {
    "phone_number": phone_number,
    "email": email if email else "N/A",
    "address": address if address else "N/A"
  }

  contacts[name] = contact_details
def edit_contact():
  name = input("Enter name of the contact to edit: ")
  if name in contacts:
    new_phone_number = input("Enter new phone number (or leave blank): ")
    new_email = input("Enter new email (or leave blank): ")
    new_address = input("Enter new address (or leave blank): ")
    if new_phone_number:
      contacts[name]["phone_number"] = new_phone_number
    if new_email:
      contacts[name]["email"] = new_email
    if new_address:
      contacts[name]["address"] = new_address

    print("Contact details updated successfully!")
  else:
    print("Contact not found.")
def delete_contact():
  name = input("Enter name of the contact to delete: ")
  if name in contacts:
    del contacts[name]
    print("Contact deleted successfully!")
  else:
    print("Contact not found.")
def search_contact():
  name = input("Enter name of the contact to search: ")
  if name in contacts:
    print("Name:", name)
    print("Phone number:", contacts[name]["phone_number"])
    print("Email:", contacts[name]["email"])
    print("Address:", contacts[name]["address"])
  else:
    print("Contact not found.")
def display_contacts():
  if contacts:
    for name, details in contacts.items():
      print("-" * 20)
      print("Name:", name)
      print("Phone number:", details["phone_number"])
      print("Email:", details["email"])
      print("Address:", details["address"])
  else:
    print("There are no contacts in your list.")
while True:
  print("\nContact Book Menu")
  print("1. Add Contact")
  print("2. Edit Contact")
  print("3. Delete Contact")
  print("4. Search Contact")
  print("5. Display All Contacts")
  print("6. Exit")

  choice = input("Enter your choice: ")
  if choice == '1':
    add_contact()
  elif choice == '2':
    edit_contact()
  elif choice == '3':
    delete_contact()
  elif choice == '4':
    search_contact()
  elif choice == '5':
    display_contacts()
  elif choice == '6':
    break
  else:
    print("Invalid choice. Please try again.")
