""" # INSTRUCTIONS: Write a program that asks the user for a number in the range of 1 through 7 etc"""

# display error message if Variable < 1 and >

# Get Variable_Input
DOWk = int(input("Please enter a number between 1 and 7: "))

if DOWk == 1:
    print("Monday")
elif DOWk == 2:
    print("Tuesday")
elif DOWk == 3:
    print("Wednesday")
elif DOWk == 4:
    print("Thursday")
elif DOWk == 5:
    print("Friday")
elif DOWk == 6:
    print("Saturday")
elif DOWk == 7:
    print("Sunday")
else:
    print("Error. That number is not in the correct range. ")
