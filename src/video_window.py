import tkinter as tk, threading
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import imageio

import time

""" A scalable looping video window.

Plays a video file (mp4, gif, webm) on loop forever.
"""
class VideoWindow(ttk.Frame):
	def __init__(self, window, filename):
		super().__init__(window)
		self.pack(fill="both", expand=True)

		self.label = tk.Label(self)
		self.label.pack()

		self.video = imageio.get_reader(filename, loop=True)

		thread = threading.Thread(target=self.stream, args=())
		thread.daemon = True
		thread.start()

	""" Play a frame of the video stream. """
	def stream(self):
		while True:
			video = self.video
			for image in video.iter_data():
				frame = ImageTk.PhotoImage(Image.fromarray(image))
				self.label.config(image=frame)
				self.label.image = frame
