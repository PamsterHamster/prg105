#   Write a GUI program that displays your name and address when a button is clicked ( you can use the school address).
#   The program window should resemble the sketch, btns at bottom of frame side by side (Canvas program module 13.1)
#   When the user clicks the Show Info button, the program should display your name and address stacked on one another

#   This program has a Quit button that calls the Tk class's destroy method when clicked


import tkinter
import tkinter.messagebox


class BasicGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create a button widget with the text 'Show Info' on face. Use the do_something method when user clicks btn
        self.my_button = tkinter.Button(self.main_window, text='Show Info', command=self.do_something)

        # Create the Quit button. When this button is clicked the root widget's destroy method is called
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.my_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The do-something method is a callback function for the button widget
    def do_something(self):
        # Display an info dialog box
        tkinter.messagebox.showinfo('Response', 'Pam Becker \n8900 Route 14')


# Create an instance of the BasicGUI class
basic_gui = BasicGUI()

