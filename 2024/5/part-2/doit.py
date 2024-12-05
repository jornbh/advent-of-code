from  my_input import *

from collections import defaultdict


rules_dict = defaultdict(set)


bad_lists = []
for before, after in rules:
    rules_dict[before].add(after)

for ind , line in enumerate(lines):
    discovered = set()
    is_good_book = True
    for page in line:
        if rules_dict[page].intersection(discovered):
            is_good_book = False
            break
        discovered.add(page)
    if is_good_book == False:
        bad_lists.append(line)

print("DONE")
#print(my_input.rules)
