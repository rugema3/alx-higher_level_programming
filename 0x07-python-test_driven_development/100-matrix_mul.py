#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
    matrix_mul: this function multiplies two matrices

    Args:
    m_a: The first matrix
    m_b: The second matrix

    Return: The product of two matrices.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else
                        "m_b must be a list")

    # Checking for list of lists
    if not all(isinstance(row, list) for row in m_a) or \
            not all(isinstance(row, list) for row in m_b):
        raise TypeError(
            "m_a must be a list of lists"
            if not all(isinstance(row, list) for row in m_a)
            else "m_b must be a list of lists"
        )
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b "
                         "can't be empty")
    if not m_a and not m_b:
        raise TypeError("both arguments m_a and m_b must be present")

    rows1 = len(m_a)
    cols1 = len(m_a[0])  # the number of elements equals the number of columns
    rows2 = len(m_b)
    cols2 = len(m_b[0])

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != cols1 for row in m_a) or \
            any(len(row) != cols2 for row in m_b):
        raise TypeError("each row of m_a must be of the same size or"
                        "each row of m_b must be of the same size")

    if cols1 != rows2:
        raise ValueError("m_a and m_b can't be multiplied")

    # Create an empty result matrix
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
