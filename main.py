# Name: Jonathan Nunez
# Date: 9/8/24
# Purpose: A driver program for the Tuffy Titan Contact List that allows the user to add, modify, delete, and view contacts.

import contacts

def main():
    contact_list = []
    
    while True:
        print("\n      *** TUFFY TITAN CONTACT MAIN MENU")
        print("1. Print list")
        print("2. Add contact")
        print("3. Modify contact")
        print("4. Delete contact")
        print("5. Exit the program")
        
        choice = input("\nEnter menu choice: ")
        
        if choice == "1":
            contacts.print_list(contact_list)
        elif choice == "2":
            contact_list = contacts.add_contact(contact_list)
        elif choice == "3":
            contact_list = contacts.modify_contact(contact_list)
        elif choice == "4":
            contact_list = contacts.delete_contact(contact_list)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
