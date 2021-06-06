import numpy as np


def left_shift(number, times):
    number = np.concatenate((number, np.zeros(times)))
    return number
