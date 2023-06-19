#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            if type(x) not in (int, float) or type(y) not in (int, float):
                raise TypeError
            if my_list_2[i] == 0:
                raise ZeroDivisionError
            div = my_list_1[i] / my_list_2[i]
            new_list.append(div)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return(new_list)
