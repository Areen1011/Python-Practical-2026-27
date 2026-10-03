contact = [999]

ch=int(input("1. Add Contact\n2. Insert Emergency Contact\n3. Update Contact\n4. Delete Contact\n5. Delete Last Contact\n6. Display Contacts\n7. Count Contacts\n8. Exit\nEnter number: "))

match(ch):
    case 1:
        contact.append(123)
        print(contact)
    case 2:
        contact.insert(0,456)
        print(contact)
    case 3:
        contact[0]=332
        print(contact)
    case 4:
        contact.pop()
        print(contact)
    case 5:
        contact.pop(-1)
        print(contact)
    case 6:
        print(contact)
    case 7:
        print(len(contact))
    case 8:
        exit