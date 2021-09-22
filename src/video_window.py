import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

""" A scalable looping video window.

Plays a video file (mp4, gif, webm) on loop forever.
"""
class VideoWindow(ttk.Frame):
	def __init__(self, window, filename):
		super().__init__(window)
		pass
