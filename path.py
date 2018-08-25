

import os.path

class Path(object):
    def __init__(self, path, link = False):
        self.abspath = os.path.abspath(path)
        self.link = link

    def exists(self):
        return os.path.exists(self.abspath)

    def isfile(self):
        return os.path.isfile(self.abspath)

    def isdir(self):
        return os.path.isdir(self.abspath)

    def basename(self):
        return os.path.basename(self.abspath)

    def extension(self):
        return None

    def __str__(self):
        return self.abspath

class File(Path):

    def __init__(self, path, link = False):
        super(File, self).__init__(path, link)
        # check if is file raise exception?

    def extension(self):
        return os.path.splitext(self.abspath)[1]

class Dir(Path):

    def __init__(self, path, link = False):
        super(Dir, self).__init__(path, link)
        # check if is file raise exception?

    def findPath(self):
        paths = [Path(x) for x in os.listdir(self.abspath)]
        return paths

    def findPathRecursive(self):
        paths = []
        for root, dirname, filename in os.walk(self.abspath):
            paths = paths + \
                    [Path(os.path.join(root, x)) for x in dirname] + \
                    [Path(os.path.join(root, x)) for x in filename]
        return paths

    def findFile(self, *extensions):
        if len(extensions) == 0:
            return [File(x.abspath) for x in self.findPath() if x.isfile()]
        else:
            for ext in extensions:
                pass
#             TODO continue from here

def test():
    f = File ("/Users/xni/PycharmProjects/ioutils/path.py")

    print(f.extension())

    d = Dir("/Users/xni/PycharmProjects/")

    for i in d.findPath():
        print(i)

    for i in d.findPathRecursive():
        print(i)

if __name__ == "__main__":
    test()
