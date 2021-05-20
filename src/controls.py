import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

import glob
import random

class Controls(ttk.Frame):
	def __init__(self):
		super().__init__()

		label = ttk.Label(self, text="Controls!")
		label.grid(row=0 , column=0)

		# Image directory chooser
		self.dir_path = tk.StringVar()
		self.dir_path.set("path/to/img/dir")
		self.dir_entry = tk.Entry(self, textvariable=self.dir_path)
		self.dir_entry.grid(row=1, column=0)
		self.dir_selector = tk.Button(self, command=self.choose_dir)
		self.dir_selector.grid(row=1, column=1)

	""" Set dir_path to chosen directory via filedialog window.	"""
	def choose_dir(self):
		# Set users chosen directory
		dir_path = filedialog.askdirectory()
		self.dir_path.set(dir_path)

		# Generate a list of the images in chosen directory
		extensions = ["jpg", "jpeg", "png"]
		self.img_list = []
		for extension in extensions:
			self.img_list.extend(glob.glob(dir_path + "/**/*." + extension,
											recursive=True))
