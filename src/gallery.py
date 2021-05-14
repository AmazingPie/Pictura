import tkinter as tk

class Gallery(tk.Frame):
	def __init__(self):
		super().__init__()

		label = tk.Label(self, text="Gallery")
		label.pack()
