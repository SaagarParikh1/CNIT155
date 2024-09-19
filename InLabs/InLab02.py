#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30pm
# Your Purdue Email: Parikh62@purdue.edu
# Program Description: CNIT155 InLab02
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main():
    
    print('This is the InLab02 for CNIT155')
    print()
    
    #1. Number of students
    students = int(input('Enter the # of students: '))
    print(f'The # of students in CNIT 155 is {students}')
    print(f'The data type of students is {type(students)}')
    print()
    
    #2. Price of the textbook
    textbook = float(input('Enter the price of the textbook: '))
    print(f'The price of the textbook is ${textbook:.2f}')
    print(f'The data type of the price is {type(textbook)}')
    print()
    
    #3. Today's Temperature
    F = float(input('Enter today\'s temp in F: '))
    C = (F-32) * 5/9
    print(f'Today\'s temp in C: {C:.2f}C')
    print(f'The data type of the temp {type(C)}')
    print()

    #4. Average Speed
    Dist = float(input('Enter the distance travelled by the car in miles: '))
    Time = float(input('Enter the duration of the trip in hours: '))
    Avg = Dist/Time
    print(f'The average speed of the car for the trip is {Avg:.2f} miles/hour')
    print(f'The data type of speed is {type(Avg)}')
main()