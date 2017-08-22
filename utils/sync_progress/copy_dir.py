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

def walkdir(root_path, X=0, foo=lambda x: x.stat().st_size):
  for entry in os.scandir(root_path):
    if entry.is_dir():
      print(entry.name, sizeof_fmt(X))
      y = walkdir(entry, 0, foo)
      print(sizeof_fmt(y))
      X += y
    else:
      print(entry.name)
      X += foo(entry)
  return X


X = walkdir(SOURCE_ROOT)

print(sizeof_fmt(X))