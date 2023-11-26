import gi
from Imagegallery import Image, ImageFile, Collection
from viewer.logic.imagedetails import ImageDetails

gi.require_version("Gtk", "3.0")
from gi.repository import GObject


class CollectionViewer(GObject.Object):

    current_index = 0
    current_image_path = GObject.Property(type=str, default="")

    def __init__(self) -> None:
        super().__init__()
        self.images: list[Image] = []
        self.current_image_details = ImageDetails()

    def has_images(self):
        return len(self.images) > 0

    def add_images(self, images: list[Image]):
        self.images = images
        self._update_current_image()

    def empty(self):
        self.images = []

    def count(self):
        return len(self.images)

    def current_image(self) -> Image:
        return self.images[self.current_index]

    def _update_current_image(self):
        if self.has_images():
            self._update_current_image_path()
            self.current_image_details.set_image_metadata(
                self.current_image().metadata
            )

    def _update_current_image_path(self):
        if self.has_images():
            self.props.current_image_path = self.current_image().file.path_as_bytes()
        else:
            self.props.current_image_path = ""


    def go_next(self):
        if self.current_index < len(self.images) - 1:
            self.current_index = self.current_index + 1
            self._update_current_image()
        return self

    def go_prev(self):
        if self.current_index > 0:
            self.current_index = self.current_index - 1
            self._update_current_image_path()
        return self

    def load_collection(self, collection: Collection):
        self.empty()
        self.add_images(collection.images)
