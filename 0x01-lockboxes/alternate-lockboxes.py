#!/usr/bin/python3

"""
Implementation of the lockboxes
Algorithm applies two pointers
"""


def canUnlockAll(boxes):
    """
    Boxes is a list of lists
    Boxes[0] is always open
    """
    new_keys = set()
    ab = len(boxes)
    unlockable = False
    for i in range(ab):
        new_keys.update(boxes[i])
        new_keys.update(boxes[ab-1])
        if i in new_keys:
            unlockable = True
            continue
        ab -= 1
    return unlockable
