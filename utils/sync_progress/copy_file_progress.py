import sys, os, math, time
from colorama import Fore, Back, Style
import colorama
import progressbar
colorama.init(autoreset=True)

SOURCE_ROOT="/Volumes/Expansion Drive/Video"
DEST_ROOT=os.path.join(os.path.abspath(os.path.curdir),"DEST")

def sizeof_fmt(num, suffix='B'):
  for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
    if abs(num) < 1024.0:
      return "%3.1f%s%s" % (num, unit, suffix)
    num /= 1024.0
  return "%.1f%s%s" % (num, 'Yi', suffix)

def determine_chunks(size):
  min_chunk_size = 2**20 # 1MB
  max_chunk_count = 100
  print(sizeof_fmt(size) + ' ({}B)'.format(size))
  if size < min_chunk_size:
    print('single chunk')
    return [size,]
  elif 1. * size / max_chunk_count < min_chunk_size:
    chunks = [chunk_id * min_chunk_size for chunk_id in range(1, math.floor(size/min_chunk_size)+1)]
    chunks.append(size)
    print('{} chunks'.format(len(chunks)))
    return chunks
  else:
    chunk_size = math.floor(size / 100. / 8) * 8
    print('100 chunks ({} each)'.format(sizeof_fmt(chunk_size)))
    chunks = [chunk_id * chunk_size for chunk_id in range(1, 100)]
    return chunks

class CopyFile:
  def __init__(self, src_path, dst_path):
    self.src_path = src_path
    self.dst_path = dst_path
    self.stat = os.stat(self.src_path)
    self.chunks = determine_chunks(self.stat.st_size)
    print(self.chunks)
    self.bar = progressbar.ProgressBar(redirect_stdout=True)
  def begin(self):
    print('opening: {} ({})'.format(src_path, sizeof_fmt(self.stat.st_size)))
    with open(src_path, 'rb') as src_fo:
      print('opening: {}'.format(dst_path))
      with open(dst_path, 'wb') as dst_fo:
        for idx in range(len(self.chunks)):
          time.sleep(0.1)
          dst_fo.write(src_fo.read(self.chunks[idx]))
          progress = math.floor(idx/(len(self.chunks)-1)*100)
          print(idx, progress)
          self.bar.update(progress)

if __name__ == "__main__":
  file_name = "A Clockwork Orange 1971.mp4"
  src_path = os.path.join(SOURCE_ROOT, file_name)
  src_path = "/Volumes/Expansion Drive/Music/Alabama Shakes/Alabama Shakes - Live KEXP/06 Interveiw 2.mp3"
  dst_path = os.path.join(DEST_ROOT, file_name)
  if os.path.exists(dst_path):
    os.remove(dst_path)
  copyFile = CopyFile(src_path, dst_path)
  copyFile.begin()