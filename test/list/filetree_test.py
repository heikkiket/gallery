import pytest

from gallery.list import Filetree
from gallery.list import Image

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

def test_image_is_right_type(tree):
    tree.add_image("foo.jpg", "jpg")
    assert tree.next().type == "jpg"

def test_dir_can_contain_img(tree):
    tree.add_dir("test_dir")
    dir = tree.next()
    dir.add_image("test.jpg", "jpg")
    assert dir.is_empty() == False

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

def test_find_returns_empty(complex_tree):
    complex_tree.add_dir("test_dir")
    dir = complex_tree.next()
    dir.add_image("test.jpg", "jpg")

    assert complex_tree.find("foo.jpg") == None

def test_find_in_root_level(tree):
    tree.add_image("test.jpg", "jpg")
    tree.add_image("foo.jpg", "jpg")
    assert tree.find("test.jpg") == tree.next()
    assert tree.find("foo.jpg") == tree.next()

def test_find_deep(complex_tree):
    target = complex_tree.next().next()
    assert complex_tree.find("test_dir/test.jpg") == target
