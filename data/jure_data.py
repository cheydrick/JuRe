from PIL import Image
from os import listdir
from os.path import isfile, join, splitext

class JuReImage():
    '''
    A JuReImage instance stores the file path and thumbnail
    for one image, along with other flags, such as whether or not
    the image is flagged for resizing.
    '''
    def __init__(self, file_name, source_path, destination_path, thumbnail_size, create_thumbnail = False, resize_percentage = 25):
        self.file_name = file_name
        self.source_path = source_path
        self.destination_path = destination_path
        self.thumbnail_size = thumbnail_size
        self.create_thumbnail = create_thumbnail
        self.resize_percentage = resize_percentage

        self.resize_flag = False
        self.image_thumbnail = None

        if self.create_thumbnail:
            self._create_thumbnail_from_file_path()

        #print("Created JureImage {}".format(self.source_path + self.file_name))

    def _create_thumbnail_from_file_path(self):
        self.image_thumbnail = Image.open(self.source_path + self.file_name).thumbnail(self.thumbnail_size)

    def resize(self):
        tmp_image = Image.open(self.source_path + self.file_name)
        new_width = int(tmp_image.width * (self.resize_percentage / 100))
        new_height = int(tmp_image.height * (self.resize_percentage / 100))
        tmp_image.resize((new_width, new_height))
        file_name_no_extension = self.file_name.split('.')[0]
        full_resize_file_path = self.destination_path + file_name_no_extension + '_resized.jpg'
        #print("Resizing: {} to {} at {} percent ({},{} to {},{}).".format(self.source_path + self.file_name, full_resize_file_path, self.resize_percentage, tmp_image.width, tmp_image.height, new_width, new_height))
        tmp_image.save(full_resize_file_path)
        

class JuReData():
    def __init__(self):
        # Folders
        self.source_path = None
        self.destination_path = None

        self.file_names_list = []

        # JureImage class instance list
        self.jure_image_list = []

        # Thumbnail options
        self.thumbnail_size = 128, 128

        self.resize_percentage = 25

        self.num_file_names = 0
        # Total number of JureImage instances in jure_image_list
        self.num_jure_images = 0
        # Number of JureImage instances created (for progress bar)
        self.num_jure_images_processed = 0
        # Number of JureImage instances resized (for progress bar)
        self.num_jure_images_resized = 0

        # Flag for whether or not to go to the image chooser
        self.continue_selected = False
        self.resize_all_selected = False

    def set_source_path(self, source_path):
        # Add code to validate path
        self.source_path = source_path

    def set_destination_path(self, destination_path):
        # Add code to validate path
        self.destination_path = destination_path

    def set_thumbnail_size(self, size):
        '''
        Sets configuration for maximum thumbnail size.
        Must be 2-tuple of pixels, such as (128, 128).
        '''
        self.thumbnail_size = size

    # # Do I really need getters and setters?
    # # I guess for the stuff that NEEDS to be get/set at some point?
    # def set_continue_selected(self, val = True):
    #     self.continue_selected = val

    # def set_resize_all_selected(self, val = True):
    #     self.resize_all_selected = val

    def set_resize_percentage(self, percentage):
        for i in self.jure_image_list:
            i.resize_percentage = percentage

    def load_file_names_list(self):
        for f in listdir(self.source_path):
            if isfile(join(self.source_path, f)):
                # TODO: Validate that these are image files!!
                self.file_names_list.append(f)
        self.num_file_names = len(self.file_names_list)

    def load_jure_image_list(self):
        '''
        This function creates all instances of JuReImage at once before returning.
        '''
        for f in self.file_names_list:
            self.jure_image_list.append(JuReImage(f, self.source_path, self.destination_path, self.thumbnail_size, resize_percentage = self.resize_percentage))

    def load_next_jure_image(self):
        '''
        This function instances a JuReImage of the next unprocessed file,
        and returns how many files total have been processed. This allows for informing
        a progress bar how much work has been done..
        '''
        index = self.num_jure_images_processed
        self.jure_image_list.append(JuReImage(self.file_names_list[index], self.source_path, self.destination_path, self.thumbnail_size, resize_percentage = self.resize_percentage))
        if self.num_jure_images_processed < self.num_file_names - 1:
            self.num_jure_images_processed += 1
        return self.num_jure_images_processed

    def resize_all(self):
        for p in self.jure_image_list:
            p.resize()

    def resize_next(self):
        index = self.num_jure_images_resized
        self.jure_image_list[index].resize()
        if self.num_jure_images_resized < len(self.jure_image_list) - 1:
            self.num_jure_images_resized += 1
        return self.num_jure_images_resized

if __name__ == '__main__':
    '''
    Test code, if this module is run on its own.
    '''
    from tkinter import filedialog

    jure_data = JuReData()

    source_folder = filedialog.askdirectory()
    destination_folder = filedialog.askdirectory()
