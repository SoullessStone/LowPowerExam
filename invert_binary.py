def invert_binary(x):
    x_inv = []
    for entry in x:
        if entry == 0:
            x_inv.append(1)
        else:
            x_inv.append(0)

    return x_inv
