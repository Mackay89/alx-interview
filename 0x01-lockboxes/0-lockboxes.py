#!/usr/bin/python3
"""
These module is for canUnlockAll method.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    :param boxes: List of lists containing keys.
    :return: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    for i in range(n):
        if not unlocked[i]:
            return False

    return True

