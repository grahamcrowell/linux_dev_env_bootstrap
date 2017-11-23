#! /usr/local/bin/python3
import os
import sys
import hashlib
import itertools

class MoveTask(object):
	def __init__(self, source_path, destination_path):
		self.source_path = source_path
		self.destination_path = destination_path
	def __str__(self):
		return "MoveTask \n\tFROM: '{source_path}'\n\tTO  : {destination_path}".format(**self.__dict__)

class SyncAbleFile(object):
	def __init__(self, file_path):
		self.file_path = file_path
		self.hash_digest = 0
		self.size = os.stat(self.file_path).st_size
		with open(self.file_path, 'rb') as file_reader:
			self.hash_digest = int(hashlib.md5(file_reader.read()).hexdigest(),16) % (10 ** 8)
	def __hash__(self):
		return self.hash_digest
	def __cmp__(self, rhs):
		return hash(self) - hash(rhs)
	def __eq__(self, rhs):
		return hash(self) == hash(rhs)
	def __str__(self):
		return "SyncAbleFile: ({hash_digest}) {file_path}".format(**self.__dict__)
	def __repr__(self):
		return str(self)


def abslistdir(path):
	filenames = os.listdir(path)
	return [os.path.abspath(os.path.join(path, filename)) for filename in filenames]

def list_files_to_move(SOURCE, DEST):
	sourceSyncs = [SyncAbleFile(source_abspath) for source_abspath in abslistdir(SOURCE)]
	destSyncs = [SyncAbleFile(dest_abspath) for dest_abspath in abslistdir(DEST)]
	return set(sourceSyncs) - set(destSyncs)
	
if __name__ == '__main__':
	SOURCE=sys.argv[1]
	DEST=sys.argv[2]
	print(abslistdir(SOURCE))
	print(list_files_to_move(SOURCE, DEST))