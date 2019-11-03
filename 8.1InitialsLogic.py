# Write a program that gets a string from the user containing a person's first, middle, and last names and then
# displays their first, middle, and last initials. (Creating a new variable and concatenating each letter plus a '.'
# is the easiest way to do this.)


def get_person_names():
    first_name = input("Please enter your first name: ")
    middle_name = input("Please enter your middle name: ")
    last_name = input("Please enter your last name: ")

    return first_name, middle_name, last_name


def get_initials(first_name, middle_name, last_name):
    first_initial = first_name[0]
    middle_initial = middle_name[0]
    last_initial = last_name[0]

    return first_initial, middle_initial, last_initial


def display_initials(first_initial, middle_initial, last_initial):
    print(first_initial, middle_initial, last_initial)


def main():
    first_name, middle_name, last_name = get_person_names()

    first_initial, middle_initial, last_initial = get_initials(first_name, middle_name, last_name)

    display_initials(first_initial, middle_initial, last_initial)


main()

"""
# IGNORE THIS ROUND
first_name = input('What is your first name? ')
middle_name = input('What is your middle name? ')
last_name = input('What is your last name? ')

# Processing (calculations, evaluating lists or strings)
# concatenate all string (input variables)
full_name = first_name + ' ' + middle_name + ' ' + last_name

# Output (display or return values)
print(full_name)

# DO fullname.split
# ie first name = fullname[0]   GRAB FIRST INITIAL CHARACTER

full_name = initials


def main():

    # Get first letter of the first name
    set1 = first_name[0: 1]
    # Get first letter of middle name
    set2 = middle_name[0: 1]
    # Get the first letter of last name
    set3 = last_name[0: 1]
    # put the sets of characters together
    initials = set1 + set2 + set3

    return initials


main()
"""
