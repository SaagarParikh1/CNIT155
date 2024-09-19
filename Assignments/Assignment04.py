#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: parikh62@purdue.edu
# Program Description: CNIT 155 Assignment04. Write program to find the roots of a quadratic equation.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

# Import math library
import math

# Define the main() function
def main():
    
    #Print header
    print("           ************************************************")
    print("           *            CNIT155 - Assignment 01           *")
    print("           *                                              *")
    print("           *             CNIT155 - Assignment 04           *")
    print("           ************************************************")    
    
    
    # Variables to store coefficients a, b, c
    a = float(input("Enter the coefficient a: "))  
    b = float(input("Enter the coefficient b: "))  
    c = float(input("Enter the coefficient c: "))  
    print()
    
    # Print Quadratic Equation with single decimal place
    print(f"Quadratic Equation: {a:.1f}x^2 + {b:.1f}x + {c:.1f}")
    print()
    
    # Compute discriminant D = b^2 - 4ac and store it in a variable
    D = pow(b, 2) - 4 * a * c

    # Display discriminant with three decimal places
    print(f"The Discriminant is: {D:.3f}")
    print()
    print()
    print('Calculating  the roots..............')
    print()
    # Check the value of D and print results
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print(f"The equation has two real roots: {root1:.3f} and {root2:.3f}")
        print()
    elif D == 0:
        root = -b / (2*a)
        print(f"The equation has one real root: {root:.3f}")
        print()
    else:
        print("The equation has no real roots")
        print()
    # Determine the minimum of coefficients a, b, c
    SC = min(a, b, c)
    print(f"The smallest coefficient is: {SC:.2f}")

main()
