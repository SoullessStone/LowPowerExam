import numpy as np


def full_number_binary(x, maxExponent):
    binRepresentation = np.zeros(maxExponent + 1)
    restOfX = x
    i = maxExponent
    while i >= 0:
        if restOfX - 2 ** i >= 0:
            restOfX = restOfX - 2 ** i
            binRepresentation[maxExponent - i] = 1
        i = i - 1

    return binRepresentation, restOfX
