
# <jorn-config>
# Command:py "doit2.py" 2>&1 | tee delete-me.pytest-log
# logfile: delete-me.pytest-log
# print-function: print
# tagged-prints: true
# disabled-extensions: open-side-definition;term-looker;open_import_definition_in_side_bar
# disabled-extensions: term-looker
# goto-last-vimtag: true
# show_logfile_without_vimtag: true
# close-terminals-on-run: true
# side-definition-start-searching-from-tag:
# side-definition-start-searching-from-line:10
#  </jorn-config>
def get_graph():
    graph = {}
    with open("input.txt") as f:
        for line in f:
            key_raw, *tail = line.split()
            key = key_raw[:-1]
            graph[key] = tail
    # graph
    return graph

import functools

@functools.cache
def solve_graph( node, over_fft, over_dac):
    # Dynamic programming
    print(f"node:  {node} vimtag13951506207966" ) #fmt: skip
    if node == 'out':
        if    over_fft  == True and  over_dac == True :
            return 1
        else:
            return 0
    if node == 'dac':
        over_dac = True
        print(f"over_dac:  {over_dac} vimtag50935880340023" ) #fmt: skip
    if node == 'fft':
        over_fft = True
    tot = 0
    for neigh in GRAPH[node]:
        tot += solve_graph( neigh, over_fft, over_dac)
    return tot




GRAPH = get_graph()
resoult = solve_graph( 'svr', False, False )
print(f"resoult:  {resoult} vimtag27527442687581" ) #fmt: skip
