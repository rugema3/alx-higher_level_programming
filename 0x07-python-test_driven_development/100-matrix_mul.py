#!/usr/bin/python3
"""100-matrix_mul module."""


def matrix_mul(m_a, m_b):
    """
    matrix_mul: this function multiplies two matrices.

    Args:
    m_a: The first matrix
    m_b: The second matrix

    Return: The product of two matrices.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else
                        "m_b must be a list")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b "
                         "can't be empty")

    rows1 = len(m_a)
    cols1 = len(m_a[0])
    rows2 = len(m_b)
    cols2 = len(m_b[0])

    if cols1 != rows2 or cols2 != rows1:
        raise ValueError("m_a and m_b can't be multiplied")

    if any(len(row) != cols1 for row in m_a):
        raise ValueError("each row of m_a must be of the same size")

    if any(len(row) != cols2 for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Create an empty result matrix
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
