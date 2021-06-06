import numpy as np


def sum_binary(x, y):
    if len(x) > len(y):
        a = x
        b = y
    else:
        a = y
        b = x

    result = np.zeros(len(a) + 1)
    carryChangeCount = 0
    bitChangeCount = 0
    ia = len(a) - 1
    ib = len(b) - 1
    carry = 0
    while ia >= 0:
        if ib < 0:
            curB = 0
        else:
            curB = b[ib]
        localSum = a[ia] + curB + carry
        if localSum == 0:
            carry = 0
            result[ia + 1] = 0
        if localSum == 1:
            carry = 0
            result[ia + 1] = 1
        if localSum == 2:
            carry = 1
            result[ia + 1] = 0
            carryChangeCount = carryChangeCount + 2
        if localSum == 3:
            carry = 1
            result[ia + 1] = 1
            carryChangeCount = carryChangeCount + 3
            bitChangeCount = bitChangeCount + result[ia + 1]
        ia = ia - 1
        ib = ib - 1
    result[0] = carry
    return result
