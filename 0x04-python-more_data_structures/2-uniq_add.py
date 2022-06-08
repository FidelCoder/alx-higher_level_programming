#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    mr = list.copy(my_list)
    mr.sort()
    for i in range(len(mr)):
        if i != 0 and mr[i] == mr[i-1]:
            continue
        else:
            sum += mr[i]
    return sum
