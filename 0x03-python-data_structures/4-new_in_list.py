#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list
    get_len = len(my_list)
    if idx >= get_len:
        return my_list
    
    else:
            new_list[idx] = element
            return new_list


     
