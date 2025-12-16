# <jorn-config>
# Command:py "doit.py" 2>&1 | tee delete-me.pytest-log
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
            print(f"key:  {key} vimtag76177370598593" ) #fmt: skip
            print(f"key, *tail:  {tail} vimtag14442086613347" ) #fmt: skip
            graph[key] = tail
    # graph
    print(f"graph:  {graph} vimtag11085668421244" ) #fmt: skip
    return graph

import functools

@functools.cache
def solve_graph( node):
    # Dynamic programming

    if node == 'out':
        return 1
    tot = 0
    for neigh in GRAPH[node]:
        tot += solve_graph( neigh)
    return tot




GRAPH = get_graph()
resoult = solve_graph( 'you')
print(f"resoult:  {resoult} vimtag27527442687581" ) #fmt: skip
