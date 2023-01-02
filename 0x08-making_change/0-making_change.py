#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """_summary_

    Args:
        coins (list): _description_
        total (_type_): _description_

    Returns: number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """    
    change = 0
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1
