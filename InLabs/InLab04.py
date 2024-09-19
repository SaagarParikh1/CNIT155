#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: parikh62@purdue.edu
# Program Description: CNIT 155 InLab04 Python program displays a menu with two options and asks the user to select one of the options. Depending on the user’s choice, the program takes the user’s input and calculates simple interest and compound interest
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================]

import math

# Define the main() function
def main():
    
    # Display the menu
    print('================MENU===================')
    print()
    print('          INTEREST CALCULATOR          ')
    print('=======================================')
    print('A. Simple Interest Calculator')
    print('B. Compound Interest Calculator')
    print('=======================================')
    print()
    
    # Prompt the user to select a menu option (A or B)
    user_choice = input("Select one of the following options to calculate the interest: ").upper()

    # Check the user's choice using an if-else statement
    if user_choice == 'A':
        print("You chose option A. Simple interest calculator")
        
        # Prompt the user for input
        P = float(input("Enter the principal amount: "))
        t = int(input("Enter the time period in years: "))
        r = float(input("Enter the interest rate in percentage %: "))

        # Calculate simple interest
        A = P * (1 +  ((r * t) / 100))

        # Display the result for SI
        print(f"The final amount in simple interest is: ${A:.2f}")

    elif user_choice == 'B':
        print("You chose option B. Compound interest calculator ")
        
        # Prompt the user for input
        P = float(input("Enter the principal amount: "))
        t = int(input("Enter the time period in years: "))
        r = float(input("Enter the interest rate in percentage %: "))
        n = int(input("Enter the number of terms per year: "))

        # Calculate compound interest
        A = P * math.pow(1 + (r / (100 * n)), n * t)

        # Display the result for CI
        print(f"The final amount in compound interest is: ${A:.2f}")
        
    # If neither correct options were selected
    else:
        print("Invalid input!")
        print("Please choose either A or B.")

# Call main() to start the program
main()
