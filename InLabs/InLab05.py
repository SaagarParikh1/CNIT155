#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: Parikh62@purdue.edu
# Program Description: CNIT 155 InLab05 - Ask user to choose options and display various computations.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def main():
    option = 0

    while option != 4:
        # print menu
        print("              While Loop Lab                   ")
        print("===============================================")
        print("1. Print all natural numbers between 1 and N")
        print("2. Display all even natural numbers from 1 to N. Compute their sum and average")
        print("3. Factorial of N")
        print("4. Exit")
        print()

        # Enter an option
        option = int(input("Choose one of the following options to perform: "))

        # if, else statement for chosen option
        if option == 1:
            N = int(input("Enter a natural number for N: "))
            print(f"Displaying natural numbers from 1 to {N}")
            i = 1
            while i <= N:
                print(i)
                i = i + 1
            print()

        elif option == 2:
            # even natural numbers, sum avg
            N = int(input("Enter a natural number (N): "))
            print(f"Displaying even natural numbers from 1 to {N}")

            i = 2
            evenSum = 0
            while (i <= N):
                print(i)
                evenSum = evenSum + i
                i = i + 2

            # Display the sum and average
            print()
            print("The sum of even numbers", N,  "is:", evenSum )
            print("The average of even numbers from 1 to", N,  "is:", evenSum/int(N/2))
            print() 
            
        elif option == 3:
            # factorial
            N = int(input("Enter a natural number (N): "))
            
            i = 1
            fact = 1
            while (i <= N):
                fact = fact * i
                i = i + 1

            # Display the factorial of N
            print(f"The factorial of" , N,  "is:", fact)
            print()

        elif option == 4:
            # print good bye
            print("Good Bye!")
            print()
            
        else:
            # print invalid input
            print("Invalid Input. Enter a number between 1 and 4.")
            print()
            
if __name__ == "__main__":
    main()
