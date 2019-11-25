# Write a program that keeps names and email addresses in a dictionary as key-value pairs.
# The program should display a menu that lets the user look up a person's email address, add a new name and email
# address, change an existing email address, and delete an existing name and email address.
# The program should pickle the dictionary and save it to a file when the user exits the program.
# Each time the program starts, it should retrieve the dictionary from the file and unpickle it.

# ==================

import pickle

# Constraints
Look_up = 1
Add = 2
Change = 3
Delete = 4
Quit = 5


# Program
def main():
    try:
        input_file = open("friends_file.dat", "rb")
        friends = pickle.load(input_file)
        print(friends)

    except (FileNotFoundError, IOError):
        print("File not found, please add a friend then quit to create the file. ")

    # Initialize for user's choice
    choice = 0

    while choice != Quit:
        # Get users menu choice
        choice = menu()
        # process choice
        if choice == Look_up:
            look_up(friends)
        elif choice == Add:
            add(friends)
        elif choice == Change:
            change(friends)
        elif choice == Delete:
            delete(friends)
        elif choice == Quit:
            save(friends)


# Present Menu
def menu():
    print()
    print("Friend email lookup ")
    print("----------------------")
    print("1.  Look up a friend")
    print("2.  Add a friend")
    print("3.  Change an email address")
    print("4.  Delete a friend")
    print("5.  Quit the program\n")

    # get the choice
    choice = int(input("Enter the number of your choice:  "))
    while choice < 1 or choice > 5:
        choice = int(input("Enter a valid choice:  "))
    return choice


# Look up a friend
def look_up(friends):
    name = input("Enter a friend's name:  ")
    print(friends.get(name, "Not Found"))


# Add a friend
def add(friends):
    # check to see if friend exists, then add friend
    name = input("Enter friend's name:  ")
    email = input("Enter friend's email address:  ")
    if name not in friends:
        friends[name] = email
    else:
        print("That entry already exists. ")


# change a friend's email
def change(friends):
    name = input("Enter the friend's name: ")
    if name in friends:
        email = input("Enter the new email address:  ")
        friends[name] = email
    else:
        print("That friend is not found. ")


# delete a friend
def delete(friends):
    name = input("Enter the friend's name to delete:  ")
    if name in friends:
        del friends[name]
    else:
        print("that friend was not found. ")


# save data file when exiting
def save(friends):
    print("This data file has been updated with your requested changes.  ")
    save_file = open("friends_file.dat", 'wb')
    pickle.dump(friends, save_file)
    save_file.close()


main()
