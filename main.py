import os
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

# TODO Actually put some validation on this
url = sys.argv[1]

url_hash = str(hash(url))
os.mkdir("dls/" + url_hash)

html = urlopen(url).read().decode()
soup = BeautifulSoup(html, "html.parser")
link_tags = soup.find_all("link")

html_file = open("dls/" + url_hash + "/index.html", "w")
html_file.write(html)
html_file.close()

for i, link in enumerate(link_tags):
    if link.attrs["rel"] == ["stylesheet"]:
        sub_url = link.attrs["href"]
        file_dir = "dls/" + url_hash
        full_url = url + "/" + sub_url
        raw_css = urlopen(full_url).read().decode() 

        current_css = open(file_dir + "/" + sub_url, "w")
        current_css.write(raw_css)
        current_css.close()

