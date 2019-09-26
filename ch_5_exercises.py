"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import random
import math

# TODO 5.2 - calling an existing function
print("=" * 10, "Section 5.2 call an existing function", "=" * 10)


# Beneath the following function, write the code to call it
# Remove the """ """ before testing
# Note: Python requires two blank lines before a function definition
# Define the function named greeting


def message():
    print("Hello, ")
    print("Sweetie!")


# Write the code to call the hello function on the next line
message()

# TODO 5.2 - creating and calling a function
print("=" * 10, "Section 5.2 create and call an existing function", "=" * 10)


# Write a function called joke that prints a joke on the screen
# Call the function


def joke():
    print("Why was six scared of seven? ")
    print("Because seven ate nine. ")


joke()

# TODO 5.3 designing a program in functions
print("=" * 10, "Section 5.3 design a program using functions", "=" * 10)


# Create a main function that will call separate functions that
# print each line in a knock knock joke. Make sure to call main
# as the last line of your code.
# I'm a music geek so here you go:
# Knock, knock!
# Who's there?
# Cymbals.
# Cymbals who?
# Cymbals have horns and others don't!


def main():
    # Display the purpose of this exercise
    startup_message()
    input("Press Enter to see the first line of joke. ")
    # Display first line joke
    line1()
    input("Press Enter to see the second line of joke. ")
    # Display second line joke
    line2()
    input("Press Enter to see the third line of joke. ")
    # Display the third line joke
    line3()
    input("Press Enter to see the fourth line of joke. ")
    # Display the fourth line joke
    line4()
    input("Press Enter to see the fifth line of joke. ")
    # Display the fifth line joke
    line5()


def startup_message():
    print("This program tells you ")
    print("a very corny knock knock joke. ")
    print("There are five lines of joke before you groan. ")
    print()

    # Line 1 introduces the joke


def line1():
    print("Knock ")
    print("knock ")
    print()


# Line 2 answers line 1
def line2():
    print("Who's ")
    print("there? ")
    print()


# Line 3 answers line 2


def line3():
    print("Cymbals. ")
    print()


def line4():
    print("Cymbals, ")
    print("who? ")
    print()


def line5():
    print("Cymbals have horns ")
    print("and others don't! ")


# Call the main function to begin the program
main()

# TODO 5.4 local variables
print("=" * 10, "Section 5.4 using local variables", "=" * 10)


# 1) Write a program with a main2 function. In main2, define a variable
#    called name and assign a name to it, then print hello
#    and the name variable. Have main2 call a second function get_name().
# 2) In the get_name function, ask the user for their name,
#    then greet them using a print statement.
# 3) Call the main2 function.
# Note - you would not normally have more than one main function
# in a program, we are just adding the number after main to allow
# us to write multiple short practice programs in a single file.

def main2():
    name = "Squiggly"
    print("Hello " + name)
    get_name()


# Definition of the get_name function
def get_name():
    name = input("Enter your name: ")
    print("Hey there " + name)


# Call the main function

main2()

# TODO 5.5 passing arguments to Functions
print("=" * 10, "Section 5.5 passing arguments", "=" * 10)


# Complete the code below to pass the my_number variable value from
# main3() into square() using a parameter name of value.
# Remove the """ """ before testing

def main3():
    # Call the my_number3 function.
    my_number = 7
    # Call the square function
    square(my_number)


def square(number):
    result = number * number
    print(result)


main3()


# Definition of the my_number function
def main4():
    num_one = 5
    num_two = 7
    add(num_one, num_two)


def add(one, two):
    total = one + two
    print(total)


# Call the main function
main4()

# TODO 5.5 passing multiple arguments
print("=" * 10, "Section 5.5 passing multiple arguments", "=" * 10)


# Complete the code below to pass the variables from main into
# parameters for add. Look at the code to determine the correct
# variable / parameter names. Remove the """ """

# total = one + two
# print(total)

# Call the main function


main4()

"""
def main():
    num_one = 5
    num_two = 7
    add(num_one, num_two)


def add(one, two):
    total = one + two
    print(total)


# Call the main function
main4()
"""

# TODO 5.7 value returning functions
print("=" * 10, "Section 5.7 value returning functions", "=" * 10)
# import random - Add a statement importing the random library at the top of this file
# Add a global constant PI with a value of 3.14 before the main5 function definition

PI = 3.14


# Import the random library

# import random
# import math

def main7():
    # Get a random number

    r = random.randint(1, 10)
    r2 = r * r
    # Display the number
    area(r2)
    # print("The number is", number_r) Note: When I try to put into """ form (my first attempt) everything turns green! Why?


def area(radius_squared):
    # my_area = PI * radius _squared
    my_area = PI * radius_squared
    print(format(my_area, ",.2f"))


main7()

# TODO 5.8 value returning functions
print("=" * 10, "Section 5.8 value returning functions", "=" * 10)


# Complete the following program, remove the """  """ before testing


def main6():
    # Get the user's physical information

    print("This program will calculate your BMI")
    height = float(input("What is your height in inches?  "))
    weight = float(input("What is your weight in pounds? "))

    # TODO call the bmi function and assign the result to a variable named answer
    my_answer = bmi(height, weight)
    # TODO print the variable answer, make sure to format it to 1 decimal place
    print(format(my_answer, ",.1f"))
    # TODO modify the bmi function to accept the height and weight
    # read the code to determine the parameter names


def bmi(height_inches, weight_pounds):
    # BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
    patient_bmi = (weight_pounds / (height_inches * height_inches)) * 703
    # TODO send the patient_bmi value back to main6
    return patient_bmi


main6()

# TODO 5.9 the math module
print("=" * 10, "Section 5.9 use the math module", "=" * 10)
# import math - Add the import math statement at the top of this file
# Write a statement that uses the ceil function on the following variable
# Display the result
number_to_round = 4.243
# My Attempt
print(math.ceil(number_to_round))
# Call the main function
