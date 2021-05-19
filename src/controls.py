import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

class Controls(ttk.Frame):
	def __init__(self):
		super().__init__()

		label = ttk.Label(self, text="Controls!")
		label.pack()
