def pad_binary(number, toLength):
    i = toLength - len(number)
    if i < 0:
        return number

    while i > 0:
        number.insert(0, 0)
        i -= 1

    return number
