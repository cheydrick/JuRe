from tkinter import Tk, Frame
from tkinter.ttk import Progressbar
from math import floor

class LoadSourceImagesProgressView(Frame):
    def __init__(self, root, max):
        super().__init__()
        self.root = root
        self.progress_bar = Progressbar(self, orient = "horizontal", length = 200, mode = "determinate")
        self.progress_bar['maximum'] = max
        
        # Override this function. It should be a function that returns
        # a value from 0-100.
        self.on_timer_function = lambda: len([])

        self.progress_bar.pack()
        self.pack()

    def on_timer(self):
        value = self.on_timer_function()
        self.progress_bar['value'] = value
        self.after(1, self.on_timer)

    def start_timer(self):
        self.on_timer()


if __name__ == '__main__':
    '''
    Test code, if this module is run on its own.
    '''
    # 
    class Val():
        def __init__(self):
            self.part = 0
            self.whole = 5000
        
        def create_val(self):
            tmp_val = floor((self.part / self.whole) * 100)
            self.part += 1
            return tmp_val

        
            
    root = Tk()
    v = Val()
    load_progress_view = LoadSourceImagesProgressView(root, )
    load_progress_view.on_timer_function = v.create_val
    load_progress_view.start_timer()

    root.mainloop()