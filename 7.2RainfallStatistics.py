# THIS IS 4.3MONTHLY RAINFALL COPIED FOR USE IN 7.2RAINFALL STATISTICS
# Write a program that uses nested loops to collect data and calculate the average rainfall over
# a period of years. The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop iterate 12 times, once for each month. Each iteration of the inner loop will ask the user for
# the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall, and the
# average rainfall per month for the entire period.

# HINT: Use nested loop statements and calculations with loops

# Variables
totalnum_months = 12
# monthly_rainfall_inches  # months = 12 * num_years
total_inches_rainfall = 0
avg_rainfall = total_inches_rainfall / totalnum_months

usernum_years = int(input("Enter the number of years:  "))

for current_year in range(1, usernum_years + 1):  # OuterLoop
    for current_month in range(1, 13):  # InnerLoop
        monthly_rainfall_inches = float(input("Type the inches of rainfall for month: " + format(current_month, "d")))
        # format d is str
        total_inches_rainfall += monthly_rainfall_inches
        totalnum_months += 1
avg_rainfall = total_inches_rainfall / totalnum_months
print("Number of months: " + format(totalnum_months, "d"),
      "Total inches of rainfall: " + format(total_inches_rainfall, ".2f"),
      "Average rainfall: " + format(avg_rainfall, ".2f"), sep="\n ")


# End 4.3

def get_rainfall_amount(names_of_months):
    totalnum_months = 12
    total_rainfall_list = []
    for current_month_index in range(13):
        monthly_rainfall = float(input("Please enter the rainfall amount for " + names_of_months[current_month_index]))
        total_rainfall_list.append(monthly_rainfall)

        return total_rainfall_list


def calculate_total_rainfall(total_rainfall_list):
    total_rainfall = 0

    for current_monthly_rainfall_index in range(len(total_rainfall_list)):
        total_rainfall = total_rainfall + total_rainfall_list[current_monthly_rainfall_index]

    return total_rainfall


# Functions

def calculate_avg_monthly_rainfall(total_rainfall, total_rainfall_list):
    num_months = len(total_rainfall_list)

    avg_rainfall = total_rainfall_list / num_months

    return avg_rainfall


def findhighest_rainfall_month(total_rainfall_list, names_of_months):
    highest_rainfall_amount = max(total_rainfall_list)
    highest_rainfall_amount_index = total_rainfall_list.index(highest_rainfall_amount)

    return names_of_months[highest_rainfall_amount_index]


def findlowest_rainfall_month(total_rainfall_list, names_of_months):
    lowest_rainfall_amount = max(total_rainfall_list)
    lowest_rainfall_amount_index = total_rainfall_list.index(lowest_rainfall_amount)
    return names_of_months[lowest_rainfall_amount_index]


def print_rainfallstatistics(total_rainfall_list, names_of_months, total_rainfall, avg_rainfall,
                             highest_rainfall_month, lowest_rainfall_month):
    # Create Loop
    for current_month_index in range(len(names_of_months)):
        print(names_of_months[current_month_index], "has a rainfall amount of ",
              total_rainfall_list[current_month_index])

    print("Total rainfall: " + str(total_rainfall),
          "Average rainfall: " + str(avg_rainfall),
          highest_rainfall_month + "has the highest rainfall. ",
          lowest_rainfall_month + "has the lowest rainfall.  ")
