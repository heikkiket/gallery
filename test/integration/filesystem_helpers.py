from pathlib import Path
from PIL import Image


def mkdir(path, sub):
    dir = path / sub
    dir.mkdir()
    return dir

def mkimg(path):
    img = Image.new('RGB', (1, 1))
    img.save(path)

def mkfile(path):
    open(path, "x")

def file_exists(path):
    file = Path(path)
    return file.is_file()
