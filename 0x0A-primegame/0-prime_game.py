#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game."""


def isWinner(x, nums):
    """
    Determines the winner after x rounds of the game.

    Args:
    x (int): The number of rounds to be played.
    nums (list of int): A list of integers representing
    the upper limits for each round.

    Returns:
    str: Name of the player with the most wins, "Maria"
    or "Ben", or None if it's a tie.
    """
    if not nums or x <= 0:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    max_num = ax(nums)
    # Sieve of Eratosthenes to mark prime numbers up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Accumulate results for each round
    for num in nums:
        # Count the number of primes up to num
        prime_count = sum(sieve[:num + 1])

        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
