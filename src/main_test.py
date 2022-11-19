import list

testdata = """
[image-1]
hash = 123456
title = "My first image"
description = "Image description"
tags = ['foo', 'bar', 'baz']
"""

def test_parse_to_gallery():
    gallery = list.parse_to_gallery(testdata)
    assert "image-1" in gallery
    assert gallery['image-1']['hash'] == 123456
