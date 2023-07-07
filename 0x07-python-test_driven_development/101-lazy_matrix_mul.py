#!/usr/bin/python3

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul: this function multiplies two matrices using NumPy

    Args:
    m_a: The first matrix
    m_b: The second matrix

    Return: The product of two matrices.
    """
    # Check if m_a or m_b is a list
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else
                        "m_b must be a list")

    # Checking for list of lists
    if not all(isinstance(row, list) for row in m_a) or \
            not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if not all(isinstance(
                        row, list) for row in m_a) else
                        "m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b "
                         "can't be empty")
    if not m_a and not m_b:
        raise TypeError("both arguments m_a and m_b must be present")

    # Convert the matrices to NumPy arrays
    a = np.array(m_a)
    b = np.array(m_b)

    # Perform matrix multiplication using the dot function
    result = np.dot(a, b)

    return result
