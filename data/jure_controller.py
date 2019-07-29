from .jure_data import JuReData
from views.choose_source_dest import JuReMainWindow
from tkinter import Tk

class JuReController():
    def __init__(self):
        root = Tk()
        self.jure_data = JuReData()
        self.jure_view = JuReMainWindow(root)
        
        # Set up the callbacks in the view
        self.jure_view.set_source_path_callback = self.set_source_path
        self.jure_view.set_destination_path_callback = self.set_destination_path


    def set_source_path(self):
        self.jure_data.set_source_path(self.jure_view.get_source_path())

    def set_destination_path(self):
        self.jure_data.set_destination_path(self.jure_view.get_destination_path())

    def resize_all(self):
        self.jure_data.set_resize_percentage(self.jure_view.get_resize_percentage())
    
    def run(self):
        pass