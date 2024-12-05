from  my_input import *

from collections import defaultdict


rules_dict = defaultdict(set)

middle_pages = []

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
    if is_good_book == True:
        middle_pages.append(line[len(line)//2])
        print(f"Is good book {ind}")

print("middle_pages  = " , middle_pages )
print("DONE")
print(sum(middle_pages))
#print(my_input.rules)
