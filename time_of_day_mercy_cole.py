# Title: time_of_day.py
# Authors: Mercy and Cole 
#
# Reads a file and pulls out time of commits
# Counts them and returns number of commits
# per hour and returns the hour and count for each


def split_line(line):
    """ Split a line into list of words

    Args:
        line - a string

    Return:
        a list of words
     """
    try:
        words = line.split(' ')
        return words
    except:
        return None


def check_for_from(lst):
    """ Isolate lists which start with From (but not From:)

    Args:
        lst - a list of strings

    Return:
        a boolean
    """
    if lst[0] == "From" and len(lst) == 7:
        return True
    else:
        return False


def hour_num(split_hour):
    """Splits time to pull just the hour returns a string

    Args:
        split_hour - a string

    Return:
        a string
    """
    nums = split_hour[:2]
    return nums


def count_occurances(time_lst):
    """"Counts the time and outputs the number of occurances

    Args:
        time_list - a list of strings

    Return:
        a list
    """
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
    filename = input('Enter file name: ')
    file = open(filename, 'r')
    time_lst = []
    for elem in file:
        temp_line = elem.replace('  ', ' ')
        temp_lst = split_line(temp_line)
        if check_for_from(temp_lst):
            hr = hour_num(temp_lst[5])
            time_lst.append(hr)
    temp_lst = count_occurances(time_lst)
    temp_lst.sort()
    for idx, elem in enumerate(temp_lst):
        print(temp_lst[idx][0], temp_lst[idx][1])


assert count_occurances(['04', '02', '02', '12', '04']) == [('04', 2),
                        ('02', 2), ('12', 1)]
assert check_for_from(['From', 'hi', 'there', 1, 2, 3, 4]) == True
assert hour_num('09:14:16') == '09'
main()
