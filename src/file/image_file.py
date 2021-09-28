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

    """ Return a thumbnail of given height and width for this image. """
    def get_thumbnail(self, width, height):
        # Make the scaled image
        img = Image.open(self.filename)
        img.thumbnail((width, height))
        return ImageTk.PhotoImage(img)
