from tkinter import Tk
from views.choose_source_dest import ChooseSourceDestDirView
from views.progress_bar import LoadSourceImagesProgressView
from data.jure_data import JuReData

if __name__ == '__main__':
    # Instance of JureData, which contains data and functions that the views will
    # need.
    jure_data = JuReData()
    
    # First present UI for choosing source and destination folder.
    root = Tk()
    choose_source_dest_view = ChooseSourceDestDirView(root, jure_data.set_source_folder, jure_data.set_destination_folder)
    root.mainloop()

    # Next set up and run the image processing and progress bar
    progress_view = LoadSourceImagesProgressView(root, jure_data.num_images)
    progress_view.on_timer_function = jure_data._load_next_jure_image
    progress_view.start_timer()

    root.mainloop()