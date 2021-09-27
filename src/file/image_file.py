import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

from file.file import File, FileType
import window.image_window as iw

""" An image representation of an image file which can be displayed. """
class ImageFile(File):
    def __init__(self, filename):
        super().__init__(filename, FileType.IMAGE)

    """ Create a new zoomable image window. """
    def create_window(self):
        super().create_window()
        self.image_window = iw.ImageWindow(self.window, self.filename)

    """ Scale an image to the size of the canvas that contains it.

    Make the image the maximum size possible so that either the width or height
    is the same as the canvas width or height respectively. Also maintain the
    aspect ratio of the image when rescaling.

    :param img_width:   width of the image to scale
    :param img_height:  height of the image to scale
    :param can_width:
    :returns:           a scaled (width, height) size tuple
    """
    def scale_to_canvas(self, img_width, img_height, can_width, can_height):
        new_width = 0
        new_height = 0
        if (img_width < img_height):
            new_height = can_height
            new_width = int(img_width / (img_height / can_height))
        else:
            new_width = can_width
            new_height = int(img_height / (img_width / can_width))

        return (new_width, new_height)

    """ Return a thumbnail of given height and width for this image. """
    def get_thumbnail(self, width, height):
        # Make the scaled image
        img = Image.open(self.filename)
        (width, height) = self.scale_to_canvas(*img.size, width, height)
        img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
