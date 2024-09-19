#!/usr/bin/python3

""" Contains makeChange function """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the total.
    
    Args:
        coins (list): The values of the coins available.
        total (int): The total amount to be made.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If the total is 0 or less, return 0.
             If the total cannot be met by any number of coins, return -1.
    """
    if not coins or total < 0:
        return -1
    if total == 0:
        return 0
    
    # Sort coins in descending order to try larger denominations first
    coins.sort(reverse=True)
    
    change = 0
    
    for coin in coins:
        if coin <= total:
            # Calculate how many coins of this denomination can be used
            num_coins = total // coin
            change += num_coins
            total -= num_coins * coin
    
    # If the total is zero, return the change count; otherwise, return -1
    return change if total == 0 else -1
