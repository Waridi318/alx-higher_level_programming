#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        return(None)
    finally:
        if ZeroDivisionError:
            print("Inside result: None")
        else:
            print("Inside result: {:f}".format(div))
    return (div)
