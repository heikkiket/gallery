from PIL import Image
from gallery.list import Galleryreader, Filetree

def test_galleryreader_returns_filetree(tmp_path):
    reader = Galleryreader()
    tree = reader.read(tmp_path)
    assert isinstance(tree, Filetree)

def test_galleryreader_reads_image_file(tmp_path):
    img = Image.new('RGB', (1, 1))
    img.save(tmp_path / "test1.png")

    tree = Galleryreader().read(tmp_path)
    assert tree.next().name == "test1.png"

def test_galleryreader_reads_several_image_files(tmp_path):
    img = Image.new('RGB', (1, 1))
    img.save(tmp_path / "test1.png")
    img.save(tmp_path / "test2.png")

    tree = Galleryreader().read(tmp_path)
    names = {tree.next().name, tree.next().name}
    assert names == {"test1.png", "test2.png"}

def test_galleryreader_recurses_to_dirs(tmp_path):
    dir = tmp_path / "sub"
    dir.mkdir()
    img = Image.new('RGB', (1, 1))
    img.save(dir / "test1.png")

    tree = Galleryreader().read(tmp_path)
    tree_dir = tree.next()
    assert tree_dir.name == "sub"
    assert tree_dir.next().name == "test1.png"
    assert "TODO: refactor this test" == ""
    assert "TODO: refactor Galleryreader and Filetree to be simpler" == ""
