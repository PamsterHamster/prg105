# import tkinter as tk
import time as tm
from random import *
from tkinter import *

# from PIL import ImageTk, Image
# print(help(Frame)) #https://www.youtube.com/watch?v=bOt1ilhZ3tk&feature=youtu.be


"""
RUBRIC & GRADING CRITERIA:
Create an original program that uses most of the skills that you have used in this class. The project must:

Use a GUI interface: coding 5pts, usability&design 5pts
Be object oriented:  5pts
Use an external file, create if doesn't exist: 10pts
Use Functions(min 2): 10 pts
Decision Statements(min 2): 5 pts
Use looping structures(While, for, recursion-2 types): 10 pts
Exception Handling: 10 pts
Use data structures (2 sets): 5 pts
Clean code, no warnings: 10 pts
Be well documented (appropriate names and comments)

"""


# Create the random color line graphics on the Canvas window https://www.youtube.com/watch?v=41GDcp4IIm4
# Position: NW corner
def random_color_code():
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    color_code = '#'
    for i in range(0, 6):
        color_code = color_code + choice(hex_chars)
    return color_code


my_window = Tk()
my_window.title("Chakras Info")
my_canvas_1 = Canvas(my_window, width=250, height=200)
my_canvas_1.grid(row=0, column=0)
# while True:     this makes loop go on forever, everything else lost . Below command of '500' limits the number times
# it will execute (500) and then all buttons/quote/canvases show up when loop has finished.
for i in range(0, 500):
    x1 = randint(0, 250)
    y1 = randint(0, 250)
    x2 = randint(0, 250)
    y2 = randint(0, 250)
    random_width = randint(1, 25)
    my_canvas_1.create_line(x1, y1, x2, y2, fill=random_color_code(), width=random_width)
    my_canvas_1.update()
    #   Note when last command above added, I lost the blue background and ALL buttons and quote--gone from view
    # Random color bars end here.
    # ************************************************************************************************
    # To Canvas_2 add 7 circles in ROTGBIV colors https://www.youtube.com/watch?v=wb2yOsgEJJg  WORKING

my_canvas_2 = Canvas(my_window, width=250, height=200, bg="black")
my_canvas_2.grid(row=0, column=1)
o_7 = my_canvas_2.create_oval(10, 10, 50, 50, fill="violet")
o_6 = my_canvas_2.create_oval(35, 35, 75, 75, fill="indigo")
o_5 = my_canvas_2.create_oval(60, 60, 100, 100, fill="blue")
o_4 = my_canvas_2.create_oval(85, 85, 125, 125, fill="lawngreen")
o_3 = my_canvas_2.create_oval(110, 110, 150, 150, fill="yellow")
o_2 = my_canvas_2.create_oval(135, 135, 175, 175, fill="orange")
o_1 = my_canvas_2.create_oval(160, 160, 200, 200, fill="red")

# To Canvas_2 add one letter in each circle to spell "Chakras" & the quote
text_11 = my_canvas_2.create_text(150, 20, text="... are like the software", font=28, fill="white")
text_10 = my_canvas_2.create_text(165, 40, text="of the entire computer body, ", font=28, fill="white")
text_9 = my_canvas_2.create_text(180, 60, text="so keep them updated ", font=28, fill="white")
text_8 = my_canvas_2.create_text(185, 80, text="and debugged often. ", font=28, fill="white")
text_7 = my_canvas_2.create_text(30, 30, text="C", font=28, fill="white")
text_6 = my_canvas_2.create_text(55, 55, text="H", font=22, fill="white")
text_5 = my_canvas_2.create_text(80, 80, text="A", font=22, fill="white")
text_4 = my_canvas_2.create_text(105, 105, text="K", font=22, fill="white")
text_3 = my_canvas_2.create_text(130, 130, text="R", font=22, fill="white")
text_2 = my_canvas_2.create_text(155, 155, text="A", font=22, fill="white")
text_1 = my_canvas_2.create_text(180, 180, text="S", font=22, fill="white")

# *********************************************************************

"""
# TESTING USING ENTIRE SCREEN IN CANVAS: add labels/buttons to new window w more chakras info..currently til line76
my_canvas_7 = Canvas(my_window, width=250, height=200, bg="violet")
my_canvas_7.grid(row=0, column=2)
label_7text = Label(my_canvas_7, text="#7: CROWN", font=("Arial", 24, "bold"), bg="violet", fg="white")
label_7text.pack(padx=50, pady=40)

my_canvas_6 = Canvas(my_window, width=250, height=200, bg="indigo")
my_canvas_6.grid(row=1, column=0)
label_6text = Label(my_canvas_6, text="#6: THIRD EYE/BROW", font=("Arial", 22, "bold"), bg="indigo", fg="white")
label_6text.pack(padx=10, pady=40)

my_canvas_5 = Canvas(my_window, width=250, height=200, bg="royalblue")
my_canvas_5.grid(row=1, column=1)
label_5text = Label(my_canvas_5, text="#5: THROAT", font=("Arial", 24, "bold"), bg="blue", fg="white")
label_5text.pack(padx=50, pady=40)

my_canvas_4 = Canvas(my_window, width=250, height=200, bg="lawngreen")
my_canvas_4.grid(row=1, column=2)
label_4text = Label(my_canvas_4, text="#4: HEART", font=("Arial", 24, "bold"), bg="lawngreen", fg="white")
label_4text.pack(padx=50, pady=40)

my_canvas_3 = Canvas(my_window, width=250, height=200, bg="yellow")
my_canvas_3.grid(row=2, column=0)
label_3text = Label(my_canvas_3, text="#3: SOLAR PLEXUS", font=("Arial", 24, "bold"), bg="yellow", fg="white")
label_3text.pack(padx=10, pady=40)

my_canvas_2b = Canvas(my_window, width=250, height=200, bg="orange")
my_canvas_2b.grid(row=2, column=1)
label_2btext = Label(my_canvas_2b, text="#2: SPLEEN", font=("Arial", 24, "bold"), bg="orange", fg="white")
label_2btext.pack(padx=52, pady=40)

my_canvas_1b = Canvas(my_window, width=250, height=200, bg="red")
my_canvas_1b.grid(row=2, column=2)
label_1btext = Label(my_canvas_1b, text="#1: ROOT/BASE", font=("Arial", 24, "bold"), bg="red", fg="white")
label_1btext.pack(padx=20, pady=40)

# buttons 8-10 on main frame
label_8 = Label(my_window, width="10", height="3", bg="white")
button_8 = Button(my_window, text="More info", width=8)  # NEEDS COMMAND=prompt
label_8.grid(row=3, column=0)
button_8.grid(row=3, column=0)


label_9 = Label(my_window, width="10", height="3", bg="white")
button_9 = Button(my_window, text="Take Quiz", width=8)  # NEEDS COMMAND=prompt Use New Class: Quiz/GUI?
label_9.grid(row=3, column=1)
button_9.grid(row=3, column=1)

# QUIT button working-YAY!
label_10 = Label(my_window, width="10", height="3", bg="red")
button_10 = Button(my_window, text="QUIT", width=8, command=my_window.destroy)
label_10.grid(row=3, column=2)
button_10.grid(row=3, column=2)

#   Size of title window and background color
my_window.configure(width=900, height=900, bg="black")

##   my_window.geometry("%dx%d+0+0" % (My_window.winfo_screenwidth(), my_window.winfo_screenheight())
# ABOVE SEGMENT WORKING
"""
#   *********** CREATING FRAMES IN OPENING PAGE *******WORKING ******  https://www.youtube.com/watch?v=HTyN25rnla0
# Create the frames, size & colors according to chakra color association USING INHERITANCE. The Frame is SuperClass/
# or Parent Class (here it's called my_window). The i.e. VioletFrame is the subclass/child class of SuperClass
# (Main/my_window) Frame
# Chakra #7: Crown  Chakra #6: Third Eye/Brow #5: Throat  #4: Heart  #3: Solar Plexus  #2: Spleen  #1: Base(root)

# Note: there are 3 'relief' options: FLAT, RAISED (3Dish), SUNKEN

frame_7 = Frame(my_window, height=200, width=250, relief=RAISED, bd=8, bg="violet")
frame_6 = Frame(my_window, height=200, width=250, relief=RAISED, bd=8, bg="indigo")
frame_5 = Frame(my_window, height=200, width=250, relief=RAISED, bd=8, bg="royalblue")
frame_4 = Frame(my_window, height=200, width=250, relief=RAISED, bd=8, bg="lawngreen")
frame_3 = Frame(my_window, height=200, width=250, relief=RAISED, bd=8, bg="yellow")
frame_2 = Frame(my_window, height=200, width=250, relief=RAISED, bd=8, bg="orange")
frame_1 = Frame(my_window, height=200, width=250, relief=RAISED, bd=8, bg="red")

# Frame placement in the main window, grid system (row/column and 0,0 uppper left corner)
# Do not combine the placement systems of pack, geometry, and grid as outlined in link below
# https://python-course.eu/tkinter_layout_management.php

frame_7.grid(row=0, column=2)
frame_6.grid(row=1, column=0)
frame_5.grid(row=1, column=1)
frame_4.grid(row=1, column=2)
frame_3.grid(row=2, column=0)
frame_2.grid(row=2, column=1)
frame_1.grid(row=2, column=2)


# NEED TO ADD LABELS AND BUTTONS to FrameSubClassesABOVE * DO NOT use 'pack' method in the grid frame placement system
# The Labels: Chakra #7: Crown  Chakra #6: Third Eye/Brow #5: Throat  #4: Heart  #3: Solar Plexus  #2: Spleen  #1: Base


# For More Chakra Info: 'Click for Chakra 1, etc' button opens up new info in a loop label for each chakra
# adapted from https://www.youtube.com/watch?v=NsSynSYrB2c

def raise_frame(frame):
    frame.tkraise()


Home = Frame(my_window)
ChakraOne = Frame(my_window)
ChakraTwo = Frame(my_window)
ChakraThree = Frame(my_window)
ChakraFour = Frame(my_window)
ChakraFive = Frame(my_window)
ChakraSix = Frame(my_window)
ChakraSeven = Frame(my_window)

for frame in (Home, ChakraOne, ChakraTwo, ChakraThree, ChakraFour, ChakraFive, ChakraSix, ChakraSeven):
    frame.grid(row=3, column=0, sticky="news")

Label(Home, text="Home", width="15", height="1", bg="black", fg="white").pack()
Button(Home, text="Click for Chakra 1 info", command=lambda: raise_frame(ChakraOne)).pack()

Label(ChakraOne, text="#1:Sound:OH Gem:Ruby Sense:Smell", bg="red", fg="white").pack()
Button(ChakraOne, text="Go to Chakra 2", command=lambda: raise_frame(ChakraTwo)).pack()

Label(ChakraTwo, text="#2:Sound:OO Gem:Opal Sense:Taste", bg="orange", fg="white").pack()
Button(ChakraTwo, text="Go to Chakra 3", command=lambda: raise_frame(ChakraThree)).pack()

Label(ChakraThree, text="#3:Sound:AHH Gem:Amber Sense:Sight", bg="yellow", fg="black").pack()
Button(ChakraThree, text="Go to Chakra 4", command=lambda: raise_frame(ChakraFour)).pack()

Label(ChakraFour, text="#4:Sound:AAY Gem:Emerald Sense:Touch", bg="lawngreen", fg="black").pack()
Button(ChakraFour, text="Go to Chakra 5", command=lambda: raise_frame(ChakraFive)).pack()

Label(ChakraFive, text="#5:Sound:EE Gem:Sapphire Sense:Auditory", bg="royalblue", fg="white").pack()
Button(ChakraFive, text="Go to Chakra 6", command=lambda: raise_frame(ChakraSix)).pack()

Label(ChakraSix, text="#6:Sound:OM Gem:Amethyst Sense:Telepathy", bg="indigo", fg="white").pack()
Button(ChakraSix, text="Go to Chakra 7", command=lambda: raise_frame(ChakraSeven)).pack()

Label(ChakraSeven, text="#7:Sound:No Gem:Diamond Sense:Oneness", bg="violet", fg="white").pack()
Button(ChakraSeven, text="Go to Home", command=lambda: raise_frame(Home)).pack()

raise_frame(Home)
# root.mainloop()

"""
# OPTION 2: Adding a scrollbar tied to button 8 "More Info" adapted https://python-course.eu/tkinter_text_widget.php

# need to bind text to button 9 via a command line
def open_scroll():
    button_9.grid(row=3, column=1) = Tk()
    button_9.pack()
T = TkText(button_9, height=20, width=50)
S = Tk.Scrollbar(button_9, command=text1.yview)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = "There are seven chakras, aligning from the base of your spine (#1: Root/Base) to the top of your head " \
        "(#7: Crown).Each is associated with a designated location, name, symbol & element, musical note, gemstone, " \
        "astrology sign, planet, sense, and food. When the chakras are in alignment you will be healthy and have " \
        "good energy. If any of the chakras are weak or out of alignment, associated physical and/or mental ailments " \
        "will develop. Chakras are kept in balance through daily meditation, best led by an experienced Yoga Master. "

T.insert(tk.END, quote)

# Labels 8-10 are in the regular SuperClass Frame
label_8 = Label(my_window, width="10", height="3", bg="black")
button_8 = Button(my_window, text="More info", width=8)  # NEEDS COMMAND=prompt
label_8.grid(row=3, column=0)
button_8.grid(row=3, column=0)


label_9 = Label(my_window, width="10", height="3", bg="black")
button_9 = Button(my_window, text="Take Quiz", width=8)  # NEEDS COMMAND=prompt Use New Class: Quiz/GUI?
label_9.grid(row=3, column=1)
button_9.grid(row=3, column=1)

"""
# QUIT button working-YAY!
label_10 = Label(my_window, width="15", height="3", bg="black")
button_10 = Button(my_window, text="QUIT PROGRAM", width=12, command=my_window.destroy)
label_10.grid(row=3, column=2)
button_10.grid(row=3, column=2)


# self.quit_button = tkinter.Button(self.my_window, text="Quit", command=self.my_window.destroy)

#   Add code & functions to buttons 8-10 above      https://www.youtube.com/watch?v=XZ2G29ZUaII&feature=youtu.be
#   see around 6:31"

#  ****OPERATION BLOCK SUBCLASS FRAMES (lines 80- 225)   AND TRY IT ALL VIA CANVAS
#   https://www.youtube.com/watch?v=HTyN25rnla0
# Create the subclass relationship of the colored frames to master TKframe: around 17'11"


class VioletFrame(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        # super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 15
        self["bg"] = "violet"


"""
        # https://www.youtube.com/watch?v=N9rPxEvfw1M&feature=youtu.be  2:02'

        self.display_string = StringVar()
        self.button = Button(self, text="Click Me", command=self.display_output)
        self.display_label = Label(self, textvariable=self.display_string, relief="solid")

        self.button.grid(row=0, column=2)
        self.display_label.grid(row=1, column=1)

    def display_output(self):
        self.display_string.set("Crown above the head")
"""


class IndigoFrame(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        # super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 15
        self["bg"] = "indigo"


class RoyalblueFrame(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        # super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 15
        self["bg"] = "royalblue"


class LawngreenFrame(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        # super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 15
        self["bg"] = "lawngreen"


class YellowFrame(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        # super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 15
        self["bg"] = "yellow"


class OrangeFrame(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        # super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 15
        self["bg"] = "orange"


class RedFrame(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        # super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 15
        self["bg"] = "red"


frame_7 = VioletFrame(my_window)
frame_6 = IndigoFrame(my_window)
frame_5 = RoyalblueFrame(my_window)
frame_4 = LawngreenFrame(my_window)
frame_3 = YellowFrame(my_window)
frame_2 = OrangeFrame(my_window)
frame_1 = RedFrame(my_window)
# print(help(VioletFrame))  # https://www.youtube.com/watch?v=bOt1ilhZ3tk&feature=youtu.be
# print(help(IndigoFrame))
# print(help(BlueFrame))
# print(help(LawngreenFrame))
# print(help(YellowFrame))
# print(help(OrangeFrame))
# print(help(RedFrame))

frame_7.grid(row=0, column=2)
frame_6.grid(row=1, column=0)
frame_5.grid(row=1, column=1)
frame_4.grid(row=1, column=2)
frame_3.grid(row=2, column=0)
frame_2.grid(row=2, column=1)
frame_1.grid(row=2, column=2)

# Labels for the Subclass Frames: Each color represents that particular Chakra name and number
label_7 = Label(frame_7, text="#7: CROWN", bg="black", fg="white")
label_7.grid(row=0, column=2)
# button_7info = Button(frame_7, text=" info")
# button_7info.grid(row=0, columnspan=2)  # code position placement? default center position overlaps label

label_6 = Label(frame_6, text="#6: THIRD EYE/BROW", bg="black", fg="white")
label_6.grid(row=1, column=0)
# button_6info = Button(frame_6, text=" info")
# button_6info.grid(row=1, columnspan=2)

label_5 = Label(frame_5, text="#5: THROAT", bg="black", fg="white")
label_5.grid(row=1, column=1)
# button_5info = Button(frame_5, text=" info")
# button_5info.grid(row=1, columnspan=2)

label_4 = Label(frame_4, text="#4: HEART", bg="black", fg="white")
label_4.grid(row=1, column=2)
# button_4info = Button(frame_4, text=" info")
# button_4info.grid(row=1, columnspan=2)

label_3 = Label(frame_3, text="#3: SOLAR PLEXUS", bg="black", fg="white")
label_3.grid(row=2, column=0)
# button_3info = Button(frame_3, text=" info")
# button_3info.grid(row=2, columnspan=2)

label_2 = Label(frame_2, text="#2: SPLEEN", bg="black", fg="white")
label_2.grid(row=2, column=1)
# button_2info = Button(frame_2, text=" info")
# button_2info.grid(row=2, columnspan=2)

label_1 = Label(frame_1, text="#1: ROOT/BASE", bg="black", fg="white")
label_1.grid(row=2, column=2)


# button_1info = Button(frame_1, text=" info")
# button_1info.grid(row=2, columnspan=2)

# CREATE THE Chakra Quiz via Class associated with main window frame 'Quiz' button

# class Quiz:


#  ABOVE WORKING ***REINSTALL ABOVE IF CANVAS METHOD NOT PREFERABLE
# Clock Below working...use if can't get scrollbar adapted.

def display_time():
    current_time = tm.strftime("%H:%M:%S")
    clock_label["text"] = current_time
    my_window.after(200, display_time)


clock_label = Label(my_window, width="15", height="3", font=80, bg="black", fg="red")
clock_label.grid(row=3, column=1)
display_time()

""""
# Install Digital Clock re Class/inheritance: FINISH https://www.youtube.com/watch?v=TiTkgTrHw5g

class DigitalClock:
    def __init__(self, the_window):
        self.the_window = the_window
        self.the_window.title("Digital Clock")
        self.clock_label = tk.Label(self.the_window, font="ariel 24", bg="black", fg="red")
        self.clock_label.grid(row=3, column=1)
        self.display_time()

    def display_time(self):
        self.current_time = tm.strftime("%H:%M:%S")
        self.clock_label["text"] = self.current_time
        self.the_window.after(200, self.display_time)


my_window = tk.Tk()
my_digital_clock = DigitalClock(my_window)

# DON"T USE BELOW STUFF
#   The overall size I want for the title window
# width_of_window = 900
# height_of_window = 900

#   To find the exact center of the screen placement for the title window
# screen_width = my_window.winfo_screenwidth()
# screen_height = my_window.winfo_screenheight()

# x_coordinate = (screen_width/2) - (width_of_window/2)
# y_coordinate = (screen_height/2) - (height_of_window/2)

#   Placing the title window in the exact center of the screen
# my_window.geometry("900x900+%d+%d")  # width_of_window, height_of_window, x_coordinate, y_coordinate


"""

my_window.mainloop()
