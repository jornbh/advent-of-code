# Nothing changed yet. One plan would be to perform the simulation, keep a
# trail of position + orientation and then see if doing one rotation will get
# you into the old trail again
#
# This will be hard if there are multiple bounces and such before leaving the area



import copy
import numpy as np


def get_input():
    with open("input.txt") as f:
        return list(map(str.strip, f))

rotator = np.array([ [0,1], [-1,0]])


def test_rotate():
    a = np.array([-1,0])
    a = rotator @ a
    assert (a == np.array([0,1])).all()
    a = rotator @ a
    print("a  = " , a )
    assert (a == np.array([1,0])).all()
    a = rotator @ a
    print("a  = " , a )
    assert (a == np.array([0,-1])).all()

def get_start_pos(lines_arg):
    for lind, line in enumerate(lines_arg):
        for cind, char in enumerate(line):
            if char == "^":
                return np.array([lind, cind])

def safe_get(matrix, pos):
    lind = pos[0]
    cind = pos[1]
    try:
        return matrix[lind][cind]
    except:
        return None

def get_new_pos_and_dp(matrix, pos, dp):
    # If wall; rotate
    while  safe_get(matrix, pos+dp)  == "#":
        dp = rotator @ dp
    new_pos = pos + dp
    return (new_pos , dp)

lines = get_input()
start_pos = get_start_pos(lines)


def search_for_exit(grid):
    dp = np.array([-1,0])
    positions = []
    visited = set()
    current_pos = start_pos
    while safe_get(grid, current_pos) is not None:
        (current_pos, dp) = get_new_pos_and_dp(grid, current_pos, dp)
        positions.append(current_pos)
        visit_el =tuple(current_pos) + tuple(dp)
        if visit_el in visited:
            return False, positions
        else:
            visited.add(visit_el)
    return True, positions


lmat = [list(l) for l in lines]
escaped , r_basis = search_for_exit(lmat)
assert escaped
if safe_get(lmat, r_basis[-1]) is None:
    r_basis.pop() # Last element is out of range

# Uniqe only
r_basis = set(map( tuple, r_basis))
print("r_basis  = " , r_basis )
tot = 0
#r_basis = [ (lind, cind)
#    for lind, line in enumerate(lines)
#        for cind, char in enumerate(line)
#           ]

obstacle_positions = []
for ind, (obstacle_lind, obstacle_cind) in enumerate(r_basis):
    old_char = lmat[obstacle_lind][obstacle_cind]
    # Print progress
    if ind % 100 == 0:
        print("progress ", ind, "/" , len(r_basis))
    if old_char != "#" and (obstacle_lind, obstacle_cind) != tuple(start_pos):
        lmat[obstacle_lind][obstacle_cind] = "#"
        escaped, r = search_for_exit(lmat)
        if not escaped:
            tot = tot +1
            obstacle_positions.append((obstacle_lind, obstacle_cind))
            print("\nsub-tot  = " , tot , end="")
        else:
            print("e", end="")
        lmat[obstacle_lind][obstacle_cind] = old_char

print()


print("obstacle_positions  = " , obstacle_positions )
print("-"*26)
print("ESCAPED", escaped)
unique_positions = set(tuple(el) for el in r_basis)
lmatp = copy.deepcopy(lmat)
for (lind, cind) in unique_positions:
    if lmatp[lind][cind] != "^":
        lmatp[lind][cind] = "X"
for lind, cind in obstacle_positions:
    lmatp[lind][cind] = "O"

for line in lmatp:
    print("".join(line))
print("-"*26)
print("\nfinal tot" , tot )

