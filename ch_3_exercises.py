
"""Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 3.1 Relational Operators
print("=" * 10, "Section 3.1 relational operators", "=" * 10)
# 1) Write a statement using the variables below and a
#    and a greater-than sign that will evaluate to true.
#    write a print statement with the statement in parentheses.
# 2) Write a statement using the variables below that
#    compares two of the variables to see if they are equal
#    write a print statement with the statement in parentheses.
# 3) Write a statement using the variables below that compares
#    two of the variables below to see if they are not equal
#    write a print statement with the statement in parentheses.
# 4) Write a statement using the variables below that uses
#    the less than or equal to operator
#    write a print statement with the statement in parentheses.

# variables
a = 6
b = 8
c = 5

# 1 sample answer
print(a > 3)
# 1_Answer
print(b > 4)

# 2_Answer
input(c == b)
print(a == b)

# 3_Answer
input(b != c)
print(b != c)

# 4_Answer
input(c <= a)
print(c  <= a)

# TODO 3.2 the if else statement
print("=" * 10, "Section 3.2 if-else", "=" * 10)
# Add code below to determine if age is greater than or equal to 18
# Depending on the answer, display the appropriate statement:
#    "You are old enough to vote" or "You are not old enough to vote"
# Use the if-else structure
age = int(input("How old are you? "))
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")

# TODO 3.3 comparing strings
print("=" * 10, "Section 3.3 comparing strings", "=" * 10)
# Complete the code below so that if the user input matches the password
# it will display "that is correct" otherwise display "that is not correct"
password = "narwhals"
user_password = input("Please enter the password:  ")

user_password = int(input("Please enter the password: "))
if user_password == narwhals:
    print("You are correct. Please proceed to the next step")
else:
    print("That is not correct.")

# TODO 3.4 if - elif - else
print("=" * 10, "Section 3.4 if-elif-else", "=" * 10)
# Complete the code to accept a number between 1 and 5 from the user
# and display a roman numeral for that number. If the number entered is
# not between 1 and 5, have the else statement display "That is not a valid number"

# Variables
number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5

number = int(input("Please enter a number between 1 and 5: "))
if number ==1:
    print("That is not a valid number")
elif number ==2:
    print("II")
elif number ==3:
    print("III")
elif number ==4:
    print("IV")
elif number >= 5:
    print("That is not a valid number")

# TODO 3.5 a series of conditions
print("=" * 10, "Section 3.5 multiple conditions", "=" * 10)
# Buffet prices are based on the persons age. If the person is a senior
# citizen (62 or over) , the charge is $9.89. If the person is age 12-
# 61, the charge is $12.89. If it is a child of under age 3, they eat
# for free. If the child is between 4 and 11 they are charged $0.99 for
# each year of age. Complete the code below. SEE SAMPLE PAGE 132

# NOTE: You cannot search the etextbook by page number, so I cannot see this example :(
# Variables of starting ages
SENIOR = 62
Regular = 12 to 61
Medium child = 4 to 11
Small child = 3 and under

# Variables of Price per person
SENIOR = $9.89
Regular = $12.89
Medium child A age 4 = $.99
Medium child B= age 5 and up is $.99 + $ .99 for each year old
Small child = $0

#If-then statements
# Input
SENIOR age >=62 then price $9.89
Regular age >=12 <=61 then price $12.89
Medium child A age ==4 then price $.99
Medium child B age > 4 < 12 then price $.99 *each year < 12
Small child age > 0 < 4

customer_age = int(input("How old is the customer?   "))
cost = 0  # initializing cost, assign the correct price to this variable
# Complete the code here to determine the correct cost based on age

age = int("How old is the customer : ")
# Determine the price
if age >=62
    print("Your cost for a customer who is " + str(customer_age) + " years old")
    print("is $9.89")

else:
    if age >= 12 <= 61
    print("Your cost for a customer who is " + str(customer_age) + " years old")
    print("is $12.89")

    else:
        if age > 4 < 12 then format(INSERT FORMULA)
        print("Your cost for a customer who is " + str(customer_age) + " years old")
            print("is + format(.99 + 11 - customer_age, ",.2f"))

        else:
            if customer_age ==4
            print("Your cost for a customer who is " + str(customer_age)) + " years old")
            print("is + $.99")

                else:
                    if age >= 0 <= 3
                    print("Your price is $0. Eat for free!")

# Output, correctly formatted -- leave this code to display the result
print("Your cost for a customer who is " + str(customer_age) + " years old")
print("is $" + format(cost, ",.2f"))

# TODO 3.5 Logical Operators
print("=" * 10, "Section 3.5 logical operators", "=" * 10)
# Using the variables below, combine relational comparisons using logical operators
# 1) write a print statement using the and operator that will evaluate to true
# 2) write a print statement using the or operator that will evaluate to true
# 3) write a print statement using the not operator that will evaluate to true
d = 10
e = 10
f = 12
# 1_Answer
if d == e and f > d:
print("d is equal to e and f is greater than d")

# 2_Answer
if e < f or d > f :
    print("e is less than f or d is greater than f ")

# 3_Answer
if not(f >= d or e):
    print("if f is greater than or equal to d or e then I am almost finished with this exercise")

# TODO 3.6 Boolean variable
print("=" * 10, "Section 3.6 boolean variables", "=" * 10)
# You are programming a baby doll. If the baby doll is tired, it will close its eyes
# if it is hungry, it will cry. Write code to print  "Eyes open" or "Eyes closed" depending
# on the tired value. Then print "Crying" or "quiet" depending on the hungry variable

tired = True
hungry = False
# Variables
tired == close eyes
hungry == crying
tired + hungry == close eyes and crying
not tired = eyes open
not hungry = quiet
not hungry or tired = quiet and eyes open

if(baby == tired):
    print("Eyes closed ")
if (baby != tired):
    print("Eyes open ")

    if(baby == hungry):
        print(Crying)
    if(baby != hungry):
        print("Quiet ")

            if(baby tired and hungry):
                print("Eyes closed and crying ")

                if(baby not(hungry or tired):
                    print("The baby is quiet and the eyes open")



































