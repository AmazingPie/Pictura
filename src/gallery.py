import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

""" The gallery component of the main application window.

This class stores previously found images/videos for later use.
"""
class Gallery(ttk.Frame):
    def __init__(self):
        super().__init__()

        label = ttk.Label(self, text="Gallery")
        label.pack()
