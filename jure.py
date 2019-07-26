from tkinter import Tk
from PIL import Image
from views.choose_source_dest import ChooseSourceDestDirView
from data.jure_data import JuReData

if __name__ == '__main__':
    jure_data = JuReData()
    
    # First present UI for choosing source and destination folder.
    root = Tk()
    choose_source_dest_view = ChooseSourceDestDirView(root, jure_data.set_source_folder, jure_data.set_destination_folder)
    root.mainloop()