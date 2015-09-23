""" Written by Cole Howard
Takes a string of characters and compresses them if possible
"""

import sys


def compress_string(str1):
    """Take a string 
    return the string or a compressed one
    """
    new_string = ""
    for i in str1:
        a = [i, str1.count(i)]
        if str1.count(i) > 2 and i not in new_string:
            new_string += (i + str(a[1]))
        elif a[1] > 2 and i in new_string:
            pass
        else:
            new_string += i
    return new_string


def break_string(str1):
    """Takes string
    returns list of strings, broken by like
    """
    i, j = 1, 0
    letter_strs = []
    letter_strs.append(str1[0])
    while i < len(str1):
        if str1[i] == str1[i-1]:
            letter_strs[j] += str1[i]
        else:
            letter_strs.append(str1[i])
            j += 1
        i += 1
    return letter_strs


def full_compress(str1):
    """Takes a string
    returns it compressed as new string if possible
    """
    lst = break_string(str1)
    answer_lst = [compress_string(i) for i in lst]
    answer = "".join(answer_lst)
    print(answer)
    return(answer)

if __name__ == '__main__':
    assert compress_string('AAA') == 'A3'
    assert break_string('AAABAAA') == ['AAA', 'B', 'AAA']
    assert full_compress('AABBAA') == 'AABBAA'
    full_compress(sys.argv[1])
