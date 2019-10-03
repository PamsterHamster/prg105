"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
print("=" * 10, "Section 7.2 lists", "=" * 10)
# 1) Create a list of days of the week, assign it to the variable days, remove """ """ to test

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(days)

# 2) Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
numbers = [0, 0, 0, 0, 0]
numbers = [0] * 5
print(numbers)

# 3) Print the contents of your days list using the for operator
for n in days:
    print(n)

# 4) Print the list item that holds the value Saturday from the days list by using it's index

print(days[5])

"""
index = 0
while index < 7:
    print(days[index])
    index += 1
"""

# 5) Create a variable called size to hold the length of the list days using the len function
size = len(days)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satruday', 'Sunday']
index = 0
while index < len(days):
    print(days[index])
    index += 1

# 6) Concatenate the two following lists together, storing the value in list3 - remove the """ """ to test

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)

# TODO 7.3 List Slicing
print("=" * 10, "Section 7.3 list slicing", "=" * 10)
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# Print work_days

work_days = days[0:5]
print(work_days)

# TODO 7.4 Finding items in Lists with the in Operator
print("=" * 10, "Section 7.4 using the in operator", "=" * 10)

# Test to see if "Tue" is in the list days - display "yes, Tue is in the list" or "no, Tue is not in the list"
"""
def main():
    search = input('Enter the day you are looking for: ')

    # Determine if that day is in the list
    if search in work_days:
        print(search, 'Yes,' + work_daysday + 'is in the list')
    else:
        print(search, 'No,' + work_days + 'is not in the list')


main()
"""

# TODO 7.5 List Methods and Useful Built-in Functions
print("=" * 10, "Section 7.5 list methods and functions", "=" * 10)

# 1) Use append() to append the last three months of the year to the list months.
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept']

def main():

    # WHY does the month_list below turn gray? If it's NOT indented, it turns black...
    month_list = list(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept'])
    # Create variable to control te loop
    again = 'y'


while again == 'y':
    # Get name from user
    month = input('Enter the first missing month: ')

    # Append month to the list
    month_list.append(month)

    # Add another one?
    print('Do you want to add another month? ')
    again = input('y = yes, anything else = no: ')
    print()

    # Display the months that were entered
    print('Here are the months you entered. ')

    for month in month_list:
        print(month)

    # Call the main function
main()

# FROM HERE ON ITS CONFUSING. I NEED TO WATCH SOME TUTORIALS..THE REST OF THESE EXERCISES SEEM TO BUILD ON ONE ANTOTHER

# 2) Get the index of "May" from the months list and print it on screen

# 3) Sort list3 from exercise 7.2 and print the results on screen

# 4) Reverse the order of list3

# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)

# 6) Print the maximum value from list 3


# TODO 7.6 Copying Lists
print("=" * 10, "Section 7.6 copying lists", "=" * 10)
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year


# TODO 7.7 Processing lists
print("=" * 10, "Section 7.7 processing lists", "=" * 10)
# 1) Total the values in list3 and print the results

# 2) Get the average of values in list3 and print the results

# 3) Open the file states.txt in read mode,
# -- read the contents of the file into the list states_list
# -- print the contents of states_list on screen


# TODO 7.8 Two-Dimensional Lists
print("=" * 10, "Section 7.8 two-dimensional lists", "=" * 10)
# 1) Create a new two dimensional list that has the months of the year
#     and the days in each month during a non leap year
#     For example, the first entry should be: January, 31

# 2) Print the contents of the entire list

# 3) Print just the values for index 3,0 and 3,1

# TODO 7.9 Tuples
print("=" * 10, "Section 7.9 tuples", "=" * 10)
# Create a tuple using the months list as its data source
