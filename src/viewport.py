import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class Viewport(ttk.Frame):
	def __init__(self):
		super().__init__()

		# Create label
		self.label = ttk.Label(self, text="Controls!")
		self.label.pack()

		# Create image
		self.img_dir = "..\\tests\\"
		self.img = Image.open(self.img_dir + "cat-low.jpg")
		(width, height) = self.img.size
		self.img = self.img.resize((width // 2, height // 2), Image.LANCZOS)
		self.img_tk = ImageTk.PhotoImage(self.img)

		# Create canvas
		self.canvas = tk.Canvas(self, width=width, height=height)
		self.canvas.create_image(width / 2, height / 2, image=self.img_tk)
		self.canvas.pack()
