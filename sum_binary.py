import numpy as np


def sum_binary(x, y, counter):
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
            # COUNT - carry
            counter.count()
            result[ia + 1] = 0
        if localSum == 3:
            carry = 1
            # COUNT - carry
            counter.count()
            result[ia + 1] = 1

        # COUNT - new sum, changed 1
        counter.countOtherValue(result[ia + 1])
        ia = ia - 1
        ib = ib - 1
    result[0] = carry
    # COUNT - also count last carry
    counter.countOtherValue(carry)
    return result
