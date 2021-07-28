files = [
    ["file1", 100, ["collection1", "collection2"]],
    ["file2", 200, ["collection2"]],
    ["file3", 200, ["collection0"]],
]

class FileSystem:
    def __init__(self, files):
        self.files = files

    def compute_size(self):
        self.total_size = 0
        for file in self.files:
            self.total_size += file[1]

        return self.total_size

    def top_collections(self, n):
        collections = {
        }

        for file in self.files:
            for collection in file[2]:
                if collection in collections:
                    collections[collection] += file[1]
                else:
                    collections[collection] = file[1]

        collections =  sorted(collections.items(), key=lambda x: x[1], reverse=True)
        return collections[:n]

fileSystem = FileSystem(files)
print(fileSystem.compute_size())

print(fileSystem.top_collections(3))




