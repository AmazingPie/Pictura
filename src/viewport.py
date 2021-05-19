import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class Viewport(ttk.Frame):
	CANVAS_WIDTH=500
	CANVAS_HEIGHT=500

	def __init__(self):
		super().__init__()

		# Create label
		self.label = ttk.Label(self, text="Controls!")
		self.label.pack()

		# Create image
		self.img_dir = "..\\tests\\"
		self.img = Image.open(self.img_dir + "cat-high.jpg")
		(width, height) = self.scale_to_canvas(*self.img.size)
		self.img = self.img.resize((width, height), Image.LANCZOS)

		self.img_tk = ImageTk.PhotoImage(self.img)

		# Create canvas
		self.canvas = tk.Canvas(self, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT,
								bg="black")
		self.canvas.create_image(self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2, image=self.img_tk)
		self.canvas.pack()

	""" Scale an image to the size of the canvas that contains it.

	Make the image the maximum size possible so that either the width or height
	is the same as the canvas width or height respectively. Also maintain the
	aspect ratio of the image when rescaling.

	:param width:	width of the image to scale
	:param height:	height of the image to scale
	:return:		a scaled (width, height) size tuple
	"""
	def scale_to_canvas(self, width, height):
		new_width = 0
		new_height = 0
		if (width < height):
			new_width = self.CANVAS_WIDTH
			new_height = int(height / (width / self.CANVAS_WIDTH))
		else:
			new_width = self.CANVAS_WIDTH
			new_height = int(height / (width / self.CANVAS_WIDTH))

		return (new_width, new_height)
