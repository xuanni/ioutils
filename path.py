

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
        paths = [Path(os.path.join(self.abspath, x)) for x in os.listdir(self.abspath)]
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
            files = []
            for ext in extensions:
                if not ext.startswith('.'):
                    ext = '.' + ext
                files = files + [File(x.abspath) for x in self.findPath() if x.isfile() and x.extension() == ext]
            return files

    def findFileRecusive(self, *extensions):
        files = []
        if len(extensions) == 0:
            for root, dirname, filename in os.walk(self.abspath):
                files = files + \
                        [File(os.path.join(root, x)) for x in filename]
        else:
            for root, dirname, filename in os.walk(self.abspath):
                for ext in extensions:
                    if not ext.startswith('.'):
                        ext = '.' + ext
                    files = files + \
                            [File(os.path.join(root, x)) for x in filename if x.endswith(ext)]
        return files

    def findDir(self):
        #dirs = [Dir(os.path.join(self.abspath, x)) for x in os.listdir(self.abspath) if os.path.isdir(x)]
        dirs = [Dir(x.abspath) for x in self.findPath() if x.isdir()]
        return dirs

    def findDirRecursive(self):
        dirs = []
        for root, dirname, filename in os.walk(self.abspath):
            dirs = dirs + \
                    [Dir(os.path.join(root, x)) for x in dirname]
        return dirs

def test():
    f = File ("/Users/xni/PycharmProjects/ioutils/path.py")

    print(f.extension())

    d = Dir("/Users/xni/PycharmProjects/")

    # for i in d.findPath():
    #     print(i)
    #
    # for i in d.findPathRecursive():
    #     print(i)
    print("find file")
    for i in d.findFile():
        print(i)
    print("--------------")
    for i  in d.findFile('xml', 'txt'):
        print(i)
    print("====================")
    for i in d.findFileRecusive('xml', 'txt'):
        print(i)

    print("find dir")
    for i in d.findDir():
        print(i)

    print("find dir recursively")
    for i in d.findDirRecursive():
        print(i)

if __name__ == "__main__":
    test()
