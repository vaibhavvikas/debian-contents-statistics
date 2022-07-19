import sys
import package_statistics
from package_statistics.service import statistics
from package_statistics.service import contents
from package_statistics.util import util
import heapq


def create_statistics(arch):
    """Method to initialize the statistics class with
    arch as the argument and finally print the result
    to the console."""
    print("Architecture:", arch)
    if arch not in package_statistics.config["architectures"]:
        print("Invalid Architecture! Exiting...")
        sys.exit()
    stats = statistics.Statistics(arch)
    stats.get_statistics()
    stats.get_top_packages()
    util.print_to_console(stats.top_packages)


def process_content(content: contents.Contents):
    """Method to set debian content file of a arch.
    It includes downloading the .gz, extract, and
    further read the file"""
    content.download_gzfile()
    content.extract_gzfile()
    return content.read_contents()


def get_top_packages(package_details):
    """Method to get top k elements with max number of
    packages from the debian content file of a arch.
    I'm using the Heap data structure as I only need to
    maintian at max k elements."""
    max_elements = package_statistics.config["max"]
    heap = []
    for package in package_details:
        if len(heap) == max_elements:
            heapq.heappushpop(heap, (len(package_details[package]), package))
        else:
            heapq.heappush(heap, (len(package_details[package]), package))
    heap.sort(reverse=True)
    return [[heap[i][1], heap[i][0]] for i in range(len(heap))]
