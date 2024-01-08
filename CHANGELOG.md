# Changelog

All notable changes to this project will be documented in this file.

## [0.3.1] - 2024-01-08

### Fixed bugs

- Collection view doesn't lose image metadata anymore - [178530f]
- Several tags are saved correctly after edits - [e9b97c1]

### Refined Documentation

- Fix changelog so that it displays the right software version - [0e1d22e]
- Use a new, git-cliff generated changelog format - [4565c24]

### Build

- Bump version - [0fca392]
## [0.3.0] - 2024-01-07

### Features

- *(Imagegallery)* Imagegallery supports editing images - [ecfde12]
- *(Imagegallery)* LibraryToml now supports editing images - [646114a]
- *(Imagegallery)* Create ImageMetadata from dict - [ee5837d]
- *(Imagegallery)* A small skeleton for edit command - [c4d52b4]
- *(Imagegallery)* Add image now supports defining metadata - [5a0476f]
- *(Imagegallery)* Metadata handling for add function - [5d5de87]
- *(Imagegallery)* Create a simple object for image metadata - [ad3daaa]
- *(Imagegallery)* Create a new 'add' functionality for gallery - [79afcc6]
- *(Imagegallery)* Create a class representation for gallery_toml - [5c2e143]
- *(filesystem_operations)* Add a function to save gallery - [04e42d7]
- *(gallery)* Support for adding images - [0df2678]
- *(gallery)* Add get and add to GalleryToml - [57b5b78]
- *(gallerycmd)* Support for editing images - [633fa8b]
- *(gallerycmd)* A first skeleton for edit command - [0c279bf]
- *(gallerycmd)* A small start for proper init command - [508a011]
- *(gallerycmd)* Add functionality now accepts parameters - [0cfc5d3]
- *(gallerycmd)* Add ensures correct metadata is always present - [a7b8b4e]
- *(gallerycmd)* Add function now saves to disk - [730803e]
- *(gallerycmd)* Adding image to imagegallery now possible - [d1c883d]
- *(gallerycmd)* A small start for add command - [27ca222]
- *(gallerycmd)* A skeleton for add command - [5fc4972]
- *(viewer)* Save library when quitting viewer - [5fd201b]
- *(viewer)* Metadata now displays with image - [cce7af9]
- *(viewer)* Add clear method to ImageDetails - [c085a85]
- *(viewer)* ImageDetails properties can be updated - [b136d27]
- *(viewer)* Scale image down when displaying it - [b3200e0]
- *(viewer)* A image detail display - [77d2eba]
- *(viewer)* Add some error handling for gallery-viewer - [cac674c]
- Add check if image exists to GalleryToml - [5ec9baa]
- A simple unittest to add images into gallery - [e19db53]

### Fixed bugs

- *(Imagegallery)* Survive when variables in Imagemetadata are None - [4323d0e]
- *(Imagegallery)* GalleryToml now adds default keys to images - [24c5a93]
- *(Imagegallery)* Reading gallery_toml now populates the object - [aea2595]
- *(gallery)* Remove an unused import that actually broke the build - [21bde37]
- *(gallerycmd)* Fix circular import bug in gallerycmd - [6c0cbde]
- *(librarysaver)* Add some minor error handling for save - [92fadf3]
- *(test)* Remove unneeded hash from example gallery - [0f6e564]
- *(tests)* Fix a failing test - [89877e2]
- *(viewer)* Remove unneeded library import - [dc92488]
- *(viewer)* Switching collection resets current image index - [a94599c]
- *(viewer)* Set Gtk Icon size appropriately - [0850312]
- *(viewer)* Viewer displays icon for missing image again - [800568a]

### Refined Documentation

- *(Imagegallery)* Update some more docstrings - [cd49058]
- *(Imagegallery)* Refine docstrings for File - [d924c67]
- *(blog)* Agile == free software - [f0f9fe7]
- *(blog)* Few fixes to open source == agility post - [fbe5996]
- *(blog)* A draft for a blog about agility - [e83af8c]
- *(blog)* Add a link to installation page - [60e9614]
- *(blog)* Start a series of blog articles - [59d6b84]
- *(dev)* A small skeleton as a start for developer documentation - [6449de3]
- *(developer)* Add bundling dependencies - [8d0323f]
- *(developers)* Small fixes to developer documentation. - [79f0287]
- *(imagemetadata)* Add a small docstring - [1187fff]
- *(todos)* Add dates to todos - [2d1fecd]
- Update screenshot for gallery-viewer - [19a9076]
- Update documentation for 0.3.0 - [49a5883]
- Add CHANGELOG and git cliff configuration to generate it - [b028233]
- Fix term in architecture overview - [04b877e]
- Add TODOs file to project - [a6e3dab]
- Move installation specific stuff to another file - [07346ea]
- Update developer documentation - [c2117da]
- Fix link in README and restructure a bit - [24cf423]
- Add some links to README - [41d5fdc]
- Finally add a GPL-3 licence - [2028fe7]
- Use the right screenshot in 'why' - [10a93f6]
- Add screenshots to README - [c4fe542]
- Insert screenshot to 'why' - [e275667]
- Upload screenshots - [3f06908]
- A small fix to 'why' - [9fda91a]
- Refine 'why' a little bit more - [d26847c]
- Rewrote parts of 'why' document - [a7949fe]
- Add a simple and short "blog post" about whys of the project. - [80c2ffc]
- Remove mention about HTML viewer - [d9a5c8f]
- Update README some more - [19b2b17]

### Build

- Add a 'clean' target - [a656672]
- Fix fpm command to build and output into right dir - [16d24da]
- Create a bin dir for builds - [e340b7c]
- Fix makefile target for viewer - [698d075]
- Change deb package version to 0.3.0 - [232a59d]
- Add help message to Makefile - [e31a2dd]
- Fix the version number in deb package - [94d3847]
- Add a new build system, allowing for deb package builds - [8b1c9a5]
- Add a placeholder/hack setup.py - [002e811]
- Rename Makefile target to dev-environment - [82b65f6]

### Change

- *(Imagegallery)* Add size counting to Collection - [c301721]
- *(Imagegallery)* Collections now contain metadata also - [98e69d7]
- *(Imagegallery)* Make imagemetadata from dict way more lax - [b91a3c2]
- *(Imagegallery)* Add a simple image object - [92fafcb]
- *(Imagegallery)* LibraryToml now returns ImageMetadata objects - [da35119]
- *(collectionviewer)* Include also image metadata - [72129e0]
- *(gallery)* LibraryToml uses ImageMetadata internally - [b9134a1]
- *(gallerycmd)* Add plumbing for edit command - [e3a06d6]
- *(gallerycmd)* Add command now returns with right exit codes - [7940cc5]
- *(imagegallery)* Add indexing related methods to collection - [39c9994]
- *(imagegallery)* Create a factory method for empty collection - [1213ae6]
- *(viewer)* Viewer saves image edits when buttons pressed - [c6735d7]
- *(viewer)* Collectionviewer can save edits made to current image - [46956d6]
- *(viewer)* ImageDetails changes metadat on eject - [21fd262]
- *(viewer)* Imagedetails can now return imagemetadata - [dbfa21a]
- *(viewer)* Add margin to image description field - [6e6efd9]
- *(viewer)* Image details now show in multiline textfield - [ec2a50e]
- *(viewer)* Firmer support for image details - [ef1b882]
- *(viewer)* Add a small stub of image details into collectionviewer - [b26d272]
- *(viewer)* Add Gobject properties to imagedetails - [fce146b]
- *(viewer)* Add a small start for image details display - [71b543c]
- *(viewer)* Move image details right hand side so they fit better - [1672bbc]
- *(viewer)* Add a simple image details display - [f61a3c1]
- Rename viewer binary name - [702939a]

### Editor

- Add emacs configuration variable setup to project - [1402dd3]
## [0.2.0] - 2023-02-12

### Features

- *(viewer)* Add GObject property to CollectionViewer - [eae345f]

### Refined Documentation

- Update README - [df2b7af]
## [0.1.0] - 2022-12-21
<!-- generated by git-cliff -->
