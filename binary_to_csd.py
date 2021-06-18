import numpy as np

from full_number_binary import full_number_binary
from invert_binary import invert_binary
from sum_binary import sum_binary


def binary_to_csd(x, counter):
    # we have to remember that it is a negative number
    isNegative = False
    if x[0] == 1:
        isNegative = True
        # if it is negative, just calculate the csd for the positive number and then invert
        x = invert_binary(x)
        # SUM - add inverted 1s to count
        counter.countOtherValue(sum(x))
        binRepresentation1, restOfX = full_number_binary(1, len(x) - 1)
        x = sum_binary(x, binRepresentation1, counter)
        # SUM - sum_binary will be counted in the method itself
        x = x[1:len(x)]
    # This allows us to find 1100000 (streak in the end
    # also it prevents endless loop due to i = len(x) -1
    x = np.insert(x, 0, 0)

    i = len(x) - 1
    oneStreak = False
    streakCount = 0
    while i >= 0:  # 01111111110
        if x[i] == 0:
            if oneStreak:
                if streakCount > 1:
                    j = i
                    while j <= i + streakCount:
                        if j == i:
                            x[j] = 1
                            # SUM - count 1
                            counter.count()
                        elif j == i + streakCount:
                            x[j] = -1
                            # SUM - count -1 as 1
                            counter.count()
                        else:
                            x[j] = 0
                        j += 1
                    i += 1  # we have to revisit the last index
                # else: we do not replace streaks of 1, just insert the 1 we didn't add and the current zero

            oneStreak = False
            streakCount = 0

        else:
            oneStreak = True
            streakCount += 1

        i -= 1

    if x[0] == 0:
        x = x[1:len(x)]

    # if it was a negative number, switch 1 to -1 (invert)
    if isNegative:
        j = 0
        while j < len(x):
            if x[j] != 0:
                x[j] = x[j] * -1
            j += 1

    return x
