from gi.repository import GObject


class Signal(GObject.Object):

    SWITCH_TO_COLLECTIONGRID_VIEW = "switch_to_collectiongrid_view"
    @GObject.Signal(name=SWITCH_TO_COLLECTIONGRID_VIEW)
    def _switch_to_collectiongrid_view_handler(self):
        pass

    SWITCH_TO_IMAGE_VIEW = "switch_to_image_view"
    @GObject.Signal(name=SWITCH_TO_IMAGE_VIEW)
    def _switch_to_image_view_handler(self):
        pass

    SWITCH_TO_COLLECTION = "switch_to_collection"
    @GObject.Signal(name=SWITCH_TO_COLLECTION, arg_types=[str])
    def _switch_to_collection_handler(self, hash):
        pass


signal = Signal()
