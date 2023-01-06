#!/usr/bin/python3
""" Each box is numbere sequentially from 0 to n - 1 and
each box may contain keys """


def canUnlockAll(boxes):
    """ solve the problem of
    loockboxes """
    unlocked = set()
    for key, val in enumerate(boxes):
        if len(val) or val == 0:
            unlocked.add(key)
        for i in val:
            if i < len(boxes) and i != key:
                unlocked.add(key)
        if len(unlocked) == len(boxes):
            return True
    return False
