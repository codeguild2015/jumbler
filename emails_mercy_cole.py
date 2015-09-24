# Written by Mercy and Cole 
# Get the names and the number of they appear from user file
# Input: User Defined
# Output: A list of tuples sorted by count (in reverse order)


def split_line(line):
    """ Split a line (comes in a string)
    Return a list of words, split on the spaces
     """
    try:
        return line.split(' ')
    except:
        return None


def check_for_from(lst):
    """ Isolate lists which start with From (but not From:)
    and of a specific length
    Return True or False
    """
    if lst[0] == 'From' and len(lst) == 7:
        return True
    else:
        return False


def count_occurances(lst):
    """ Gets list of names
    Return counts per name
    List of tuples (count, name)
    """
    goofy = [(lst.count(emails), emails) for emails in lst]
    compressed = []
    for elem in goofy:
        if elem in compressed:
            continue
        else:
            compressed.append(elem)
    return compressed


def main():
    f = input("input filename ")
    filename = open(f, 'r')
    name_lst = []
    for line in filename:
        temp_line = line.replace('  ', ' ') # Account for extra spaces.
        temp_lst = split_line(temp_line)
        if check_for_from(temp_lst):
            name_lst.append(temp_lst[1])
    count_list = count_occurances(name_lst)
    count_list.sort(reverse=True)
    [print(count_list[idx][0], count_list[idx][1]) for idx, elem in
     enumerate(count_list)]


if __name__ == '__main__':
    assert split_line('Are you working?') == ['Are', 'you', 'working?']
    assert split_line(None) == None 
    assert split_line('') == ['']
    assert check_for_from(['From', 'hi', 'a', 1, 2, 3, 4]) == True
    assert check_for_from(['From:', 'j', 1, 2, 3, 'a', 3]) == False
    assert count_occurances(['jim', 'ann', 'ann']) == [(1, 'jim'), (2, 'ann')]
    main()

