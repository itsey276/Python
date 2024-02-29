import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

def load_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, 0:2]
    y = data[:, 2]
    return X, y

X, y = load_data("data.csv")

#generate a model of polynomial features
poly = PolynomialFeatures(degree=2)

#transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
X_ = poly.fit_transform(X)

#generate the regression object
clf = linear_model.LinearRegression(fit_intercept=False)
#preform the actual regression
clf.fit(X_, y)

# print(poly.get_feature_names_out(['x', 'y']))
# print(clf.coef_)
cf = clf.coef_
print(f"{cf[0]} + {cf[1]} x + {cf[2]} y + {cf[3]} x^2 + {cf[4]} xy + {cf[5]} y^2")
