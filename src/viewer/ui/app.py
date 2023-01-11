from viewer.ui.mainwindow import Mainwindow
from viewer.logic.viewer import Viewer
from Imagegallery import Imagegallery

def main():

    imagegallery = Imagegallery()
    imagegallery.load()

    images = []
    paths = imagegallery.filetree.flatten().keys()

    for path in paths:
        images.append(path)

    app = Mainwindow()
    viewer = Viewer()
    viewer.add_images(images)
    app.imageviewerwidget.set_viewer(viewer)
    app.start()
