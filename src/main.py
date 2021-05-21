import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

from controls import Controls
from viewport import Viewport
from gallery import Gallery

class Main(ttk.Frame):
	def __init__(self, master):
		super().__init__()

		self.master = master
		self.master.title("Pictura")
		self.controls = Controls(self.update_state)
		self.controls.grid(row=0, column=0)
		self.viewport = Viewport()
		self.viewport.grid(row=1, column=1)
		self.gallery = Gallery()
		self.gallery.grid(row=0, column=1)

	""" Update the state of the globabl application
	This allows individual components of the application communicate their own
	state with each other.

	This is most notably used to allow the controls component to interact with
	and update the viewport and gallery.

	:param name:	name of the state 'variable' to update
	:param value:	value to give the state 'variable'
	"""
	def update_state(self, name, value=None):
		if (name == "img"):
			self.viewport.update_image(value)
		elif (name == "new_img_window"):
			window = tk.Toplevel(self.master)
			self.viewport.create_img_window(window)
		elif (name == "toggle_borders"):
			self.viewport.toggle_borders()
		else:
			print("No state 'variable' called: ", name)

root = tk.Tk()
main_window = Main(root)
main_window.mainloop()
