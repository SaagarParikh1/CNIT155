#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: parikh62@purdue.edu
# Program Description: CNIT155 InLab08 - Allow users to enter students’ GPAs and compute the average of entered GPAs
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

# Define the main function
def main():
    # Enter the number of students in the class
    n = int(input("How many students are there in your class?: "))
    
    # Create two empty lists to store students names and GPAs
    Names = []
    Gpa = []    
    
    # Loop to get names and GPAs and add them to the lists
    for i in range(n):
        name = input("Input student #{} name: ".format(i+1))
        gpa = float(input("Input student #{} GPA: ".format(i+1)))
        
        # Check if GPA is valid (between 0 and 4.0)
        while gpa < 0 or gpa > 4.0:
            print("A GPA must be between 0 and 4.0 (both inclusive)!")
            print()
            gpa = float(input("Input student #{} GPA: ".format(i+1)))
        
        # Append name and GPA 
        Names.append(name)
        Gpa.append(gpa)
    
    # Print entered students' names and GPAs 
    print("====================== List ==========================")
    print("              Name\t\t\tGPA")
    print("            -----------\t\t\t----------                   ")
    for i in range(n):
        print("            {}\t\t\t{:.2f}".format(Names[i], Gpa[i]))
    
    # Calculate the sum of GPAs
    gpa_sum = sum(Gpa)
    
    # Calculate the average of GPAs
    gpa_avg = gpa_sum / n
    
    # Find the maximum and minimum values
    gpa_max = max(Gpa)
    gpa_min = min(Gpa)
    
    # Print the average, maximum, and minimum of entered GPAs
    
    print("===========================================================")
    print("The average of entered GPAs is {:.2f}".format(gpa_avg))
    print("The Maximum GPA is {:.2f}".format(gpa_max))
    print("The Minimum GPA is {:.2f}".format(gpa_min))
    print("===========================================================")

# Call the main function 
main()

    
    
    