# gallery
## A simple image gallery

This image gallery is meant to be a minimalistic, simple and plain-text centric tool for your personal photo management.

This project has three parts:

 * specification for a simple image gallery
 * command line tool for managing image gallery
 * simple viewer program

## Useful links
Before we hop to all that, here's some links that give you a quick jump to other parts of documentation

 - [Installation](INSTALL.md)
 - [Why a world needs an UNIX-style image collection manager?](docs/why.md)
 - [Blog](docs/blog)

## gallery specification

Your image gallery is just a directory tree containing pictures plus a library.toml file. An example directory tree could look like this:
```
~/Pictures/gallery/
├── 2021
│   └── 12
│       └── 15
│           └── image1.png
├── 2022
│   ├── 01
│   │   └── 15
│   │       └── image2.png
│   └── 03
│       └── 02
│           └── image3.jpg
└── library.toml
```

In this image gallery pictures are organized to `year-month-day` directory structure. You can use whatever structure you want, of course.

### library.toml fileformat

All the metadata is saved to a library.toml file. It looks like this:

```
["Wallpapers/Studio_Ghibli_Laputa_Laputa_Castle_in_the_Sky_Movie_Screenshots_far_view_anime_animated_movies-1845525.jpg"]
title = ""
description = ""
tags = ['movie', 'Laputa']

["holiday pictures/IMG_20220301_130811.jpg"]
title = "In the forest"
description = ""
tags = ['nature', 'forest']

["holiday pictures/IMG_20220301_132625.jpg"]
title = "A huge tree"
description = ""
tags = ['nature', 'tree', forest]

["holiday pictures/IMG_20220301_132650.jpg"]
title = "Nice rock"
description = "This is a nice rock I found"
tags = ['nature', 'rock']

```

Basically you just reference every image with its path and then give it title, description and tags. This file is easy to write by hand and pretty human-readable as well, but you can also generate and handle it automatically.

The idea here is that the whole library.toml is easily hackable so you (or others) can extend the system however you like.

## gallery command

![Picture of gallery command line tool](./docs/screenshots/gallery-cmd.png)

There is a simple, alpha-level utility called `gallery` that can be used to manipulate this gallery. Currently it has following functions.

 * init
 * list
 * add
 * edit

The basic idea with this command and all these utilities is similar to for example Git: you use this command at the root of your image library. For example, if your images reside in `~/Photos/test_image_library`, then you will run all these commands in that directory.

In that same directory resides your `library.toml` file.

### gallery list
This command lists all the pictures in the library.toml. It checks that every image really exists on the disk and prints out *** FILE MISSING *** for ones that don't exist. Just go to the directory where library.toml sits and issue this command there.

You can also filter pictures by tag:

`gallery list --tag nature`
This gives you a list of all pictures tagged "nature".

### gallery init
This command creates a new library.toml by collecting all the image files from the current work directory and its subdirectories. It does not save the file anywhere but only prints its contents out. You can easily create a library.toml file by piping results into file. Following command overwrites an earlier library.toml.

```
gallery init > library.toml
```

### gallery add
This command adds a new file into library.toml file.
One can define title, description or tags for an image by using this. Only filename is a mandatory argument.

    gallery add -t "My image title" -d "A description for this image" --tags tag1 tag2 tag3 my_image.jpg

### gallery edit
With this you can edit image in a photo library. The command syntax is basically identical with add command.

    gallery edit -t "My edited image title" -d "A new description" --tags newtag1 tag1 tag2 tag3 my_image.jpg

If you only want to edit for example title, just give that argument like so:

    gallery edit -t "My edited image title" my_image.jpg

## gallery-viewer (GTK)

![Picture of gallery-viewer](./docs/screenshots/gallery-viewer.png)

gallery-viewer is a simple GTK-based program that can be started from command line and used to view images in the gallery. Start the program in the same directory that contains a library.toml file.

Gallery-viewer actually allows also editing image metadata. So you can do quick fixes to your image library with that!

In order to function gallery-viewer needs python3 installed in the host system as well as PyGobject library.

## Go and install it!
 Head to [INSTALL.md](INSTALL.md) to find out how!

## Check out changelog
I have a ugly but functional [CHANGELOG.md](CHANGELOG.md) generated with [git-cliff](https://github.com/orhun/git-cliff).

## Want to contribute?
I value that greatly! Head on to [CONTRIBUTING.md](./CONTRIBUTING.md) to find out how to build the project.
