import os
import pytest

from _pytest import monkeypatch

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
    monkeypatch.chdir(tmp_path)
