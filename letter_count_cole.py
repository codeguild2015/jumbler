""" Written by Cole
Counts the letters in a file and returns them in
decreasing frequency
"""

def letters_in_line():
    """ Takes in a string and a dictionary.
    Counts the number of occurances of each letter.
    Returns updated dictionary
    """

def main():
    filename = input('Enter file name: ')
    file = open(filename, 'r')
    # build dictionary 
    #for line in file:
        # count # of each letter


if __name__ == '__main__':
    assert letters_in_line('abba bcca', {'a': 0, 'b': 0, 'c': 0}) ==
                            {'a': 3, 'b', 3, 'c', 2}
    assert letters_in_line('', {'a': 0, 'b': 0, 'c': 0}) == 
                            {'a': 0, 'b': 0, 'c': 0}