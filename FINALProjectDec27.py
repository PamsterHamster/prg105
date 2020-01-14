from random import *
from tkinter import *

# from PIL import ImageTk, Image


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
# or Parent Class. The i.e. VioletFrame is the subclass/child class of SuperClass (Main/my_window) Frame
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
# Labels 1-7 w Chakras are in the SubFrames   : What is the code?
# The Labels: Chakra #7: Crown  Chakra #6: Third Eye/Brow #5: Throat  #4: Heart  #3: Solar Plexus  #2: Spleen  #1: Base


# Labels 8-10 are in the regular SuperClass Frame
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


# self.quit_button = tkinter.Button(self.my_window, text="Quit", command=self.my_window.destroy)


#   Add code & functions to buttons 8-10 above      https://www.youtube.com/watch?v=XZ2G29ZUaII&feature=youtu.be
#   see around 6:31"


#  ****OPERATION BLOCK SUBCLASS FRAMES (lines 80- 225)   AND TRY IT ALL VIA CANVAS
#   https://www.youtube.com/watch?v=HTyN25rnla0
# Create the subclass relationship of the colored frames to master TKframe: around 17'11"

class VioletFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 8
        self["bg"] = "violet"


class IndigoFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 8
        self["bg"] = "indigo"


class RoyalblueFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 8
        self["bg"] = "royalblue"


class LawngreenFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 8
        self["bg"] = "lawngreen"


class YellowFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 8
        self["bg"] = "yellow"


class OrangeFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 8
        self["bg"] = "orange"


class RedFrame(Frame):
    def __init__(self, the_window):
        super().__init__()
        self["height"] = 200
        self["width"] = 250
        self["relief"] = RAISED
        self["bd"] = 8
        self["bg"] = "red"


frame_7 = VioletFrame(my_window)
frame_6 = IndigoFrame(my_window)
frame_5 = RoyalblueFrame(my_window)
frame_4 = LawngreenFrame(my_window)
frame_3 = YellowFrame(my_window)
frame_2 = OrangeFrame(my_window)
frame_1 = RedFrame(my_window)

frame_7.grid(row=0, column=2)
frame_6.grid(row=1, column=0)
frame_5.grid(row=1, column=1)
frame_4.grid(row=1, column=2)
frame_3.grid(row=2, column=0)
frame_2.grid(row=2, column=1)
frame_1.grid(row=2, column=2)

#  ABOVE WORKING ***REINSTALL ABOVE IF CANVAS METHOD NOT PREFERABLE





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

# Create a Menu Bar/display the Chakra colors when clicked  https://www.youtube.com/watch?v=3Q8mquTM8gA
#   Menu Bar Functions   SECTION NOT WORKING/only main tk window appears
def violet_color():
    my_window['bg'] = 'violet'


def indigo_color():
    my_window['bg'] = 'indigo'


def blue_color():
    my_window['bg'] = 'blue'


def green_color():
    my_window['bg'] = 'green'


def yellow_color():
    my_window['bg'] = 'yellow'


def orange_color():
    my_window['bg'] = 'orange'


def red_color():
    my_window['bg'] = 'red'


# Menu Bar Code---numbers may not be necessary after menubar word/cont at 4:27
my_window = Tk()
my_menubar = tk.Menu(my_window)
my_dropdown_menu = tk.Menu(my_menubar)
my_dropdown_menu.add_command(label='Crown', command=violet_color)
my_dropdown_menu.add_command(label='Third Eye', command=indigo_color)
my_dropdown_menu.add_command(label='Throat', command=blue_color)
my_dropdown_menu.add_command(label='Heart', command=green_color)
my_dropdown_menu.add_command(label='SolarPlexus', command=yellow_color)
my_dropdown_menu.add_command(label='Spleen', command=orange_color)
my_dropdown_menu.add_command(label='Spine', command=red_color)
my_menubar.add_cascade(label='ChakraColors', menu=my_dropdown_menu)
my_window.config(menu=my_menubar)


#   Create Title Window Buttons w text (Chakra labels)  https://www.youtube.com/watch?v=qJtf0J0Vrkg&feature=youtu.be
btn_8 = Button(my_window, text="Take a Quiz")
btn_7 = Button(my_window, text="#7: Crown")
btn_6 = Button(my_window, text="#6: 3rd Eye")
btn_5 = Button(my_window, text="#5: Throat")
btn_4 = Button(my_window, text="#4: Heart")
btn_3 = Button(my_window, text="#3: Solar Plexus")
btn_2 = Button(my_window, text="#2: Spleen")
btn_1 = Button(my_window, text="#1: Base")

# Create the grid screen/How many rows & columns available on the screen

# Placement of Title Window Buttons  https://www.youtube.com/watch?v=qJtf0J0Vrkg&feature=youtu.be
btn_8.grid(row=3, column=2)
btn_7.grid(row=2, column=1)
btn_6.grid(row=3, column=1)
btn_5.grid(row=4, column=1)
btn_4.grid(row=5, column=1)
btn_3.grid(row=6, column=1)
btn_2.grid(row=7, column=1)
btn_1.grid(row=8, column=1)

# Pack the buttons (only if use geometry method, not grid method)


# Label
label_1 = Label(my_window, text="Chakras are like the software of the entire computer body. ", bg="yellow")
label_1.grid(row=0, column=0)

# Consider building the main title window with Chakra 'Frames': https://www.youtube.com/watch?v=2j9sYld4uaM
"""

my_window.mainloop()
