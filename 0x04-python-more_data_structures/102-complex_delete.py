#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return(a_dictionary)
    for k, v in list(a_dictionary.items()):
        if a_dictionary[k] is value:
            del a_dictionary[k]
    return(a_dictionary)
