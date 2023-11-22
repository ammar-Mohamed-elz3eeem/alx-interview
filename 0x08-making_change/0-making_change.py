#!/usr/bin/python3
""" Making change module
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """ return least number of coins to get to the total

    Args:
        coins (List[int]): list of coins
        total (int): total amount needed

    Returns:
        int: least number of coins to get to the total
    """
    count = 0
    if not coins:
        return -1
    if total <= 0:
        return count
    for coin in sorted(coins)[::-1]:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1
