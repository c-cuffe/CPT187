import tkinter as t
import tkinter.messagebox as tm


class CallCalcGui:
    def __init__(self):
        # Create the GUI window and title
        self.main_window = t.Tk()
        self.main_window.geometry("300x200")
        self.main_window.title("Long-Distance Calls")

        # Create frames
        self.frame1 = t.Frame(self.main_window)
        self.frame2 = t.Frame(self.main_window)
        self.frame3 = t.Frame(self.main_window)
        self.frame4 = t.Frame(self.main_window)

        # Create headers for radio buttons
        self.info = t.StringVar()
        self.info_label = t.Label(self.frame1, textvariable=self.info)
        headers = "Rate Category\t\t\tRate Per Minute"
        self.info.set(headers)

        # Create holder variable for radio buttons, set variable to 0
        self.radio_var = t.IntVar()
        self.radio_var.set(0)
        # Create buttons
        self.daytime = t.Radiobutton(self.frame1, text="Daytime (6:00 A.M. through 5:59 P.M.)\t$0.07",
                                     variable=self.radio_var,
                                     value=1)
        self.evening = t.Radiobutton(self.frame1, text="Evening (6:00 P.M. through 11:59 P.M.)\t$0.12",
                                     variable=self.radio_var,
                                     value=2)
        self.off_peak = t.Radiobutton(self.frame1, text="Off-Peak (midnight through 5:59 A.M.)\t$0.05",
                                      variable=self.radio_var,
                                      value=3)

        # Pack label, buttons, and frame 1
        self.info_label.pack()
        self.daytime.pack()
        self.evening.pack()
        self.off_peak.pack()
        self.frame1.pack()

        # Create label and entry widgets for call length
        self.minutes_label = t.Label(self.frame2, text="Enter Call Length in Minutes: ")
        self.minutes_entry = t.Entry(self.frame2, width=10)

        # Pack label and entry widgets, and frame 2
        self.minutes_label.pack(side="left")
        self.minutes_entry.pack(side="left")
        self.frame2.pack()

        # Create a calculate button
        self.calc_button = t.Button(self.frame3, text="Calculate Cost", command=self.calc)

        # Pack calculate button and frame 3
        self.calc_button.pack()
        self.frame3.pack()

        # Create label for call cost output, a holding variable for the cost, and an output label for the cost
        self.cost_output_label = t.Label(self.frame4, text="Call Cost:")
        self.cost_value = t.StringVar()
        self.cost_output = t.Label(self.frame4,
                                   textvariable=self.cost_value)

        self.cost_output_label.pack(side="left")
        self.cost_output.pack(side="left")
        self.frame4.pack()

        # Start listening for events
        t.mainloop()

    def calc(self):
        # Create placeholder variables for cost and minutes
        cost = 0
        minutes = 0

        # Ensure that the minutes are entered as an integer
        try:
            minutes = int(self.minutes_entry.get())
        except:
            tm.showerror("Invalid Input", "Invalid Entry for Minutes")
            return
        # Ensure user has selected option from list
        if self.radio_var.get() == 0:
            tm.showerror("Invalid Selection", "Must Select an Option from List")

        # Based on selection, calculate cost
        elif self.radio_var.get() == 1:
            cost = .07 * minutes
        elif self.radio_var.get() == 2:
            cost = .12 * minutes
        elif self.radio_var.get() == 3:
            cost = .05 * minutes
        # Create string to hold cost
        cost_string = "${:.2f}".format(cost)
        # Set cost value variable to the cost string
        self.cost_value.set(cost_string)


my_gui = CallCalcGui()
