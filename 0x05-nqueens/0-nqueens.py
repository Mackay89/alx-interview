#!/usr/bin/python3
'''N-Queens Challenge'''
import sys


def is_safe(placed_queens, row, col):
    '''Check if it's safe to place a queen at (row, col)'''
    for r, c in placed_queens:
        if c == col or r + c == row + col or r - c == row - col:
            return False
    return True


def solve_nqueens(n, row=0, placed_queens=None):
    '''Recursively find all solutions for the N-Queens problem'''
    if placed_queens is None:
        placed_queens = []

    if row == n:
        return [placed_queens[:]]

    solutions = []
    for col in range(n):
        if is_safe(placed_queens, row, col):
            placed_queens.append((row, col))
            solutions.extend(solve_nqueens(n, row + 1, placed_queens))
            placed_queens.pop()

    return solutions


def print_solutions(solutions):
    '''Print all solutions for the N-Queens problem'''
    for solution in solutions:
        print([[r, c] for r, c in solution])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)

