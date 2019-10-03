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
number = [0] * 5
print(number)

# 3) Print the contents of your days list using the for operator
for day in days:
    print(day)

# 4) Print the list item that holds the value Saturday from the days list by using it's index

print(days[6])

"""
index = 0
while index < 7:
    print(days[index])
    index += 1
"""

# 5) Create a variable called size to hold the length of the list days using the len function
size = len(days)
print(size)

"""
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satruday', 'Sunday']
index = 0
while index < len(days):
    print(days[index])
    index += 1
# FIRST TRY WAS ABOVE
"""

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
if "Tue" in days:
    print("Yes, Tue is in the list. ")
else:
    print("No, Tue is not in the list. ")

"""
def main():
    search = input('Enter the day you are looking for: ')

    # Determine if that day is in the list
    if search in work_days:
        print(search, 'Yes,' + work_days + 'is in the list')
    else:
        print(search, 'No,' + work_days + 'is not in the list')


main()
"""

# TODO 7.5 List Methods and Useful Built-in Functions
print("=" * 10, "Section 7.5 list methods and functions", "=" * 10)

# 1) Use append() to append the last three months of the year to the list months.
months = lst = (['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept'])
months.append("Oct")
months.append("Nov")
months.append("Dec")
print(months)

""" 
# First attempt below
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
"""

# FROM HERE ON ITS CONFUSING. I NEED TO WATCH SOME TUTORIALS..THE REST OF THESE EXERCISES SEEM TO BUILD ON ONE ANTOTHER

# 2) Get the index of "May" from the months list and print it on screen
month_index = months.index("May")
print(month_index)

# 3) Sort list3 from exercise 7.2 and print the results on screen  p.359
list3.sort()
print(list3)

# 4) Reverse the order of list3  p361
list3.reverse()
print(list3)

# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)
del list3[5]
print(list3)

# 6) Print the maximum value from list 3
print(max(list3))

# TODO 7.6 Copying Lists
print("=" * 10, "Section 7.6 copying lists", "=" * 10)
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year
months_of_the_year = months
print(months)

# TODO 7.7 Processing lists
print("=" * 10, "Section 7.7 processing lists", "=" * 10)
# 1) Total the values in list3 and print the results
total = 0
for item in list3:
    total += 3
    print("Total = " + str(total))

# 2) Get the average of values in list3 and print the results
print("Average = " + format(total / len(list3), ",.2f"))

# 3) Open the file states.txt in read mode,  p373
infile = open('states.txt', 'r')

# -- read the contents of the file into the list states_list
states_list = infile.readlines

# -- print the contents of states_list on screen
print(states_list)
infile.close()

# TODO 7.8 Two-Dimensional Lists
print("=" * 10, "Section 7.8 two-dimensional lists", "=" * 10)
# 1) Create a new two dimensional list that has the months of the year
#     and the days in each month during a non leap year
#     For example, the first entry should be: January, 31    p376

months_days = [['Jan', '31'], ['Feb', '28'], ['Mar', '31'], ['Apr', '30'], ['May', '31'], ['June', '30'],
               ['July', '31'], ['Aug', '31'], ['Sep', '30'], ['Oct', '31'], ['Nov', '30'], ['Dec', '31']]

# 2) Print the contents of the entire list
for item in months_days:
    print(item)

# 3) Print just the values for index 3,0 and 3,1
print(months_days[3][0], months_days[3][1])

# TODO 7.9 Tuples
print("=" * 10, "Section 7.9 tuples", "=" * 10)
# Create a tuple using the months list as its data source
months_tuple = tuple(months)
print(months_tuple)
