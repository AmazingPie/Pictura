import tkinter as tk

from controls import Controls
from viewport import Viewport
from gallery import Gallery

class Main(tk.Frame):
	def __init__(self, master):
		super().__init__()

		self.master = master
		self.master.title("Pictura")
		#self.pack()
		self.controls = Controls()
		self.controls.grid(row=0, column=0)
		self.viewport = Viewport()
		self.viewport.grid(row=1, column=1)
		self.gallery = Gallery()
		self.gallery.grid(row=0, column=1)



root = tk.Tk()
main_window = Main(root)
main_window.mainloop()
