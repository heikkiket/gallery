import tomli

def parse_to_gallery(file_contents):
    return tomli.loads(file_contents)

def format(gallery):
    rows = []
    for image in gallery.values():
        rows.append(image["title"])
        rows.append(image["description"])
        rows.append("")
    return rows

if __name__ == "__main__":
    images = open("../samples/images.toml", "rb")
    parsed = tomli.load(images)
    print(parsed)
