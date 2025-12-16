
# <jorn-config>
# Command:py "largest-number.py" 2>&1 | tee delete-me.pytest-log
# logfile: delete-me.pytest-log
# print-function: print
# tagged-prints: true
# disabled-extensions: open-side-definition;term-looker;open_import_definition_in_side_bar
# disabled-extensions: term-looker
# goto-last-vimtag: true
# # disable_side_view: false
# show_logfile_without_vimtag: true
# close-terminals-on-run: true
# side-definition-start-searching-from-tag:
# side-definition-start-searching-from-line:10
#  </jorn-config>

# this seems to work for the simple case. not tested for the big one

import functools
basis = "123456789987654321"
@functools.cache
def foo(start, end, n_letters):
    slice = basis[start:end]
    if len(slice) < n_letters:
        return "" # Always dominated by longer numbers
    if n_letters == 1:
        candidates = map(int, slice)
        m = max(candidates)
        return str(m)

    maximum = 0
    for ind in range(len(slice)):
        head = slice[ind]
        tail = foo(start + ind + 1, end, n_letters - 1 )
        candidate = int(head + tail )
        maximum = max( maximum, candidate)
    return str(maximum)
res = foo(0, len(basis), 3)
