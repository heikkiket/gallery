import pytest
import tomli

from filesystem_operations.libraryreader import LibraryFileMissing, load_library


def test_load_gallery_fails_without_filename():
    with pytest.raises(TypeError, match="missing 1 required positional argument"):
        load_library()

def test_file_not_found(tmp_path):
    with pytest.raises(LibraryFileMissing):
        load_library(tmp_path / "foo")

def test_file_not_toml(tmp_path):
    not_toml = open(tmp_path / "foo.toml", 'w')
    not_toml.write("this is not a TOML file")
    not_toml.close()

    with pytest.raises(tomli.TOMLDecodeError):
        load_library(tmp_path / "foo.toml")

def test_loads_toml_file(tmp_path):
    toml = open(tmp_path / "library.toml", 'w')
    toml.write('this="a test"')
    toml.close()

    result = load_library(tmp_path / "library.toml")
    assert result["this"] == "a test"
