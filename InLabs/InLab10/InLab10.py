#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: parikh62@purdue.edu
# Program Description: CNIT155 InLab10 - write a program to practice reading and writing to a text file
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#================================================================

#Define Main function
def main():
    try:
        # Open the 2 files
        inputFile = open("scores.txt", "r")
        outputFile = open("scores_stat.txt", "w")
        
        # Read the contents of the input file
        scores = inputFile.readlines()
        
        # Convert the numeric items in the list from strings to floats
        scores = [float(score.strip()) for score in scores[3:]]
        
        # Printing the contents of the scores list 
        print("Printing the contents of the file...")
        print()
        print(scores)
        
        # Calculating statistical data: maximum, minimum, average, and list length
        maximim= max(scores)
        minimum = min(scores)
        average = sum(scores) / len(scores)
        length = len(scores)
        
        # Writing output of these calculations
        outputFile.write("The number of scores in the list is " + str(length) + "\n")
        outputFile.write(f"The average of scores int he list is {average:.2f}\n")
        outputFile.write(f"The Maximum score is {maximim}\n")
        outputFile.write(f"The Minimum score is {minimum}\n")
        
        
        # Closing both files
        inputFile.close()
        outputFile.close()
        
    except FileNotFoundError:
        # Informing the user if the input file doesn't exist
        print("This program failed to open the file. Make sure of the following:")
        print("\tThe file to read is located in the same folder where this program is!")
        print("\tThe file's name is spelled correctly!")
#End main function
main()