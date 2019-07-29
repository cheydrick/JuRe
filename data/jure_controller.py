from .jure_data import JuReData
from views.choose_source_dest import JuReMainWindow
from views.progress_bar import ResizeImagesProgressView
from tkinter import Tk

class JuReController():
    def __init__(self):
        self.root = Tk()
        self.jure_data = JuReData()
        self.jure_view = JuReMainWindow(self.root)
        self.progress_bar = ResizeImagesProgressView(self.root)

        # Still thinking about how to integrate the progress bar properly. For now, it's 
        # treated like a seperate view packed into the main window.
        self.progress_bar.pack()
        
        # Set up the callbacks in the views
        self.jure_view.set_source_path_callback = self.set_source_path
        self.jure_view.set_destination_path_callback = self.set_destination_path
        self.jure_view.resize_all_callback = self.resize_all

        # Default resize percentage
        self.jure_view.set_resize_percentage(25)

    def set_source_path(self):
        self.jure_data.set_source_path(self.jure_view.get_source_path())

    def set_destination_path(self):
        self.jure_data.set_destination_path(self.jure_view.get_destination_path())

    def resize_all(self):
        # Lots to do here - maybe offload it to another function for clarity?
        self.jure_data.set_resize_percentage(self.jure_view.get_resize_percentage())
        self.jure_data.load_file_names_list()
        self.jure_data.load_all_jure_images()
        self.jure_data.set_all_jure_image_resize_flag(True)
        self.progress_bar.on_timer_function = self.on_timer
        self.progress_bar.set_max_runs(self.jure_data.get_num_jure_images())
        self.progress_bar.set_progress_bar_max(self.jure_data.get_num_jure_images())
        self.progress_bar.start_timer()

    def on_timer(self):
        return self.jure_data.resize_next()
    
    def run(self):
        self.root.mainloop()