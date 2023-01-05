from viewer import Image

def test_image_has_filename():
    image = Image()
    assert image.filename == None

def test_images_have_different_names():
    img1 = Image()
    img2 = Image()
    img1.filename = "img1.jpg"
    assert img1.filename == "img1.jpg"
    assert img2.filename == None
