#!/usr/bin/python3
"""12-pascal_triangle module."""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n: An integer representing the number of rows in Pascal's triangle.

    Returns:
        A list of lists of integers representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
