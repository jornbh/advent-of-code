Width = 101
Height  = 103
Time = 100
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


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

    mods = np.array([width, height])
    moded = (positions + dp) % mods
    return moded


def print_res(end_set):
    for x in range(Width):
        line = []
        for y in range(Height  ):
            if (x,y) in end_set:
                line.append("X")
            else:
                line.append(".")
        print("".join(line))

    print("")
    print("")
    print("")
    print("")
    print("")

#Most of the robots should arrange themselves


t_end = 10**6
hallmarks = list(round(el) for el in reversed( np.linspace(0, t_end, num=1000)))
print("hallmarks : ", hallmarks );
bestx = 0
besty = 0
bestt =0
variances_x = []
variances_y = []
times = range(49, t_end, 103)
for end_time in times :
    if end_time == hallmarks[-1]:
        while end_time == hallmarks[-1]:
            hallmarks.pop()
        print("progress:",  end_time, "/", t_end, hallmarks[-1])
    moded =  get_end_positions(positions, velocities, time=end_time )

    vx = np.var(moded[:,0])
    vy = np.var(moded[:,1])

    variances_x .append(vx)
    variances_y .append(vy)

    if vx + vy < 1200:
        print("TIME:", end_time)
        end_set = set(list(map(tuple, moded)))
        print_res(end_set)
#    print("var:", vx+vy)
#    # An egg is convex, so there should only be 2 crossings
#    end_set = set(list(map(tuple, moded)))
#    ddx = defaultdict(int)
#    ddy = defaultdict(int)
#    bad_egg = False
#
#    for x,y in end_set:
#        ddx[x] +=1
#        ddy[y] +=1
#        if ddx[x] > 2 or ddy[y] > 2:
#            bad_egg = True
#
#    xmatches = len([x for x, n in  ddx.items() if n <= 2])
#    ymatches = len([y for y, n in  ddy.items() if n <= 2])
#    print("x matches" , xmatches, ymatches, "/", (bestx, besty, bestt))
#    print("y matches" , )
#
#    if xmatches +ymatches > bestx + besty :
#        bestt = end_time
#        bestx = (xmatches)
#        besty = (ymatches)
#        print_res(end_set)
#
#    if bad_egg :
#        continue



print("variances_x : ", variances_x );
print("variances_y : ", variances_y );


plt.plot(times, np.array(variances_x)*np.array(variances_y))
#plt.plot(times, variances_x)
#plt.plot(times, variances_y)
plt.legend(["vx", "vy"])
plt.show()
print("DONE")


# Interesting points:
# Number 49
# Number 98

# orange: 49 and 152 => 103 period
# Blue 98, 199 => 101 period
# THey are coprime

basea = 49
stepa=103

baseb = 98
stepb = 101


#98 - 49 = 49
# => Number 76 is the displacement of number 49
# =>
#
# 49 as orignal offset, and then, there is the other one.
