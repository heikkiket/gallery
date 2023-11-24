from pathlib import Path
from Imagegallery.image import Image
from Imagegallery.imagefile import ImageFile
from Imagegallery.imagemetadata import ImageMetadata

def test_image():
    image = Image(ImageFile(Path("img1.jpg"), "jpg"),
                  ImageMetadata(title="foo",
                               description="bar"))
    assert image.metadata.title == "foo"
    assert image.file.name == "img1.jpg"
