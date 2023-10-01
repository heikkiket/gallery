import os
import pytest

from _pytest import monkeypatch

from test.integration.filesystem_helpers import mkimg, mkdir

@pytest.fixture()
def environment(tmp_path, monkeypatch):
    file = open(tmp_path / "gallery.toml", "w")
    file.writelines([
        '["path/to/image1.jpg"]\n',
        'hash = 123456\n',
        'title = "My first image"\n',
        'description = "Image description"\n',
        "tags = ['foo', 'bar', 'baz']\n"
    ])
    mkdir(tmp_path, "path")
    mkdir(tmp_path / "path", "to")
    mkimg(tmp_path / "path" / "to" / "image1.jpg")

    mkimg(tmp_path / "image 4.jpg")
    monkeypatch.chdir(tmp_path)
