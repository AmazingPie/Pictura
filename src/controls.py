import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

import glob
import random

from file.file import File, FileType
from file.image_file import ImageFile
from file.video_file import VideoFile

""" The controls component of the main application window.

This class contains various inputs (buttons, text entry boxes, etc...) to allow
the user to control the rest of the application. The class itself does very
little processing and is mostly a front end interface combined which then
communicates instructions to other main application window components.
"""
class Controls(ttk.Frame):
    def __init__(self, update_state):
        super().__init__()

        self.update_state = update_state
        self.img_list = []
        self.video_list = []

        label = ttk.Label(self, text="Controls!")
        label.grid(row=0 , column=0)

        # Image/Video directory chooser
        self.dir_path = tk.StringVar()
        self.dir_path.set("path/to/dir")
        self.dir_entry = tk.Entry(self, textvariable=self.dir_path)
        self.dir_entry.grid(row=1, column=0)
        self.dir_selector = tk.Button(self, command=self.choose_dir)
        self.dir_selector.grid(row=1, column=1)

        gen_rand_img = tk.Button(self,
                                 command=lambda: self.choose_rand_file(self.img_list),
                                 text="\nGenerate Image\n")
        gen_rand_img.grid(row=2, column=0)

        gen_rand_video = tk.Button(self,
                                   command=lambda: self.choose_rand_file(self.video_list),
                                   text="\nRandom Video\n")
        gen_rand_video.grid(row=3, column=0)

        add_to_window = tk.Button(self, command=self.add_to_window,
                                        text="\nAdd to window\n")
        add_to_window.grid(row=4, column=0)

        toggle_borders = tk.Button(self, command=self.toggle_borders,
                                        text="\nToggle borders\n")
        toggle_borders.grid(row=5, column=0)

    """ Set dir_path to chosen directory via filedialog window. """
    def choose_dir(self):
        # Set users chosen directory
        dir_path = filedialog.askdirectory()
        self.dir_path.set(dir_path)

        # Populate lists with files from the chosen directory
        self.img_list = self.find_files_from_ext(["jpg", "jpeg", "png"])
        self.video_list = self.find_files_from_ext(["gif", "mp4"])

    """ Find filenames with the given extensions.

    :param extensions:  a string array with file extensions to find
    :returns:           an array of filenames that have one of the given
                        extensions
    """
    def find_files_from_ext(self, extensions):
        filenames = []
        for extension in extensions:
            filenames.extend(glob.glob(self.dir_path.get() + "/**/*." + extension,
                                       recursive=True))
        return filenames

    """ Choose a random file from the given list and use it to update the
        viewport.

    :param file_list:   list of files
    """
    def choose_rand_file(self, file_list):
        length = len(file_list)
        self.file_path = file_list[random.randint(0, length)]

        file = None
        file_type = File.determine_file_type(self.file_path)
        if (file_type == FileType.IMAGE):
            file = ImageFile(self.file_path)
        elif (file_type == FileType.VIDEO):
            file = VideoFile(self.file_path)
        else:
            # Might want to re-choose another file instead here.
            file = File(file_path)
            print("WARNING: File: '{}' type is not recognised.", self.file_path)

        self.update_state("new_file", file)

    """ Add the currently selected file (the one in the viewport) to its own
        window.
    """
    def add_to_window(self):
        if (hasattr(self, "file_path")):
            self.update_state("new_window")
        else:
            print("Nothing in viewport")

    """ Remove borders for all children windows. """
    def toggle_borders(self):
        self.update_state("toggle_borders")
