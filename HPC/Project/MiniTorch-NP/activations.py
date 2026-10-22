import numpy as np

def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_derivative(z):
    s= sigmoid(z)
    return s*(1.0 - s)

def relu(z):
    return np.maximum(0.0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

def tanh(z):
    return np.tanh(z)

def tanh_derivative(z):
    t = np.tanh(z)
    return 1.0 - t**2


