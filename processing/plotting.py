# starts jul-18 ends jan-20

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = np.genfromtxt('consumption-data.csv', delimiter=',')[1::]
months = [l[0] for l in data]
wtp1 = [l[1] for l in data]
wtp2 = [l[2] for l in data]
total = [l[3] for l in data]

# plt.plot(months, total, 'o', color = 'black')
# plt.plot(months, wtp1, 'o', color = 'red')
# plt.plot(months, wtp2, 'o', color = 'blue')
# plt.show()

poly_reg = PolynomialFeatures(degree = 6)
months_poly = poly_reg.fit_transform(months)
pol_reg = LinearRegression()
pol_reg.fit(months_poly, wtp1)

def visualize():
    plt.plot(months, wtp1, 'o', color = 'red')
    plt.plot(months, pol_reg.predict(poly_reg.fit_transform(months)), color='blue')
    plt.show()
    return

visualize()
