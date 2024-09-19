#===============================================================
# Program Description: make a simple program using GUI which displays a) a title of a book, b) the number of a or A, and c) the number of words in the title
#=================================================================

from graphics import *
from button import *

def main():
    # Create a window with 500 * 400 dimension.
    window = GraphWin("Manipulating String in Python", 500, 400)

    # Create a title for this program
    title = Text(Point(250, 25), "Manipulating String in Python")
    title.setSize(20)  # Set the title's font size to 20
    title.setStyle("bold")  # Make the title bold
    title.setTextColor("purple")  # Make the title purple!
    title.draw(window)  # Now draw it on the window!

    # Create a label
    label1 = Text(Point(250, 60), "Enter title of a book:")
    label1.setSize(15)
    label1.setStyle("bold")
    label1.draw(window)

    # Create an input textbox for strings that will be entered by the user
    inputBox = Entry(Point(250, 90), 30)
    inputBox.setSize(15)
    inputBox.setFill("white")
    inputBox.draw(window)

    # Create a display box to print the results
    display = Rectangle(Point(50, 120), Point(450, 380))
    display.draw(window)

    # Create a button to receive the user's input
    btn = Button(window, Point(450, 60), 100, 30, "Enter")
    btn.activate()  # Activate Enter button

    # Create a button for exit
    quit_btn = Button(window, Point(450, 100), 100, 30, "Exit")
    quit_btn.activate()  # Activate Exit button

    while True:
        p = window.getMouse()
        if btn.clicked(p):  # When the Enter button is clicked
            string = inputBox.getText()
            num_a = string.lower().count('a')  # Count 'a' and 'A'
            titled_string = string.title()  # Make first letter of each word uppercase
            word_count = len(string.split())  # Count number of words

            # Clear previous results
            for item in window.items[:]:
                if isinstance(item, Text) and item.getAnchor().getY() > 100:
                    item.undraw()

            # Print the results as Desired Outputs in the display textbox
            Text(Point(250, 160), f"The title is...: {titled_string}").draw(window)
            Text(Point(250, 180), f"Ther is/are {num_a} A/a(s).").draw(window)
            Text(Point(250, 200), f"The number of words in the string is/are: {word_count}").draw(window)

        elif quit_btn.clicked(p):  # When the Exit button is clicked, it closes the window.
            window.close()
            return
# End program
main()
