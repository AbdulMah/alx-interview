#!/usr/bin/python3
""" Each box is numbere sequentially from 0 to n - 1 and
each box may contain keys """


def canUnlockAll(boxes):
    """ solve the problem of
    loockboxes """
    for key in range(1, len(boxes) - 1):
        control = False
        for i in range(len(boxes)):
            control = (key in boxes[i] and key != i)
            if control:
                break
        if control == False:
            return control
    return True
