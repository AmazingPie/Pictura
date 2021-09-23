import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

import image_window as iw
import video_window as vw

from enum import Enum
import os.path

""" The viewport component of the main application window.

This class represents the currently selected file via a viewport from which
files can be previewed before further action is taken by the user.
"""
class Viewport(ttk.Frame):
    CANVAS_WIDTH=500
    CANVAS_HEIGHT=500

    def __init__(self):
        super().__init__()

        self.borderless = False
        self.file_type = FileType.UNKNOWN
        self.img_windows = []
        self.video_windows = []

        # Create label
        self.label = ttk.Label(self, text="Controls!")
        self.label.pack()

        # Create canvas
        self.canvas = tk.Canvas(self, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT,
                                bg="black")
        self.canvas.pack()

    """ Get the type of a file from it's extension.

    :param filename:    the name of the file
    :returns:           the type of the file
    """
    def get_file_type(self, filename):
        _, ext = os.path.splitext(filename)
        if ((ext == ".jpg") or (ext == ".jpeg") or (ext == ".png")):
            return FileType.IMAGE
        elif ((ext == ".gif") or (ext == ".mp4") or (ext == ".webm")):
            return FileType.VIDEO
        else:
            return FileType.UNKNOWN

    """ Update the viewport with the image or video given by the filename. """
    def update_viewport(self, filename):
        self.filename = filename

        self.file_type = self.get_file_type(filename)
        if (self.file_type == FileType.IMAGE):
            self.update_image()
        elif (self.file_type == FileType.VIDEO):
            self.update_video()
        else:
            print("Error: file type not recognised.")

    """ Update the viewport image with the currently selected file. """
    def update_image(self):
        # Make the scaled image
        img = Image.open(self.filename)
        (width, height) = self.scale_to_canvas(*img.size)
        img = img.resize((width, height), Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)

        # Add the image to the canvas
        if (hasattr(self, "img_canvas")):
            self.canvas.itemconfig(self.img_canvas, image=self.img_tk)
        else:
            self.img_canvas = self.canvas.create_image(self.CANVAS_WIDTH / 2,
                                                       self.CANVAS_HEIGHT / 2,
                                                       image=self.img_tk)

    """ Update the viewport with a thumbnail of the current file. """
    def update_video(self):
        print(self.filename)
        pass

    """ Scale an image to the size of the canvas that contains it.

    Make the image the maximum size possible so that either the width or height
    is the same as the canvas width or height respectively. Also maintain the
    aspect ratio of the image when rescaling.

    :param width:   width of the image to scale
    :param height:  height of the image to scale
    :returns:       a scaled (width, height) size tuple
    """
    def scale_to_canvas(self, width, height):
        new_width = 0
        new_height = 0
        if (width < height):
            new_height = self.CANVAS_HEIGHT
            new_width = int(width / (height / self.CANVAS_HEIGHT))
        else:
            new_width = self.CANVAS_WIDTH
            new_height = int(height / (width / self.CANVAS_WIDTH))

        return (new_width, new_height)

    """ Create a new image or video window from the image/video currently in
        the viewport.

    Because Viewport is a component and not the main application window we
    must be passed the basic empty window (Toplevel widget) which we will set
    up.

    :param: a new empty window
    """
    def create_window(self, window):
        if (self.file_type == FileType.IMAGE):
            self.create_img_window(window)
        elif (self.file_type == FileType.VIDEO):
            self.create_video_window(window)
        else:
            print("Error: file type not recognised.")

    """ Create a new zoomable image window from the current image in the
        viewport.

    :param window: a new empty window
    """
    def create_img_window(self, window):
        self.img_windows.append(window)

        window.title("Image")
        window.geometry("500x720")
        window.overrideredirect(self.borderless)
        img_window = iw.ImageWindow(window=window, filename=self.filename)

    """ Create a new looping video window from the current video in the
        viewport.

    :param window: a new empty window
    """
    def create_video_window(self, window):
        self.video_windows.append(window)

        window.title("Video")
        window.geometry("500x720")
        window.overrideredirect(self.borderless)
        video_window = vw.VideoWindow(window=window, filename=self.filename)

    """ Remove the borders from all windows. """
    def toggle_borders(self):
        for window in self.img_windows:
            window.overrideredirect(not self.borderless)    # toggle border

        self.borderless = not self.borderless   # toggle the border state

class FileType(Enum):
    UNKNOWN = 0
    IMAGE   = 1
    VIDEO   = 2
