#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: parikh62@purdue.edu
# Program Description: This assignment is provided with a text file (input.txt) that contains 20 students’ names and their GPAs. Write a program that reads those values from the sample file, performs statistical analysis with them, and writes the results to another text file (output.txt).
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main():
    try:
        # Using 'with' for safe opening and closing of files
        with open("input.txt", "r") as inputFile, open("output.txt", "w") as outputFile:
            Names = []  # List to store names
            Scores = []  # List to store scores

            print("Printing every content in the file...")

            for line in inputFile:
                Temp = line.strip().split(',')  # Split the line into name and score
                Names.append(Temp[0].title())  # Capitalize and add the name to the Names list
                Scores.append(float(Temp[1]))  # Convert score to float and add to the Scores list
                
            #print names and scores
            print(Names)
            print(Scores)

            # Find the maximum score
            maxScore = max(Scores)
            maxScoreNames = [Names[i] for i, score in enumerate(Scores) if score == maxScore]

            # Write names with the highest score to the output file
            outputFile.write(f"Maximum score is: {maxScore}\n")
            for name in maxScoreNames:
                outputFile.write(f"{name}, {maxScore}\n")

            outputFile.write("\nUpdated score(s) with letter grade:\n")

            # Update scores and write to the output file
            for i in range(len(Scores)):
                Scores[i] = round(Scores[i], 2)  # Round off to two decimal places
                # Determine letter grade
                if Scores[i] >= 3.7:
                    grade = 'A'
                elif Scores[i] >= 3.5:
                    grade = 'B'
                elif Scores[i] >= 3.0:
                    grade = 'C'
                elif Scores[i] >= 2.5:
                    grade = 'D'
                else:
                    grade = 'F'
                outputFile.write(f"{Names[i]}, {Scores[i]}, {grade}\n")

            
    except FileNotFoundError:
        # Informing the user if the input file doesn't exist
        print("This program failed to open the file. Make sure of the following:")
        print("\tThe file to read is located in the same folder where this program is!")
        print("\tThe file's name is spelled correctly!")
        
#end main function    
main()
