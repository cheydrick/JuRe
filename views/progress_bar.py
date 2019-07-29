from tkinter import Tk, Frame
from tkinter.ttk import Progressbar
from math import floor

# This is sloppy, fix it.

class ResizeImagesProgressView(Frame):
    def __init__(self, root, max):
        super().__init__()
        self.root = root
        self.progress_bar = Progressbar(self, orient = "horizontal", length = 200, mode = "determinate")
        self.progress_bar['maximum'] = max
        
        # Override this function. It should be a function that returns
        # a value from 0-100.
        self.on_timer_function = lambda: len([])

        self.running = False
        self.max_runs = 0
        self.current_runs = 0

        self.progress_bar.pack()
        self.pack()

    def on_timer(self):
        if self.running:
            value = self.on_timer_function()
            self.progress_bar['value'] = value
            self.after(1, self.on_timer)

    def start_timer(self, max_runs):
        self.running = True
        self.max_runs = max_runs
        self.on_timer()

    def stop_timer(self):
        self.running = False
