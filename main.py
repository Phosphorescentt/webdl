import os
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Just rewrite the whole thing and think more about how to make stuff work.

def decompose_path(path: str) -> [list, list]:
    components = path.split("/")
    f = components.pop()
    d = components
    return [d, f]

def create_directories(directories: list) -> bool:
    path = "dls/"
    for i in range(len(directories)):
        path += directories.pop()
        try:
            os.mkdir(path)
        except OSError as e:
            print(e)
            return False

    return True

# TODO Actually put some validation on this
url = sys.argv[1]

url_hash = str(hash(url))
try:
    os.mkdir("dls/" + url_hash)
except OSError as e:
    print(e)

html = urlopen(url).read().decode()
soup = BeautifulSoup(html, "html.parser")
link_tags = soup.find_all("link")
img_tags = soup.find_all("img")

html_file = open("dls/" + url_hash + "/index.html", "w")
html_file.write(html)
html_file.close()

# Get all CSS files
for i, link in enumerate(link_tags):
    if link.attrs["rel"] == ["stylesheet"]:
        sub_url = link.attrs["href"]
        file_dir = "dls/" + url_hash
        full_url = url + "/" + sub_url
        raw_css = urlopen(full_url).read().decode() 

        current_css = open(file_dir + "/" + sub_url, "w")
        current_css.write(raw_css)
        current_css.close()

# Get all images
for i, image in enumerate(img_tags):
    sub_url = image.attrs["src"]
    file_dir = "dls/" + url_hash
    full_url = url + "/" + sub_url
    image = urlopen(full_url).read()

    directories, file_name = decompose_path(file_dir)
    create_directories(directories)

    current_image = open(file_dir + "/" + sub_url, "w")
    current_image.write(image)
    current_image.close()
    pass

print("Data stored in dls/" + url_hash)
