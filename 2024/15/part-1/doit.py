import numpy as np
from collections import defaultdict
import json
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]

grid_lines = list()
for ind, line in enumerate(lines):
    if line.strip() == "":
        last_line = ind
        break
    else:
        grid_lines.append(line)

commands = "".join(line for line in lines[last_line:])
print("commands : ", commands );

for ind, el in enumerate(grid_lines):
    print(ind, el)




# Find robo start position
for lind, line in enumerate(lines):
    for cind, char in enumerate(line):
        if "@" == char:
            r = np.array([lind, cind])
            break
            print("r : ", r );

command_to_dp = {
        "^" : np.array([-1,0]),
        "v" : np.array([1,0]),
        "<" : np.array([0,-1]),
        ">" : np.array([0,1]),
        }






char = commands[0]
print("char : ", char );
dp =command_to_dp[char]
print("dp : ", dp );
def get(grid, pos):
    lind, cind = pos
    return grid[lind][cind]

nrp = r + dp
print("nrp : ", nrp );

c = get(grid_lines, nrp)
print("c : ", c );

