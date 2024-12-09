from functools import reduce
from collections  import deque
from collections  import defaultdict
def mapL(*args):
    return list(map(*args))
def get_input():
    with open("input.txt") as f:
        lines = (mapL(str.strip, f))
    return lines


totstring_examples = [
"00...111...2...333.44.5555.6666.777.888899",
"0099.111...2...333.44.5555.6666.777.8888..",
"0099.1117772...333.44.5555.6666.....8888..",
"0099.111777244.333....5555.6666.....8888..",
"00992111777.44.333....5555.6666.....8888..",
]
def make_total_list(moved, moved_to):
    total = []
    for ind, el in enumerate(ids[:-1]):
        if not moved[ind]:
            total.extend([ind] * size_of_page(ind) )
        else:
            total.extend([None] * size_of_page(ind) )

        # The free pages are after the normal ones
        for moved_to_el in moved_to[ind]:
            repeated_page = [moved_to_el] * size_of_page(moved_to_el)
            total.extend(repeated_page )
        used_space = sum(map(size_of_page, moved_to[ind]))
        unused_space = ( free_lens[ind] - used_space )
        total.extend([None] * unused_space )
    return total

def make_total_string(total):
    totstringlist= []
    for total_el in total:
        if total_el is not None :
            totstringlist.append(total_el,)
        else:
            totstringlist.append(".")
    totstring = "".join(map(str, totstringlist))
    return totstring

# There is only one
def get_line():
    lines = get_input()
    assert lines
    return lines[0]

# TODO : Loop
line = get_line()

page_sizes=(mapL(int, line[0::2]))
free_lens=(mapL(int, line[1::2]))


ids = range(len(page_sizes))



# Global mutable state
moved = [False for el in ids]
moved_to = [[] for el in free_lens]

def size_of_page(pid):
#    print("Size of page: ", pid, page_sizes[pid])
    return page_sizes[pid]

assert size_of_page(1)  > 0


def room_in_free_space(frid, moved_to_el):
    used_list = [size_of_page(el) for el in moved_to_el]
    return free_lens[frid] -  sum(used_list)

for page_index, page_size in reversed(list(enumerate(page_sizes))):
    print(page_index)
    # temp_totstring = make_total_string(make_total_list(moved, moved_to))
#    print("temp_totstring  = " , temp_totstring )


    # Test all possible move-to locations
    for tind, moved_to_el in enumerate(moved_to[:page_index]):
        move_to_space = room_in_free_space(tind, moved_to_el)
        if move_to_space >= page_size:
            moved_to[tind].append(page_index)
            moved[page_index] = True
            break





#Last one
if not moved[-1]:
    total.extend([-1] * size_of_page(-1) )

print("moved_to  = " , moved_to )
print("moved  = " , moved )

total = make_total_list(moved, moved_to)
totsum = 0
for ind,el in enumerate(total):
    if el:
        totsum += ind*el


print("totsum  = " , totsum )

print("total  = " , total )
print("free_lens = " , free_lens)

totstring = make_total_string(total)
"00...111...2...333.44.5555.6666.777.888899"
print("totstring  = " , totstring )
print("Ref" , "00992111777.44.333....5555.6666.....8888.." )
assert "00992111777.44.333....5555.6666.....8888.." == totstring
