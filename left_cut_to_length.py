def left_cut_to_length(number, desiredLength):
    if len(number) > desiredLength:
        return number[len(number) - desiredLength:len(number)]
    else:
        return number
