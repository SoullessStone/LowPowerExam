from binary_to_csd import binary_to_csd
from counter import Counter
from invert_binary import invert_binary
from left_cut_to_length import left_cut_to_length
from left_shift import left_shift
from sign_extend_to_length import sign_extend_to_length
from subtraction_binary import subtraction_binary
from sum_binary import sum_binary


# based on Example 10 from:
# Efficient Multiplication and Division Using MSP430™ MCUs
# Texas Instruments
def multiplication_csd_horner(x, m):
    isNegativeM = False
    if m[0] == 1:
        isNegativeM = True
    resultLength = len(x) + len(m)
    # Warning: x stays binary, m becomes csd
    x = sign_extend_to_length(x, resultLength)
    m = binary_to_csd(m)
    print(x)
    print(m)
    # X
    result = x
    if isNegativeM:
        # -X
        inverted_x = invert_binary(x)
        result = sum_binary(inverted_x, [1], Counter())[1:len(x) + 1]

    last1index = len(m) - 1
    while last1index > 0:
        if m[last1index] == 1 or m[last1index] == -1:
            break
        last1index -= 1
    lastShift = len(m) - last1index - 1
    print('lastShift')
    print(lastShift)

    i = 0
    count = 0
    firstOneFound = False
    while i < len(m):
        print("i: " + str(i))
        if m[i] == 1 or m[i] == -1:
            if firstOneFound:
                # shift by 2^count
                print("next 1 found, distance: " + str(count))
                print("before left_shift: " + str(result))
                result = left_shift(result, count)
                result = left_cut_to_length(result, resultLength)
                print("after left_shift: " + str(result))
                if m[i] == 1:
                    result = sum_binary(result, x, Counter())
                else:
                    result = subtraction_binary(result, x)

                if i == last1index:
                    result = left_shift(result, lastShift)

                result = left_cut_to_length(result, resultLength)
                count = 0
            else:
                firstOneFound = True
            count += 1
        else:
            if firstOneFound:
                count += 1
        print("count: " + str(count))
        print("firstOneFound: " + str(firstOneFound))
        i += 1

    return result
