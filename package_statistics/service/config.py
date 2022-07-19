"""Config class for handling the inputs inside config file"""
from package_statistics.util import util


class Config:
    config_file = "./config/config.yaml"

    def __init__(self):
        self.config = self.config_loader()

    def config_loader(self):
        return util.yaml_loader(self.config_file)
