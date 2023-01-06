#!/usr/bin/python3
""" Each box is numbere sequentially from 0 to n - 1 and
each box may contain keys """


def canUnlockAll(boxes):
    """ solve the problem of
    loockboxes """
    for key in range(1, len(boxes) - 1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = (key in boxes[idx] and key != idx)
            if ctr:
                break
        if ctr is False:
            return ctr
    return True
