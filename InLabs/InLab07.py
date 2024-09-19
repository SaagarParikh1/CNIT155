#===============================================================
# Program Description: InLab07 - The user will be prompted to enter three sides of a triangle and check if the given numbers form a valid triangle.
#=================================================================
    
# Define function to display info
def displayMyInfo():
    # Print heading
    print("******************************")
    print("*        Saagar Parikh       *")
    print("*      Parikh62@purdue.edu   *")
    print("*        CNIT155 InLab07     *")
    print("******************************")
    print()
  
# Define a function to validate whether three sides can form a triangle
def validate(a, b, c):
    # Check the triangle inequality theorem to validate the sides
    if (a + b >= c) and (a + c >= b) and (b + c >= a):
        return True  # Valid triangle
    else:
        return False  # Invalid triangle

# Define function to compute and return the perimeter using Heron's formula
def computePerimeter(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Use Heron's formula to compute the perimeter
    perimeter = a + b + c
    return perimeter

# Define main function
def main():
    displayMyInfo()
    
    choice = True
    while choice == True:
        # Ask user the length of the sides of the triangle
        a = float(input("Enter the length of side A of a triangle: "))
        b = float(input("Enter the length of side B of a triangle: "))
        c = float(input("Enter the length of side C of a triangle: "))
        print()
        # Print validating triangle
        print("Validating a triangle...")
        print()
        
        # Validate whether the inputs can form a triangle
        if validate(a, b, c) == True:
            # If valid, compute the perimeter using computePerimeter function
            print("This is a valid triangle")
            perimeter = computePerimeter(a, b, c)  
            # Display the computed perimeter with two decimal places
            print(f"The perimeter of the triangle is: {perimeter:.2f}")
            print()            
            repeat = True
            
        else: #If triangle is not valid
            print("Inputs can not form a triangle. Please enter different numbers!")
            print()
            repeat = False
            
        while repeat == True:
            # Ask the user whether to compute again
            user_choice = input("Do you want to compute again? (Y/N): ")
            print()
            
            # Check user's choice to continue or end the program
            if user_choice == 'Y' or user_choice == 'y':
                choice = True
                repeat = False
            elif user_choice == 'N' or user_choice == 'n':
                choice = False
                print("End of the Program")
                break
            else:  # if invalid input entered
                print("Invalid Input")
                user_choice = input("Press Y or N, case-insensitive: ")
                repeat = True

# Call main function
main()
