#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """minOperations
    Gets fewest of operations needed 
    to result in exactly n H characters

    Args:
        n (int): number
    Returns:
        int: num_ops
    """
    num_ops, min_ops = 0, 2
    while n > 1:
        while n % min_ops == 0:
            num_ops += min_ops
            n /= min_ops
        min_ops += 1
    return num_ops
