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


def discover_frontier(point, discovered = None , mat=lmat):
    if discovered is None:
        discovered = {point}

    current_val = lmatget(point, mat=mat)

    same_border = { new_point for new_point in border(point) if lmatget(new_point) == current_val}
    frontier = same_border   - discovered

    discovered.update(frontier)

    # Visit ing the different points will update the discovered set
    for new_point in frontier:
        discover_frontier(new_point, discovered=discovered, mat=mat)

    assert len(discovered) > 0
    return discovered





#type_sets = map(set, lmat)
#types = set.union(*type_sets) - {None}
#char_to_num = {char: ind for ind, char in enumerate(types)}
#print("char_to_num  = " , char_to_num )
#print("types  = " , types )


matching_numbers = np.zeros([len(lmat) -1, len(lmat[0])-1], np.int64)
areas = np.zeros([len(lmat) -1, len(lmat[0])-1], np.int64)

remembered = dict()

# Don't care about the None padding
for lind, line in enumerate(lmat[:-1]):
    for cind, char in enumerate(line[:-1]):
        for tel in border((lind, cind)):
            if char == lmatget(tel, mat=lmat):
                matching_numbers[lind, cind] += 1

        # Do the proper border thing per element
        if remembered.get((lind, cind)) is None:
            frontier = discover_frontier((lind,cind))

            area = len(frontier )
            for p in frontier:
                remembered[p] = area
        else:
            area = remembered[(lind, cind)]
        assert area > 0
        areas[lind, cind]= area

print("matching_numbers  = \n" , matching_numbers )
print("areas  = \n" , areas )
fences = 4 - matching_numbers
print("fences  = \n" , fences )

tot = np.sum(areas*(fences))
print("tot  = \n" , tot )
#disc = discover_frontier((0,0))
#disc_list = list(disc)
#disc_list.sort()
#print("disc_list  = " , disc_list )
#print("matching_numbers  = " , matching_numbers )
