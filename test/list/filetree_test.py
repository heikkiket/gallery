import pytest

from gallery.list import Filetree
from gallery.list import Image

@pytest.fixture
def tree():
    return Filetree()

def test_new_filetree_is_empty(tree):
    assert tree.is_empty()

def test_add_dir(tree):
    tree.add_dir("test_dir")
    assert tree.is_empty() == False

def test_add_image(tree):
    tree.add_image("foo.jpg", "jpg")
    assert tree.is_empty() == False

def test_image_is_right_type(tree):
    tree.add_image("foo.jpg", "jpg")
    assert tree.next().type == "jpg"

def test_dir_can_contain_img(tree):
    tree.add_dir("test_dir")
    dir = tree.next()
    dir.add_image("test.jpg", "jpg")
    assert dir.is_empty() == False

def test_next_works(tree):
    tree.add_dir("test_dir")
    tree.add_dir("test_dir2")
    assert tree.next().name == "test_dir"
    assert tree.next().name == "test_dir2"

def test_reset_works(tree):
    tree.add_dir("test_dir")
    tree.add_dir("test_dir2")
    tree.next()
    tree.reset()
    assert tree.next().name == "test_dir"
