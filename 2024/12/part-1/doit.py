import numpy as np
from collections import defaultdict
import json
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]

# Make a padded matrix to simplify operations
lmat = [list(line) + [None] for line in lines]
lmat.append( [None for _ in range(len(lines[0]))])
print("lmat + = " , *lmat , sep="\n")


def border(point):
    x,y = point
    yield (x +1,y)
    yield (x -1,y)
    yield (x ,y +1)
    yield (x ,y +-1)

def lmatget(point, mat=lmat) :
    x,y = point
    return mat[x][y]


type_sets = map(set, lmat)
types = set.union(*type_sets) - {None}
char_to_num = {char: ind for ind, char in enumerate(types)}
print("char_to_num  = " , char_to_num )
print("types  = " , types )


matching_numbers = np.zeros([len(lmat) -1, len(lmat[0])-1], np.int64)

# DOn't care about the None padding
for lind, line in enumerate(lmat[:-1]):
    for cind, char in enumerate(line[:-1]):
        for tel in border((lind, cind)):
            if char == lmatget(tel, mat=lmat):
                matching_numbers[lind, cind] += 1

print("matching_numbers  = " , matching_numbers )
