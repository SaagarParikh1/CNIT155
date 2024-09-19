#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30pm
# Your Purdue Email: Parikh62@purdue.edu
# Program Description: CNIT155 Assignment02
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main():
    
#Part 1
    print("           ************************************************")
    print("           *            CNIT155 - Assignment 01           *")
    print("           *                                              *")
    print("           *             Conversion Calculator            *")
    print("           ************************************************")
    
    name = input('Enter your full name: ')
    print(f'My name is {name}')    
    print()
#Part 2
    print("** 1st. Pounds to Kilograms conversion **")
    P = float(input('Enter the weight in pounds to convert it to kilograms: '))
    Kg = P/2.2046
    print(f'The weight entered in pounds is {P:.2f} lbs and it is {Kg:.2f} kg')     
    print()
#Part 3
    print("** 2nd. Celcius to Farenheit conversion **")
    C = float(input('Enter the Celcius temperature to convert it to Farenheit: '))
    F = (C * 9/5) + 32
    print(f'The entered temperature in Celcius is {C:.2f} C and it is {F:.2f} F') 
    print()
#Part 4
    print("** 3rd. Miles to Kilometers conversion **")
    Miles = float(input('Enter miles to convert it to kilometers: '))
    Km = Miles * 1.609344
    print(f'The entered distance in miles is {Miles:.2f} mi and it is {Km:.2f} km') 
    print()
#Part 5
    print("** 4th. Yards to Meters conversion **")
    Yards = float(input('Enter yards to convert it to meters: '))
    Meters = Yards * 0.9144
    print(f'The entered distance in yards is {Yards:.2f} yd and it is {Meters:.2f} m') 
    print()
#Part 6
    print("** 5th. Feet and Inches to Centimeters conversion **")
    print("What is your height in feet and inches?")
    Feet = float(input('Feet?: '))
    Inches = float(input('Inches?: '))
    Cm = (Inches + (Feet*12)) * 2.54
    print(f'The entered height is {Feet} feet {Inches} inches and is {Cm:.2f} cm') 
    print()
main()