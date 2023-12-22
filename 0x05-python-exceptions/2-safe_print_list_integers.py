#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """print the first x elements of a list that are intergers.
    Args:
        my_list (list): The  to print element from.
        x (int): The number of element of my_list to print.
    Returns:
        number of element printed."""

    count = 0
    try:
        for i in range(0, x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end="")
                count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
