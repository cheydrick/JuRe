from tkinter import Tk, Frame
from tkinter.ttk import Progressbar
from math import floor

class ResizeImagesProgressView(Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.progress_bar = Progressbar(self, orient = "horizontal", length = 200, mode = "determinate")
        self.progress_bar['maximum'] = 1000

        self.on_timer_function = lambda: len([])

        self.running = False
        self.max_runs = 0
        self.current_runs = 0

        self.progress_bar.pack()
        self.pack()

    def set_progress_bar_max(self, max):
        self.progress_bar['maximum'] = max

    def set_max_runs(self, max):
        self.max_runs = max

    def on_timer(self):
        print(self.current_runs)
        print(self.max_runs)
        if self.current_runs < self.max_runs:
            value = self.on_timer_function()
            self.progress_bar['value'] = value
            self.current_runs += 1
            self.after(1, self.on_timer)

    def start_timer(self):
        self.progress_bar['value'] = 0
        self.on_timer()
