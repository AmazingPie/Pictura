import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

from file.file import FileType

""" The viewport component of the main application window.

This class represents the currently selected file via a viewport from which
files can be previewed before further action is taken by the user.
"""
class Viewport(ttk.Frame):
    CANVAS_WIDTH=500
    CANVAS_HEIGHT=500

    def __init__(self):
        super().__init__()

        self.windows = []

        # Create label
        self.filename = tk.StringVar()
        self.filename.set("...")
        self.filename_label = ttk.Label(self, textvariable=self.filename)
        self.filename_label.pack()

        # Create canvas
        self.canvas = tk.Canvas(self, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT,
                                bg="black")
        self.canvas.pack()

    """ Update the viewport with the given file. """
    def update_viewport(self, file):
        self.file = file
        self.filename.set(self.file.get_name())

        if (self.file.get_file_type() == FileType.UNKNOWN):
            print("ERROR: File type unknown - cannot create thumbnail.")
            return

        self.img_tk = self.file.get_thumbnail(self.CANVAS_HEIGHT,
                                              self.CANVAS_WIDTH)
        # Add the image to the canvas
        if (hasattr(self, "img_canvas")):
            self.canvas.itemconfig(self.img_canvas, image=self.img_tk)
        else:
            self.img_canvas = self.canvas.create_image(self.CANVAS_WIDTH / 2,
                                                       self.CANVAS_HEIGHT / 2,
                                                       image=self.img_tk)

    """ Create a new image or video window from the file currently in the
        viewport.
    """
    def create_window(self):
        if (self.file.get_file_type() == FileType.UNKNOWN):
            print("ERROR: File type unknown - cannot create window.")
            return

        self.file.create_window()
        self.windows.append(self.file)

    """ Remove the borders from all windows. """
    def toggle_borders(self):
        for window in self.windows:
            window.toggle_border()
