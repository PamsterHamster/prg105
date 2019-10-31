"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
print("=" * 10, "Section 8.1 string operations", "=" * 10)
# 1) Print all the characters from the name variable by accessing one character at a time
name = 'John Jacob Jingleheimer Schmidt'
for ch in name:
    print(ch)

# 2) Use the index value to access and print the capital s in Schmidt from the variable name

my_string = 'John Jacob Jingleheimer Schmidt'
ch = my_string[23]
print(my_string[23])

# 3) Use a negative index value to print the letters from the last name "Schmidt" in name

my_string = 'John Jacob Jingleheimer Schmidt'
print(my_string[-7], my_string[-6], my_string[-5], my_string[-4], my_string[-3], my_string[-2], my_string[-1])

# TODO 8.2 String slicing
print("=" * 10, "Section 8.2 string slicing", "=" * 10)
# 1) Use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
name = 'John Jacob Jingleheimer Schmidt'

full_name = 'John Jacob Jingleheimer Schmidt'
middle_name = full_name[5:10]

# 2) Print middle
print(middle_name)


# TODO 8.3 Testing, Searching, and manipulating strings
print("=" * 10, "Section 8.3 manipulating strings", "=" * 10)
# 1) Test to see if the string "Jacob" is in name, print the result
text = 'John Jacob Jingleheimer Schmidt'
if 'Jacob' in text:
    print('The string name Jacob was found.')
else:
    print('The string Jacob was not found.')


# 2) Test to see if the string "Michael" is in name, print the result
text = 'John Jacob Jingleheimer Schmidt'
if 'Michael' in text:
    print('The string name Michael was found.')
else:
    print('The string Michael was not found.')

# 3) Test to see if name contains a number, print the result

string1 = 'John Jacob Jingleheimer Schmidt'
if string1.isdigit():
    print(string1, 'contains a digit')
else:
    print(string1, 'contains characters other than digits.')

# 4) Test to see if number contains a number, print the result
number = 42
string2 = '42'
if string2.isdigit():
    print(string2, 'contains only digits.')
else:
    print(string2, 'contains characters other than digits')

# 5) Search for "J" in name, replace with "j" (lower case), print the result
#    Note: You can assign this to a variable first, or just print


string = 'John Jacob Jingleheimer Schmidt'
new_string = string.replace('J', 'j')
print(new_string)

# 6) Split the string name into the variable name_list, replace the "", print the result


def main():
    split_string = 'John Jacob Jingleheimer Schmidt'

    # Split the string
    name_list = split_string.split()

    # Print
    print(name_list)


# Call main function
main()
