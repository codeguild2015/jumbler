""" Written by Mercy and Cole 
Get the names and the number of they appear from user file
Input: User Defined
Output: A list of tuples sorted by count (in reverse order)
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
    if 'From' in lst:
        return True
    else:
        return False

def count_occurances(lst):
    """ Gets list of names
    Return counts per name
    List of tuples (count, name)
    """
    goofy = []
    for emails in lst:  
        goofy.append((lst.count(emails), emails))
    compressed = []
    for elem in goofy:
        if elem in compressed:
            continue
        else:
            compressed.append(elem)
    return compressed

def sort_list(lst):
    """ Get a list tuples
    Return the list reverse order of names & number
    """
    lst.sort(reverse = True)
    return lst 

def main():
    filename = input("input filename ")
    name_lst = []
    for line in file:
        temp_lst = split_line(line)
        if check_for_from(temp_lst):
            name_lst.append(temp_lst[1])
    count_list = count_occurances(name_lst)
    lst_srtd = sort_list(count_list)
    for idx, elem in enumerate(lst_srtd):
        print(lst_srtd[idx][0], lst_srtd[idx][1])

if __name__ == '__main__':
    assert split_line('Are you working?') == ['Are', 'you', 'working?']
    assert split_line(None) == None 
    assert split_line('') == ['']
    assert check_for_from(['From', 'hi@gmail', 'aldkfjasdf']) == True
    assert check_for_from(['From:', 'jimmy@hotmail', 'a;lksdjf']) == False
    assert count_occurances(['jim', 'jim', 'anne', 'anne', 'anne']) == 
                            [(2, 'jim'), (3, 'anne')]
    assert sort_list([(2, 'jim'), (3, 'anne')]) == [(3, 'anne'), (2, 'jim')]
    main()
