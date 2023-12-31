#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists.

    Args:
        my_list_1 (list): the first list.
        my_list_2 (list): the second list.
        list_length (int): the number of element to divide

    Returns:
        A new list of length list_length containing all the division"""
    result = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0
            division_result = element_1 / element_2
            result.append(division_result)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            pass

    return result
