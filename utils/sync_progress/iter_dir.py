import sys, os
from itertools import *
from functools import *
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset=True)

SOURCE_ROOT="/Volumes/Expansion Drive/Video"
# SCAN_DIR=list(os.scandir(SOURCE_ROOT))
# print(SCAN_DIR)
# class DirStat:
    # def __init__(self, root_path):
        # self.

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def getSize(dirEntry):
    return dirEntry.stat().st_size

def getCount(dirEntry):
    return 1

def walkdir(root_path, foo=getSize, out=0):
    for entry in os.scandir(root_path):
        if entry.is_dir():
            fooOut = walkdir(entry, foo)
            out += fooOut
        else:
            out += foo(entry)
    return out

# total_size = walkdir(SOURCE_ROOT, getSize)
# print(sizeof_fmt(total_size))


def flat_folder(root_path, out=list()):
    for entry in os.scandir(root_path):
        if entry.is_dir():
            fooOut = flat_folder(entry.path, out=list())
            out.extend(fooOut)
        else:
            out.append(entry)
    return out

# folder = flat_folder(SOURCE_ROOT)
# print(len(folder))


class Folder:

    def __init__(self, path):
        self.path = path
        self.files = []
        self.sub_folders = []
        self.total_size = 0
        self.total_file_count = 0

    def build_cache(self):
        for entry in os.scandir(self.path):
            if entry.is_dir():
                pass
            else:
                self.total_size += entry.stat().st_size
                self.files.append(entry)
        self.total_file_count = len(self.files)
        for entry in os.scandir(self.path):
            if entry.is_dir():
                folder = Folder(entry.path)
                folder.build_cache()
                self.total_size += folder.total_size
                self.total_file_count += folder.total_file_count
                self.sub_folders.append(folder)

f = Folder(SOURCE_ROOT)
f.build_cache()



