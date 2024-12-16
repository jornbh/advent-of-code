import numpy as np
from collections import defaultdict
import json
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]


stones = [ int(el) for el in lines[0].split()]

def update_stone(stone):
    stone_str = (str(stone))

    if stone == 0:
        output = [1]
    elif len(stone_str) % 2 == 0:
        stone_1 = stone_str[:(len(stone_str)//2) ]
        stone_2 = stone_str[(len(stone_str)//2): ]
        output = [int(stone_1), int(stone_2)]
    else:
        output = [stone *2024 ]
    return output

def flatten(list_of_lists):
    for sublist in list_of_lists:
        for el in sublist:
            yield el
print("stones  = " , stones )



def count_stones(stones_dict):
    return sum(val for key, val in stones_dict.items())

def stones_list_to_stones_dict(start_stones):
    stones = defaultdict(int)
    for stone in start_stones:
        stones[stone] += 1
    return stones

# We may be able to cache some of this stuff and then solve it using dynamic programming
# This is not solvable by normal means at least
def expand_stones(start_stones, n_blinks=25):
    # The key is the kind of stone, the el is the number of stones
    stones = stones_list_to_stones_dict(start_stones)

    # Missing the flat part of the flatmap
    for blink_no in range(n_blinks) :
        new_stones_unflattened = ((update_stone(ind), el) for ind,el in stones.items())

        new_stones = defaultdict(int)
        for stone_list, count  in new_stones_unflattened:
            for stone in stone_list:
                new_stones[stone] += count
        stones = new_stones
        print( "iteration" , blink_no, count_stones(stones))
    return stones

## Test the function
def test_foo():
    test_inputs = [
    [125,17],
    [253000,1,7],
    [253,0,2024,14168],
    [512072,1,20,24,28676032],
    [512,72,2024,2,0,2,4,2867,6032],
    [1036288,7,2,20,24,4048,1,4048,8096,28,67,60,32],
    [2097446912,14168,4048,2,0,2,4,40,48,2024,40,48,80,96,2,8,6,7,6,0,3,2],
    ]

    test_stones =   [125 , 17]
    for ind, test_line  in enumerate(test_inputs):
        test_result = expand_stones(test_stones, n_blinks=ind)
        print("test_result  = " , ind, test_result )
        test_result_stones = test_line
        assert stones_list_to_stones_dict(test_result_stones) == test_result, f"{test_result_stones} == {test_result}"
        print("test_result  = " , test_result )
        print("test_result  = " , len(test_result) )

    assert count_stones(test_result) == 22

test_foo()

print("stones = " , stones)
#stones = expand_stones(stones, n_blinks=25)
stones = expand_stones(stones, n_blinks=75)

print("stones  = " , stones )
print("stones  = " , count_stones(stones) )



