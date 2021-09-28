from PIL import Image, ImageTk
import imageio

from file.file import File, FileType
import window.video_window as vw

""" A representation of a video file. """
class VideoFile(File):
    def __init__(self, filename):
        super().__init__(filename, FileType.VIDEO)

    """ Create a new looping video window. """
    def create_window(self):
        super().create_window()
        self.video_window = vw.VideoWindow(self.window, self.filename)

    """ Return a thumbnail of given height and width for this video. """
    def get_thumbnail(self, width, height):
        reader = imageio.get_reader(self.filename)
        image = Image.fromarray(reader.get_next_data())
        image.thumbnail((width, height))
        return ImageTk.PhotoImage(image)
