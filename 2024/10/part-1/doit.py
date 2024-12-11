from functools import reduce
import itertools
import functools
import numpy as np
from collections import defaultdict
from collections  import deque
def mapL(*args):
    return list(map(*args))
def get_input():
    with open("input.txt") as f:
        lines = (mapL(str.strip, f))
    return lines
lines = get_input()
print("lines  = " , lines )

diffs = np.array( [ [1,0], [-1,0], [0,1], [0,-1], ])
print("diffs  = " , diffs )

start_points = [tuple([int(lind), int(cind)]) for lind, line in enumerate(lines) for cind, char in enumerate(line) if char == "0" ]
print("start_points  = " , start_points )

@functools.cache
def recursive_follow_trails(start_point):
    new_poins_to_explore = []
    current_height = int(lines[start_point[0]][start_point[1]])

    # Already found the top
    if current_height == 9:
        return [ start_point ]
    for diff in diffs:
        new_point = np.array(diff) + np.array(start_point)
        lind= new_point[0]
        cind= new_point[1]
        if lind >= 0 and cind >= 0  and lind < len(lines) and cind < len(lines[0]):
            new_heicht_el =lines[lind][cind]
            new_height =  (new_heicht_el != "." ) and int(new_heicht_el)
            if new_height == current_height +1:
                new_poins_to_explore.append(tuple(new_point ))
        else:
            new_height =None

    # Follow the newly_constructed_border
    total_list = list()
    for new_point in new_poins_to_explore:

        new_addition = recursive_follow_trails(new_point)
        total_list  += (new_addition)
        print("new_height  = " , new_height )
    return total_list

followed_trails = []

for ind, start_point in enumerate(start_points):
    print(f"Progress {ind}/{len(start_points)}")
    followed_trails.append( recursive_follow_trails(start_point))

print("followed_trails  = " , followed_trails )

one_trail = list(itertools.chain(*followed_trails))

for el in one_trail:
    lind = el[0]
    cind = el[1]
    char = lines[lind][cind]
print("rank",len(one_trail))



#print("only_endings  = " , only_endings )
##trail_ranks = [  len(el for el in trailhead if  ) for trailhead in trail_ends ]
#print("trail_ranks  = " , trail_ranks )
#total_rank = sum(trail_ranks)
#print("total_rank  = " , total_rank )
