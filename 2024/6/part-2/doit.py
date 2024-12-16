import copy
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

rotator = np.array([
                    [0,1],
                    [-1,0]
                    ])

def test_rotator():
    def test(test_input, expected) :
        arr = np.array(test_input)
        print("arr = " , arr)
        output = rotator @ arr
        print("output  = " , output )
        assert tuple(output) == expected, f"Not expected {tuple(arr), expected}"
    test((-1,0) , (0,1))
    test((0,1) , (1,0))
    test((1,0) , (0,-1))
    test((0,-1) , (-1,0))

test_rotator()

def get_input():
    with open("input.txt") as f:
        return list(map(str.strip, f))



def get_grid(lines_arg):
    grid = np.zeros([len(lines) +1 , len(lines[0]) +1], np.int_)
    for lind, line in enumerate(lines_arg):
        for cind, char in enumerate(line):
            if char == "#":
                grid[lind,cind] = -1
    # Padding to test if inside or not
    grid[:,-1] = -2
    grid[-1,:] = -2
    return grid
def is_collision(grid,pos):
    return grid[pos[0], pos[1]] == -1

lines = get_input()
basis_grid = get_grid(lines)

def is_inside(grid, pos):
    return -2 != grid[pos[0], pos[1]]
    # is_smaller = grid.shape > pos
    # is_bigger = pos >= 0
    # return np.all(is_smaller) and  np.all(is_bigger)

def new_pos_and_dp(grid, pos, dp):
    new_pos = pos + dp
    new_dp = dp
    counter = 0
    # If outside, it is good
    while is_inside(grid, new_pos) and is_collision(grid,new_pos):
        new_dp = rotator @ new_dp
        new_pos = pos + new_dp
        counter += 1
        assert counter < 5 #Just a desperate trick
    return new_pos, new_dp


def test_is_inside():
    play_grid = np.array([
            [0, -1,0],
            [-1, 0,-1],
            [0, -1,0],
    ])
    g1 = copy.deepcopy(play_grid)
    tested = is_inside(g1, np.array([0,1]))
    print("tested  = " , tested )
    assert is_inside(g1, np.array([0,1]))
test_is_inside()
def test_grid_stuff():
    play_grid = np.array([
            [0, -1,0],
            [-1, 0,-1],
            [0, -1,0],
    ])
    start_pos = np.array([1,1])


    def test(grid, expected):
        print("grid = " , grid)
        start_dp = np.array([-1,0])
        print("start_dp  = " , start_dp )
        print("start_pos = " , start_pos)
        new_pos, new_dp = new_pos_and_dp(grid, start_pos, start_dp)
        print("new_pos, new_dp  = " , new_pos, new_dp )
        assert tuple(new_pos) == expected, f"{(tuple(new_pos), expected)}"


    g1 = copy.deepcopy(play_grid)
    g1[2,1] = 0
    test(g1, (2,1))
    g2 = copy.deepcopy(play_grid)
    g2[1,0] = 0
    g2[1,2] = 0
    print("g2  = " , g2 )
    test(g2, (1,2) )
    g3 = copy.deepcopy(play_grid)
    g3[1,2] = 0
    test(g3, (1,2))
    g4 = copy.deepcopy(play_grid)
    g4[0,1] = 0
    test(g4, (0,1))

# test_grid_stuff()


def sim(grid, start_pos):
    dp = np.array([-1,0], np.int_)
    pos = start_pos
    visited = []
    while is_inside(grid, pos):
        grid[pos[0], pos[1]] += 1
        if grid[pos[0], pos[1]] > 6:
            return None # No escape
        pos, dp = new_pos_and_dp(grid, pos, dp)
        visited.append(pos)
    visarray = np.array(visited)
    # plt.plot( - visarray[:,1], - visarray[:,0], "-x")
    # plt.plot(- start_pos[1], - start_pos[0],   "rx")
    # plt.show()
    return visited


def main():
    lines = get_input()

    start_points = [(lind, cind)
    for lind , line in enumerate(lines)
        for cind, char in enumerate(line)
                if char == "^"]
    lind, cind = start_points[0]
    first_start_pos = np.array([lind,cind])


    base_grid = get_grid(lines)

    grid = copy.deepcopy(base_grid) 
    v = sim(grid, first_start_pos)

    good_obstructions = []
    later_start_pos = first_start_pos
    for ind, pos in enumerate(v):
        if ind > 1:
            # later_start_pos = v[ind -1]
            later_start_pos = first_start_pos
        if ind % 10 == 0:
            print("Progress; " , ind, "/", len(v))
        grid = np.copy(base_grid)
        # Set obstruction
        grid[pos[0], pos[1]] = -1
        v_obstructed = sim(grid, later_start_pos)
        if v_obstructed is None:
            assert [p for p in v if np.all(p == pos)], f"No pos {pos}"
            good_obstructions.append(pos)
            print("adding")

        #profiling hack
        # if ind > 1000:
        #     break
#    print("TOTAL is ", tot)
    
    grid = copy.deepcopy(base_grid) 
    v = sim(grid, first_start_pos)
    obst_arr = np.array(good_obstructions) 
    varr = np.array(v)
    plt.plot( varr[:,1], -varr[:, 0], "-x")
    plt.plot( obst_arr[:,1], -obst_arr[:,0], "yo")
    plt.plot([first_start_pos[1]], [-first_start_pos[0]], "rx")

    for ind, line in enumerate(grid):
        r = np.arange(len(line))
        o =  np.ones(line.shape)
        
        m = grid[ind,:] == -1
        plt.plot(r[m], - ind*o[m], "ko")
 
    lend,cend =  grid.shape
    plt.plot([0, cend, cend, 0,0] , 
        [0, 0, -lend, -lend,0], "k")

   
    print("TOTAL is  = " , len(set(tuple(el) for el in good_obstructions)) )
    plt.show() 
    print("good_obstructions  = " , good_obstructions )
    print("TOTAL is  = " , len(set(tuple(el) for el in good_obstructions)) )



main()


