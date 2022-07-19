"""ArgParser class to take arguments and handle them."""
import argparse


class ArgParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Process arch!")
        self.parser.add_argument("arch", nargs="?",
                                 help="takes architecture you want \
                                 to find the top packages of.")
        self.parse_arguments()

    def parse_arguments(self):
        args = self.parser.parse_args()
        if not args.arch:
            self.parser.error("No argument provided")
        self.arch = args.arch
