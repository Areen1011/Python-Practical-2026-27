contacts = []

while True:
    print("\n--- Mobile Contact Management ---")
    print("1. Add Contact")
    print("2. Insert Emergency Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Delete Last Contact")
    print("6. Display Contacts")
    print("7. Count Contacts")
    print("8. Exit")
    
    choice = input("Select an option (1-8): ").strip()
    
    # Python's version of a Switch statement
    match choice:
        case '1':
            name = input("Enter Name: ")
            contacts.append({"name": name})
            
            
        case '2':
            name = input("Enter Emergency Name: ")
            phone = input("Enter Phone: ")
            contacts.insert(0, {"name": name, "phone": phone, "emergency": True})
            print("Emergency contact added to the top.")
            
        case '3':
            name_to_update = input("Enter Name to update: ")
            found = False
            for contact in contacts:
                if contact["name"].lower() == name_to_update.lower():
                    contact["phone"] = input("Enter New Phone: ")
                    print("Contact updated.")
                    found = True
                    break
            if not found:
                print("Contact not found.")
                
        case '4':
            name_to_delete = input("Enter Name to delete: ")
            found = False
            for contact in contacts:
                if contact["name"].lower() == name_to_delete.lower():
                    contacts.remove(contact)
                    print("Contact deleted.")
                    found = True
                    break
            if not found:
                print("Contact not found.")
                
        case '5':
            if len(contacts) > 0:
                removed = contacts.pop()
                print(f"Removed last contact: {removed['name']}")
            else:
                print("The contact list is already empty.")
                
        case '6':
            if not contacts:
                print("No contacts to display.")
            else:
                print("\nYour Contacts:")
                for index, contact in enumerate(contacts, 1):
                    tag = " [EMERGENCY]" if contact["emergency"] else ""
                    print(f"{index}. {contact['name']} - {contact['phone']}{tag}")
                    
        case '7':
            print(f"Total Contacts: {len(contacts)}")
            
        case '8':
            print("Exiting application. Goodbye!")
            break
            
        case _:
            print("Invalid choice. Please pick a number from 1 to 8.")

print(contacts)