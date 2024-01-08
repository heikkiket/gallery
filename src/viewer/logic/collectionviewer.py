import gi
from Imagegallery import Image, Collection
from viewer.logic.imagedetails import ImageDetails

gi.require_version("Gtk", "3.0")
from gi.repository import GObject


class CollectionViewer(GObject.Object):

    current_index :int
    current_image_details :ImageDetails
    collection :Collection

    current_image_path= GObject.Property(type=str, default="") 

    def __init__(self) -> None:
        super().__init__()
        self._reset_index()
        self.current_image_details = ImageDetails()
        self.collection = Collection.create_empty()

    def load_collection(self, collection: Collection):
        self.collection = collection
        self._reset_index()
        self._update_current_image()

    def has_images(self):
        return not self.collection.is_empty()

    def count(self):
        return self.collection.size()

    def current_image(self) -> Image:
        return self.collection.nth(self.current_index)

    def go_next(self):
        if self.collection.has_after(self.current_index):
            self.save_image_edits()
            self.current_index = self.current_index + 1
            self._update_current_image()
        return self

    def go_prev(self):
        if self.collection.has_before(self.current_index):
            self.save_image_edits()
            self.current_index = self.current_index - 1
            self._update_current_image()
        return self

    def save_image_edits(self):
        """Saves edits made to current image details into collection"""
        self.current_image().metadata = self.current_image_details.eject_metadata()

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

    def _reset_index(self):
        self.current_index = 1

