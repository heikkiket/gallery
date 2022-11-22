import pytest

import list

singleimage = """
["path/to/image1.jpg"]
hash = 123456
title = "My first image"
description = "Image description"
tags = ['foo', 'bar', 'baz']
"""

many_images = """
["path/to/image1.jpg"]
hash = 123456
title = "My first image"
description = "Image description"
tags = ['foo', 'bar', 'baz']

["path/to/image2.jpg"]
hash = 7890123
title = "My second image"
description = "Image description as well"
tags = ['foo']
"""

@pytest.fixture
def simple_gallery():
    return list.parse_to_gallery(singleimage)
@pytest.fixture
def complex_gallery():
    return list.parse_to_gallery(many_images)

def test_parse_to_gallery(simple_gallery):
    assert "path/to/image1.jpg" in simple_gallery
    assert simple_gallery['path/to/image1.jpg']['hash'] == 123456

def test_list_single_image(simple_gallery):
    formatted = list.format(simple_gallery)
    assert formatted == [
        "[path/to/image1.jpg]:",
        "My first image",
        "Image description",
        ""]

def test_list_many_images(complex_gallery):
    formatted = list.format(complex_gallery)
    assert formatted == [
        "[path/to/image1.jpg]:",
        "My first image",
        "Image description",
        "",
        "[path/to/image2.jpg]:",
        "My second image",
        "Image description as well",
        ""]
