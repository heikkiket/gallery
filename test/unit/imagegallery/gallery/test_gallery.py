from Imagegallery import Gallery

def test_gallery():
    gallery = Gallery({})
    assert gallery.images() == []
    assert not gallery.has_images()

def test_initiating(gallery_toml):
    gallery = Gallery(gallery_toml)
    gallery.has_images()

def test_list_images(gallery_toml):
    gallery = Gallery(gallery_toml)
    assert gallery.images() == [
        "path/to/image1.jpg",
        "path/to/image2.jpg",
        "path/to/image3.jpg"
    ]
