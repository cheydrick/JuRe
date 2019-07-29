from tkinter import Tk
from views.choose_source_dest import ChooseSourceDestDirView, JuReMainWindow
from views.progress_bar import LoadSourceImagesProgressView, ResizeImagesProgressView
from data.jure_data import JuReData

if __name__ == '__main__':
    # Instance of JureData, which contains data and functions that the views will
    # need.
    jure_data = JuReData()
    
    # First present UI for choosing source and destination folder.
    root = Tk()
    root.title('JuRe - Just Resize!')
    jure_main_window = JuReMainWindow(root)
    root.mainloop()
