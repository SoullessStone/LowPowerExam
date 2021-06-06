import numpy as np


def sum_16bit_binary(x, y):
    result = np.zeros(17)
    carryChangeCount = 0
    bitChangeCount = 0
    i = 15
    carry = 0
    while i >= 0:
        localSum = x[i] + y[i] + carry
        if localSum == 0:
            carry = 0
            result[i + 1] = 0
        if localSum == 1:
            carry = 0
            result[i + 1] = 1
        if localSum == 2:
            carry = 1
            result[i + 1] = 0
            carryChangeCount = carryChangeCount + 2
        if localSum == 3:
            carry = 1
            result[i + 1] = 1
            carryChangeCount = carryChangeCount + 3
            bitChangeCount = bitChangeCount + result[i + 1]
        i = i - 1
    result[0] = carry
    return result
