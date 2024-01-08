from pathlib import Path

from PhotoLibrary import ImageFile


def test_imagefile_has_filename():
    image = ImageFile(Path("foo.img"), "jpg")
    assert image.name == "foo.img"

def test_imagefiles_have_different_names():
    img1 = ImageFile(Path("img1.jpg"), "jpg")
    img2 = ImageFile(Path("img2.jpg"), "jpg")
    assert img1.name == "img1.jpg"
    assert img2.name == "img2.jpg"

def test_imagefile_returns_path_as_bytes():
    img1 = ImageFile(Path("img1.jpg"), "jpg")
    assert img1.path_as_bytes() == "img1.jpg"
