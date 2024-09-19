#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Args:
        coins (list): The values of the coins in your possession.
        total (int): The amount to be met.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if the total
             cannot be met.
    """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            num_coins = total // coin
            total -= num_coins * coin
            coin_count += num_coins
    
    return coin_count if total == 0 else -1

