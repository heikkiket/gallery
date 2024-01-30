# Developing an application with GTK

I started doing GTK application development with Python little bit over a year ago. It has been easy and delightful experience and I'd like to tell about my findings a bit.

## Background
I chose Python as a language because it is pretty popular, general-purpose language and because GTK had reasonably good documentation for it.

I chose my development language by rejecting worse options: I won't touch C unless someone pays me significant amounts of money, Vala is a special language used only by Gnome projects and Gnome's JavaScript is not the same thing as JavaScript I know from web development world. I probably couldn't use all the JS innovations from last ten years. At least this is what I do believe! Maybe someone proves me wrong. And while Rust is a nice and interesting language, I think it is pretty low-level for graphical desktop applications.

In reality the quality of documentation could be a lot better, of course. That's the main reason I decided to write this blog: I hope I can do my part bridging the gap between Hello World examples, Python GTK 3 tutorial and API documentation.

But in general it's not too bad if you already know how to program.

If you don't, there's plenty of nice Python tutorials out there. And when you have something working, it's pretty easy to add GUI parts with GTK on top of that.

## My development environment
I use LTS Ubuntu with Gnome desktop for development. My editor of choice is Emacs, because I use it otherwise. It is important for me to use a free, native, general purpose editor that handles all my programming needs.

But I recommend trying Gnome builder. I have sometimes tried Gnome development with it and it's great. Learning Emacs takes away few years you could use for better purposes, e.g. developing free software. On the other hand, Emacs may be the last software you have to learn ;)

I use LSP and Microsoft's language server for Python. As a test framework I chose pytest. I do my development inside Python virtual environment.

I think every developer deserves a proper, native, stand-alone terminal emulator. My terminal of choice is Tilix.

I push allmy code to Github. I don't feel good hosting my free software project in proprietary service.

## Nature of GTK

If you have ever been working with 90's style native UI kits like JavaFX or .Net or whatever else, working with GTK feels familiar. Every user interface element is an object that can contain other objects. We interact with them via an object-oriented API.

That means code gets easily filled with getters and setters where I put one object inside other or pull from one object a reference to another in order to set some third object inside it. Also, you sometimes have to 'show' or 'activate' things with separate call. At least you have to show a window when you create it.

This is a pretty stark contrast (or at least a mild one) to a present-day Web UI frameworks like React or Vue or whatever, where stuff is composed from components by using HTML-like template code and data flows via properties from parents to children.

And of course you have to write signal and action handlers, but that is pretty similar to what one does with JS frameworks.

Usually one doesn't worry about references when developing with those frameworks. In this sense GTK feels more "low-level". In reality references between components of course exist in JavaScript frameworks as well. And with Python there's no need to worry about references other than passing them around. No memory management or anything like that.

## Creating UI:s

I define all UI:s via XML documents, in pure 90's/00's style. I don't like XML at all so I used Glade to do UI design. I don't like Glade either, because it has so weird and clunky user interface. I found a project called Cambalache which I plan to move next. There is a little bit of porting in order to move my .ui files to work with it.

I use functionality called Gtk.Template which allows me to load those XML files as part of my Python classes.

I have to insert a little bit of boilerplate to do it, but only few lines.

Here's an example what it takes to load a .ui file and combine it with a class:
```
template = os.path.dirname(__file__) + "/mainwindow.ui"

@Gtk.Template(filename=template)
class Mainwindow(Gtk.ApplicationWindow):
    __gtype_name__ = "main_window"
```

I'm trying to keep my UI definitions small. I define small fragments (maybe I could call them views?) which I compose together in code.

## Development style
My general development style is pretty object-oriented. I create a lot of small objects that reference to other small objects. Almost all functionality in my application is realised with one object talking to bunch of others.

I also test almost all my code with unit tests. This means most of the time I have already a working feature before any of it shows in the screen.

Doing a lot of unit testing affects to my architecture. I have to separate GTK-related code from my actual application logic. More about that in next section.

I do small commits, usually several per hour, into a single main branch of my git repository.


## Architecture of this application

In general I have a three-level architecture in my application: a library module, an I/O module and a GUI application part.

I try to push all the actual functionality  into the library module that offers a clean object API outside. I/O module handles writing and reading to the disk. The GTK stuff I put into the GUI application module.

Inside GUI application module I divide functionality into two sub-modules: a model-part and a presenter/view sub-module. I first coined this architecture and then decided to call it Model-View-Presenter in the spirit of this Wikipedia article: https://en.m.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter

I'm not too pedantic about naming, patterns and such, but I like to call my creations with precise and hopefully canonical names.

Model sub-module consists of calls to my library code and offering simple properties and hooks to my presenter/view sub-module. Model also carries some simple logic that is tightly related to GUI application itself.

For example, I have next/previous buttons to browse images back and forth and for them I need a simple boundary-checking logic to prevent browsing past the list end.

This way I can put all the GTK-related code into the presenter/view sub-module of my application. My goal is that in this sub-module there isn't a single if statement and hopefully not any for loops. Or in other words: no application logic lives inside presenter/view subsection of GUI module.

And on the other hand: no dependencies to GTK exists outside GUI module.

I also try to keep the model sub-module of my GUI unit-testable. That means only GTK dependency allowed inside GUI/model is GObject dependencies: I don't want to mock any gui elements or suchlike. This way I can bind GObject properties from model to view/presenter submodule and on the other hand easily test my GObject property logic with unit tests.

Here's one example of a model, inheriting GObject.Object:
```
class ImageDetails(GObject.Object):
    title = GObject.Property(type=str, default="")
    description = GObject.Property(type=str, default="")
    tags = GObject.Property(type=str, default="")
```

And this is the sample unit test for it:

```
def test_image_details_has_needed_properties():
    assert ImageDetails().get_property("title") == ""
    assert ImageDetails().get_property("description") == ""
    assert ImageDetails().get_property("tags") == ""
```

I have modelled all my user interfaces with a separate Cambalache application and exported them as .ui files. In addition, I have widget classes defined with Gtk.Template decorator, and there I connect all the signals and define click handlers and such.

I call these classes "presenters", think my ui-files as views and put inside these presenter classes a member property called "model" which references a model object from the model sub-module of my application.

Here's an example of a widget class, playing a role of presenter:

```
template = os.path.dirname(__file__) + "/imagedetails.ui"

@Gtk.Template(filename=template)
class ImageDetailsWidget(Gtk.Box):
    __gtype_name__ = "imagedetails"

    def __init__(self, model :ImageDetails = ImageDetails()):
        super().__init__()

        self.model = model
        self.model.bind_property("title", self.title, "text",
                                 GObject.BindingFlags.BIDIRECTIONAL)
        self.model.bind_property("description", self.description.get_buffer(), "text",
                                 GObject.BindingFlags.BIDIRECTIONAL)
        self.model.bind_property("tags", self.tags, "text",
                                 GObject.BindingFlags.BIDIRECTIONAL)
```

Actually, this is the class almost in its entirety. Note how declarative the code here is, when all the application logic resides in the model. GObject properties allow also declaring data bindings between model and presenter without any logic or model method calls.

Here's also an example of my simple dependency injection style, where model is passed as a parameter to the class during instantiation.

In general I think it is good to separate all external library dependencies from the core application logic. My idea is that later I can easily move to a newer version of GTK. Also it would be possible to port my core application logic into some more performant language than Python if needed.

## My experiences
Developing with GTK and PyGObject is not too bad at all, in my opinion. It is a little bit more complicated than using modern Web UI frameworks like React or Vue in a sense that somewhat more boilerplate is needed.

Also, I had to come up a good architecture by myself. For example with Vue it is basically pretty easy to separate all logic to a VueX state and use means it provides (actions, mutations, getters and so on) to wire data into the components and create almost declarative component syntax.

On the other hand, Vue and React actually use some pretty modern/advanced programming paradigms, often originating from functional programming. Python plus GTK is pretty simple stuff and can be done with almost imperative style, only a little bit of object-oriented strucrures on the side.

Of course I'm not sure how a beginner programmer sees these matters. Is Python with GTK a PHP-like combination where it is easy to write quick and dirty, hacky code and get things done? I myself value that kind of easiness although I'm a great proponent of clean code and clean architecture.

And is it actually a pro that PyGObject is more Object-oriented than functional in style? I would need to do some more tinkering in ordee to find out how well GTK supports functional-style application development.

## Simple prototyping

The best bit with PyGObject is that in modern Ubuntu you only need to install one package, open whatever text editor and you're scripting and developing already. I would recommend this combo for your own simple utility applications where you only want a simple gui for example to run few command line commands.

Another nice aspect of quick prototyping is GUI builders that can be used with Gtk.Template. That way one needs to just write few lines of GTK-related code and the rest will be just plain Python.
