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

total_size = walkdir(SOURCE_ROOT, getSize)
print(sizeof_fmt(total_size))


def walkdir(root_path, out=list()):
  for entry in os.scandir(root_path):
    if entry.is_dir():
      # print(entry.path)
      fooOut = walkdir(entry.path, out=list())
      # print(fooOut)
      out.extend(fooOut)
    else:
      out.append(entry)
  return out

folder = walkdir(SOURCE_ROOT)
# print(folder)
print(folder[-1])
print(folder[-2])
print(folder[-3])
print(folder[-4])
# print(len(folder[-5]))
# print(folder[-5][-5][-5])
print(len(folder))

def walkdir(root_path, out=set()):
  for entry in os.scandir(root_path):
    if entry.is_dir():
      # print(entry.path)
      fooOut = walkdir(entry.path)
      out.union(fooOut)
    else:
      out.add(entry)
  return out

folder = walkdir(SOURCE_ROOT)
print(len(folder))

class Folder:
  def __init__(self):
    self.files = []
    self.subfolders = []
    self.total_size = 0

