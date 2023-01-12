from viewer.ui.mainwindow import Mainwindow
from viewer.logic.viewer import Viewer
from Imagegallery import Imagegallery

from viewer.ui.widgets.imageviewer import ImageViewerWidget

def main():

    imagegallery = Imagegallery.from_disk()

    images = []
    paths = imagegallery.filetree.flatten().keys()

    for path in paths:
        images.append(path)

    viewer = Viewer()
    viewer.add_images(images)

    app = Mainwindow(
        ImageViewerWidget(
            model=viewer
        )
    )
    app.start()
