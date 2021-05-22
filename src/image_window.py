import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

import time

NANO_TO_MILI = 1000000  # Divide time_ns() by this to get time in ms.

class ImageWindow(ttk.Frame):
    REFRESH_RATE = 150  # Time in ms between refreshing image when resizing.

    def __init__(self, window, filename):
        super().__init__(window)
        self.pack(fill="both", expand=True)

        self.ms_between_event = time.time_ns() // NANO_TO_MILI

        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.update()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind("<MouseWheel>", self.on_scroll)    #windows only
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<Configure>", self.on_resize)

        # Create the image
        self.img = Image.open(filename)
        (width, height) = self.scale_to_canvas(*self.img.size)
        self.current_size = (width, height)
        img = self.img.resize((width, height), Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)

        self.img_x = self.canvas_width / 2
        self.img_y = self.canvas_height /2
        self.img_canvas = self.canvas.create_image(self.img_x,
                                               self.img_y,
                                               image=self.img_tk)

    """ Scale an image to the size of the canvas that contains it.

    Make the image the maximum size possible so that either the width or height
    is the same as the canvas width or height respectively. Also maintain the
    aspect ratio of the image when rescaling.

    :param width:   width of the image to scale
    :param height:  height of the image to scale
    :return:        a scaled (width, height) size tuple
    """
    def scale_to_canvas(self, width, height):
        new_width = 0
        new_height = 0
        if (width < height):
            new_height = self.canvas_height
            new_width = int(width / (height / self.canvas_height))
        else:
            new_width = self.canvas_width
            new_height = int(height / (width / self.canvas_width))

        return (new_width, new_height)

    """ Handle a scrollwheel event. """
    def on_scroll(self, e):
        if (e.delta < 0):   #scroll down -- zoom out
            (width, height) = map(lambda x : int(x * (1/1.1)), self.current_size)
            self.current_size = (width, height)
            img = self.img.resize((width, height), Image.HAMMING)
        else:               #scroll up   -- zoom in
            # Resize image.
            (width, height) = map(lambda x : int(x * 1.1), self.current_size)
            self.current_size = (width, height)
            img = self.img.resize((width, height), Image.BILINEAR)

            # Move image a little closer to the mouse pointer.
            delta_x = (self.img_x - e.x) // 4
            delta_y = (self.img_y - e.y) // 4
            self.canvas.move(self.img_canvas, delta_x, delta_y)

        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.img_canvas, image=self.img_tk)

    """ Handle an event when the mouse moves after being pressed. """
    def on_drag(self, e):
        # Work out how far the mouse moved (should be 1,-1 or 0).
        delta_x = self.img_x - e.x
        delta_y = self.img_y - e.y
        # For the first movement our self.img_* is not set correctly so ignore
        # the first movement.
        if ((abs(delta_x) > 1) | (abs(delta_y) > 1)):
            self.img_x = e.x
            self.img_y = e.y
            return
        self.canvas.move(self.img_canvas, -delta_x * 3, -delta_y * 3)

    """ Handle an event when the canvas/window has been resized. """
    def on_resize(self, e):
        # Only refresh the screen every REFRESH_RATE(ms) to reduce lag.
        current_time = time.time_ns() // NANO_TO_MILI
        if (current_time < self.ms_between_event + self.REFRESH_RATE):
            return
        else:
            self.ms_between_event = current_time

        # Get our new size.
        self.canvas_width = e.width
        self.canvas_height = e.height
        self.current_size = self.scale_to_canvas(*self.current_size)

        # Resize and re-locate our image on the canvas.
        img = self.img.resize(self.current_size, Image.BILINEAR)
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.img_canvas, image=self.img_tk)
        self.canvas.coords(self.img_canvas, e.width / 2, e.height / 2)
