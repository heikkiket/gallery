import pytest

from pathlib import Path

from Imagegallery.filetree import Filetree
from Imagegallery.image import Image

@pytest.fixture
def tree():
    return Filetree()

@pytest.fixture
def complex_tree():
    tree = Filetree()
    tree.add_dir("test_dir")
    tree.add_dir("test_dir2")
    dir = tree.next()
    dir.add_image("test.jpg", "jpg")
    tree.reset()
    return tree

def test_new_filetree_is_empty(tree):
    assert tree.is_empty()

def test_add_dir(tree):
    tree.add_dir("test_dir")
    assert tree.is_empty() == False

def test_add_image(tree):
    tree.add_image("foo.jpg", "jpg")
    assert tree.is_empty() == False

def test_dir_has_path(tree):
    tree.add_dir("test_dir")
    assert tree.next().path == Path("test_dir")

def test_image_has_right_name(tree):
    tree.add_image("test.jpg", "jpg")
    assert tree.next().name == "test.jpg"

def test_image_is_right_type(tree):
    tree.add_image("foo.jpg", "jpg")
    assert tree.next().type == "jpg"

def test_image_has_right_path(tree):
    tree.add_image("test.jpg", "jpg")
    img = tree.next()
    assert img.path == Path("test.jpg")

def test_dir_can_contain_img(tree):
    tree.add_dir("test_dir")
    dir = tree.next()
    dir.add_image("test.jpg", "jpg")
    assert dir.is_empty() == False

def test_dir_in_dir_has_right_path(complex_tree):
    dir = complex_tree.next().add_dir("subdir")
    assert dir.path == Path("test_dir/subdir")

def test_img_in_dir_has_right_path(complex_tree):
    img = complex_tree.next().next()
    assert img.path == Path("test_dir/test.jpg")


def test_next_works(complex_tree):
    complex_tree.add_dir("test_dir")
    complex_tree.add_dir("test_dir2")
    assert complex_tree.next().name == "test_dir"
    assert complex_tree.next().name == "test_dir2"

def test_reset_works(complex_tree):
    complex_tree.add_dir("test_dir")
    complex_tree.add_dir("test_dir2")
    complex_tree.next()
    complex_tree.reset()
    assert complex_tree.next().name == "test_dir"
