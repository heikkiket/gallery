import pytest
from filesystem_operations.libraryreader import load_library
from gallerycmd.edit import edit_image
from gallerycmd.edit.edit import NeedsNamedArgument

def test_edit_no_such_file(environment):
    with pytest.raises(FileNotFoundError):
        edit_image("foo.jpg", title="foo")

def test_needs_one_named_argument(environment):
    with pytest.raises(NeedsNamedArgument):
        edit_image("path/to/image1.jpg")

    edit_image("path/to/image1.jpg", title="foo")
    edit_image("path/to/image1.jpg", description="foo")
    edit_image("path/to/image1.jpg", tags=["foo"])

def test_edit_succeeds(environment):
    edit_image("path/to/image1.jpg", title="new title")
    toml_file = load_library("library.toml")
    assert toml_file["path/to/image1.jpg"]["title"] == "new title"

