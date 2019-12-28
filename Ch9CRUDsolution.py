import pickle


"""
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person's email address, add a new name & email address,
change an existing email address, and delete an existing name & email address.
The program should pickle the dictionary and save it to a file when the user exits the program.
Each time the program starts, it should retrieve the dictionary from the file and unpickle it.

"""
#   MENU CONSTANTS

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    # Data
    customers = {}
    try:
        end_of_file = False
        input_file = open("customers.dat", 'rb')
        while not end_of_file:
            try:
                customers = pickle.load(input_file)
                print(customers)  # for testing purposes only
            except EOFError:
                end_of_file = True
        input_file.close()
    except IOError:
        customers = {}  # creates customer dictionary if file doesn't exists

    menu_option = 0
    while menu_option != 5:
        menu_option = menu()

        if menu_option == 1:
            look_up(customers)
        elif menu_option == 2:
            add_customer(customers)
        elif menu_option == 3:
            change_customer(customers)
        elif menu_option == 4:
            delete_customer(customers)
        elif menu_option == 5:
            print("Thank you, program terminating")
        else:
            print("That was not a valid selection. Please enter a number between 1 and 5.")


def menu():
    print("\n\n***************Customer Service******************\n\n")
    print("1. Look up a customer")
    print("2. Add a customer")
    print("3. Change a customer email")
    print("4. Delete a customer")
    print("5. Quit")

    menu_option = int(input("Please enter the number of the menu option:  "))
    return menu_option


def look_up(customers):
    print("****************Find a Customer*******************")
    name = input("Please enter the customer name:   ")
    if name in customers:
        print(name, customers[name])
    else:
        print("That customer does not exist")


def add_customer(customers):
    print("*************Add a Customer *******************")
    name = input("Please enter the customer name:   ")
    email = input("Please enter the customer email:   ")
    if name in customers:
        print(name + "already exists")
    else:
        customers[name] = email
        save_customers(customers)


def change_customer(customers):
    print("*****************Change Customer **************")
    name = input("Please enter the customer name:   ")
    if name in customers:
        email = input("Please enter the customer email:   ")
        customers[name] = email
        print(name + email + "  will be updated with this email. ")
        save_customers(customers)
    else:
        add_choice = input("That name does not exist. Would you like to add it? (y/n) ")
        if add_choice == "y" or add_choice == "Y":
            add_customer(customers)


def delete_customer(customers):
    print("*******************Remove Customer********************")
    name = input("Please enter the customer name:  ")
    if name in customers:
        print(name, customers[name], "Will be deleted")
        del customers[name]
        save_customers(customers)
    else:
        print("That customer does not exist")


def save_customers(customers):
    print("**************Saving File **********************")
    output_file = open("customers.dat", 'wb')
    pickle.dump(customers, output_file)
    output_file.close()
    print("\n Your data has been saved.  \n")


main()
