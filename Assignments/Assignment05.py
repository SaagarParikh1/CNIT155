#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: Parikh62@purdue.edu
# Program Description: CNIT 155 Assignment05 - display a menu with five options and perform various computations depending on the user’s choice
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def main():
    
    option = ''

    while option != 'E':
        # print menu

        print("                 While Loops                   ")
        print("***********************************************")
        print("A. Sum of odd natural numbers from 1 to N")
        print("B. Sum of cubes of odd natural numbers from 1 to N")
        print("C. Check if N is a prime number")
        print("D. Print the multiplication table of N")
        print("E. Exit")
        print("***********************************************")
        print()
        
        # Enter an option
        option = input("Choose one of the following options to perform: ").upper()

        # if, else statement for chosen option
        if option == 'A':
            # odd natural numbers, sum 
            N = int(input("Enter a natural number for N: "))
            print(f"Displaying odd natural numbers from 1 to {N}")
    
            i = 1
            oddSum = 0
            while i <= N:
                print(i)
                oddSum += i
                i += 2
    
            # Display the sum 
            print()
            print("The sum of odd natural numbers from 1 to", N, "is:", oddSum)
            print()

            
        elif option == 'B':
            # cube of odd natural numbers
            N = int(input("Enter a natural number for N: "))
            print(f"Displaying the cubes of odd natural numbers from 1 to {N}")
        
            i = 1
            cubeSum = 0
            while i <= N:
                cube = (pow(i, 3))
                print(cube)
                cubeSum += cube
                i += 2
        
            # Display the sum of cubes
            print()
            print("The sum of cubes of odd natural numbers from 1 to", N, "is:", cubeSum)
            print()


        elif option == 'C':
            # Check if natural number N is a prime number
            N = int(input("Enter a natural number for N: "))
            
            # Check if N is greater than 1
            if N > 1:
                # Check for factors
                for i in range(2, int(pow(N, 0.5)) + 1):
                    if (N % i) == 0:
                        print(N, "is not a prime number")
                        break
                else:
                    print(N, "is a prime number")
                    print()
            else:
                print(N, "is not a prime number")    
                print()

        elif option == 'D':
            # Print a multiplication table for N
            N = int(input("Enter a natural number for N: "))
            
            print(f"Multiplication table of {N}:")
            for i in range(1, 11):
                result = N * i
                print(f"{N} x {i} = {result}")
                print()

        elif option == 'E':
            # print good bye
            print("Good Bye!")
            print()
            
        else:
            # print invalid input
            print("Invalid Input! Choose an option between A and E.")
            print()
            
main()