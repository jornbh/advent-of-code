import numpy as np
from collections import defaultdict
import json
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]

# Make a padded matrix to simplify operations
lmat = [list(line) + [None] for line in lines]
lmat.append( [None for _ in range(len(lines[0])+1)])
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


def get_good_fences(lind, cind , mat=lmat):
        point = np.array((lind, cind))
        print("point  = " , point )
        displacement_base = np.array([1,0])
        diagonal_displacement = np.array([1,1])
        left_rotator =  np.array([
            [0,-1],
            [1,0]], np.int64)

        are_good = [True]*4
        char = lmatget(point,  mat)

        for i in range(4):
            # There can be no fence within the same shape
            oposing_char  = lmatget(point + displacement_base, mat)
            is_good = oposing_char != char


            # If there is a continuation of the wall, it does not add anything,
            # unless the one on the left does not have a wall itself

            left_displacement = left_rotator @ displacement_base
            left_char = lmatget(point + left_displacement, mat)
            diaglonal_left_char = lmatget(point + diagonal_displacement, mat)

            is_bad = left_char == char  and diaglonal_left_char != left_char
            is_good = is_good and  not (is_bad)
            are_good[i] =  is_good
            displacement_base = left_displacement
            diagonal_displacement = left_rotator @ diagonal_displacement
        return are_good
sh = len(lmat), len(lmat[-1])
print("sh  = " , sh )
lmat[-1][10]
are_good = get_good_fences(0, 1 , mat=lmat)
print("are_good  = " , are_good )
#exit(0)

#type_sets = map(set, lmat)
#types = set.union(*type_sets) - {None}
#char_to_num = {char: ind for ind, char in enumerate(types)}
#print("char_to_num  = " , char_to_num )
#print("types  = " , types )


fences = np.zeros([len(lmat) -1, len(lmat[0])-1], np.int64)
areas = np.zeros([len(lmat) -1, len(lmat[0])-1], np.int64)


# Don't care about the None padding
# Calculate number of fences for a new patch
for lind, line in enumerate(lmat[:-1]):
    for cind, char in enumerate(line[:-1]):

        are_good = get_good_fences(lind, cind, mat=lmat)

        fences[lind,cind]  = len([ el for el in are_good if el ])

#        border_list = list(border((lind, cind)))
#        matching_chars = (border_el for border_el in border_list  if char == lmatget(border_el, lmat))

        # For the upper edge, we can say that it does not start a new edge if
        # it has a patch above it or to the left of it
        #
        # i.e
        #
        # AX : The x does not start anythign, becasue we say it belongs to the one on the left
        #
        # A
        # X  : THere is no need for a new fence if there is already one there


#        for tel in border((lind, cind)):
#            if char == lmatget(tel, mat=lmat):
#                matching_numbers[lind, cind] += 1


remembered = dict()
# Calculate areas
for lind, line in enumerate(lmat[:-1]):
    for cind, char in enumerate(line[:-1]):
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


tot = np.sum(areas*(fences))
print("fences  = " , fences )
print("areas  = " , areas )
print("tot  = \n" , tot )
#disc = discover_frontier((0,0))
#disc_list = list(disc)
#disc_list.sort()
#print("disc_list  = " , disc_list )
#print("matching_numbers  = " , matching_numbers )
