import numpy as np

from left_trim import left_trim
from pad_binary import pad_binary


# Based on:
# Low Power 4*4 Canonical Signed Digit
# Multiplier using 90nm Technology
# Saloni1, Dr. Neelam Rup Prakash
def multiplication_csd_2(a_param, b_param, counter):
    a = a_param.copy()
    b = b_param.copy()
    # left trim a+b, because we want to only have as many partial products as we need
    a = left_trim(a)
    b = left_trim(b)

    resultLength = len(a) + len(b)

    # partial products
    partialProducts = []
    i = len(b) - 1
    while i >= 0:
        curB = b[i]

        ppi = 0
        partialProduct = []
        while ppi < len(a):
            curBTimeA = curB * a[ppi]
            partialProduct.append(curBTimeA)
            if curBTimeA == -1 or curBTimeA == 1:
                counter.count()
                # count all changing 1s
            ppi += 1

        # shift x times
        j = len(b) - i - 1
        while j > 0:
            partialProduct.append(0)
            j = j - 1
        # uniform length of partial products
        partialProduct = pad_binary(partialProduct, resultLength)
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
                # COUNT - result change
                counter.count()
            if localSum == 2:
                carry = 1
                # COUNT - carry
                counter.count()
                result[j] = 0
            if localSum == 3:
                carry = 1
                # COUNT - carry
                counter.count()
                result[j] = 1
                # COUNT - result change
                counter.count()
            if localSum == -1:
                carry = 0
                result[j] = -1
                # COUNT - result change
                counter.count()
            if localSum == -2:
                carry = -1
                # COUNT - carry
                counter.count()
                result[j] = 0
            if localSum == -3:
                carry = -1
                # COUNT - carry
                counter.count()
                result[j] = -1
                # COUNT - result change
                counter.count()
            j = j - 1
        i = i + 1
    return result
