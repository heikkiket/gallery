# Why a world needs an UNIX-style image collection manager?

It doesn't, but I do. That's why I'm prototyping the idea. I'll try to describe what I'm after.

I have never liked any of the photo management applications I have tried on my Linux machine. Most of them feel like they lock me up with themselves. I start to manage my image gallery there and I'm now married with this one tool. Moreover, I can't easily sync my image collection between several devices.

Most of those tools don't let me easily move and rename my photos on disk. All their edits are done in their own database and own image store. Those that let me modify images on disk still store all the image metadata in their own database.

I want a simple photo management solution. Photos sit in a directory tree and all the metadata sits next to them, in a plain text file. Sounds familiar? This is what I think Unix philosophy is about. Simple hierarchical directory tree, plain text metadata.

That kind of photo collection is easy to sync with Rsync, Nextcloud or whatever tool.

## How to create a simple photo library

Create a directory tree containing pictures plus a library.toml file. An example directory tree could look like this:
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

In this image gallery pictures are organized to `year/month/day` directory structure. You can use whatever structure you want, of course.

All the metadata is saved to a library.toml file. It looks like this:

```
["2021/12/15/image1.png"]
title = "A beautiful flower"
description = "I saw this flower when walking in a forest"
tags = ['nature', 'flower']

["2022/01/15/image2.jpg"]
title = "In the forest"
description = "This is a moody photo I took during a walk"
tags = ['nature', 'forest']

```

And that's it!

Gallery.toml file uses TOML syntax, so basically one can put whatever keys and things there. Currently just those in the example are supported: title, description and tags. I couldn't come up with anything more that I would need.

## What are my next plans

My idea is that anyone computer-savvy can understand this thing and do whatever they want with it. Syncing galleries over Nextcloud or Rsync? Diffing metadata? Creating machine learning tool that automatically generates titles for all the images? Why not!

Will this scale? I dont know, but I don't have hundreds of thousands of photos anyway, so I believe it's good enough for me.

Currently this whole thing is pre-alpha state. It would help me tremendously if you could review this, test this or even leave some comments about your ideas. I have built the first version with Python, because it's a fast prototyping tool. Maybe one day I will rewrite it with Rust ;)

## How you can try this

I have two sample programs to manage this gallery: one is a command line utility called `gallery` which currently lets you to list and query your images. Another one is `gallery-viewer`, a really simple GTK 3 application for viewing images.

![Picture of gallery command line tool](./screenshots/gallery-cmd.png)

More info about how to install and use them can be found from [README](../README.md).
