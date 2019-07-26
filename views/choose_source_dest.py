from tkinter import Tk, Frame, Button, Label

class ChooseSourceDestDirView(Frame):
    '''
    This displays an interface for choosing the image source folder,
    and the resized image destination folder.
    '''
    def __init__(self, root):
        super().__init__()
        self.init_view()

    def init_view(self):
        self.choose_source_folder_button = Button(self, text = 'Choose Original Image Source Folder')
        self.choose_destination_folder_button = Button(self, text = 'Choose Resize Image Destination Folder')

        self.choose_source_folder_button.pack()
        self.choose_destination_folder_button.pack()
        self.pack()

if __name__ == '__main__':
    root = Tk()
    choose_source_dest = ChooseSourceDestDirView(root)
    root.mainloop()