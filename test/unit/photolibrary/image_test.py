from pathlib import Path
from PhotoLibrary.image import Image
from PhotoLibrary.imagefile import ImageFile
from PhotoLibrary.imagemetadata import ImageMetadata

def test_image():
    image = Image(ImageFile(Path("img1.jpg"), "jpg"),
                  ImageMetadata(title="foo",
                               description="bar"))
    assert image.metadata.title == "foo"
    assert image.file.name == "img1.jpg"
