from tkinter import Tk
from views.choose_source_dest import ChooseSourceDestDirView
from views.progress_bar import LoadSourceImagesProgressView, ResizeImagesProgressView
from data.jure_data import JuReData

if __name__ == '__main__':
    # Instance of JureData, which contains data and functions that the views will
    # need.
    jure_data = JuReData()
    
    # First present UI for choosing source and destination folder.
    root = Tk()
    choose_source_dest_view = ChooseSourceDestDirView(root, jure_data.set_source_folder, jure_data.set_destination_folder, resize_all_button_callback = jure_data.set_resize_all_selected, continue_button_callback = jure_data.set_continue_selected)
    root.mainloop()

    if jure_data.continue_selected:
        # If "continue" was clicked, set up and run the image processing and progress bar
        progress_view = LoadSourceImagesProgressView(root, jure_data.num_images)
        progress_view.on_timer_function = jure_data._load_next_jure_image
        progress_view.start_timer()

        root.mainloop()

    if jure_data.resize_all_selected:
        jure_data._load_image_file_paths_list()
        jure_data._load_jure_image_list()
        progress_view = ResizeImagesProgressView(root, jure_data.num_images)
        progress_view.on_timer_function = jure_data._resize_next_jure_image
        progress_view.start_timer()
        # If "Resize All" was clicked, do that.
        root.mainloop()
        print("Resizing All!")