from counter import Counter
from full_number_binary import full_number_binary
from invert_binary import invert_binary
from sum_binary import sum_binary


def twos_complement(x):
    if x < 0:
        binRepresentationX, restOfX = full_number_binary(-x, 15)
        binRepresentation1, restOfX = full_number_binary(1, 15)
        inverted_x = invert_binary(binRepresentationX)
        twosComplement = sum_binary(inverted_x, binRepresentation1, Counter())[1:17]
    else:
        binRepresentationX, restOfX = full_number_binary(x, 15)
        twosComplement = binRepresentationX

    return twosComplement
