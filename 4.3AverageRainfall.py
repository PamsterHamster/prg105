# Write a program that uses nested loops to collect data and calculate the average rainfall over
# a period of years. The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop iterate 12 times, once for each month. Each iteration of the inner loop will ask the user for
# the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall, and the
# average rainfall per month for the entire period.

# HINT: Use nested loop statements and calculations with loops

# Variables
totalNumberOfMonths = 12
#monthly_rainfall_inches  # months = 12 * num_years
totalinches_rainfall = 0
avg_rainfall = totalinches_rainfall / totalNumberOfMonths

usernum_years = int( input( "Enter the number of years: " ) )

for currentYear in range( 1, usernum_years + 1 ):  #OuterLoop
    for currentMonth in range(1, 13 ):   #InnerLoop
        monthly_rainfall_inches = float( input("Type the inches of rainfall for month " + format( currentMonth, "d")))  #format d is str
        totalinches_rainfall += totalinches_rainfall
        totalNumberOfMonths += 1
avg_rainfall = totalinches_rainfall / totalNumberOfMonths
print("Number of months: " + format(totalNumberOfMonths, "d"),
       "Total inches of rainfall: " + format(totalinches_rainfall, ".2f"),
       "Average rainfall: " + format(avg_rainfall, ".2f"), sep="\n ")



