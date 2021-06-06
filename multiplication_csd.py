import numpy as np

from full_number_binary import full_number_binary
from invert_binary import invert_binary
from left_trim import left_trim
from pad_binary import pad_binary
from sum_binary import sum_binary


# probably better not use that one. problems with negative numbers.
def multiplication_csd(a, b):
    resultLength = len(left_trim(a)) + len(left_trim(b))

    # pad to resultlength, so 2-complement works on all zeros
    a = pad_binary(a, resultLength)
    # left trim b, because we want to only have as many partial products as we need
    b = left_trim(b)

    # partial products
    partialProducts = []
    i = len(b) - 1
    while i >= 0:
        curB = b[i]

        applyTwosComplementToPp = False
        if curB == -1:
            applyTwosComplementToPp = True
            curB = 1

        ppi = 0
        partialProduct = []
        while ppi < len(a):
            partialProduct.append(curB * a[ppi])
            ppi += 1

        # shift x times
        j = len(b) - i - 1
        while j > 0:
            partialProduct.append(0)
            j = j - 1
        # wieder auf resultLength trimmen
        partialProduct = partialProduct[len(partialProduct) - resultLength:len(partialProduct)]

        # TODO Vorher oder nach shifting twos complement anwenden?
        if applyTwosComplementToPp:
            partialProduct = invert_binary(partialProduct)
            binRepresentation1, restOfX = full_number_binary(1, resultLength - 1)
            partialProduct = sum_binary(partialProduct, binRepresentation1)
        # wieder auf resultLength trimmen
        partialProduct = partialProduct[len(partialProduct) - resultLength:len(partialProduct)]
        partialProducts.append(partialProduct)
        i = i - 1

    # Summing up the partial products
    result = np.zeros(resultLength)
    i = 0
    while i < len(partialProducts):
        partialProduct = partialProducts[i]
        carry = 0
        j = len(result) - 1
        while j >= 0:
            localSum = result[j] + partialProduct[j] + carry
            if localSum == 0:
                carry = 0
                result[j] = 0
            if localSum == 1:
                carry = 0
                result[j] = 1
            if localSum == 2:
                carry = 1
                result[j] = 0
            if localSum == 3:
                carry = 1
                result[j] = 1
            j = j - 1
        i = i + 1
    return result
