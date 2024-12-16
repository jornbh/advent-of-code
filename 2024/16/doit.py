import numpy as np
import re
from collections import defaultdict
import json
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
reg = re.compile("\\d+")
to_nums = lambda line: reg.findall(line)
a_buttons_lines = np.array([ to_nums(line) for line in  lines[0::4]])
print("a_buttons_lines  = " , a_buttons_lines )
b_buttons_lines = np.array([to_nums(line) for line in lines[1::4]])
prizes_lines = np.array([to_nums(line) for line in lines[2::4]])
