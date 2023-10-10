#!/usr/bin/python3
"""Module that have lockboxes algorithm
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """initializer for checkboxes Recursively to
    determine if all boxes can be unlocked or not

    Args:
        boxes (List[List[int]]): List of Boxes that have keys to each other

    Returns:
        bool: True if all boxes can be unlocked, false otherwise
    """
    unlocked = [0]
    return canUnlockBoxesRec(boxes, unlocked)


def canUnlockBoxesRec(boxes: List[List[int]], unlocked: List[int],
                      boxesUnloced: int = 1) -> bool:
    """_summary_

    Args:
        boxes (List[List[int]]): List of Boxes that have keys to each other
        unlocked (List[int]): unlocked boxes by its location
        boxesUnloced (int, optional): number of unlocked boxes so far.
        Defaults to 1.

    Returns:
        bool: True if all boxes can be unlocked, call itself otherwise
    """
    if boxesUnloced >= len(boxes):
        return True
    unlockedLen = len(unlocked)
    for box in unlocked:
        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
                boxesUnloced += 1
    if (len(unlocked) == unlockedLen):
        return boxesUnloced == len(boxes)
    return canUnlockBoxesRec(boxes, unlocked, boxesUnloced)


print(canUnlockAll([ [7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5], ]))
