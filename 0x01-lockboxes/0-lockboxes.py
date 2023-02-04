#!/usr/bin/python3
""" Lockboxes challenge
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked
    Returns:
        True if all boxes can be opene
        False if not
    """
    all_boxes = len(boxes)
    unique_keys = set()
    unlock_key = []
    i = 0

    while i < all_boxes:
        prev = i
        unlock_key.append(i)
        unique_keys.update(boxes[i])
        for key in unique_keys:
            if key != 0 and key < all_boxes and key not in unlock_key:
                i = key
                break
        if prev != i:
            continue
        else:
            break

    for i in range(all_boxes):
        if i not in unlock_key and i != 0:
            return False
    return True
