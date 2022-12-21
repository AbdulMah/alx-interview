#!/usr/bin/python3
"""
    S 0-pascal_triangle.py: pascal_triangle()
"""


def pascal_triangle(n: int):
    """
        returns a lis of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    result = []
    if n <= 0:
        return result

    for i in range(1, n + 1):
        level = []
        val = 1
        for j in range(1, i + 1):
            level.append(val)
            val = val * (i - j) // j
        result.append(level)
    return result
