from collections import defaultdict
import sys
import requests
import gzip
import shutil
import yaml


def yaml_loader(yaml_file):
    """Method to read the yaml file. Here I am using this
    method to read the config.yaml file which includes
    global variables like url, arch etc."""
    try:
        with open(yaml_file, "r") as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(str(e))
        sys.exit()


def gz_downloader(url, filename):
    """Method to download debian content .gz file"""
    try:
        file = requests.get(url)
        open(filename, "wb").write(file.content)
    except Exception as e:
        print(str(e))
        sys.exit()


def extract_gzfile(gzip_file, filename):
    """Method to extract debian content .gz file"""
    try:
        with gzip.open(gzip_file, 'rb') as f_in:
            with open(filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    except Exception as e:
        print(str(e))
        sys.exit()


def read_file(file):
    """Method to read debian content .gz file and
    storia=ng it as a dictionary based on package name
    as the key"""
    try:
        contents = defaultdict(list)
        with open(file, "r") as f:
            for line in f:
                package_info = line.rstrip("\n").split()
                contents[package_info[1]].append(package_info[0])
        return contents
    except Exception as e:
        print(str(e))
        sys.exit()


def print_to_console(data):
    """Method to print the result to console with proper
    formatiing."""
    print("S.NO.".ljust(7), "PACKAGES".ljust(80), "COUNT")
    for i, package_info in enumerate(data):
        print(str(i+1).ljust(7), package_info[0].ljust(80), package_info[1])
