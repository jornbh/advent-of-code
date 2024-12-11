import numpy as np


def get_input():
    with open("input.txt") as f:
        lines = list(map(str.strip, f))
    return lines

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
def get_start_pos(lines):
    for lind, line in enumerate(lines):
        for cind, char in enumerate(line):
            if char == "^":
                return np.array([lind, cind])

def lget(lines, pos):
    lind = pos[0]
    cind = pos[1]
    try:
        return lines[lind][cind]
    except:
        return None

def get_new_pos_and_dp(lines, pos, dp):
    # If wall; rotate
    while  lget(lines, pos+dp)  == "#":
        dp = rotator @ dp
    new_pos = pos + dp
    return (new_pos , dp)

lines = get_input()
start_pos = get_start_pos(lines)
dp = np.array([-1,0])

positions = []

pos = start_pos
while lget(lines, pos) is not None:
    (pos, dp) = get_new_pos_and_dp(lines, pos, dp)
    positions.append(pos)
# The last position is outside the map, drop the last one
positions= positions[:-1]
unique_positions = set(map(tuple, positions))
# The start positon may not have been visited yet, so it must be added
unique_positions.add(tuple(start_pos))
print("unique_positions  = " , len(unique_positions ) )


lmat = [list(l) for l in lines]

for (lind, cind) in unique_positions:
    lmat[lind][cind] = "X"

#for line in lmat:
#    print("".join(line))

#for line in lines:
#    print(line)
