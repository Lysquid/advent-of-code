from sys import argv
from copy import deepcopy

def addsublist(l1, l2):
    if type(l1) == type(l2) == type(0):
        return l1, l2
    elif type(l1) != type(l2):
        if type(l1) == type(0):
            l1 = [l1]
        else:
            l2 = [l2]
    i = 0
    while i < len(l1) and i < len(l2):
        l1[i], l2[i] = addsublist(l1[i], l2[i])
        i += 1
    return l1, l2

def comp(l1, l2):
    l1, l2 = addsublist(deepcopy(l1), deepcopy(l2))
    return l1 < l2

with open(argv[1], "r") as file:
    i = 1
    d1, d2 = [[2]], [[6]]
    packets = [d1, d2]
    while True:
        l1 = eval(file.readline().strip())
        l2 = eval(file.readline().strip())
        packets.append(l1)
        packets.append(l2)
        if file.readline() == "":
            break
        i += 1
