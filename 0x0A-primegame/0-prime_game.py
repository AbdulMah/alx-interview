#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """ Maria and Ben are playing a game
    """

    ben = 0
    maria = 0

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    myList = [1 for x in range(sorted(nums)[-1] + 1)]
    myList[0], myList[1] = 0, 0

    for i in range(2, len(myList)):
        rm_multiples(myList, i)

    if sum_operation(myList, nums):
        ben += 1
    else:
        maria += 1

    if ben > maria:
        return "Ben"
    elif ben < maria:
        return "Maria"
    return None


def sum_operation(ls, x):
    """sum operations

    Args:
        ls (list): list
        x (list): list
    Returns: 
        bool: True or False
    """
    for i in x:
        if sum(ls[0:i + 1]) % 2 == 0:
            return True
        else:
            return False


def rm_multiples(ls, x):
    """removes multiple
        of primes
    Args:
        ls (list): list
        x (int): value
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
