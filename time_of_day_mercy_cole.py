""" Written by Mercy and Cole 
Reads a file and pulls out time of commits
Counts them and returns number of commits
per hour and returns the hour and count for each
"""


def split_line(line):
    """ Split a line (comes in a string)
    Return a list of words, split on the spaces
     """
    try:
        words = line.split(' ')
        return words
    except:
        return None


def check_for_from(lst):
    """ Isolate lists which start with From (but not From:)
    Return True or False
    """
    if lst[0] == "From":
        return True
    else:
        return False


def hour_num(split_hour):
    """Splitting time to pull just the hour returns a string"""
    nums = split_hour[:2]
    return nums


def count_occurances(time_lst):
    """"Counts the time and outputs the number of occurances
    returns a list"""
    goofy = []
    for num in time_lst:    
        goofy.append((num, time_lst.count(num)))
    compressed = []
    for elem in goofy:
        if elem in compressed:
            continue
        else:
            compressed.append(elem)
    return compressed


def main():
    """Import file, get time of day from 'From' lines, sort into list"""
    filename = input('Enter file name: ')
    file = open(filename, 'r')
    time_lst = []
    for elem in file:
        temp_lst = split_line(elem)
        if check_for_from(temp_lst):
            hr = hour_num(temp_lst[6])
            time_lst.append(hr)
    temp_lst = count_occurances(time_lst)
    temp_lst.sort()
    for idx, elem in enumerate(temp_lst):
        print(temp_lst[idx][0], temp_lst[idx][1])


assert count_occurances(['04', '02', '02', '12', '04']) == [('04', 2), ('02', 2), ('12', 1)]
assert check_for_from(['From', 'hi', 'there']) == True
assert hour_num('09:14:16') == '09'
main()
