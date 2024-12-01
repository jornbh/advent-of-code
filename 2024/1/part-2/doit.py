# Using vim to maually separate the input is faster in this case
from collections import defaultdict


with open('b.txt', 'r') as f:
    b= [int(line) for line in f]

with open('a.txt', 'r') as f:
    a= [int(line) for line in f]

occ = defaultdict(lambda : 0 )
for el in b:
    occ[el] += 1
tot = 0
for el in a:
    tot += el * occ[el]
print(tot )
