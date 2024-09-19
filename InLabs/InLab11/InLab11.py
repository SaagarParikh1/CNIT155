#===============================================================
# Your Name & Lab Section: Saagar Parikh, Friday 3:30
# Your Purdue Email: parikh62@purdue.edu
# Program Description: This program reads book titles from a file, manipulates the strings, and writes the results to another file.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

#Define main function
def main():
    try:
        # Open the input and output files
        with open('books1.txt', 'r') as file_reader, open('books_analysis.txt', 'w') as file_writer:
            # Read all lines from the file
            books = file_reader.readlines()
            # Print the contents of the file 
            print(books)

            # Number of books
            num_books = len(books)
            file_writer.write("======= Analysis Results =======\n\n")
            
            file_writer.write(f"1. The number of books in the file: {num_books}\n\n")
 

            # Books with titles longer than two words
            long_titles = [book for book in books if len(book.split()) > 2]
            file_writer.write(f"2. Titles of Books which have more than two words:\n\n" + ''.join(long_titles))
            
            # Titles in proper case
            proper_titles = [book.title() for book in books]
            file_writer.write("3. Organized Book Titles:\n\n" + ''.join(proper_titles))


    except FileNotFoundError:
        print("This program failed to open the file. Make sure of the following:")
        print("\tThe file to read is located in the same folder where this program is!")
        print("\tThe file's name is spelled correctly!")

# Call the main function
main()