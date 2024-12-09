from collections import defaultdict
import numpy as np



with open("input.txt") as f:
    lines = [l.strip() for l in f]

dd = defaultdict(list)
for lind, line in enumerate(lines):
    for cind, char in enumerate(line):
        if char != "." and char != "#":
            dd[char].append(np.array([lind,cind]))

print("dd  = " , dd )

def is_inside_frame(lmax, cmax, pos):
    return (
    pos[0] < lmax
    and pos[1] < cmax
    and pos[0] >= 0
    and pos[1] >= 0
    )
is_inside = lambda pos : is_inside_frame(len(lines), len(lines[0]), pos)


antinodes = []

for char, positions  in dd.items():
    for ind, p1 in enumerate(positions) :
        for p2 in positions[ind:]:
            if p1 is p2:
                continue
            dp1 = p1 - p2
            antinode_1 = p1 + dp1
            if is_inside(antinode_1) :
                antinodes.append(antinode_1)



            dp2 = p2 - p1
            antinode_2 = p2 + dp2
            if is_inside(antinode_2) :
                antinodes.append(antinode_2)



print("antinodes  = " , (antinodes ) )
print("antinodes  = " , len(set( map(tuple, antinodes)  ) ))

print("lines  = " , *lines , sep="\n")
