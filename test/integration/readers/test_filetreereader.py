import pytest

from readers.filetreereader import Filetreereader
from models.filetree import Filetree
from test.integration.filesystem_helpers import mkdir, mkimg, mkfile

def test_filetreereader_returns_filetree(tmp_path):
    reader = Filetreereader()
    tree = reader.read(tmp_path)
    assert isinstance(tree, Filetree)

def test_filetreereader_reads_image_file(tmp_path):
    mkimg(tmp_path / "test1.png")

    tree = Filetreereader().read(tmp_path)
    image = tree.next()
    assert image.name == "test1.png"
    assert image.type == "png"

def test_filetreereader_reads_several_image_files(tmp_path):
    mkimg(tmp_path / "test1.png")
    mkimg(tmp_path / "test2.png")

    tree = Filetreereader().read(tmp_path)
    names = {tree.next().name, tree.next().name}
    assert names == {"test1.png", "test2.png"}

def test_filetreereader_recurses_to_dirs(tmp_path):
    dir = mkdir(tmp_path, "sub")
    mkimg(dir / "test1.png")

    tree = Filetreereader().read(tmp_path)
    tree_dir = tree.next()
    assert tree_dir.name == "sub"
    assert tree_dir.next().name == "test1.png"

def test_filereader_reads_only_images(tmp_path):
    mkfile(tmp_path / "foo")
    tree = Filetreereader().read(tmp_path)
    assert tree.is_empty()
