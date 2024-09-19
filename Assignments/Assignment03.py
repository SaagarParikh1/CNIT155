#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email:
# Program Description: CNIT 155 Assignment 03
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

#import and begin program
import math

def main():
    
    # UserInputs (D1, D2, W, L)
    D1 = float(input('Enter a value for Depth1 (D1): '))
    D2 = float(input('Enter a value for Depth2 (D2): '))
    
    #If else statement, check if D2 is greater than D1
    if D2 > D1:
        W = float(input('Enter a value for Width (W): '))
        L = float(input('Enter a value for Length (L): '))
        
        #break
        print()
        print('Calculating....')
        print()
            
        # Initialize and calculate variables (side area, bottom area, volume)
        D3 = D2 - D1
        SA = (D1 + D2) * L / 2
        BA = math.sqrt(pow(D3, 2) + pow(L, 2)) * W
        volume = SA * W

        # Print results
        print(f'The side area of the pool is: {SA:.2f}')
        print(f'The bottom area of the pool is: {BA:.2f}')
        print(f'The volume of the pool is: {volume:.2f}')
    else:
        print('Invalid Input! D2 must be greater than D1')
    
main()