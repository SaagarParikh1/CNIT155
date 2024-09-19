#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: parikh62@purdue.edu
# Program Description: CNIT155 InLab09 - This Python program allows users to enter prices in US dollars and converts them to Yuan
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified. 
# I have not given other fellow student(s) access to my program.
#=================================================================

def UsdtoYuan(lst):
    # Make a blank list to store Yuan equivalents
    yuan_list = []
    # Convert USD to Yuan 
    for i in lst:
        # Multiply each USD value by the exchange rate and append to the Yuan list
        yuan_list.append(i * 7.21)
    # Return the list of Yuan equivalents
    return yuan_list

# Function to print lst1 and lst2
def PrintInfo(lst1, lst2):
    # Print header
    print("     USD($)          Yuan(¥)     ")
    print("#################################")
    for i in range(len(lst1)):
        # Print the elements 
        print(f'     {lst1[i]:.2f}          {lst2[i]:.2f}')
        
def Average(lst):
    # Calculate the sum
    sum_lst = sum(lst)
    # Calculate the average
    avg = (sum_lst / len(lst))
    # Return the average
    return avg    
    
def FindPrice(lst1, lst2):
    # Print header
    print("#########Price(s) under $70#########")
    print("     USD($)          Yuan(¥)     ")
    print("   ---------       ----------    ")    
    # Loop through lists 
    for i in range(len(lst1)):
        # If value is less than $70, print it along with its Yuan equivalent
        if lst1[i] < 70:
            print(f'     {lst1[i]:.2f}          {lst2[i]:.2f}')   
    
def main():
    # Declare lists to store USD and Yuan prices
    usd_lst = []
    yuan_lst = []
    
    while True:
        price = input("Enter a price in USD. Use NN or nn to stop data entry: ")
        if price.lower() == 'nn':
            break
        else:
            usd_lst.append(float(price))
            
    print('\nNumber of prices entered: ', len(usd_lst)) 
    print()
    
    # Get Yuan conversion using the UsdtoYuan function
    yuan_lst = UsdtoYuan(usd_lst)
    
    # Display USD and Yuan prices using the PrintInfo function
    PrintInfo(usd_lst, yuan_lst)
    
    # Display header for average prices
    print("\n#################################")
    print("############ Averages ##########")
    
    # Calculate and display average prices in USD and Yuan
    print(f"The average of the prices in USD is ${Average(usd_lst):.2f}")
    print(f"The average of the prices in Yuan is ¥{Average(yuan_lst):.2f}")    
    print()
    # Display prices under $70 and their Yuan equivalents using the FindPrice function
    FindPrice(usd_lst, yuan_lst)
    
# Call the main function to run the program
main()
