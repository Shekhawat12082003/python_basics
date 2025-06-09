contacts={}

def add_contact():
     name = input("Enter name: ").strip()
     phone = int(input("Enter phone number: ")).strip()
     email = input("Enter email: ").strip()
    
     if name in contacts:
          print ("Name Exist")
     else :
          contacts[name]={"phone":phone,"email":email}
          print ("Contact Added")

def view_contact():
     if not contacts:
          print("No Contact Found")
     else :
          for name , info in contacts :
               print(f"Name: {name}")
               print(f"Phone: {info['phone']}")
               print(f"Email{info['email']}")
def search_contact():
     name = input ("Enter Name: ")
     if name in contacts :
          info = name [contacts]
          print(f"Name: {name}")
          print(f"Phone: {info['phone']}")
          print(f"Email{info['email']}")
     else:
          print("Contact not found")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def contact_book():
    print("Welcome to Contact Book!")

    while True:
        print("\n1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Try again.")

contact_book()