import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from enum import Enum
import os.path

""" A generic file which Pictura can display. """
class File():
    def __init__(self, filename, file_type):
        self.window = None
        self.borderless = False
        self.filename = filename
        self.file_type = file_type

    """ Get the type of a file from it's extension.

    :param filename:    the name of the file
    :returns:           the type of the file
    """
    @staticmethod
    def determine_file_type(filename):
        _, ext = os.path.splitext(filename)
        if ((ext == ".jpg") or (ext == ".jpeg") or (ext == ".png")):
            return FileType.IMAGE
        elif ((ext == ".gif") or (ext == ".mp4") or (ext == ".webm")):
            return FileType.VIDEO
        else:
            return FileType.UNKNOWN

    """ Return the full file path to this file. """
    def get_name(self):
        return self.filename

    """ Return this file's type. """
    def get_file_type(self):
        return self.file_type

    """ Remove the borders from the window. """
    def toggle_border(self):
        if (self.window != None):
            self.window.overrideredirect(not self.borderless)
            self.borderless = not self.borderless

    """ UNSURE IF THIS IS NEEDED??? """
    def create_window(self):
        self.window = tk.Toplevel()
        self.window.title(self.filename)
        self.window.geometry("500x720")

    """ Return a thumbnail of given height and width for this file. """
    def get_thumbnail(self, width, height):
        pass


""" The type of a given file. """
class FileType(Enum):
    UNKNOWN = 0
    IMAGE   = 1
    VIDEO   = 2
