import os
import pytest

from _pytest import monkeypatch

from test.integration.filesystem_helpers import mkimg

@pytest.fixture()
def environment(tmp_path, monkeypatch):
    file = open(tmp_path / "gallery.toml", "w")
    file.writelines([
        '["path/to/image.jpg"]\n',
        'hash = 123456\n',
        'title = "My first image"\n',
        'description = "Image description"\n',
        "tags = ['foo', 'bar', 'baz']\n"
    ])
    file.close()
    mkimg(tmp_path / "image 4.jpg")
    monkeypatch.chdir(tmp_path)
