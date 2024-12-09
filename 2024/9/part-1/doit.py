from functools import reduce
from collections  import deque
def mapL(*args):
    return list(map(*args))
def get_input():
    with open("input.txt") as f:
        lines = (mapL(str.strip, f))
    return lines
lines = get_input()
assert lines

# TODO : Loop
line = lines[0]

page_sizes=(mapL(int, line[0::2]))
free_lens=(mapL(int, line[1::2]))

ids_base = (range(len(page_sizes)))


pages = mapL(lambda psize, basis : [ basis ]*psize , page_sizes, ids_base)
empty_spaces  = [list("."*length) for length in free_lens]
# print("empty_spaces   = " , empty_spaces  )
# print("pages  = " , list(pages) )


print("combs  = " , len(pages) )
print("combs  = " , len(empty_spaces) )
combs = mapL(list, zip( pages, empty_spaces))
print("combs  = " , combs )


combs = mapL(lambda tu: tu[0] + tu[1]  , combs)
print("combs  = " , combs )
# HACK
output_list = reduce(lambda x,y: x+y , combs)
output_list += pages[-1]
print("output_list + = " , output_list )



i = 0
while i < len(output_list):
    if output_list[i] == ".":
        last_char = output_list.pop()
        while  last_char == "." :
            last_char = output_list.pop()
        # print("output_list[i]  = " , output_list )
        # print(i)
        if i < len(output_list):
            output_list[i] = last_char
        else:
            output_list.append(last_char)
    i+=1
#compacted_string = "".join(output_list)

print("output_list + = " , output_list )
#dot_filler = "."* (len(base_string) - len(compacted_string))
#output_string = compacted_string + dot_filler
# print("output_string  = ".ljust(40) , output_string )
# print("combs  = ".ljust(40) , "".join(combs) )

checksum_parts = list(
        (ind*int(el)) for ind,el in
enumerate(output_list)
)
# print("checksum_parts  = " , checksum_parts )

checksum = sum(checksum_parts)
print("checksum  = " , checksum )



#
#output=[]
#
#output.append(ids_base.popleft())
#free_lens_ind = 0
#free_space=free_lens[0]
#
#while (ids_base):
#    last = ids_base.pop()
#    if page_sizes[last] <= free_space:
#        free_space -= page_sizes[last]
#        output.append(last)
#    else:
#        free_lens_ind += 1
#        free_space = free_lens[free_lens_ind]
#        ids_base.append(last)
#        first = ids_base.popleft()
#        output.append(first)
#    print("last id, last size, free space = " , last ,
#          page_sizes[last]
#          , free_space
#          )
