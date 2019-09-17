# Write a program that calculates the amount of money a person would earn over a period of time if his or her
# salary is one penny the first day, two  pennies the second day, and continues to double each day. The program
# should ask the user for the number of days. Display a table showing what the salary was for each day, then
# show the total pay at end of the period. The output should be displayed in a dollar amount, not the number of pennies.

# Variables

# time (will hold number of days)

# SALARY (Constant, starting salary)
#
# total_earned(the accumulator)
#
# daily_income(the daily income)
#
# # PSEUDOCODE
# Time = int(input “ How many days did you work? “)
# Time +=1
#
# Print the header information
#
# for day in range (1, time)
# 	if day == 1
# 		daily_income = SALARY
# else
# 	daily_income *= 2
#
# total_earned + = daily_income

# print(format (day,  ‘5,d’) + ”     |   $” + format(daily_income, ’30, .2f’ ))

# Print the grand total at the bottom

## Variables
totalNum_pennies = 0
num_daysworked = int(input("How many days did you work? "))
payperday = .01

print ("Salary chart")

print( "Day\tSalary" )
for currentDay in range(num_daysworked):
    penniesFortheDay = 2 ** currentDay
    totalNum_pennies += penniesFortheDay
    print(currentDay + 1, "\t", penniesFortheDay)

totalPay = totalNum_pennies * .01
print( "total pay: ", totalPay )
