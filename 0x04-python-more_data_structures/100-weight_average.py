#!/usr/bin/python3
def weight_average(my_list=[]):
    if not (my_list):
        return 0
    sum = 0
    number = 0
    for tupl in my_list:
        sum += tupl[0] * tupl[1]
        number += tupl[1]
    return (sum/number)
