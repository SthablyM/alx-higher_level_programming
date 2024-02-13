#!/usr/bin/python3
"""Define division function"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    Args:
        matrix (list): A list of lists of ints or float
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-number
        TyepeError: If the matrix contain row different size
    Returns:
        a new matrix"""

    if not all(isinstance(row, list) for row in matrix) or \
        not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"

        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
