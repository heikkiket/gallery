import tomli, sys

## Throw this if the gallery dictionary is not in a right format
class InvalidGalleryFormat(Exception):
    pass

def read_file(path):
    return open(path, 'rb')

def parse_to_gallery(file_contents):
    return tomli.loads(file_contents)

# Takes an image_gallery and returns a set containing all tags in the gallery
def tags(gallery):
    tags = set()
    for image in gallery.values():
        tags.update(image['tags'])
    return tags

def filter_by_tag(gallery, tag):
    results = {}

    if tag == "":
        return gallery
    for path, image in gallery.items():
        if tag in image["tags"]:
            results[path] = image

    return results

def format(gallery):
    rows = []
    for path, image in gallery.items():
        rows.append("[" + path + "]:")
        rows.append(image["title"])
        rows.append(image["description"])
        rows.append("")
    return rows

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("Give a .toml gallery filename")
        exit(0)

    imagefile = read_file(filename)
    image_gallery = tomli.load(imagefile)
    formatted = format(image_gallery)
    tags = tags(image_gallery)
    print(
        "This gallery has following {} tags: {}".format(len(tags), tags)
          )
    print("\n".join(formatted))
