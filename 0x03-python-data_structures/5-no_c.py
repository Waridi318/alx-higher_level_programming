#!/usr/bin/python3
def no_c(my_string):
    my_str1 = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            my_str1 += char
    return(my_str1)
