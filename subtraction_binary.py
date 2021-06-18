from pad_binary import pad_binary


# Changed, but main idea from https://levelup.gitconnected.com/computing-binary-numbers-with-python-a6e00be69bea
def subtraction_binary(a, b, counter):
    maxLength = max(len(a), len(b))

    a = pad_binary(a, maxLength)
    b = pad_binary(b, maxLength)

    result = []
    temp = 0

    i = maxLength - 1

    while i >= 0:
        num = a[i] - b[i] - temp
        if num % 2 == 1:
            result.insert(0, 1)
            counter.count()
            # SUM - Count this 1
        else:
            result.insert(0, 0)

        if num < 0:
            temp = 1
            counter.count()
            # SUM - Count this 1
        else:
            temp = 0

        i -= 1

    return result
