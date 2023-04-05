#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    nume = 0
    deno = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[i])-1):
            nume = nume + (my_list[i][j] * my_list[i][j + 1])
            deno = deno + (my_list[i][j + 1])
    return(nume / deno)
