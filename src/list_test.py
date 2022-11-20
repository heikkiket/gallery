import list, pytest

singleimage = """
[image-1]
hash = 123456
title = "My first image"
description = "Image description"
tags = ['foo', 'bar', 'baz']
"""

many_images = """
[image-1]
hash = 123456
title = "My first image"
description = "Image description"
tags = ['foo', 'bar', 'baz']

[image-2]
hash = 7890123
title = "My second image"
description = "Image description as well"
tags = ['foo']
"""

@pytest.fixture
def simple_gallery():
    return list.parse_to_gallery(singleimage)

def test_parse_to_gallery(simple_gallery):
    assert "image-1" in simple_gallery
    assert simple_gallery['image-1']['hash'] == 123456

def test_list_single_image(simple_gallery):
    formatted = list.format(simple_gallery)
    assert formatted == "My first image\nImage description"
