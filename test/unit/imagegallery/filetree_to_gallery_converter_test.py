import pytest

from Imagegallery.filetree import Filetree

def test_empty_filetree_returns_empty_dict():
    assert Filetree().flatten() == {}

def test_ignores_dir():
    tree = Filetree()
    tree.add_dir("sub")
    assert tree.flatten() == {}

def test_single_image_gives_len_1():
    tree = Filetree()
    tree.add_image("img.jpg", "jpg")

    result = tree.flatten()
    assert len(result) == 1
    assert "img.jpg" in result

def test_many_images_in_root_level():
    tree = Filetree()
    tree.add_image("img.jpg", "jpg")
    tree.add_image("img2.jpg", "jpg")

    result = tree.flatten()
    assert len(result) == 2
    assert "img2.jpg" in result

def test_multiple_levels():
    tree = Filetree()
    tree.add_image("img.jpg", "jpg")
    tree.add_image("img2.jpg", "jpg")
    sub = tree.add_dir("sub")
    sub.add_image("img3.png", "png")

    result = tree.flatten()
    assert len(result) == 3

def test_flattened_body():
    tree = Filetree()
    tree.add_image("img.jpg", "jpg")

    result = tree.flatten()
    assert result["img.jpg"] == {
        "title": "",
        "description": "",
        "tags": []
    }
