#!/usr/bin/python3


def safe_print_division(a, b):
    """Returns the division of a by b."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
        return result
