import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

class Gallery(ttk.Frame):
	def __init__(self):
		super().__init__()

		label = ttk.Label(self, text="Gallery")
		label.pack()
