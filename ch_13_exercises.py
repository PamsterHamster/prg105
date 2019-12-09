"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)


# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2

class MyGUI2:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Add a label to MyGUI2 (above) that prints your first and last name; pack the label
        self.label = tkinter.Label(self.main_window, text='Pam Becker')

        # Call the label widget's pack method
        self.label.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()


# Create an instance of the MyGUI2 class
my_gui2 = MyGUI2()

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label--SEE ABOVE

# Create an instance of MyGUI2  --SEE ABOVE


# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)


# Create a MyGUI3 class that creates a window with two frames


class MyGUI3:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create two frames, one for the top of the window and one for the bottom of the window
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # In the top Frame add labels with your name and major
        self.label1 = tkinter.Label(self.top_frame, text='Pam Becker')
        self.label2 = tkinter.Label(self.top_frame, text='Internatl Business Certificate & Grad School Music Cognition')

        # Pack the labels in the top frame, using 'top' argument to stack on top of each other
        self.label1.pack(side='top')
        self.label2.pack(side='top')

        # In the bottom frame add labels with the classes you are taking this semester
        self.label3 = tkinter.Label(self.bottom_frame, text='International Business')
        self.label4 = tkinter.Label(self.bottom_frame, text='Principles of Importing/Exporting')
        self.label5 = tkinter.Label(self.bottom_frame, text='Intro to Computer Programming 105')

        # Pack the labels in the bottom frame, using 'top' argument to stack on top of each other
        self.label3.pack(side='top')
        self.label4.pack(side='top')
        self.label5.pack(side='top')

        # Pack the top and bottom frames
        self.top_frame.pack()
        self.bottom_frame.pack()


    # Create an instance of MyGUI3


my_gui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)


# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI

# Import the tkinter.messagebox at the very top of program--DONE

class MyGUI4:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create the button widget with the opening like of the joke on the face of the button
        # The do-something method should be executed when the user clicks the button
        self.my_button = tkinter.Button(self.main_window, text='How does a mathematician plow fields?',
                                        command=self.do_something)

        # Pack the Button
        self.my_button.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The do_something method is a callback function for the Button widget

    def do_something(self):
        # Display an info dialog box, this one with the joke reply
        tkinter.messagebox.showinfo('Response', 'With a pro-tractor.')


# Create an instance of the MyGUI class.
my_gui4 = MyGUI4()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)


# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters

class InchesConverterGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a length in inches: ')
        self.inches_entry = tkinter.Entry(self.top_frame, width=15)

        # Pack the top frame widgets
        self.prompt_label.pack(side='left')
        self.inches_entry.pack(side='left')

        # Create widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame, text='Converted to centimeters: ')

        # A StringVar object is needed to associate w output label. Use the object's set method to store a string of
        # blank characters
        self.value = tkinter.StringVar()
        self.value.set("centimeters")

        # Create a label and associate it w the StringVar object. Any value stored in the StringVar object will
        # automatically display in the label.
        self.centimeters_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # Pack the middle frame widgets
        self.descr_label.pack(side='left')
        self.centimeters_label.pack(side='left')

        # Create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

        # The convert method is a callback function for the Calculate button

    def convert(self):
        # Get the value entered by user into the inches_entry widget
        inches = float(self.inches_entry.get())

        # Convert inches to centimeters
        centimeters = inches / 2.54

        #   Convert centimeters to a string and store it in the StringVar object. This will automatically update
        #   the centimeters_label widget
        self.value.set(centimeters)

        #   Display results in an info dialog box
    #   tkinter.messagebox.show.info('Results', str(inches) + 'inches is equal to ' + str(centimeters) + 'centimeters')

    # Create instance of the InchesConverterGUI class.


inches_conv = InchesConverterGUI()
