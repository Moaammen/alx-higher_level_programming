#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    get_len = len(my_list)
    if idx >= get_len:
        return my_list
    
    else:
            new_list = my_list
            new_list[idx] = element
            return new_list


     
