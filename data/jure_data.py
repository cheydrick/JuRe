from PIL import Image
from os import listdir
from os.path import isfile, join

class JuReImage():
    '''
    A JuReImage instance stores the file path and thumbnail
    for one image, along with other flags, such as whether or not
    the image is flagged for resizing.
    '''
    def __init__(self, image_file_path, thumbnail_size):
        self.image_file_path = image_file_path
        self.thumbnail_size = thumbnail_size
        self.resize_flag = False
        self.image_thumbnail = None

        self._create_thumbnail_from_file_path()

    def _create_thumbnail_from_file_path(self):
        self.image_thumbnail = Image.open(self.image_file_path).thumbnail(self.thumbnail_size)
        

class JuReData():
    def __init__(self):
        # Folders
        self.source_folder = None
        self.destination_folder = None

        # File lists
        self.image_file_paths_list = []

        # JureImage class instance list
        self.jure_image_list = []

        # Thumbnail options
        self.thumbnail_size = 128, 128

        # JureImage list progress variables
        self.num_images = 0
        self.num_jure_images_processed = 0

    def set_source_folder(self, source_folder):
        # Add code to validate path
        self.source_folder = source_folder
        self._load_image_file_paths_list()

    def set_destination_folder(self, destination_folder):
        # Add code to validate path
        self.destination_folder = destination_folder

    def set_thumbnail_size(self, size):
        '''
        Sets configuration for maximum thumbnail size.
        Must be 2-tuple of pixels, such as (128, 128).
        '''
        self.thumbnail_size = size

    def _load_image_file_paths_list(self):
        for f in listdir(self.source_folder):
            if isfile(join(self.source_folder, f)):
                # TODO: Validate that these are image files!!
                self.image_file_paths_list.append(join(self.source_folder, f))
        
        self.num_images = len(self.image_file_paths_list)

    def _load_jure_image_list(self):
        '''
        This function creates all instances of JuReImage at once before returning.
        Ideally there needs to be a function that does one-at-a-time, or otherwise
        yields to the caller, so that I can implement a progress bar in the view.
        '''
        for p in self.image_file_paths_list:
            self.jure_image_list.append(JuReImage(p, self.thumbnail_size))

    def _load_next_jure_image(self):
        '''
        This function instances a JuReImage of the next unprocessed file,
        and returns how many files total have been processed. This allows for informing
        a progress bar how much work has been done without resorting to threading.
        '''
        index = self.num_jure_images_processed
        self.jure_image_list.append(JuReImage(self.image_file_paths_list[index], self.thumbnail_size))
        if self.num_jure_images_processed < self.num_images - 1:
            self.num_jure_images_processed += 1
        return self.num_jure_images_processed

if __name__ == '__main__':
    '''
    Test code, if this module is run on its own.
    '''
    from tkinter import filedialog

    jure_data = JuReData()

    source_folder = filedialog.askdirectory()

    jure_data.set_source_folder(source_folder)
    jure_data._load_image_file_paths_list()
    jure_data._load_jure_image_list()

    for p in jure_data.image_file_paths_list:
        print(p)
        
    for i in jure_data.jure_image_list:
        print(i)