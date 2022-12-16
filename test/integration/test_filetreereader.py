import pytest

from PIL import Image
from readers.filetreereader import Filetreereader
from models.filetree import Filetree

def mkdir(path, sub):
    dir = path / sub
    dir.mkdir()
    return dir

def mkimg(path):
    img = Image.new('RGB', (1, 1))
    img.save(path)

def test_filetreereader_returns_filetree(tmp_path):
    reader = Filetreereader()
    tree = reader.read(tmp_path)
    assert isinstance(tree, Filetree)

def test_filetreereader_reads_image_file(tmp_path):
    mkimg(tmp_path / "test1.png")

    tree = Filetreereader().read(tmp_path)
    assert tree.next().name == "test1.png"

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
