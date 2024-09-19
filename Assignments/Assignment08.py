#===============================================================
# Program Description: Make 3 pre-defined lists that store 6 different item names, IDs, and prices for products sold in a store. Then, make 4 user-defined functions to perform certain tasks. 
#=================================================================

# Discount function
def Discount(lst):
    updated_prices = []  # Create an empty list to store updated prices
    for price in lst: 
        updated_price = price * 0.7  # Calculate the updated price after taking 30% off
        updated_prices.append(updated_price) 
    return updated_prices  # Return the list of updated prices

# PrintInfo function
def PrintInfo(lst1, lst2, lst3):
    for i in range(len(lst1)):  
        print("\t", lst1[i], "\t\t", lst2[i], "\t\t", "{:.2f}".format(lst3[i]))  # Print elements

# Average function
def Average(lst):
    total = sum(lst)  # Calculate the sum of prices
    avg = total / len(lst)  # Calculate the average price
    return avg  # Return the average price

# Search function
def Search(lst1, lst2, lst3, avg):
    for i in range(len(lst3)): 
        if lst2[i] <= avg:  # Check if the price is less than or equal to the average
            print("\t", lst1[i], "\t\t", lst3[i], "\t\t", "{:.2f}".format(lst2[i]))  # Print the name, ID, and price of the product
            
# Define main function
def main():
    # Define names, IDs, and prices
    Names = ["Paint Brush", "Sander", "Hand Drill", "Vac Cleaner", "Roller", "Chainsaw"]
    IDs = [3750, 4389, 3986, 9562, 1967, 2988]
    Prices = [12.99, 82.49, 117.89, 178.99, 57.49, 199.99]

    print("***************************************************************")
    print("=======================  Assignment 08  =======================")
    print("***************************************************************")

    # Call PrintInfo to display three lists
    print("\tName\t\t\tID\t\tPrice")
    print("================================================================")
    PrintInfo(Names, IDs, Prices)
    print()

    # Call Average
    avg_before_discount = Average(Prices)

    # Print the average value before discount
    print("***************************************************************")
    print("========================    Averages   ========================")
    print()
    print("The average of prices before the discount is ${:.2f}".format(avg_before_discount))
    print()
    print()

    # Call Discount
    discounted_prices = Discount(Prices)
    
    # Print after the discount
    print("***************************************************************")
    print("Prices have been adjusted!")
    print("\tName\t\t\tID\t\tPrice")
    print("================================================================")    
   
    # Print the adjusted prices
    PrintInfo(Names, IDs, discounted_prices)  
    
    # Call Average again with the discounted prices
    avg_after_discount = Average(discounted_prices)

    # Print the average value after discount
    print("***************************************************************")
    print("========================    Averages   ========================")
    print()
    print("The average of prices after the discount is ${:.2f}".format(avg_after_discount))
    print()
    print()
    
    # Call Search to display names, IDs, and prices of products with prices less than or equal to the average after discount
    print("==============    Products under <=${:.2f}".format(avg_after_discount),"   ==============")
    print("\tName\t\t\tID\t\tPrice")
    print("================================================================")    
    print("Products with prices less than or equal to the average after discount:")
    Search(Names, discounted_prices, IDs, avg_after_discount)    

# End main function
main()
