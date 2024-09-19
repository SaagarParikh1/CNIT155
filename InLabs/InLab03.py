#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: Parikh62@purdue.edu
# Program Description: CNIT 155 InLab03 - using formulas to find the volume, lateral area, and surface area of a truncated cone
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

import math

def main():
    #Print Header
    print('                    Properties of a Truncated Cone')
    print('                    ------------------------------')
    
    #UserInputs (r1, h, s, r2)
    r1 = float(input('Enter radius 1 (r1) of a cone: '))
    h = float(input('Enter height of a cone: '))
    s = float(input('Enter slant height of a cone: '))
    r2 = float(input('Enter radius 2 (r2) of a cone: '))
    print()
    print('______________________________________________')
    print()
    
    #Initialize and calculate variables (volume, lateral area, surface area)
    volume = 1/3 * math.pi * h*(pow(r1, 2) + pow(r2, 2) + r1*r2)
    latArea = s * math.pi * (r1 + r2)
    surfArea = latArea + math.pi*(pow(r1, 2) + pow(r2, 2))
    
    #Print results
    print('Calculating...')
    print()
    print(f'The volume of the truncated cone is: {volume:.2f}')
    print(f'The lateral area of the truncated cone is: {latArea:.2f}')
    print(f'The surface area of the truncated cone is: {surfArea:.2f}')
    
    
main()