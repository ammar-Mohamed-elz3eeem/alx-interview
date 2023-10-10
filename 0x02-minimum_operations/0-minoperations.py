#!/usr/bin/python3
"""make python module to get minimum operations to
fill a file with number of bytes
"""
from math import sqrt, floor
import typing


def minOperations(n: int) -> int:
    """get minimum number of operations to
    write n bytes to a file

    Args:
        n (int): bytes needed in a file

    Returns:
        int: minimum number of operations needed
    """
    if (n <= 0):
        return 0
    divisors_sum = []
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            print(i)
            divisors_sum.append(i + (n // i))
    return min(divisors_sum)
