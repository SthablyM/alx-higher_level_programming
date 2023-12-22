#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """prints x elements of a list.
    Args:
        my_list (list): The list to print element from.
        x (int): the numberbof elements of my_list to print.

        Returns:
            The number of elements printed."""
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print("")
        return count
