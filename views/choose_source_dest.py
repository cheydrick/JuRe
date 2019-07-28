from tkinter import Tk, Frame, Button, Label, filedialog, IntVar, StringVar, Entry

class ChooseSourceDestDirView(Frame):
    '''
    This displays an interface for choosing the image source folder,
    and the resized image destination folder.

    Args:
        root - Instance of Tk
        set_source_folder_callback - function that takes a folder path as an argument
        set_destination_folder_callback - function that takes a folder path as an argument
    '''
    def __init__(self, root, set_source_folder_callback = None, set_destination_folder_callback = None, resize_all_button_callback = None, continue_button_callback = None, default_resize_percentage = 25):
        super().__init__()
        self.root = root
        self.set_source_folder_callback = set_source_folder_callback
        self.set_destination_folder_callback = set_destination_folder_callback
        self.resize_all_button_callback = resize_all_button_callback
        self.continue_button_callback = continue_button_callback
        self.default_resize_percentage = default_resize_percentage
        self.init_view()

    def init_view(self):
        self.choose_source_folder_button = Button(self, text = 'Choose Original Image Source Folder', command = self.set_source_folder)
        self.choose_destination_folder_button = Button(self, text = 'Choose Resized Image Destination Folder', command = self.set_destination_folder)
        self.resize_all_button = Button(self, text = "Resize All", command = self.resize_all_button_clicked)
        self.continue_button = Button(self, text = "Continue", command = self.continue_button_clicked)

        self.resize_percent_entry_var = StringVar()
        self.resize_percent_entry_var.set(str(self.default_resize_percentage))
        self.resize_percentage_entry = Entry(self, textvariable = self.resize_percent_entry_var)
        
        self.choose_source_folder_button.pack()
        self.choose_destination_folder_button.pack()
        self.resize_percentage_entry.pack()
        self.resize_all_button.pack()
        self.continue_button.pack()
        self.pack()

    def set_source_folder(self):
        source_folder = filedialog.askdirectory()
        if self.set_source_folder_callback != None:
            self.set_source_folder_callback(source_folder)

    def set_destination_folder(self):
        destination_folder = filedialog.askdirectory()
        if self.set_destination_folder_callback != None:
            self.set_destination_folder_callback(destination_folder)

    def get_resize_percentage(self):
        return int(self.resize_percent_entry_var.get())

    def continue_button_clicked(self):
        if self.continue_button_callback != None:
            self.continue_button_callback()

        self.root.quit()

    def resize_all_button_clicked(self):
        if self.resize_all_button_callback != None:
            self.resize_all_button_callback()

        self.root.quit()

if __name__ == '__main__':
    '''
    Test code, if this module is run on its own.
    '''
    def folder_path_print(folder_path):
        print(folder_path)
    
    root = Tk()
    root.title('JuRe - Just Resize!')
    choose_source_dest = ChooseSourceDestDirView(root, folder_path_print, folder_path_print)
    root.mainloop()

