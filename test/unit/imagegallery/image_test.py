from pathlib import Path

from Imagegallery import ImageFile


def test_image_has_filename():
    image = ImageFile(Path("foo.img"), "jpg")
    assert image.name == "foo.img"

def test_images_have_different_names():
    img1 = ImageFile(Path("img1.jpg"), "jpg")
    img2 = ImageFile(Path("img2.jpg"), "jpg")
    assert img1.name == "img1.jpg"
    assert img2.name == "img2.jpg"

def test_image_returns_path_as_bytes():
    img1 = ImageFile(Path("img1.jpg"), "jpg")
    assert img1.path_as_bytes() == "img1.jpg"
