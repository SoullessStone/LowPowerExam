import numpy as np


def invert_csd(csd):
    csdInv = np.zeros(len(csd))
    i = 0
    while i < len(csd):
        if csd[i] == 0:
            csdInv[i] = 0
        elif csd[i] == 1:
            csdInv[i] = -1
        else:
            csdInv[i] = 1
        i += 1

    return csdInv
