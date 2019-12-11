import tkinter


# Make up an interface for a business offering 7-10 services or product options with prices
# Write a GUI program and allow the user to click buttons to add services or products and show a total at the bottom.
# Make sure all necessary labels and instructions to the user are included in your GUI.
# Provide options using data fields, radio buttons or check boxes.


# Instrument Order Menu: Violin
# Violin size: 1/4, 1/2, 3/4 or full   (radio buttons)
# Violin grade: student -$300  advanced -$1,500  professional-$10,000  (radio buttons)
# Add-ons: fine tuners (set of 4), gold inlay pegs (set of 4), mute (check boxes)
# order & quit buttons


class Violin:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.violin_frame = tkinter.Frame(self.main_window)
        self.size_frame = tkinter.Frame(self.main_window)
        self.grade_frame = tkinter.Frame(self.main_window)
        self.add_ons_frame = tkinter.Frame(self.main_window)
        self.order_frame = tkinter.Frame(self.main_window)
        self.charges_frame = tkinter.Frame(self.main_window)

        # variable for radiobutton widget
        self.violin_var = tkinter.IntVar()
        self.grade_var = tkinter.IntVar()

        # initialize radio button widgets
        self.violin_var.set(1)
        self.grade_var.set(1)

        self.violin_label = tkinter.Label(self.violin_frame, text='Violin size')
        self.buzz1 = tkinter.Radiobutton(self.violin_frame, text='1/4', variable=self.violin_var, value=1)
        self.buzz2 = tkinter.Radiobutton(self.violin_frame, text='1/2', variable=self.violin_var, value=2)
        self.buzz3 = tkinter.Radiobutton(self.violin_frame, text='3/4', variable=self.violin_var, value=3)
        self.buzz4 = tkinter.Radiobutton(self.violin_frame, text='full 4/4', variable=self.violin_var, value=4)

        self.violin_label.pack()
        self.buzz1.pack(side='left')
        self.buzz2.pack(side='left')
        self.buzz3.pack(side='left')
        self.buzz4.pack(side='left')

        self.grade_label = tkinter.Label(self.grade_frame, text='Grade')
        self.grade1 = tkinter.Radiobutton(self.grade_frame, text='student - $300', variable=self.grade_var, value=1)
        self.grade2 = tkinter.Radiobutton(self.grade_frame, text='advanced -$1,500', variable=self.grade_var, value=2)
        self.grade3 = tkinter.Radiobutton(self.grade_frame, text='professional -$10,000', variable=self.grade_var,
                                          value=3)

        self.grade_label.pack()
        self.grade1.pack(side='left')
        self.grade2.pack(side='left')
        self.grade3.pack(side='left')

        # add ins
        # checkbox variables
        self.finetuners_var = tkinter.IntVar()
        self.goldpegs_var = tkinter.IntVar()
        self.mute_var = tkinter.IntVar()

        self.finetuners_var.set(0)
        self.goldpegs_var.set(0)
        self.mute_var.set(0)

        self.add_label = tkinter.Label(self.add_ons_frame, text='Add-ons')
        self.finetuners = tkinter.Checkbutton(self.add_ons_frame, text='fine tuners(4)', variable=self.finetuners_var)
        self.goldpegs = tkinter.Checkbutton(self.add_ons_frame, text='gold pegs:set of 4',
                                            variable=self.goldpegs_var)
        self.mute = tkinter.Checkbutton(self.add_ons_frame, text='mute', variable=self.mute_var)

        self.add_label.pack()
        self.finetuners.pack(side='left')
        self.goldpegs.pack(side='left')
        self.mute.pack(side='left')

        # order

        self.order_button = tkinter.Button(self.order_frame, text='Order', command=self.display)
        self.quit_button = tkinter.Button(self.order_frame, text='Quit', command=self.main_window.destroy)

        self.order_button.pack(side='left')
        self.quit_button.pack(side='left')

        # charges

        self.order_info = tkinter.StringVar
        self.order_output = tkinter.Label(self.charges_frame, textvariable=self.order_info)
        self.order_output.pack()

        # pack frames

        self.violin_frame.pack()
        self.grade_frame.pack()
        self.add_ons_frame.pack()
        self.charges_frame.pack()

        tkinter.mainloop()

    def display(self):
        output = 'You ordered a '
        if self.violin_var.get() == 1:
            output += 'a 1/4 size violin. '
        elif self.violin_var.get() == 2:
            output += 'a 1/2 size violin. '
        elif self.violin_var.get() == 3:
            output += 'a 3/4 size violin. '
        elif self.violin_var.get() == 4:
            output += 'a 4/4 full size violin. '

        if self.grade_var.get() == 1:
            output += 'student '
        elif self.grade_var.get() == 2:
            output += 'advanced '
        elif self.grade_var.get() == 3:
            output += 'professional '

        if self.grade_var.get() == 1:
            output += ' for $200 '
        elif self.grade_var.get() == 2:
            output += ' for $1,500 '
        elif self.grade_var.get() == 3:
            output += ' for $10,000 '

        if self.finetuners_var.get() == 1:
            output += '\nwith fine tuners '
        if self.goldpegs_var.get() == 1:
            output += '\nwith gold pegs '
        if self.mute_var.get() == 1:
            output += '\nwith mute '

        self.order_info.set(output)


violin = Violin()

# PROBLEM: Order and Quit Buttons don't show
