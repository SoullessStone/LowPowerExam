def sign_extend_to_32bit(x):
    result = x
    extendWith = 0
    if x[0] == 1:
        extendWith = 1
    while len(result) < 32:
        result.insert(0, extendWith)
    return result
