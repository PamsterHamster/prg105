# This program will give the user information on the different Chakras associated with the Human energy balance.
# Chakras are useful when working with Reiki or Yoga

# THE PROGRAM

"""
def main():
# Define variables
#   chakra_imagebutton_userchoice = []
#   chakra_lotus_image = []

    # DATA COLLECTION   # Based on Geddis Ch 7.3 Names Assignment/Engel
    in_file = open('ChakraImages.png', 'r') # opens file in read mode
    chakra_imagebutton_userchoice = in_file.readlines() # 'primes the pump' by reading the first image #CAN IT READ
        # IMAGES INSTEAD OF TEXT?

    in_file.close()
    input_file.close()

    index = 0
"""

# Create the main window to hold the background image

from tkinter import *


def run1():
    print("Welcome to the Root Chakra. ")


# Put in a stop (loop?) function for each run.
# Add more info text: number, color, location, sound, pitch-- OR put these into class/object?

def run2():
    print("Welcome to the Spleen Chakra. ")


def run3():
    print("Welcome to the Solar Chakra. ")


def run4():
    print("Welcome to the Heart Chakra. ")


def run5():
    print("Welcome to the Throat Chakra. ")


def run6():
    print("Welcome to the Brow Chakra. ")


def run7():
    print("Welcome to the Crown Chakra. ")


window = Tk()
window.title("Chakras Information")
window.geometry("900x900")

welcome_text = Label(text="Welcome to the Chakra Center. Press a chakra button for more details. ",
                     fg="white", bg="gray")
welcome_text.pack()  # Cite: https://www.youtube.com/watch?v=J-chyaIVuzE

# Create Chakra info button
Chaone_btn = Button(text="Root", fg="black", bg="red", command=run1)
Chaone_btn.place(x=450, y=750)  # X axis stays same, Y changes for alignment of 7 buttons:TEST THESE OVER IMAGE

Chatwo_btn = Button(text="Spleen", fg="black", bg="orange", command=run2)
Chatwo_btn.place(x=450, y=675)

Chathree_btn = Button(text="Solar", fg="black", bg="yellow", command=run3)
Chathree_btn.place(x=450, y=600)

Chafour_btn = Button(text="Heart", fg="black", bg="green", command=run4)
Chafour_btn.place(x=450, y=525)

Chafive_btn = Button(text="Throat", fg="black", bg="blue", command=run5)
Chafive_btn.place(x=450, y=475)

Chasix_btn = Button(text="Brow", fg="black", bg="purple", command=run6)
Chasix_btn.place(x=450, y=400)

Chaseven_btn = Button(text="Crown", fg="black", bg="pink", command=run7)
Chaseven_btn.place(x=450, y=325)

window.mainloop()  # place at end of graphics

#  # THE MAIN WINDOW  cite: https://pythonprogramming.net/python-3-tkinter-basics-tutorial/

# OPTION 2


"""

# OPTION 1
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


root.geometry("900x900")    # For main Chakras Information window
app = Window(root)          # For main Chakras Information window


root.mainloop()


# THE MAIN IMAGE (LOTUS POSITION BODY) Inside the MAIN WINDOW


photo = PhotoImage(file="lotus.jpg")  # Cite: https://www.youtube.com/watch?v=lt78_05hHSk
label = Label(root, image=photo)
label.pack()




# Save & run—-then resize it



# Adding widgets to the Main (root) window: from https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
Label(root, text = 'Get Your Chakras On', font = ('Verdana', 20)).pack(side = TOP, pady = 15)

# Creating a photoimage object to use in Main Window
# from https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
photo = PhotoImage(file = r"C:PATH ON HARDRIVE") # Find the path and add here. CONTINUE FROM THIS POINT


        # Create a button instance
        # Quit Button-- small, on main program windwow. Is this Quit for the entire program?? I think yes.
        quit.Button = Button(self, text "Quit or other text")
        # Placing the button on the original window
        quitButton.place (x=250, y=250)  #places button at upper left.  # NOT APPEARING

"""
