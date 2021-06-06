import numpy as np


def binary_to_csd(x):
    # This allows us to find 1100000 (streak in the end
    # also it prevents endless loop due to i = len(x) -1
    x = np.insert(x, 0, 0)

    i = len(x) - 1
    oneStreak = False
    streakCount = 0
    while i >= 0:#01111111110
        if x[i] == 0:
            if oneStreak:
                if streakCount > 1:
                    j = i
                    while j <= i + streakCount:
                        if j == i:
                            x[j] = 1
                        elif j == i + streakCount:
                            x[j] = -1
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

    return x
