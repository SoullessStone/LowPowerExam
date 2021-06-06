from binary_to_csd import binary_to_csd
from invert_binary import invert_binary
from left_shift import left_shift
from left_trim import left_trim
from subtraction_binary import subtraction_binary
from sum_binary import sum_binary


# based on Example 10 from:
# Efficient Multiplication and Division Using MSP430™ MCUs
# Texas Instruments
def multiplication_csd_horner(x, m):
    # Warning: x stays binary, m becomes csd
    m = binary_to_csd(m)
    print(x)
    print(m)
    # X
    result = x

    last1index = len(m) - 1
    while last1index > 0:
        if m[last1index] == 1:
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
                print("after left_shift: " + str(result))
                if m[i] == 1:
                    result = sum_binary(result, x)
                    result = left_trim(result)
                else:
                    result = subtraction_binary(result, x)

                if i == last1index:
                    result = left_shift(result, lastShift)

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
