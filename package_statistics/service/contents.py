"""Contents class for handling debian content file"""
import package_statistics
from package_statistics.util import util


class Contents:

    def __init__(self, arch):
        self.arch = arch
        self.url = package_statistics.config["url"].replace("$arch", arch)
        self.gz_file = package_statistics.config["temp"] + self.url.split("/")[-1]
        self.filename = self.gz_file.split(".")[0]

    def download_gzfile(self):
        util.gz_downloader(self.url, self.gz_file)

    def extract_gzfile(self):
        util.extract_gzfile(self.gz_file, self.filename)

    def read_contents(self):
        return util.read_file(self.filename)
