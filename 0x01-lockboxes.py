#!/usr/bin/python3
""" Each box is numbere sequentially from 0 to n - 1 and
each box may contain keys """


def canUnlockAll(boxes):
    for key in range(1, len(boxes) - 1):
        default = False
        for idx in range(len(boxes)):
            default = (key in boxes[idx] and key != idx)
            if default:
                break
        if default == False:
            return default
    return True
