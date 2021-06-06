from binary_to_csd import binary_to_csd
from full_number_binary import full_number_binary
from invert_csd import invert_csd


def full_number_to_csd(x):
    if x < 0:
        binary, rest = full_number_binary(-x, 16)
        csd = binary_to_csd(binary)
        return invert_csd(csd)
    else:
        binary, rest = full_number_binary(x, 16)
        return binary_to_csd(binary)
