import tkinter
import tkinter.messagebox


#   Write a GUI program that calculates a car's gas mileage.
#   The program window should have Entry widgets that lets the user enter
#   the number of gallons the gas the car holds, number of miles it can go on a full tank.
#   When the calculate MPG button is clicked, the program should display the number of miles the car can be driven
#   per gallon of gas.
#   Use the following formula to calculate the miles per gallon: MPG = miles/gallons

class MPGConverterGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.prompt_totalgallons = tkinter.Label(self.top_frame,
                                                 text=' Enter total number of gallons your gas tank holds: ')
        self.totalgallons_entry = tkinter.Entry(self.top_frame, width=15)
        self.prompt_totalgallons = tkinter.Label(self.top_frame,
                                                 text=' Enter total number miles you can drive on one tank: ')
        self.milespertank_entry = tkinter.Entry(self.top_frame, width=15)

        # Pack the top frame's widgets

        self.prompt_totalgallons.pack(side='left')
        self.totalgallons_entry.pack(side='left')

        # Create the widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame, text='Converted to miles per gallon: ')

        # We need a StrVar object to associate with an output label. Use the object's set method to store a string
        # of blank characters
        self.value = tkinter.StringVar()

        # Create a label and associate it with the StringVar object. Any value stored in the StringVar object will
        # automatically display in the label.
        self.mpg_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        # Pack the middle frame's widgets
        self.mpg_label.pack(side='left')
        self.milespertank_entry.pack(side='left')

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
        # Get the value entered by the user into the totalgallon_entry widget
        gas = float(self.totalgallons_entry.get())
        miles = float(self.milespertank_entry.get())

        # Convert the gallons into miles per gallon
        # MPG = milespertank_entry / totalgallon_entry

        mpg = "You get " + format(miles / gas, ",.2f") + "miles per gallon."

        # Convert the MPG to a string and stor it in the StringVar object. This will automatically update the mpg_label
        # widget
        self.value.set(mpg)


# Create an instance of the MPGConverterGUI class
mpg_conv = MPGConverterGUI

# PROBLEM: Green check, but when tested, no windows display/conversion
