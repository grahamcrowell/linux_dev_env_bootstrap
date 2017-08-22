import os


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class FileSize:
    def __init__(self, byte_count):
        self.byte_count = byte_count

    def __str__(self):
        return sizeof_fmt(self.byte_count)


class File:
    def __init__(self, dir_entry):
        self.path = dir_entry.path
        self.stat = dir_entry.stat()
        self.file_size = FileSize(self.stat.st_size)

    def __str__(self):
        return 'File:\n\t{} ({})'.format(os.path.split(self.path)[1],self.file_size)

    def __repr__(self):
        return '{} ({})'.format(os.path.split(self.path)[1],self.file_size)


class Folder:

    def __init__(self, path):
        self.path = path
        self.files = []
        self.sub_folders = []
        self.total_size = 0
        self.total_file_count = 0
        self.file_count = 0
        self.sub_folder_count = 0

    def build_cache(self):
        for entry in os.scandir(self.path):
            if entry.is_dir():
                pass
            else:
                self.total_size += entry.stat().st_size
                self.files.append(File(entry))
        self.file_count = len(self.files)
        self.total_file_count = len(self.files)
        for entry in os.scandir(self.path):
            if entry.is_dir():
                self.sub_folder_count += 1
                sub_folder = Folder(entry.path)
                sub_folder.build_cache()
                self.total_size += sub_folder.total_size
                self.total_file_count += sub_folder.total_file_count
                self.sub_folders.append(sub_folder)
                self.sub_folder_count += sub_folder.sub_folder_count

    def __str__(self):
        self.sub_folder_count = len(self.sub_folders)
        # self.file_count = 10000
        out = '\n\nDirectory:\n\tPath: {path}\n\tTotal Size: {}\n\tFile Count: {file_count:,d}\n\tSub-Folder Count: {sub_folder_count}\n'
        return out.format(sizeof_fmt(self.total_size), **self.__dict__)

    def apply_files(self, func):
        return list([func(file) for file in self.files])

    def apply_sub_folders(self, func):
        return list([func(sub_folder) for sub_folder in self.sub_folders])

    def show(self):
        print(self)
        self.apply_files(lambda file: print('\t{}'.format(file)))
        self.apply_sub_folders(lambda folder: folder.show())

    def recursive_apply(self, func):
        func(self)
        self.apply_files(func)
        self.apply_sub_folders(lambda folder: folder.recursive_apply(func))


def fraction(total, progress=0):
    return lambda abs_progress: (1.*abs_progress+progress)/total



# def print_progress()

f = fraction(15)(4)
print(f)


if __name__ == "__main__":
    SOURCE_ROOT = "/Volumes/Expansion Drive/Video"
    src_folder = Folder(SOURCE_ROOT)
    src_folder.build_cache()
    print(src_folder)
    # src_folder.apply_files(lambda line: print('\t{}'.format(line)))
    # src_folder.apply_sub_folders(lambda line: print('{}'.format(line)))
    # src_folder.show()
    src_folder.recursive_apply(print)
