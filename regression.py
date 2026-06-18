import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample Data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5, 7])

# Create and Train Model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Equation
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)
print(f"Equation: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")

# Plot
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)
plt.show()