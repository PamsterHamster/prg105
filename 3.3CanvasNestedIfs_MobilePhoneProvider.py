"""
customer_pkgA = A # 39.99 month to 450 min, .45 per addtl min
customer_pkgB = B # 59.99 month to 900 min, .40 per addtl min
customer_pkgC = C # 69.99 month unlimited min
"""

minutes_used = int(input(minutes_used))

# Calculate the package price with overtime
minutes_used > 450 < 900
total_costA = minutes_used - 450 * .45 + 39.99

minutes_used > 900
total_costB = minutes_used - 900 * .40 + 59.99

total_costC = 69.99

customer_pkg = int("Which phone package do you have, A, B or C? : ")
# Get the total month package price
if customer_pkg == "A" or "a":
    print("You have chosen Package A. The package price is 39.99 per month up to 450 minutes: ")

elif int("How many minutes were used? : "):
    print("You have entered " + str(input(minutes_used)) + "Minutes over 450 per month are charged .45 per minute. ")
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
    print("You have entered " + int(input(minutes_used)) + "Minutes over 900 per month are charged .40 per minute. ")
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
    print("Error. Please try again.")
