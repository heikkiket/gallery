import pytest

from pathlib import Path

from models.filetree import Filetree

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
