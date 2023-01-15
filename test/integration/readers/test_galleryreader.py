import pytest
import tomli

from readers.galleryreader import load_gallery


def test_load_gallery_fails_without_filename():
    with pytest.raises(TypeError, match="missing 1 required positional argument"):
        load_gallery()

def test_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_gallery(tmp_path / "foo")

def test_file_not_toml(tmp_path):
    not_toml = open(tmp_path / "foo.toml", 'w')
    not_toml.write("this is not a TOML file")
    not_toml.close()

    with pytest.raises(tomli.TOMLDecodeError):
        load_gallery(tmp_path / "foo.toml")

def test_loads_toml_file(tmp_path):
    toml = open(tmp_path / "gallery.toml", 'w')
    toml.write('this="a test"')
    toml.close()

    result = load_gallery(tmp_path / "gallery.toml")
    assert result["this"] == "a test"
