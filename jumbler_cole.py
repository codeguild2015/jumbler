""" Written by Cole Howard
Takes in a string and a file name from the command line

Arguments:
string
string (name of file in the directory, or path thereto)

Returns number of anagrams of string in the file
"""

import sys


def main():
    try:
        word, file_name = sys.argv[1], sys.argv[2]
    except:
        print('Not the right info.  Need a string and a filename.')
        exit(1)
    word = word.strip()
    f = open(file_name, 'r')
    matches = 0
    for idx, line in enumerate(f):
        line = line.strip()
        if sorted(word) == sorted(line) and word != line:
            print(line)
            matches += 1
    print('{} matches in {} lines.'.format(matches, idx))


if __name__ == '__main__':
    main()
