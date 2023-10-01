import pytest
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

