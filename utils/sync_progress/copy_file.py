import sys, os
<<<<<<< Updated upstream
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset=True)

=======

print(os.curdir)
>>>>>>> Stashed changes
print(os.path.abspath(os.path.curdir))

SOURCE_ROOT="/Volumes/Expansion Drive/Video"
DEST_ROOT=os.path.join(os.path.abspath(os.path.curdir),"DEST")
print(DEST_ROOT)
print(os.path.exists(DEST_ROOT))

<<<<<<< Updated upstream
def validate_dir(dir_path):
  valid = os.path.isdir(dir_path)
  if not valid:
    print(Fore.RED + 'dir_path invalid: {}'.format(src_path))
    raise NotADirectoryError(dir_path)

def validate_src(src_path):
  valid = os.path.exists(src_path) and os.path.isfile(src_path)
  if not valid:
    print(Fore.RED + 'src_path invalid: {}'.format(src_path))
    raise FileNotFoundError(src_path)

def validate_dst(dst_path):
  exists = not os.path.exists(dst_path) and os.path.isdir(os.path.split(os.path.abspath(dst_path))[0])
  if exists:
    print(Fore.RED + 'dst_path invalid: {} already exists'.format(dst_path))
    raise FileExistsError(dst_path)

class CopyFileTask:
  def __init__(self, src_path, dst_path):
    
    validate_src(src)
    validate_dst(dst)


def silly():
    file_name = "A Clockwork Orange 1971.mp4"
    src = os.path.join(SOURCE_ROOT, file_name)
    dst = os.path.join(DEST_ROOT, file_name)
    src_fd = os.open(src, os.O_RDONLY)
    dst_fd = os.open(dst, os.O_CREAT | os.O_WRONLY)
    data = os.read(src_fd, 1000)
    os.write(dst_fd, data)

if __name__ == "__main__":
    file_name = "A Clockwork Orange 1971.mp4"
    src_path = os.path.join(SOURCE_ROOT, file_name)
    dst_path = os.path.join(DEST_ROOT, file_name)
    src_fo = open(src_path, 'r')
    dst_fo = open(dst_path, 'w')
    dst_fo.write(src_fo.read())
    src_fo.close()
    dst_fo.close()
=======

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
>>>>>>> Stashed changes
