#! /usr/bin/python3

import os
import sys
import hashlib
import itertools
import shutil

class SyncAbleFile(object):
	def __init__(self, file_path, hash_digest, size):
		self.file_path = file_path
		self.hash_digest = hash_digest
		self.size = size
	@classmethod
	def from_path(cls, file_path):
		hash_digest = 0
		size = os.stat(file_path).st_size
		with open(file_path, 'rb') as file_reader:
			hash_digest = int(hashlib.md5(file_reader.read()).hexdigest(),16) % (10 ** 8)
		return cls(file_path, hash_digest, size)
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

class MoveTask(SyncAbleFile):
	def __init__(self, syncable_file, destination_path):
		super().__init__(**syncable_file.__dict__)
		self.destination_path = destination_path
	def __str__(self):
		return "MoveTask \n\tFROM: {file_path} ({size})\n\tTO  : {destination_path}".format(**self.__dict__)
	def move(self):
		shutil.copy(self.file_path, self.destination_path)
		print(self + "\n\tCOMPLETE\n")



def abslistdir(path):
	"""
	@brief      absolute paths of all files in path
	
	@param      path  The path

	@return     absolute paths of all files in path
	"""
	filenames = os.listdir(path)
	return [os.path.abspath(os.path.join(path, filename)) for filename in filenames]

def dirdiff(SOURCE, DEST):
	sourceSyncs = [SyncAbleFile.from_path(source_abspath) for source_abspath in abslistdir(SOURCE)]
	destSyncs = [SyncAbleFile.from_path(dest_abspath) for dest_abspath in abslistdir(DEST)]
	return set(sourceSyncs) - set(destSyncs)

class SyncManager(object):
	def __init__(self, SOURCE, DEST):
		self.SOURCE = SOURCE
		self.abs_dest = os.path.abspath(DEST)
		self.diff = dirdiff(self.SOURCE, self.abs_dest)
		self.tasks = [MoveTask(source, self.abs_dest) for source in self.diff]
		self.remaining_tasks = self.tasks
	def status(self):
		return "{} of {} tasks complete\n".format(len(self.tasks)-len(self.remaining_tasks), len(self.tasks))
	def begin(self):
		while len(self.remaining_tasks) > 0:
			current_task = self.remaining_tasks.pop()
			print("{}".format(current_task))
			current_task.move()


	
if __name__ == '__main__':
	SOURCE=os.path.abspath(sys.argv[1])
	DEST=os.path.abspath(sys.argv[2])
	# print(abslistdir(SOURCE))
	# print(dirdiff(SOURCE, DEST))
	sync = SyncManager(SOURCE, DEST)
	print(sync.status())
	sync.begin()


