import tkinter as tk

class Controls(tk.Frame):
	def __init__(self):
		super().__init__()

		label = tk.Label(self, text="Controls!")
		label.pack()

