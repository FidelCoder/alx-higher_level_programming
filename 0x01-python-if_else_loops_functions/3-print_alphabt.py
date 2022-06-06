#!/usr/bin/python3
for j in range(97, 123):
    if chr(j) != 'q' and chr(j) != 'e':
        print('{:c}'.format(j), end='')
