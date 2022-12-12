from gallery.list import Filetree
from gallery.list import File

def test_new_filetree_is_empty():
    tree = Filetree()
    assert tree.is_empty()

def test_add_dir():
    tree = Filetree()
    tree.add_dir("test_dir")
    assert tree.is_empty() == False

def test_add_image():
    tree = Filetree()
    tree.add_image("foo.jpg", File.JPG)
    assert tree.is_empty() == False

def test_image_is_right_type():
    tree = Filetree()
    tree.add_image("foo.jpg", File.JPG)
    assert tree.next().type == File.JPG
