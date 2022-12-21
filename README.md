# gallery
## A simple image gallery

This image gallery is meant to be a minimalistic, simple and plain-text centric tool for your personal photo management.

Your image gallery is just a directory tree containing pictures plus a gallery.toml file. An example directory tree could look like this:
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
└── gallery.toml
```

In this image gallery pictures are organized to `year-month-day` directory structure. You can use whatever structure you want, of course.

## gallery.toml fileformat

All the metadata is saved to a gallery.toml file. It looks like this:

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

The idea here is that the whole gallery.toml is easily hackable so you (or others) can extend the system however you like.

## gallery command

There is a simple, alpha-level utility called `gallery` that can be used to manipulate this gallery. Currently it has two functions.

### gallery list
This command lists all the pictures in the gallery.toml. It checks that every image really exists on the disk and prints out *** FILE MISSING *** for ones that don't exist. Just go to the directory where gallery.toml sits and issue this command there.

You can also filter pictures by tag:

`gallery list --tag nature`
This gives you a list of all pictures tagged "nature".

### gallery init
This command creates a new gallery.toml by collecting all the image files from the current work directory and its subdirectories. It does not save the file anywhere but only prints its contents out. You can easily create a gallery.toml file by piping results into file. Following command overwrites an earlier gallery.toml.

```
gallery init > gallery.toml
```

## A demo image viewer
There is a simple image viewer program running inside browser. Just save this gallery.html to the same dir with gallery.toml.

Run this program by opening the file in the web browser and then uploading gallery.toml via the form visible. You need to explicitly upload a gallery.toml because a web browser cannot read files from local filesystem by default.
