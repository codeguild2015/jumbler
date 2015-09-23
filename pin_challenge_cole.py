"""Written by Cole
Take a 4 digit input from the command line
Output will be four characters in the format C-V-C-V
That will be meaningless but pronouncable
"""

import sys


CONSONANTS = "bcdfghjklmnpqrstvwyz" 
VOWELS = "aeiou"  


def split_to_double_digits(num):
    """Takes a number and splits into a list of double (or less) digits
    Returns a list of the double digits"""
    num_list = []
    while num >= 1:
        num_list.append(num%100)
        num //= 100
    num_list.reverse()
    return num_list


def convert_to_letters(num):
    """Takes in a num of two digits
    Convert that to letters
    """
    letter_list = [CONSONANTS[num//5], VOWELS[num%5]]
    return "".join(letter_list)


def split_to_pairs(str1):
    """Take in a string of indeterminate length and split it into a list of
    pairs of letters.
    Return list of pairs (each pair a list)
    """
    lst = list(str1)
    return [[lst[x], lst[x+1]] for x in range(0, len(lst)-1, 2)]


def convert_to_numbers(str_list):
    """Take in a list of 2 Alphabetic chars and 
    convert them to numbers
    Returns two digits as string
    """
    return str(CONSONANTS.index(str_list[0])*5 + VOWELS.index(str_list[1]))


def foo(pincode):
    """Create a list of doubledigits or alpha chars from pincode
    and swap in the appropriate direction.
    """
    try:
        pincode = int(pincode)
        ans_lst = [convert_to_letters(x) for x in 
                    split_to_double_digits(pincode)]
    except ValueError:
        pincode = str(pincode)
        ans_lst = [convert_to_numbers(x) for x in split_to_pairs(pincode)]
    except TypeError:
        return None
    answer = "".join(ans_lst)
    return answer


if __name__ == '__main__':
    assert split_to_double_digits(556655) == [55, 66, 55]
    assert convert_to_letters(34) == 'ju'
    assert split_to_pairs('ABAB') == [['A', 'B'], ['A', 'B']]
    assert convert_to_numbers(['d', 'e']) == '11' 
    
    ## Get pin code from command line
    try:   
        pincode = sys.argv[1]
    except:
        print("Usage: python3 alphacode 9999")
        exit(1)  ## Quit the program right here, indicating a problem 
    print(foo(pincode))

