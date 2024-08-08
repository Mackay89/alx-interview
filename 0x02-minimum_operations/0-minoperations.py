#!/usr/bin/python3
"""
This module contains the function minOperations.
"""

def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The number of H characters desired.

    Returns:
        int: The minimum number of operations, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

