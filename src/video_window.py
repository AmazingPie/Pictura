import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import vlc

""" A scalable looping video window.

Plays a video file (mp4, gif, webm) on loop forever.
"""
class VideoWindow(ttk.Frame):
	def __init__(self, window, filename):
		super().__init__(window)
		self.pack(fill="both", expand=True)

		# Create vlc instance and objects
		self.instance = vlc.Instance("--mouse-hide-timeout=1000")
		self.list_player = self.instance.media_list_player_new()
		self.player = self.list_player.get_media_player()
		media_list = self.instance.media_list_new([filename])

		# Configure media
		self.list_player.set_media_list(media_list)
		self.list_player.set_playback_mode(vlc.PlaybackMode.loop)
		self.player.set_hwnd(self.winfo_id()) 		# Use our window
		self.player.audio_set_mute(True)

		self.list_player.play()

	def __del__(self):
		self.player.stop()
