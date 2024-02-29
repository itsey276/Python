import numpy as np
from scipy.optimize import curve_fit

def load_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    return x, y, z

def func(X, a, b, c, d, e, f):
    x,y = X
    return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f

x, y, z = load_data("data.csv")

coeff, variance = curve_fit(func, (x,y), z)
print(f"{coeff[0]} x^2 + {coeff[1]} y^2 + {coeff[2]} xy + {coeff[3]} x + {coeff[4]} y + {coeff[5]}")
