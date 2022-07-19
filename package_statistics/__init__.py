"""Top-level package for Debian Package Statistics."""

from package_statistics.service.config import Config
from package_statistics.service.impl import statistics_impl
from package_statistics.service import args_parser
from pathlib import Path


__author__ = """Vaibhav Vikas"""
__email__ = 'vbhvvikas@gmail.com'
__version__ = '0.1.0'


# Initializing configuration
config = Config().config


# Creating Temp Directory for storing files
Path(config["temp"]).mkdir(parents=True, exist_ok=True)


def initialize():
    _args_parser = args_parser.ArgParser()
    statistics_impl.create_statistics(_args_parser.arch)
