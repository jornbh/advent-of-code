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

def is_parallel_points(test_point, sender_1, sender_2):
    d1 = test_point - sender_1
    d2 = test_point - sender_2

    inner_squared = np.inner(d1, d2)**2
    abs_squared = np.inner(d1, d1) * np.inner(d2, d2)
    return abs_squared == inner_squared

def test_point(dd, point):


    for char, positions  in dd.items():
        for ind, sender_1 in enumerate(positions) :
            for sender_2 in positions[ind:]:
                if sender_1 is sender_2:
                    continue
                if is_parallel_points(point, sender_1, sender_2) :
                    return True
    return False



antinodes = []

for lind, line in enumerate(lines):
    for cind, char in enumerate(line):
        point = np.array([lind, cind])
        if test_point(dd, point):
            antinodes.append(point)

print("___________________")
tmat = [[(char) for char in line] for line in lines]
for antinode in antinodes:
    lind, cind = antinode
    tmat[lind][cind]="¤"

for line in tmat:
#    print("line = " , line)
    joined_list = "".join(line)
    print(joined_list, sep="\n")

print("___________________")
print("antinodes  = " , (antinodes ) )
print("antinodes  = " , len(set( map(tuple, antinodes)  ) ))

print("lines  = " , *lines , sep="\n")
