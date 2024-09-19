#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: Parikh62@purdue.edu
# Program Description: CNIT 155 InLab06 - This Python program displays a menu with five options and asks the user to select one of the options. Depending on the user’s choice, the program performs various computations. 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

#Define main
def main():
    
    option = 0
    
    while option != 4:
        #Print header
        print("***************************************************")
        print("                For Loops Lab                      ")
        print("***************************************************")
        print("")
        print("1. Display and add even natural numbers from 1 to N")
        print("")
        print("2. Multiplication table of N")
        print("")
        print("3. Print triangle of Numbers")
        print("")
        print("4. Exit")
        print("")
        print("***************************************************")
        
        #Allow user to pick function
        option = float(input("\n\nChoose one of the following options to perform: "))
    
         #Display even natural numbers, sum   
        if option == 1:
            N = float(input("Enter a natural number for N: "))
            print("Displaying even natural numbers from 1 to",N)
            Natnum = 2
            sum = 0
            while (Natnum<=N):
                print(Natnum)
                #Sum of even natural numbers
                sum = sum+Natnum
                Natnum = Natnum + 2  
            print("\n\nThe sum of even numbers from 1 to",N,"is ",sum)
            
            
        #Multiplication table for N    
        elif option == 2:
            N = int(input("Enter natural number for N: "))
            print("multiplication table of",N)
            Natnum = 1
            #Make sure the multiplication stops at 10
            while (Natnum!=11):
                multi = Natnum * N#
                print(N,"x",Natnum,"=",multi)
                Natnum = Natnum + 1 
             
            print()
            
        #Print triangle of numbers
        elif option == 3:            
            natnum = int(input("Enter a number of rows to print triangle of numbers: "))
            for i in range(1,(natnum+2)): #create digits
                for j in range(1,i):# create rows
                    print(j, end="");
                print()
                
     #Print goodbye - option 4         
    else:
        print("Good bye!")
        print()
    

            
                
main()
