import pytest

from gallerycmd.init import init_gallery
from gallerycmd.init.init import LibraryExistsError

from test.integration.filesystem_helpers import file_exists

def test_init(tmp_path):
    init_gallery()
    assert not file_exists("library.toml")

def test_init_throws_library_exists(environment):
    with pytest.raises(LibraryExistsError):
        init_gallery()
