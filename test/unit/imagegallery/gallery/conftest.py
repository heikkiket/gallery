import pytest

@pytest.fixture
def gallery_toml():
    return {
        "path/to/image1.jpg":
        {
            "hash": 123456,
            "title": "My first image",
            "description" : "Image description",
            "tags" : ['foo', 'bar', 'baz']
        },

    "path/to/image2.jpg":
        {
            "hash" : 7890123,
            "title" : "My second image",
            "description" : "Image description as well",
            "tags" : ['foo']
        },

    "path/to/image3.jpg":
        {
            "hash" : 7890123,
            "title" : "My Third image",
            "description" : "Image description like others",
            "tags" : ['foo', 'baz']
        }
    }
