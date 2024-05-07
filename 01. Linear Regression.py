import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

X_points = points.values[:, :-1]
Y_points = points.values[:, -1]

fit = LinearRegression().fit(X_points, Y_points)

m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print(f"m = {m}")
print(f"b = {b}")

plt.plot(X_points, Y_points, 'o')
plt.plot(X_points, m * X_points + b)
plt.show()
