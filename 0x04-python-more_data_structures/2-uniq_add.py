#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum1 = 0
    set1 = set(my_list)
    new_list = list(set1)
    for i in range(len(new_list)):
        sum1 = sum1 + new_list[i]
    return(sum1)
