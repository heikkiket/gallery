This is a simple method to pass signals around in your application.

In some situations you need to pass signals between components or processes. For example, if you need to pass an event between two widgets that are in the different sides of the same application.

When I ran into this kind of problem in my application, I decided to define a global singleton class named Signal.

Here's the definition, in its entirety.

```
class Signal(GObject.Object):

    SWITCH_TO_COLLECTIONGRID_VIEW = "switch_to_collectiongrid_view"
    @GObject.Signal(name=SWITCH_TO_COLLECTIONGRID_VIEW)
    def _switch_to_collectiongrid_view_handler(self):
        pass

signal = Signal()
```

This is actually a pretty verbose way to do this. The handler function definition here is just plain useless and only needed for the Python decorator, `@Signal`. I'm hoping to find a way to just define a signal.

Now, when I want to define an actual signal handler, I do something like this:

```
from signal import signal

class Mainwindow(Gtk.ApplicationWindow):
    def __init__(self,
        signal.connect(signal.SWITCH_TO_COLLECTIONGRID_VIEW,
                       self.switch_to_collectiongrid_view)

    def switch_to_collectiongrid_view(self, _):
        print("Switched to collection grid view")
```

And then I can emit the signal from anywhere in my application like this:

```
from signal import signal

    def click_handler():
        signal.emit(signal.SWITCH_TO_COLLECTION_GRID_VIEW)
```
