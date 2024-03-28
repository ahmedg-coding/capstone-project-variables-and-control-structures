# The following program allows a user to access and use two different financial calculators: an investment calculator and a home loan repayment calculator.
import math

# Menu options which the user will first see when they run the program
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print()

# Obtaining the chosen option from user 
option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# if statement for checking whether input from user is valid 
if option == 'investment':
    # Obtain necessary input for investment calculation 
    amount_depositing = float(input("Please input the amount of money you are depositing: "))
    interest_rate = float(input("Please input the interest rate (as a percentage): "))
    num_years = int(input("Please input the number of years you plan on investing: "))
    interest = input("Would you like 'simple' or 'compound' interest? ").lower()

    # Converting the percentage of the interest rate inputted from user into a decimal 
    r = interest_rate / 100

    # Calculating total amount depending on the option chosen by user 'simple' or 'compound'
    if interest == 'simple':
        total_amount = amount_depositing * (1 + r * num_years)
    elif interest == 'compound':
        total_amount = amount_depositing * math.pow((1 + r), num_years)
    else:
        print("Sorry, input is not valid. Try again by only inputting either 'simple' or 'compound'")
        exit()

    # Result of calculation outputted to screen
    print(f"The total amount is: ${total_amount:.2f}")

elif option == 'bond':
    # Obtain necessary input for bond calculation 
    present_value = float(input("Please input the present value of the house: "))
    interest_rate = float(input("Please input the annual interest rate: "))
    num_months = int(input("Please input the number of months you plan to take to repay the bond: "))

    # Converting interest rate 
    i = (interest_rate / 100) / 12

    # Calculation for repayment(monthly)
    repayment = (i * present_value) / (1 - math.pow(1 + i, -num_months))

    # Result of calculation outputted to screen
    print(f"The amount of money you have to repay each month is: ${repayment:.2f}")

else:
    print("Sorry, input is not valid. Try again by only inputting either 'investment' or 'bond'")
