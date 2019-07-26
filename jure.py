from tkinter import Tk
from PIL import Image
from views.choose_source_dest import ChooseSourceDestDirView

class JuReImage():
    '''
    A JuReImage instance stores the file path and thumbnail
    for one image, along with other flags, such as whether or not
    the image is flagged for resizing.
    '''
    def __init__(self, image_file_path):
        self.image_file_path = image_file_path
        self.resize_flag = False
        self.image_thumbnail = None
        pass

class JuReData():
    def __init__(self):
        # Folders
        self.source_folder = None
        self.destination_folder = None

        # Thumbnail options
        self.thumbnail_size = 128, 128

    def set_source_folder(self, source_folder):
        # Add code to validate path
        self.source_folder = source_folder

    def set_destination_folder(self, destination_folder):
        # Add code to validate path
        self.destination_folder = destination_folder

    def set_thumbnail_size(self, size):
        '''
        Sets configuration for maximum thumbnail size.
        Must be 2-tuple of pixels, such as (128, 128).
        '''
        self.thumbnail_size = size

if __name__ == '__main__':
    jure_data = JuReData()
    
    # First present UI for choosing source and destination folder.
    root = Tk()
    choose_source_dest_view = ChooseSourceDestDirView(root, jure_data.set_source_folder, jure_data.set_destination_folder)
    root.mainloop()