## Installation

You can install this program by just downloading a binary file from releases and running it on your computer.

If you don't know how to do that, there's also an deb-installation package for Ubuntu and probably other Debian-like operating systems.

[Head to releases and download this!](https://github.com/heikkiket/gallery/releases)

### Installing PyGObject

**In Ubuntu (and hopefully Debian as well):**
Install following packages: `python3-gi python3-gi-cairo gir1.2-gtk-3.0`

**In Fedora:**
Install following packages: `python3-gobject gtk3`

You can find more information and help about installing PyGObject from their official documentation: https://pygobject.readthedocs.io/en/latest/getting_started.html

## Technical details

This software is written in Python. Binaries are self-containing and self-extracting python archives. They are made with a tool called `shiv`. When ran, they create a hidden directory `~/.shiv` and download needed dependencies inside that.
