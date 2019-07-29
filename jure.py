from tkinter import Tk
from views.choose_source_dest import JuReMainWindow
from views.progress_bar import ResizeImagesProgressView
from data.jure_data import JuReData
from data.jure_controller import JuReController
   
if __name__ == '__main__':
    app = JuReController()
    app.run()
