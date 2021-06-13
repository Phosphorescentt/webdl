import os
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Settings:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return str(self.__dict__)

    def __str__(self) -> str:
        return str(self.__dict__)

    def parse_clargs(self, clargs: list) -> None:
        # Handle CSS settings
        if "-c" in clargs:
            clargs.remove("-c")
            settings.css = True
        else:
            settings.css = False

        # Handle image settings
        if "-i" in clargs:
            clargs.remove("-i")
            settings.images = True
        else:
            settings.images = False

        # Handle opening browser after download
        if "-o" in clargs:
            clargs.remove("-o")
            settings.open = True
        else:
            settings.open = False

        # Handle setting custom directory to save webpage to
        if "-d" in clargs:
            index = clargs.index("-d")
            directory = clargs[index + 1]
            clargs.remove(index)
            clargs.remove(arg)
            settings.directory = arg
        else:
            settings.directory = "dls/"

        if len(clargs) > 1:
            raise Exception("Unexpected command line argument. \n" + str(settings))
        else:
            self.url = clargs[0]

class Webdler:
    def __init__(self, settings: Settings):
        self.settings = settings
        pass

    def clean_url(self, url: str) -> str:
        pass

    def hash_url(self, url: str) -> str:
        pass

    def get_url(self, url: str) -> str:
        return urllopen(url).read().decode()

    def create_directory(self, directory: str) -> None:
        pass

    def run(self) -> bool, str:
        print(settings)
        # Clean and hash URL
        cleaned_url = self.clean_url(settings.url)
        hashed_url = self.hash_url(cleaned_url)

        # Get data
        data = self.get_url(cleaned_url)

        # Create directories
        self.create_directory(hashed_url)
        # url_hash

        # Get webpage
        webpage = self.get_url(cleaned_url)

        if settings.css:
            # Create CSS directory
            self.create_directory(hashed_url + "/css")
            # Get all stylesheets and save them to url_hash/css

        if settings.images:
            # Create images directory
            self.create_directory(hashed_url + "/images")
            # Get all images and save them to url_has/images

        return True, hashed_url

if __name__ == "__main__":
    # Handle command line input
    settings = Settings()
    settings.parse_clargs(sys.argv)

    webdler = Webdler(settings)
    success, directory = webdler.run()

    if success:
        print("Data downloaded to " + settings.url + "/" + directory)
