import pytest

from photoscmd.init import init_photolibrary
from photoscmd.init.init import LibraryExistsError

from test.integration.filesystem_helpers import file_exists

def test_init(tmp_path):
    init_photolibrary()
    assert not file_exists("library.toml")

def test_init_throws_library_exists(environment):
    with pytest.raises(LibraryExistsError):
        init_photolibrary()
