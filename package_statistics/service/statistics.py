"""Statistics class for handling stats for a particular architecture"""
from package_statistics.service.impl import statistics_impl
from package_statistics.service import contents


class Statistics:

    def __init__(self, architecture):
        self.architecture = architecture
        self.contents = contents.Contents(self.architecture)

    def get_statistics(self):
        self.data = statistics_impl.process_content(self.contents)

    def get_top_packages(self):
        self.top_packages = statistics_impl.get_top_packages(self.data)
