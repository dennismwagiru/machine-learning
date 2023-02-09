import numpy as np
import matplotlib.pyplot as plt

# Load data
X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

# Let's turn X and Y into numpy arrays
X = np.array(X)
Y = np.array(Y)

# Plot to see what it looks like
# plt.scatter(X, Y)
# plt.show()

# Apply the equations to calculate a and b
denominator = X.dot(X) - X.mean() * X.sum()
a = (X.dot(Y) - Y.mean() * X.sum()) / denominator
b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denominator

Yhat = a*X + b

plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()
