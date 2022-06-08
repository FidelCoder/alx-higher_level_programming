#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if roman_string is None or type(roman_string) != str:
        return 0
    sum = 0
    ite = False
    for n in range(0, len(roman_string), 1):
        x = roman[roman_string[n]]
        if ite:
            ite = False
            continue

        def y(x, y): return roman[roman_string[n+1]] if x <= y else 0
        z = y(n+1, len(roman_string) - 1)
        if z > x:
            sum += z - x
            ite = True
        else:
            sum += x

    return sum
