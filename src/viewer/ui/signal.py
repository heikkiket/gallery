from gi.repository import GObject


class Signal(GObject.GObject):

    switch_to_gallery_view = "switch_to_gallery_view"
    @GObject.Signal(name=switch_to_gallery_view)
    def _switch_to_gallery_view_handler(self):
        pass


signal = Signal()
