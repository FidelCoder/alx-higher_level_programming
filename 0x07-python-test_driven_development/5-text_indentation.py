#!/usr/bin/python3
"""
Indentation in Python
function that prints a text with 2 new lines 
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    functions thats adds new line after 
    . ? and :
    """
    newl = ['.', '?', ':']
    sFlag = True
    spaces = [-1, False]
    if type(text) != str:
        raise TypeError("text must be a string")
    str2 = []
    for char in text:
        if char == ' ' and sFlag:
            continue
        if char in newl:
            str2.append(char)
            str2.append('\n')
            str2.append('\n')
            sFlag = True
            continue
        if char == '\n':
            if spaces[1] and spaces[0] > 0:
                for i in range(spaces[0] - 1, len(str2)):
                    str2[i] = ''
            spaces[1] = False
            str2.append(char)
            sFlag = True
            continue
        str2.append(char)
        sFlag = False
        if char == ' ':
            if spaces[1] == False:
                spaces[0] = len(str2)
            spaces[1] = True
        else:
            spaces[1] = False
            spaces[0] = -1

    print("{}".format(''.join(str2)), end='')
