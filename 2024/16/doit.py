import numpy as np
import re
from collections import defaultdict
import json
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
reg = re.compile("\\d+")
to_nums = lambda line: reg.findall(line)
a_buttons_lines = np.array([ to_nums(line) for line in  lines[0::4]],  np.int64)
b_buttons_lines = np.array([to_nums(line) for line in lines[1::4]],  np.int64)
prizes_lines = np.array([to_nums(line) for line in lines[2::4]],  np.int64)

# Solution for part 2
prizes_lines += 10000000000000

def cost(pair):
    a_presses, b_presses = pair
    return  3* a_presses + b_presses

totals = []



for i in range(len(prizes_lines)):
    a_col = a_buttons_lines[i,:]
    b_col = b_buttons_lines[i,:]
    prize_col = prizes_lines[i,:]

    con = np.vstack([a_col,b_col], ).transpose()
    sol_double  = np.linalg.solve(con, prize_col)
    sol = np.round(sol_double)
    if np.all( ( con @ sol == prize_col ) ) and np.all( sol >= 0 ) :
        totals.append(sol)


#for i in range(len(prizes_lines)):
#    a_col = a_buttons_lines[i,:]
#    b_col = b_buttons_lines[i,:]
#    prize_col = prizes_lines[i,:]
#    matches = [ (amul, bmul) for amul in range(100) for bmul in range(100) if np.all((amul*a_col + bmul*b_col) == prize_col) ]
#    if matches:
#        totals.append(min(matches, key=cost))
#    else:
#        pass




print("totals  = " , totals )

tot = sum(map(cost, totals))
print("tot  = " , tot )

