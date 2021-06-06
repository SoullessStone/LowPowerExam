import numpy as np

from sign_extend_to_length import sign_extend_to_length


def multiplication_twos_complement(a_16bit, b_16bit):
    # sign extend a and b
    a = sign_extend_to_length(a_16bit, 32)
    b = sign_extend_to_length(b_16bit, 32)

    # partial products
    partialProducts = []
    i = 0
    while i < len(a):
        curB = b[len(a) - i - 1]
        partialProduct = [curB * a[0], curB * a[1], curB * a[2], curB * a[3], curB * a[4], curB * a[5], curB * a[6],
                          curB * a[7], curB * a[8], curB * a[9], curB * a[10], curB * a[11], curB * a[12], curB * a[13],
                          curB * a[14], curB * a[15], curB * a[16], curB * a[17], curB * a[18], curB * a[19],
                          curB * a[20], curB * a[21], curB * a[22], curB * a[23], curB * a[24], curB * a[25],
                          curB * a[26], curB * a[27], curB * a[28], curB * a[29], curB * a[30], curB * a[31]]
        # shift x times
        j = 1
        while j <= i:
            partialProduct.append(0)
            j = j + 1
        # wieder auf 32bit trimmen
        partialProduct = partialProduct[len(partialProduct) - 32:len(partialProduct)]
        partialProducts.append(partialProduct)
        i = i + 1

    # Summing up the partial products
    result = np.zeros(32)
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
