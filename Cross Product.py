from math import sqrt, asin

a = [1, -0.1, 0]
b = [0, 1, 0]
Pi = 355 / 113

def cross3D(a, b):
    S = [0, 0, 0]
    assert len(a) == 3
    assert len(b) == 3
    S[0] = a[1] * b[2] - a[2] * b[1]
    S[1] = a[2] * b[0] - a[0] * b[2]
    S[2] = a[0] * b[1] - a[1] * b[0]
    return S

def norm(a):
    return sqrt(a[1]**2 + a[2]**2 + a[0]**2)


print(a, ' X ', b, " = ", cross3D(a, b))
print(b, ' X ', a, " = ", cross3D(b, a))

