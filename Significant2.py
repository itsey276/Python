from math import floor, log10

def significant(x, precision):

    x = float(x)
    precision = int(precision)

    return round(x, -int(floor(log10(abs(x)))) + (precision - 1))


for i in range(10):
    print(i, ':', significant('123.056789', i))
