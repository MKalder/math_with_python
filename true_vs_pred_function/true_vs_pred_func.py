import numpy as np #type: ignore

from plot import plot_fuction

# Generating 100 random values
np.random.seed(42)  
x_values = np.random.uniform(-2, 6, 100)  
y_values = np.random.uniform(-2, 6, 100)

# True function with noise
def true_function(x, y):
    noise = np.random.normal(0, 0.5)  # random noise
    return (x - 3)**2 + (y - 2)**2 + np.sin(3 * x) * np.cos(2 * y) + noise

# True z-values 
z_true = np.array([true_function(x, y) for x, y in zip(x_values, y_values)])

# Model function 
def model_prediction(x, y):
    return (x - 2.5)**2 + (y - 1.5)**2 + np.sin(2.5 * x) * np.cos(1.8 * y)

# Model prediciton values
z_pred = np.array([model_prediction(x, y) for x, y in zip(x_values, y_values)])

# SSR calculation
ssr = np.sum((z_true - z_pred) ** 2)
print(f"Sum of Squared Residuals (SSR): {ssr:.4f}")

# Plotting true vs prediction
plot_fuction(z_true, z_pred)