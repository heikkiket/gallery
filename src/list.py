import tomli

def parse_to_gallery(file_contents):
    return tomli.loads(file_contents)

def format(gallery):
    value = ""
    for image in gallery.values():
        value += image["title"] + "\n" + image["description"]
    return value

if __name__ == "__main__":
    images = open("../samples/images.toml", "rb")
    parsed = tomli.load(images)
    print(parsed)
