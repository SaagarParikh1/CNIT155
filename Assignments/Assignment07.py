#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30pm
# Your Purdue Email: parikh62@purdue.edu
# Program Description: CNIT155 Assignment07 - Display a menu and ask the user to select one of options.  
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

# Define function to display info
def displayMyInfo():
    # Print heading
    print("--------------------------------")
    print("|        Saagar Parikh         |")
    print("|    CNIT155 Assignment 07     |")
    print("|      Parikh62@purdue.edu     |")
    print("--------------------------------")
    print()
  
# Function to compute factorial
def factorial(n):
    # Compute n Factorial
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Find the maximum of 3 numbers
def maximumNo(a, b, c):
    # Determining the maximum of three given floats and returning it
    return max(a, b, c)

# Determine and Display the number of digits in a given number
def digits(n):
    # Determining the number of digits in a given positive integer using a while loop
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count 

# Define main function
def main():
    displayMyInfo()
    
    
choice = True
while choice:
    # Display the menu
    print("===================== User Defined Functions Menu ==================")
    print("1. Compute n Factorial")
    print("2. Find the Maximum")
    print("3. Find the number of digits")
    print("4. Exit")
    print("===================================================================")
    print()
    
    # Prompt user for menu selection
    choice = int(input("Choose one of the options to perform: "))

    if choice == 1:
        # Option 1: Compute n Factorial
        print("1. Compute n Factorial")
        n = int(input("Enter a natural number for N: "))
        print(n, "!=", factorial(n))
        print()

    elif choice == 2:
        # Option 2: Find the maximum of 3 numbers
        print("2. Find the Maximum")
        n1 = int(input("Enter the 1st number: "))
        n2 = int(input("Enter the 2nd number: "))
        n3 = int(input("Enter the 3rd number: "))
        print("The greatest number among the three numbers is: ", maximumNo(n1, n2, n3))
        print()
        

    elif choice == 3:
        # Option 3: Determine and Display the number of digits in a given number
        print("3. Find the number of digits")
        n = int(input("Enter a natural number for N: "))
        print("The number of digits in", n, "is:", digits(n))
        print()

    elif choice == 4:
        # Option 4: Exit
        print("Bye!")
        choice = False
        print()

    else:
        # Invalid selection
        print("Invalid option! Enter a number between 1 and 4")
        print()


# Call main function
main()
