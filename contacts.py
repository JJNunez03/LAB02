# Name: Jonathan Nunez
# Date: 9/6/24
# Purpose: A module to manage a contact list for Tuffy Titan, providing functions to print, add, modify, and delete contacts.

def print_list(contact_list):
    """
    Print the contact list with index numbers, first names, and last names.
    """
    print("\n================== CONTACT LIST ==================")
    print(f"{'Index':8}{'First Name':22}{'Last Name':22}")
    print(f"{'======':8}{'====================':22}{'====================':22}")
    for i in range(len(contact_list)):
        print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')
    print()

def add_contact(contact_list):
    """
    Add a new contact to the list by prompting the user for the first and last name.
    """
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    contact_list.append([first_name, last_name])
    return contact_list

def modify_contact(contact_list):
    """
    Modify an existing contact in the list by prompting the user for the index number.
    """
    try:
        index = int(input("Enter the index number: "))
        if index < 0 or index >= len(contact_list):
            print("Invalid index number.")
            return contact_list
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        contact_list[index] = [first_name, last_name]
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return contact_list

def delete_contact(contact_list):
    """
    Delete a contact from the list by prompting the user for the index number.
    """
    try:
        index = int(input("Enter the index number: "))
        if index < 0 or index >= len(contact_list):
            print("Invalid index number.")
            return contact_list
        contact_list.pop(index)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return contact_list
