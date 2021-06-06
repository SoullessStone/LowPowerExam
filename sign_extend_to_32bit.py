def sign_extend_to_length(x, toLength):
    result = x
    extendWith = 0
    if x[0] == 1:
        extendWith = 1
    while len(result) < toLength:
        result.insert(0, extendWith)
    return result
