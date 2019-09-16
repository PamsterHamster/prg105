"""
customer_pkgA = A # 39.99 month to 450 min, .45 per addtl min
customer_pkgB = B # 59.99 month to 900 min, .40 per addtl min
customer_pkgC = C # 69.99 month unlimited min
"""
"""
# Variables
minutes_used = str("minutes_used")

# Calculate the package price with overtime
minutes_usedA <= 450
total_costA = int(input(minutes_used)) - 450 * .45 + 39.99

0 < minutes_usedB > 900
total_costB = int(minutes_used)) - 900 * .40 + 59.99

minutes_usedC < 0
total_costC = 69.99

customer_pkg = int("Which phone package do you have, A, B or C? : ")
# Get the total month package price
if customer_pkg == "A" or "a":
    print("You have chosen Package A. The package price is 39.99 per month up to 450 minutes: ")

elif int("How many minutes were used? : "):
    print("You have entered " + str("minutes_usedA") + "Minutes over 450 per month are charged .45 per minute. ")
elif 1 < minutes_used <= 450:
    print("You are within the allocated monthly minute range. Your bill this month is 39.99 ")
elif minutes_used >= 451:
    print("Oops! You are over your monthly allocation. The charge this month will be " + format(
        total_costA == minutes_used - 450 * .45 + 39.99, " .2f"))
    print(format(total_costA, ".2f"))
    print("Please pay the above amount ")

if customer_pkg == "B" or "b":
    print("You have chosen Package B. The package price is 59.99 per month up to 900 minutes: ")

elif int("How many minutes were used? : "):
    print("You have entered " + str("minutes_usedB") + "Minutes over 900 per month are charged .40 per minute. ")
elif 1 < minutes_used <= 900:
    print("You are within the allocated monthly minute range. Your bill this month is 59.99 ")
elif minutes_used >= 900:
    print("Oops! You are over your monthly allocation. The charge this month will be " + format(
        total_costB == minutes_used - 900 * .40 + 59.99, " .2f"))
    print(format(total_costA, ".2f"))
    print("Please pay the above amount ")

if customer_pkg == "C" or "c":
    print("You have chosen Package C. The package price is 69.99 with unlimited minutes: ")
    print("Please pay 69.99 ")

else:
    print("Error. Please try again.") """

# CORRECTED VERSION 10 SEPTEMBER 2019
package = input("Which package do you have? A, B, C: ")
print("You entered Package " + package)
# minutes_used = int(input("How many minutes did you use this month? "))

if package == "A" or package == "a":
    package_price = 39.99
    minutes_used = int(input("How many minutes did you use this month? "))
    if minutes_used > 450:
        additional_minutes = minutes_used - 450
        minutes_cost = additional_minutes * .45
        total_cost = package_price + minutes_cost
        print("With package " + package + "and " + str(minutes_used) + " minutes used, you owe: $" + format(total_cost,
                                                                                                            ".2f"))

    else:
        print(
            "With package " + package + "and " + str(minutes_used) + " minutes used, you owe: $" + format(package_price,
                                                                                                          ".2f"))
elif package == "B" or package == "b":
    package_price = 59.99
    minutes_used = int(input("How many minutes did you use this month? "))
    if minutes_used > 900:
        additional_minutes = minutes_used - 900
        minutes_cost = additional_minutes * .40
        total_cost = package_price + minutes_cost
        print("With package  " + package + "and " + str(minutes_used) + " minutes used, you owe: $" + format(total_cost,
                                                                                                             ".2f"))
elif package == "C" or package == "c":
    print("You owe 69.99.")

""" 
     print("With package  " + package + "and " + str(minutes_used) + " minutes used, you owe: $" + format(package_price,
                                                                                                   ".2f"))"""
"""elif package == "C" or "c":
    print("You owe 69.99 ")"""

# revised Sep16 2019

