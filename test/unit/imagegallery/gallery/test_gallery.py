from Imagegallery import GalleryToml

def test_gallery():
    gallery = GalleryToml({})
    assert gallery.filenames() == []
    assert not gallery.has_images()

def test_initiating(gallery_toml):
    gallery = GalleryToml(gallery_toml)
    gallery.has_images()

def test_list_images(gallery_toml):
    gallery = GalleryToml(gallery_toml)
    assert gallery.filenames() == [
        "path/to/image1.jpg",
        "path/to/image2.jpg",
        "path/to/image3.jpg"
    ]
