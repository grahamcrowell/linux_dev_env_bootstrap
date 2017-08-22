import sys, os

print(os.curdir)
print(os.path.abspath(os.path.curdir))

SOURCE_ROOT="/Volumes/Expansion Drive/Video"
DEST_ROOT=os.path.join(os.path.abspath(os.path.curdir),"DEST")
print(DEST_ROOT)
print(os.path.exists(DEST_ROOT))


# print(os.listdir(SOURCE_ROOT))

file_name = "A Clockwork Orange 1971.mp4"

def validate_path(test_path):
  exists = os.path.exists(test_path)
  if not exists:
    pass

class CopyFileTask:
  def __init__(self, src, dst):
    pass

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')