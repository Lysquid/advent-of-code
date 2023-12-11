from sys import argv


class File:
    
    def __init__(self, name, parent=None, size = 0) -> None:
        self.name = name
        self.parent = parent
        self.size = size
        self.childs = []

    def getParent(self):
        return self.parent

    def getChild(self, name):
        for child in self.childs:
            if child.name == name:
                return child

    def addChild(self, child):
        self.childs.append(child)

    def calcSmallest(self):
        if self.size != 0:
            return (self.size, [])
        size = self.size
        total = []
        for child in self.childs:
            childSize, childTotal = child.calcSmallest()
            size += childSize
            total.extend(childTotal)
        total.append(size)
        return (size, total)

with open(argv[1], "r") as file:

    origin = File("")
    root = File("/", origin)
    origin.addChild(root)
    current = origin
    for line in file:
        if "$ cd" in line:
            if ".." in line:
                current = current.getParent()
            else:
                child = line.strip().split(" ")[2]
                current = current.getChild(child)
        elif "$ ls" in line:
            continue
        else:
            size, name = line.strip().split(" ")
            if size == "dir":
                current.addChild(File(name, current))
            else:
                current.addChild(File(name, current, int(size)))
    rootSize, total = root.calcSmallest()
    available = 70000000 - rootSize
    needed = 30000000 - available
    total.sort()
    for folder in total:
        if folder >= needed:
            print(folder)
            break
