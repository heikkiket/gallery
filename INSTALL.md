## Installation

You can install this program by just downloading a binary file from releases and running it on your computer.

If you don't know how to do that, there's also a deb-installation package for Ubuntu and probably other Debian-like operating systems.

[Head to releases and download it!](https://github.com/heikkiket/gallery/releases)

If you aren't sure how to install and run these files, don't worry! This is an alpha level software, so if you can't install it, probably you couldn't use it either. Wait for few years and maybe this thing takes over the world! Then installation and usage will hopefully be easy.

### Installing PyGObject

If you downloaded a binary file, you need to install PyGObject by hand in order to run the gallery-viewer.

**On Ubuntu and Debian:**
Install following packages: `python3-gi python3-gi-cairo gir1.2-gtk-3.0`

**On Fedora:**
Install following packages: `python3-gobject gtk4`

**On Arch:**
Install following packages: `python3-gobject gtk4`

You can find more information and help about installing PyGObject from their official documentation: https://pygobject.readthedocs.io/en/latest/getting_started.html

## Technical details

This software is written in Python. Binaries are self-containing and self-extracting python archives. They are made with a tool called `shiv`. When ran, they create a hidden directory `~/.shiv` and download needed dependencies inside that.
