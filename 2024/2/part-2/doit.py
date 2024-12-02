from my_input import *
import numpy as np


print(basis)


tot = 0

def test_growing_case(experiment):
    good = True
    for ind,el in enumerate(experiment[0:-1]):
        diff = experiment[ind+1] - el
        good_size = abs(diff) <=3 and abs(diff) >=1
        is_growing = diff >= 0
        good = good and (good_size and is_growing )
    return good
for experiment_list in basis:
    experiment = np.array(experiment_list)
    print(experiment)
    good = test_growing_case(experiment)
    good_neg = test_growing_case(-experiment)

    if good or good_neg :
        tot += 1
        continue
    selector = np.full(experiment.shape, True)

    break_selector = False
    for ind in range(len(selector)):
        selector[ind] = False


        good = test_growing_case(experiment[selector])
        good_neg = test_growing_case(-experiment[selector])
        if good or good_neg :
            print("Drop fix", ind)
            break_selector = True
            break

        selector[ind] = True
    if break_selector :
        print(ind)
        print("brsel", selector)
        tot += 1
        continue

    print("Good", good, good_neg )


print(tot)
