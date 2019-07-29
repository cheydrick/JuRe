from tkinter import Tk
from views.choose_source_dest import ChooseSourceDestDirView, JuReMainWindow
from views.progress_bar import LoadSourceImagesProgressView, ResizeImagesProgressView
from data.jure_data import JuReData
from data.jure_controller import JuReController

# This is a dead end
""" def resize_all(jure_main_window_instance, jure_data_instance):
    if isinstance(jure_main_window_instance, JuReMainWindow) and isinstance(jure_data_instance, JuReData):
        resize_percentage = jure_main_window_instance.get_resize_percentage()
        source_path = jure_main_window_instance.source_path
        destination_path = jure_main_window_instance.destination_path """

    
if __name__ == '__main__':
    app = JuReController()
    app.run()
"""     # TODO - make a proper controller class to deal with all this
    root = Tk()
    root.title('JuRe - Just Resize!')

    # Instance JuReData
    jure_data = JuReData()
    # Instance main UI element
    jure_main_window = JuReMainWindow(root)
    # Instance progress bar UI element
    progress_bar = ResizeImagesProgressView(root, max = 100)
        
    j
    
    root.mainloop()
 """