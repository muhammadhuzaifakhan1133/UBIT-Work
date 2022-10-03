import os
from time import ctime


class Finder:

    def listFilesByScandirFunction(self, directory, extension):
        for entry in os.scandir(directory):
            path = entry.path.replace("\\", "//")
            if entry.is_file():
                if path.endswith(extension):
                    info = entry.stat()
                    print(ctime(info.st_ctime), 
                        ctime(info.st_atime), 
                        ctime(info.st_mtime), 
                        entry.name, 
                        str(info.st_size) + " bytes", 
                        sep=" | ")
            else:
                self.listFilesByScandirFunction(entry, extension)

    def listFilesByWalkFunction(self, directory, extension):
        total_files = 0
        total_size = 0
        for root, dirs, files in os.walk(directory):
            count = 0
            for file in files:
                if file.endswith(extension):
                    if (count==0):
                        print(f"\n\t{root}\n")
                    path = os.path.join(root, file)
                    dateCreation = ctime(os.path.getctime(path))
                    dateLastAccess = ctime(os.path.getatime(path))
                    dateLastModified = ctime(os.path.getmtime(path))
                    size = os.path.getsize(path)
                    total_files += 1
                    total_size += size
                    count += 1
                    print(dateCreation, dateLastAccess, dateLastModified, file, str(size)+" bytes", sep=" | ")
        print(f"\n\n{total_files} Files Found of Size {total_size}")


directory = "C:/"
# directory = directory.replace('\\', "/")
finder = Finder()
finder.listFilesByWalkFunction(directory, ".py")