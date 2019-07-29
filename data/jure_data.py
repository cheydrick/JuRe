from PIL import Image
from os import listdir
from os.path import isfile, join, splitext

class JuReImage():
    '''
    A JuReImage instance stores the file path and optionall a thumbnail
    for one image, along with a resizing flag.
    '''
    def __init__(self, file_name, source_path, destination_path, thumbnail_size, create_thumbnail = False, resize_percentage = 25, resize_flag = False):
        self.file_name = file_name
        self.source_path = source_path
        self.destination_path = destination_path
        self.thumbnail_size = thumbnail_size
        self.create_thumbnail = create_thumbnail
        self.resize_percentage = resize_percentage

        self.resize_flag = resize_flag
        self.image_thumbnail = None

        if self.create_thumbnail:
            self._create_thumbnail_from_file_path()

    def _create_thumbnail_from_file_path(self):
        self.image_thumbnail = Image.open(self.source_path + self.file_name).thumbnail(self.thumbnail_size)

    def set_resize_flag(self, flag):
        self.resize_flag = flag

    def resize(self):
        if self.resize_flag:
            tmp_image = Image.open(self.source_path + self.file_name)
            new_width = int(tmp_image.width * (self.resize_percentage / 100))
            new_height = int(tmp_image.height * (self.resize_percentage / 100))
            tmp_image = tmp_image.resize((new_width, new_height))
            file_name_no_extension = self.file_name.split('.')[0]
            full_resize_file_path = self.destination_path + file_name_no_extension + '_resized.jpg'
            tmp_image.save(full_resize_file_path)
        

class JuReData():
    def __init__(self):
        # Image source and resized image destination paths
        self.source_path = None
        self.destination_path = None
        
        # List of file names
        self.file_names_list = []
        # Number of file names in file_names_list
        self.num_file_names = 0

        # JureImage class instance list
        self.jure_image_list = []
        # Number of JureImage instances in jure_image_list

        # Thumbnail options
        self.thumbnail_size = 128, 128

        # Resize percentage
        self.resize_percentage = 25

        # Number of JureImage instances created (for progress bar)
        self.num_jure_images_created = 0
        # Number of JureImage instances resized (for progress bar)
        self.num_jure_images_resized = 0

        # Flag for whether or not to go to the image chooser
        self.continue_selected = False

        # Flag for whether or not to resize all
        self.resize_all_selected = False

    def set_source_path(self, source_path):
        self.source_path = source_path

    def set_destination_path(self, destination_path):
        self.destination_path = destination_path

    def set_thumbnail_size(self, size):
        '''
        Sets configuration for maximum thumbnail size.
        Must be 2-tuple of pixels, such as (128, 128).
        '''
        self.thumbnail_size = size

    def set_resize_percentage(self, percentage):
        '''
        Sets JuReData resize percentage, AND sets resize percentage
        for all instanced JuReImages. Should it do both?
        '''
        self.resize = percentage
        for i in self.jure_image_list:
            i.resize_percentage = percentage

    def set_all_jure_image_resize_flag(self, flag):
        for i in self.jure_image_list:
            i.set_resize_flag(flag)        

    def load_file_names_list(self):
        for f in listdir(self.source_path):
            if isfile(join(self.source_path, f)):
                # TODO: Validate that these are image files!!
                self.file_names_list.append(f)
        self.num_file_names = len(self.file_names_list)

    def load_all_jure_images(self):
        '''
        Creates all instances of JuReImage at once before returning.
        '''
        for f in self.file_names_list:
            self.jure_image_list.append(JuReImage(f, self.source_path, self.destination_path, self.thumbnail_size, resize_percentage = self.resize_percentage))
        self.num_jure_images_created = len(self.jure_image_list)
        return self.num_jure_images_created

    def load_next_jure_image(self):
        '''
        This function instances a JuReImage of the next unprocessed file,
        and returns how many files total have been processed. This allows for informing
        a progress bar how much work has been done.
        '''
        index = self.num_jure_images_created
        self.jure_image_list.append(JuReImage(self.file_names_list[index], self.source_path, self.destination_path, self.thumbnail_size, resize_percentage = self.resize_percentage))
        if self.num_jure_images_created < self.num_file_names - 1:
            self.num_jure_images_created += 1
        return self.num_jure_images_created

    def get_num_jure_images(self):
        return len(self.jure_image_list)
        
    def resize_all(self):
        '''
        Resizes all JuReImages at once before returning.
        '''
        for p in self.jure_image_list:
            p.resize()
        self.num_jure_images_resized = len(self.jure_image_list)
        return self.num_jure_images_resized

    def resize_next(self):
        '''
        This function resizes the next unresized JuReImage,
        and returns how many in total have been resized. This allows for informing
        a progress bar how much work has been done.
        '''
        index = self.num_jure_images_resized
        self.jure_image_list[index].resize()
        if self.num_jure_images_resized < len(self.jure_image_list) - 1:
            self.num_jure_images_resized += 1
        return self.num_jure_images_resized

if __name__ == '__main__':
    '''
    Test code, if this module is run on its own.
    '''
    source_path = "C:\\Users\\chris\\Code\\JuRe\\Photos2\\"
    destination_path = "C:\\Users\\chris\\Code\\JuRe\\Resized\\"

    #jure_image = JuReImage("TESTPICTURE.jpg", source_path, destination_path, (120,120), resize_percentage = 10)
    #jure_image.set_resize_flag(True)
    #jure_image.resize()

    jure_data = JuReData()
    jure_data.set_source_path(source_path)
    jure_data.set_destination_path(destination_path)
    jure_data.set_resize_percentage(10)
    jure_data.load_file_names_list()
    jure_data.load_all_jure_images()
    jure_data.set_all_jure_image_resize_flag(True)
    jure_data.resize_all()