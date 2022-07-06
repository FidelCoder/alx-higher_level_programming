#!/usr/bin/python3
"""creates a pascal triangle"""


def pascal_triangle(n):
    """creates a pascal triangle of size n"""
    my_list = []
    if n < 1:
        return ([])
    for i in range(0, n):
        newl = [1]
        if len(my_list) > 0:
            x = my_list[-1]
            for z in range(0, len(x)):
                try:
                    y = x[z] + x[z+1]
                    newl.append(y)
                except Exception as e:
                    newl.append(1)
        else:
            my_list.append(newl)
            continue

        my_list.append(newl)

    return my_list
