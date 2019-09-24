# Write Rubric here
# Write a program that asks the user to enter monthly costs from his/her automobile: loan payment, insurance, gas
# and maintenance. Display the total monthly cost of these expenses and total annual cost of these expenses.

def askForExpenses():
    monthlyLoanPayment = float( input("How much do you pay for your monthly loan?: " ) )
    monthlyInsurancePayment = float( input("How much do you pay for your monthly insurance?: " ) )
    monthlyGasPayment = float( input("How much do you pay for your monthly gas?: " ) )
    monthlyMaintenancePayment = float( input("How much do you pay for your monthly maintenance?: " ) )

    return monthlyLoanPayment, monthlyInsurancePayment, monthlyGasPayment, monthlyMaintenancePayment

def calculateTotalMonthlyCost( payment1, payment2, payment3, payment4 ):
    totalMonthlyCost = payment1 + payment2 + payment3 + payment4
    return totalMonthlyCost

def calculateTotalAnnualCost( totalMonthlyCost ):
    TotalAnnualCost = totalMonthlyCost * 12
    return TotalAnnualCost

def printDetails( totalMonthlyCost, TotalAnnualCost ):
    print( "Your total monthly cost is $" + format( totalMonthlyCost, ",.2f") + \
           "\nYour total annual cost is $" + format( TotalAnnualCost, ",.2f") )

def main():
    monthlyLoanPayment, monthlyInsurance Payment, monthlyGasPayment, monthlyMainenancePayment = askForExpenses():

    totalMonthlyCost = calculateTotalMonthlyCost( monthlyLoanPayment, monthlyInsurance Payment, monthlyGasPayment, monthlyMaintenancePayment ):

    TotalAnnualCost = calculateTotalAnnualCost( totalMonthlyCost )

    printDetails( totalMonthlyCost, TotalAnnualCost )

main()



"""
# Variables--make all money ones floats
monthly
    loan
    insurance
    Gas
    maintenance
    monthly_cost

# Steps
Get user input
calculate total
print formatted total

call yearly, pass monthly_cost

# Variables --argument variable of month_total
yearly
    calculate yearly cost  (multiply by 12 months)
    Display main()

# Group steps into logical functions (Data entry together, calculations all together)
"""
