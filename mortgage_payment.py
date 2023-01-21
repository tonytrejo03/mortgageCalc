# Anthony Trejo
# CPSC 21000 002
# Mortgage Payment - In this program we will calculate your
# monthy payment for your mortgage.
'''
Algorithmn:
Heading and instructions
ask user for cost_of_the_home
ask user for down_payment
ask user for interest_rate
ask user for length_of_loan_years
'''

# constant
INTRODUCTION = '''
******************************************************
           Home Mortgage Payment Calculator
******************************************************

In this program, we will calculate the
monthly mortgage payment of your house
or future house. You will start of by
entering the cost of your house, the
down payment, the interest rate, and
the length of the loan. Just a heads up,
if the down payment is less than 20%, there
will be a fee of $100 per month for the
mortgage insurace. Please enter the
information below.
'''
print(INTRODUCTION)

import math

# Asking user for data
cost_of_the_home = float(input("Enter the cost of the house: "))

down_payment = float(input("Enter the down payment of the house: "))

if down_payment < 0.2 * cost_of_the_home:
    insurance_fee = 100
    print("It looks like you'll have a fee of $100 per month for mortgage insurance.")
else:
    insurance_fee = 0
    print("No insurance fee will be applied.")
    
interest_rate = float(input("Enter annual interest rate: "))

intrate = interest_rate/100

length_of_loan = float(input("Enter the length of loan in years: "))

months = length_of_loan*12

payment = ((intrate/12) * (cost_of_the_home-down_payment))/( 1 - pow(1+(intrate/12),-months))
# payment = (intrate/12) * (1/(1-(1+intrate/12)**(-months)))*(cost_of_the_home-down_payment)

loan_amount = cost_of_the_home - down_payment

print("\n")

# Summary
print("Here is the summary of the loan: ")
print("%-15s%10.2f" % ("Loan amount:         $",loan_amount))
print("%-15s%10.2f" % ("Annual interest rate $",interest_rate))
print("%-15s%10.2f" % ("Number of years      $",length_of_loan))
print("%-15s%10.2f" % ("Monthly mortgage     $", payment))
print("%-15s%10.2f" % ("Mortgage insurance   $", insurance_fee))
print("%-15s%10.2f" % ("Total per month      $", payment+ insurance_fee))

# Constant
THANKS = '''
*********************************************************
    Thank you for using monthly mortgage calculator
*********************************************************
'''
print(THANKS)





