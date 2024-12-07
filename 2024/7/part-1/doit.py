

with open("input.txt") as f:
    lines = [line.strip() for line in f]

total = 0

for line in lines:
    ans, params_str = line.split(":")
    ans=int(ans)
    params =[int(el) for el in params_str.strip().split()]
    subtots = [params[0]]
    for new_param  in params[1:]:
        new_subtots_mat = [ [
            subtot + new_param,
            subtot * new_param,
            int(str(subtot) + str(new_param))
            ] for subtot in subtots ]
        subtots = { el for li in new_subtots_mat for el in li }
    if ans in subtots:
        print("yes", line)
        total +=ans
    else:
        print("NO", line)

print(total)
