# This program will give the user information on the different Chakras associated with the Human energy balance.
# Chakras are useful when working with Reiki or Yoga

# THE PROGRAM


def main():
# Define variables
#   chakra_imagebutton_userchoice = []
#   chakra_MAINBODY_image = []

    # DATA COLLECTION   # Based on Geddis Ch 7.3 Names Assignment/Engel
    in_file = open('ChakraImages.png', 'r') # opens file in read mode
    chakra_imagebutton_userchoice = in_file.readlines() # 'primes the pump' by reading the first image #CAN IT READ
        # IMAGES INSTEAD OF TEXT?

    in_file.close()
    input_file.close()

    index = 0



# Create the main window to hold the background image
#  # THE MAIN WINDOW  cite: https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # Name the Master Window
        self.master.title("Chakras Information")
        # Let the widget take up the full space of the window
        self.pack(fill=BOTH, expand=1)

"""
# Adding widgets to the Main (root) window: from https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
Label(root, text = 'Get Your Chakras On', font = ('Verdana', 20)).pack(side = TOP, pady = 15)

# Creating a photoimage object to use in Main Window
# from https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
photo = PhotoImage(file = r"C:PATH ON HARDRIVE") # Find the path and add here. CONTINUE FROM THIS POINT


        # Create a button instance
        # Quit Button-- small, on main program windwow. Is this Quit for the entire program?? I think yes.
        quit.Button = Button(self, text "Quit or other text")
        # Placing the button on the original windwo
        quitButton.place (x=0, y=0)  #places button at upper left.  # NOT APPEARING

"""





root = Tk()
root.geometry("900x900")
app = Window(root)

root.mainloop()

# Save & run—-then resize it
