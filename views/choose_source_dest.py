from tkinter import Tk, Frame, Button, Label, filedialog

class ChooseSourceDestDirView(Frame):
    '''
    This displays an interface for choosing the image source folder,
    and the resized image destination folder.

    Args:
        root - Instance of Tk
        set_source_folder_callback - function that takes a folder path as an argument
        set_destination_folder_callback - function that takes a folder path as an argument
    '''
    def __init__(self, root, set_source_folder_callback = None, set_destination_folder_callback = None, ok_button_callback = None):
        super().__init__()
        self.root = root
        self.set_source_folder_callback = set_source_folder_callback
        self.set_destination_folder_callback = set_destination_folder_callback
        self.ok_button_callback = ok_button_callback
        self.init_view()

    def init_view(self):
        self.choose_source_folder_button = Button(self, text = 'Choose Original Image Source Folder', command = self.set_source_folder)
        self.choose_destination_folder_button = Button(self, text = 'Choose Resized Image Destination Folder', command = self.set_destination_folder)
        self.ok_button = Button(self, text = "Continue", command = self.ok_button_clicked)

        self.choose_source_folder_button.pack()
        self.choose_destination_folder_button.pack()
        self.ok_button.pack()
        self.pack()

    def set_source_folder(self):
        source_folder = filedialog.askdirectory()
        if self.set_source_folder_callback != None:
            self.set_source_folder_callback(source_folder)

    def set_destination_folder(self):
        destination_folder = filedialog.askdirectory()
        if self.set_destination_folder_callback != None:
            self.set_destination_folder_callback(destination_folder)

    def ok_button_clicked(self):
        if self.ok_button_callback != None:
            self.ok_button_callback()

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