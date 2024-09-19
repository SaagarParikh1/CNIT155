#===============================================================
# Program Description: This program calculates the total miles walked over a week based on daily steps input by the user. 
#=================================================================

#define steps to miles conversion function
def StepsToMiles(lst):
    miles = [steps / 2000 for steps in lst]  # 1 mile = 2000 steps
    return miles

#define main function
def main():
    # Print header
    print("************************************************")
    print("**********                            **********")
    print("**********  Step to Miles Calculator  **********")
    print("**********                            **********")
    print("************************************************")
    print()
    #create new list
    count = 0
    stepslst = []
    
    while len(stepslst) < 7:
        day = len(stepslst) + 1
        try:
            steps = int(input(f"Enter the number of steps for Day {day}: "))
            if steps < 0:
                raise ValueError            
            stepslst.append(steps)
        except ValueError:
            print()
            print("Exception: wrong value entered")
            print("Please enter an integer value in a correct format!")
            print()

    # Convert steps to miles
    miles_walked = StepsToMiles(stepslst)

    # Display miles walked each day
    print("*** The number of miles you walked this week ***")
    for day, miles in enumerate(miles_walked, 1):
        print(f"Day {day}: {miles:.2f} miles")

    # Calculate and display average miles walked
    average_miles = sum(miles_walked) / len(miles_walked)
    print()
    print(f"The average of miles walked: {average_miles:.2f}")
    print()

    # Program end message
    print("End of the program")

#end program
main()
