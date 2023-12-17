import gi
from Imagegallery import Image, Collection
from viewer.logic.imagedetails import ImageDetails

gi.require_version("Gtk", "3.0")
from gi.repository import GObject


class CollectionViewer(GObject.Object):

    current_index = 0
    current_image_path = GObject.Property(type=str, default="")
    current_image_details :ImageDetails
    collection :Collection

    def __init__(self) -> None:
        super().__init__()
        self.current_image_details = ImageDetails()
        self.collection = Collection.create_empty()

    def has_images(self):
        return not self.collection.is_empty()

    def empty(self):
        self.collection.images = []
        self.current_image_details.clear()

    def count(self):
        return len(self.collection.images)

    def go_next(self):
        if self.current_index < len(self.collection.images) - 1:
            self.current_index = self.current_index + 1
            self._update_current_image()
        return self

    def go_prev(self):
        if self.current_index > 0:
            self.current_index = self.current_index - 1
            self._update_current_image()
        return self

    def load_collection(self, collection: Collection):
        self.empty()
        self.collection = collection
        self._update_current_image()

    def current_image(self) -> Image:
        return self.collection.images[self.current_index]

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

    def save_collection(self):
        pass
