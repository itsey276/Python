def significant(num, digits):
    numstring = str(num)
    non_sig = 0
    start = 0
    decimal = 0
    count = 0
    zeros = 0

    for char in numstring:
        if char in '0.' and start == 0:
            non_sig += 1
        else:
            start = non_sig
        if char == '.':
            decimal = 1
        else:
            count += 1
        if count > digits and decimal == 0:
            zeros += 1

    if digits == 0:
        return None
    if zeros > 0:
        return float((numstring[0: digits])) * 10**zeros
    if num > 1:
        return (numstring[0: digits + decimal])
    else:
        return (numstring[0 : start + digits])

for n in range(10):
    print(significant(0.1230456, n))
            






            
