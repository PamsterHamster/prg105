import time as tm
from random import *
from tkinter import *

# Import statements above should be (sometimes they hide, then program won't run):
# import time as tm
# from random import *
# from tkinter import *

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

# Pam's Summary: I hope, despite the hours of tutorials both in and out of class, and blocks encountered during my 
# journey of this project, that what I have created is not the end. It's the Final Project for PRG 105 Fall term, but 
# I would like to expand this project in the future (like getting the Digital Clock and Quiz to work via 
# Inheritance/Frame method and conquer many of the questions which came up and still remain unanswered. I did overcome 
# multiple roadblocks during this process. I also realize this entire Python language is just the tip of the iceberg. 
# What I did miss was the help of an assistant and/or open lab hours---it probably would have speeded up my progress 
# and/or gotten me further than what I ended here with. In any case, Thank You for your dedication to your students.-Pam

"""


# Create the random color line graphics on the Canvas window https://www.youtube.com/watch?v=41GDcp4IIm4 WORKING
# Position: NW corner--but can't say that officially w Grid System
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
# NOTE: I created the Main Window (Chakras Info) twice, via two working methods: Canvas and Frames via Inheritance.
# I got the Canvas looking very similar to the Frame version, but chose to pursue the Frame method to play around with
# Inheritance--that gave me many headaches (sidenote)
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
# or Parent Class (here it's called my_window).
# i.e. VioletFrame is the subclass/child class of SuperClass

# print(help(Frame)) #https://www.youtube.com/watch?v=bOt1ilhZ3tk&feature=youtu.beThe

# Chakra #7: Crown  Chakra #6: Third Eye/Brow #5: Throat  #4: Heart  #3: Solar Plexus  #2: Spleen  #1: Base(root)

# Note: there are 3 'relief' options: FLAT, RAISED (3Dish), SUNKEN
# frame_8 = Frame(my_window, height=200, width=250, relief=FLAT, bd=8, bg="black")
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
# frame_8.grid(row=3, column=1)
frame_7.grid(row=0, column=2)
frame_6.grid(row=1, column=0)
frame_5.grid(row=1, column=1)
frame_4.grid(row=1, column=2)
frame_3.grid(row=2, column=0)
frame_2.grid(row=2, column=1)
frame_1.grid(row=2, column=2)


# For More Chakra Info: 'Click for Chakra 1, etc' button opens up new info in a loop label for each chakra
# adapted from https://www.youtube.com/watch?v=NsSynSYrB2c
# Note: Doing this added extra space on either side of Column 0, corresponding to longest label length in the Loop.
# However, to fix it I would make each grid square (and SubFrame) larger, but it's too time consuming at this point.
# I'll leave it for sth to improve on if I ever revisit this project in the future, and I hope to.


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
# Labels 8-10 are in the regular SuperClass Frame
# update: Label/Button 8 got turned into the Home/More Chakra Info For Loop
label_8 = Label(my_window, width="10", height="3", bg="black")
button_8 = Button(my_window, text="More info", width=8)  # NEEDS COMMAND=prompt
label_8.grid(row=3, column=0)
button_8.grid(row=3, column=0)

# update: Label/Button 9 got abandoned for the Digital Clock (procedural mode). Digital Clock was Backup Plan.
# The original plan was to have this button start the GUI Quiz, but I couldn't get/find the correct command to get it 
# started. The Quiz code is still here in this program, below, just commented out.
label_9 = Label(my_window, width="15", height="3", bg="black")
button_9 = Button(my_window, text="Take Quiz", width=8)  # NEEDS COMMAND to start Quiz/GUI
label_9.grid(row=3, column=1)
button_9.grid(row=3, column=1)

"""
# QUIT button working-YAY!
label_10 = Label(my_window, width="15", height="3", bg="black")
button_10 = Button(my_window, text="QUIT PROGRAM", width=12, command=my_window.destroy)
label_10.grid(row=3, column=2)
button_10.grid(row=3, column=2)


#  ****OPERATION BLOCK SUBCLASS FRAMES************
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

    # *********************************************************************


"""
    # GUI Quiz adapted from Ch10 assignment and https://www.youtube.com/watch?v=zVv6EbJlpqs NOT FINISHED, NOT WORKING

    # from tkinter import *  DONE ALREADY


q = ["If your Root chakra is out of alignment, you are at risk for which addiction?", "If your Spleen chakra is out \
    of alignment, you are at risk for which addiction?", "If your Solar Plexus chakra is out of alignment, you are at \
    risk for which addiction?", "If your Heart chakra is out of alignment, you are at risk for which addiction?",
     "If your Throat chakra is out of alignment, you are at risk for which addiction?", "If you experience trouble \
    with respiratory ailments, work on which chakra?", "If you experience trouble with blood sugar ailments, work on \
    which chakra?", "If you experience trouble with reproductive system ailments, work on which chakra?", "If you \
    experience trouble with blood pressure ailments, work on which chakra? ?", "If you experience trouble with sinus \
    ailments, work on which chakra?", ]

options = ["food", "cigarettes", "compulsive gambling", "sex"], ["homework", "sugar", "pets", "video games"], \
          ["food", "water sports", "sunshine", "shopping"], ["sex", "animals", "food", "cigarettes"], \
          ["nasal inhalants", "caffeine", "wind", "travel"], ["spleen", "crown", "throat", "heart"], \
          ["solar plexus", "spleen", "heart", "brow"], ["crown", "heart", "solar plexus", "root"], ["crown", "throat",
                                                                                                    "solar plexus",
                                                                                                    "heart"], ["root",
                                                                                                               "heart",
                                                                                                               "throat",
                                                                                                               "brow"]

a = [4, 2, 1, 4, 1, 3, 1, 4, 4, 3]


#    answers in order of questions: sex, sugar, food, cigarettes, nasal inhalants, throat, solar plexus, root, heart,
#    throat

class Quiz(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        self.the_window = the_window
        self.the_window.title("Chakra Quiz")
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(the_window, self.qn)
        self.opts = self.create_options(the_window, 4)
        self.display_q(self.qn)
        self.button = Button(the_window, text="Back", command=self.back_btn)
        # self.button.pack(side=BOTTOM)
        self.button = Button(the_window, text="Next", command=self.next_btn)
        # self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        # w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="text", variable=self.opt_selected, value=b_val + 1)
            b.append(btn)
            # btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques["text"] = q[qn]
        for op in options[qn]:
            self.opts[b_val]["text"] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(q))

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct!")
            self.correct += 1
        else:
            print("Sorry. That isn't correct")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)


# my_window = Tk()
# my_window.geometry("500x300")
app = Quiz(my_window)
"""
# frame_8 = Quiz(my_window)
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

# frame_8.grid(row=3, column=1)
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
# button_7info.grid(row=0, columnspan=2)  # code position placement? default center position in each grid overlaps label

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

#  ABOVE WORKING *Use this version instead of overall Canvas

# Digital Clock Below WORKING via Procedural Method...use if can't get clock via inheritance version running

def display_time():
    current_time = tm.strftime("%H:%M:%S")
    clock_label1["text"] = current_time
    my_window.after(200, display_time)


clock_label1 = Label(my_window, width="15", height="3", font="Times 14", bg="black", fg="lawngreen")
clock_label1.grid(row=3, column=1)
# clock_label2 = Label(my_window, text="Time to work with Chakras!", width="15", height="3", font=14, bg="black", fg="orange")
# clock_label2.grid(row=3, column=1) # Same problem as labeling Chakra Frames: How to place labels and/or buttons
# besides center position only, using grid system?
display_time()

"""
# Install Digital Clock re Class/inheritance: https://www.youtube.com/watch?v=TiTkgTrHw5g NOT WORKING YET
# Problems getting it working in the subclassFrame / Grid method


class DigitalClock(Frame):
    def __init__(self, the_window):
        Frame.__init__(self, master=the_window)
        self.the_window = the_window
        self.the_window.title("Digital Clock")
        self.clock_label = tk.Label(self.the_window, font="Times 24", bg="black", fg="yellow")
        self.clock_label.grid(row=3, column=1)
        self.display_time()

    def display_time(self):
        self.current_time = tm.strftime("%H:%M:%S")
        self.clock_label["text"] = self.current_time
        self.the_window.after(200, self.display_time)


my_window = Tk()
my_digital_clock = DigitalClock(the_window)
"""

my_window.mainloop()
