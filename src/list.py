import tomli, sys

def read_file(path):
    return open(path, 'rb')

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
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("Give a .toml gallery filename")
        exit(0)
    images = read_file(filename)
    parsed = tomli.load(images)
    formatted = format(parsed)
    print("\n".join(formatted))
