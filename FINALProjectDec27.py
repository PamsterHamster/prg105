from random import *
from tkinter import *

"""
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
my_canvas_1.grid(row=1, column=0)
# while True:     this makes loop go on forever. Below command limits the number of times it will execute (500) and
# then all buttons/quote/canvases show up when loop has finished.
for i in range(0,500):
    x1=randint(0,200)
    y1=randint(0,250)
    x2=randint(0,200)
    y2=randint(0,250)
    random_width=randint(1,25)
    my_canvas_1.create_line(x1,y1,x2,y2, fill=random_color_code(), width=random_width)
    my_canvas_1.update()
    #   Note when last command above added, I lost the blue background and ALL buttons and quote--gone from view
    # Random color bars end here. Do sth with blank canvas 2&3 below or delete

my_canvas_2 = Canvas(my_window, width=250, height=200)
my_canvas_2.grid(row=1, column=1)
my_canvas_3 = Canvas(my_window, width=250, height=200)
my_canvas_3.grid(row=1, column=2)
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

#   Size of title window and background color
my_window.configure(width=900, height=900, bg="navy")
#   my_window.geometry("%dx%d+0+0" % (My_window.winfo_screenwidth(), my_window.winfo_screenheight())
# ABOVE SEGMENT WORKING

# Create a Menu Bar/display the Chakra colors when clicked--FINISH THIS https://www.youtube.com/watch?v=3Q8mquTM8gA
#   Menu Bar Functions   SECTION NOT WORKING
def Crown():
    my_window['bg']='violet'

def ThirdEye():
    my_window['bg']='indigo'

def Throat():
    my_window['bg']='blue'

def Heart():
    my_window['bg']='green'

def SolarPlexus():
    my_window['bg']='yellow'

def Spleen():
    my_window['bg']='orange'

def Spine():
    my_window['bg']='red'



# Menu Bar Code---numbers may not be necessary after menubar word/cont at 4:27
my_window = tk.Tk()
my_menubar = tk.Menu(my_window)
my_menubar.add_command(label="Crown", command=violet_color)
my_menubar.add_command(label="Third Eye", command=indigo_color)
my_menubar.add_command(label="Throat", command=blue_color)
my_menubar.add_command(label="Heart", command=green_color)
my_menubar.add_command(label="SolarPlexus", command=yellow_color)
my_menubar.add_command(label="Spleen", command=orange_color)
my_menubar.add_command(label="Spine", command=red_color)
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


my_window.mainloop()
