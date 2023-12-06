#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    new_list = my_list.copy()
    for num in new_list:
        if num == search:
            new_list.remove(num)
            new_list.insert(i, replace)
        i += 1
    return (new_list)
