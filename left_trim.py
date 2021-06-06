def left_trim(number):
    result = []
    i = 0
    firstOneReached = False
    while i < len(number):
        if firstOneReached is False and (number[i] == 1 or number[i] == -1):
            firstOneReached = True
        if firstOneReached:
            result.append(number[i])
        i += 1
    return result
