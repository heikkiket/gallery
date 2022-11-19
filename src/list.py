import tomli

def parse_to_gallery(file_contents):
    return tomli.loads(file_contents)

if __name__ == "__main__":
    images = open("../samples/images.toml", "rb")
    parsed = tomli.load(images)
    print(parsed)
