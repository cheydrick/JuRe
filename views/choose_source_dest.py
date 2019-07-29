from tkinter import Tk, Frame, Button, Label, filedialog, IntVar, StringVar, Entry, Label

class JuReMainWindow(Frame):
    '''
    Main JuRe window. Source/Destination folder selection, resize setting, and resize button.

    It's up to the caller (ideally some controller class) to set important callbacks.
    '''
    def __init__(self, root):
        self.root = root
        super().__init__()

        self.set_source_path_callback = lambda: len([])
        self.set_destination_path_callback = lambda: len([])
        self.resize_all_callback = lambda: len([])

        self.source_path = ""
        self.destination_path = ""
        self.init_view()

    def init_view(self):
        self.set_source_path_button = Button(self, text = 'Set Image Source Location', command = self.set_source_path_button_clicked)
        self.set_destination_path_button = Button(self, text = 'Set Resized Image Location', command = self.set_destination_path_button_clicked)
        self.resize_percentage_label = Label(self, text = 'Resize Percentage:')
        self.resize_percent_entry_var = StringVar()
        self.resize_percentage_entry = Entry(self, textvariable = self.resize_percent_entry_var)
        self.resize_all_button = Button(self, text = 'Resize All', command = self.resize_all_button_clicked)

        self.set_source_path_button.grid(row = 0, column = 0, columnspan = 2)
        self.set_destination_path_button.grid(row = 1, column = 0, columnspan = 2)
        self.resize_percentage_label.grid(row = 2, column = 0)
        self.resize_percentage_entry.grid(row = 2, column = 1)
        self.resize_all_button.grid(row = 3, column = 0, columnspan = 2)

        self.pack()

    def set_resize_percentage(self, percentage):
        self.resize_percent_entry_var.set(str(percentage))

    def get_resize_percentage(self):
        return int(self.resize_percent_entry_var.get())

    def get_source_path(self):
        return self.source_path + '/'

    def get_destination_path(self):
        return self.destination_path + '/'
        
    def set_source_path_button_clicked(self):
        self.source_path = filedialog.askdirectory()
        self.set_source_path_callback()

    def set_destination_path_button_clicked(self):
        self.destination_path = filedialog.askdirectory()
        self.set_destination_path_callback()

    def resize_all_button_clicked(self):
        self.resize_all_callback()
