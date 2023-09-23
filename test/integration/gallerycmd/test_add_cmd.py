import pytest
import os

from test.integration.filesystem_helpers import mkdir, mkfile, mkimg

from gallerycmd.add.add import add_image

@pytest.fixture()
def environment(tmp_path):
    gallery_dir = tmp_path / "integration_gallery"

    gallery_dir.mkdir()
    file = open(gallery_dir / "gallery.toml", "w")
    file.writelines([
        '["path/to/image.jpg"]\n',
        'hash = 123456\n',
        'title = "My first image"\n',
        'description = "Image description"\n',
        "tags = ['foo', 'bar', 'baz']\n"
    ])
    file.close()
    mkimg(gallery_dir / "image 4.jpg")
    os.chdir(gallery_dir)

def test_add_cmd(environment):
    imagegallery = add_image("image 4.jpg")
    assert imagegallery.GalleryToml.has("image 4.jpg")

def test_add_no_such_file(environment):
    with pytest.raises(FileNotFoundError):
        imagegallery = add_image("foo.jpg")

