import tkinter as t
import tkinter.messagebox as tm


class InfoGUI:
    def __init__(self):
        # Create the GUI window
        self.main_window = t.Tk()
        self.main_window.geometry("300x100")
        self.main_window.title("Name and Address")

        # Create frames
        self.frame1 = t.Frame(self.main_window)
        self.frame2 = t.Frame(self.main_window)
        # Create placeholder for data
        self.info = t.StringVar()
        self.info_label = t.Label(self.frame1, textvariable=self.info)
        # Create buttons
        self.show_info = t.Button(self.frame2,
                                  text="Show Info",
                                  command=self.print_info)
        self.quit_button = t.Button(self.frame2,
                                    text="Quit",
                                    command=self.main_window.destroy)

        #Pack label and buttons
        self.info_label.pack()
        self.show_info.pack(side="left")
        self.quit_button.pack(side="left")

        #Pack frames
        self.frame1.pack()
        self.frame2.pack()

        # Start listening for events
        t.mainloop()

    def print_info(self):
        info = "Cecilia Cuffe\n4274 Graystone Court\nLittle River, SC 29566"
        self.info.set(info)


my_info = InfoGUI()
