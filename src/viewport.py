import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

import image_window

class Viewport(ttk.Frame):
	CANVAS_WIDTH=500
	CANVAS_HEIGHT=500

	def __init__(self):
		super().__init__()

		self.borderless = False
		self.img_windows = []

		# Create label
		self.label = ttk.Label(self, text="Controls!")
		self.label.pack()

		# Create canvas
		self.canvas = tk.Canvas(self, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT,
								bg="black")
		self.canvas.pack()

	""" Update the viewport image with the image given by the filename. """
	def update_image(self, filename):
		self.filename = filename
		# Make the scaled image
		img = Image.open(filename)
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
			new_height = self.CANVAS_HEIGHT
			new_width = int(width / (height / self.CANVAS_HEIGHT))
		else:
			new_width = self.CANVAS_WIDTH
			new_height = int(height / (width / self.CANVAS_WIDTH))

		return (new_width, new_height)

	""" Create a new zoomable image window.

	Because Viewport is a component and not the main application window we
	must be passed the basic empty window (Toplevel widget) which we will set
	up.

	:param window: a new empty window
	"""
	def create_img_window(self, window):
		self.img_windows.append(window)

		window.title("Image")
		window.geometry("500x500")
		window.overrideredirect(self.borderless)
		img_window = image_window.ImageWindow(window=window, filename=self.filename)

	""" Remove the borders from all image windows. """
	def toggle_borders(self):
		for window in self.img_windows:
			window.overrideredirect(not self.borderless)	# toggle border

		self.borderless = not self.borderless	# toggle the border state
