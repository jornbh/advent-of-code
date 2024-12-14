Width = 101
Height  = 103
Time = 100
import numpy as np
from collections import defaultdict

with open('input.txt') as f:
    lines = list(line.strip() for line in f)
positions_list = []
velocities_list = []
for line in lines:
    p_part, v_part = line.split()
    px,py = p_part.strip("p=").split(",")
    positions_list.append((int(px),int(py)))
    vx,vy = v_part.strip("v=").split(",")
    velocities_list.append((int(vx),int(vy)))



positions=np.array(positions_list)
velocities = np.array(velocities_list)
print("velocities : ", velocities.shape );
print("positions: ", positions.shape);
def get_end_positions(positions, velocities, time=Time, width = Width, height = Height):
    dp = time * velocities
    print("dp : ", dp );

    mods = np.array([width, height])
    moded = (positions + dp) % mods
    print("moded : ", moded );
    return moded

moded =  get_end_positions(positions, velocities, time=Time )


dd = defaultdict(int)
borders = 0
for xend, yend in moded:
    if xend != (Width//2) and yend != (Height // 2) :
        ind = (xend // (Width//2+1) ,yend // (Height//2+1) )
        print("ind : ", ind );

        dd[ind] += 1
    else:
        borders += 1
print("borders : ", borders );
print("dd")
for key,val in sorted(dd.items()):
    print(key, val)
tot = 1
for key,item in dd.items():
    tot *=item
print("tot *: ", tot );



