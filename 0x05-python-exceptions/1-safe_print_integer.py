#!/usr/bin/python3


def safe_print_integer(value):
    """safe_print_interger with"{:d}".format().

    Args:
        value (int): The interger to print.
    Returns:
        if a TypeError or
        ValueError occurs - False.
        otherwise - True."""
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
