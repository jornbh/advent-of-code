from  my_input import *

from collections import defaultdict


rules_dict = defaultdict(set)
for before, after in rules:
    rules_dict[before].add(after)


def is_good_book_foo(book):
    discovered = set()
    is_good_book = True
    for page in book:
        if rules_dict[page].intersection(discovered):
            is_good_book = False
            break
        discovered.add(page)
    return is_good_book
def split_good_or_bad_books(imput_lines):
    bad_lists = []
    good_lists = []
    for ind , book in enumerate(imput_lines):
        if is_good_book_foo(book) == False:
            bad_lists.append(book)
        else:
            good_lists.append(book)

    return good_lists,bad_lists

good, bad_lists = split_good_or_bad_books(lines)



#fixed_bad_books = [sorted(el, key=lambda page: rules_dict[page]) for el in bad_lists ]

# TODO: Fix the bad sorting

#good2, bad2 = split_good_or_bad_books(fixed_bad_books)



def get_characteristics():
    lenrules = [len(rules_dict[ el ])  for line in bad_lists  for el in line  ]
    keys_and_vals = [ (key, val) for key, val in rules_dict.items() ]
    print(*keys_and_vals, sep="\n")

def need_to_swap(lhs, rhs):
    # Needs to be swapped
    # No idea why this was the correct logic, lol, I thought it was going to be the oposite first
    if rhs in rules_dict[lhs]:
        return False
    return True



# buble sort using a different function
def fix_book(book):
    for i in range(len(book)):
        for j in range(i, len(book)):
            if need_to_swap(book[i], book[j]):
                book[i], book[j] = book[j], book[i]
    return book


# Asserts are golden to see that your code does what you think it does
assert len(bad_lists) > 0


fixed_books = []

for book in bad_lists:
    is_good = is_good_book_foo(book)
    assert (not is_good)
    book = fix_book(book)
    is_good = is_good_book_foo(book)
    assert (is_good)
    get_characteristics()
    fixed_books.append(book)

print("good, bad_lists  = " , good, bad_lists )
middle_pages = [
        el[len(el)//2] for el in fixed_books ]
tot = sum(middle_pages)
print("tot  = " , tot )
print("middle_pages  = " , middle_pages )
print("DONE")
