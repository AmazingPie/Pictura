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
        print("Thumbnail for: " + self.filename)
