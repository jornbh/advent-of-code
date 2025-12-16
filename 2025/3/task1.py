
# <jorn-config>
# Command:py "task1.py" 2>&1 | tee delete-me.pytest-log
# logfile: delete-me.pytest-log
# print-function: info
# tagged-prints: true
# disabled-extensions: term-looker
# disabled-extensions: open-side-definition;term-looker;open_import_definition_in_side_bar
# goto-last-vimtag: true
# # disable_side_view: false
# show_logfile_without_vimtag: true
# close-terminals-on-run: true
# side-definition-start-searching-from-tag:
# side-definition-start-searching-from-line:10
#  </jorn-config>

def info(*args, **kwargs):
    return
    print(*args, **kwargs)
def get_joltages():
    with open( "input.txt" ) as f:
        li = [
         [int(char) for char in line.strip()]
         for line in f
         ]
    return li

BATERIES = []
def get_max_joltage(bat_no, start_ind , capacity=2):
    batery = BATERIES[bat_no][start_ind:]
    # info(f"CALLING batery, capacity:  {batery, capacity} vimtag65764624980247" ) #fmt: skip
    if len(batery) == 1:
        return int(batery[0])
    if len(batery) == 0:
        return ""
    if capacity == 1 :
        return max(batery)

    assert batery, f"batery, {batery}"
    candidate_strings = []
    for ind, head in enumerate(batery):
        info(f"head:  {head} vimtag6340835127803" ) #fmt: skip
        # Break before it gets bad
        if ind+1 == len(batery):
            break
        new_ind = ind + start_ind + 1
        sliced = batery[ind+1:]
        tail_result = get_max_joltage(bat_no, new_ind , capacity=capacity -1 )
        candiate_str = str(head) + str(tail_result)
        candidate_strings.append(candiate_str )
        assert candidate_strings
        info(f"candiate_str:  {candiate_str} vimtag75130229316901" ) #fmt: skip
    info(f"candidate_strings:  {candidate_strings} vimtag23786101113313" ) #fmt: skip
    assert candidate_strings
    return max(map(int,candidate_strings))
    # return


bats = get_joltages()
BATERIES = bats
# info(f"bats:  {bats} vimtag1746148140331" ) #fmt: skip
# info(f"cand:  {cand} vimtag16812762234336" ) #fmt: skip
joltages = []
for ind in range(len(bats)):
    joltage = get_max_joltage(ind, 0, capacity=2)
    joltages.append(joltage)
    print(f"joltage:  {joltage} vimtag84823010777984" ) #fmt: skip
info(f"joltages:  {joltages} vimtag37755537611186" ) #fmt: skip
tot = sum(joltages)
print(f"tot:  {tot} vimtag11649918082019" ) #fmt: skip
# info(f"bats:  {bats} vimtag22460262569841" ) #fmt: skip
