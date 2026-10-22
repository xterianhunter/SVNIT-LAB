import numpy as np 

from activations import (sigmoid, sigmoid_derivative, relu, relu_derivative, tanh, tanh_derivative,)

z = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

print("Input:                       ", z)
print("Sigmoid:                     ", sigmoid(z))
print("Sigmoid derivative :         ", sigmoid_derivative(z))
print("Relu:                        ", relu(z))
print("Relu derivative:             ", relu_derivative(z))
print("tanh:                        ", tanh(z))
print("tanh derivative:             ", tanh_derivative(z))

assert np.all((sigmoid(z) > 0) & (sigmoid(z) < 1))
assert np.allclose(relu(z), [0,0,0,1,2])
assert np.allclose(relu_derivative(z), [0,0,0,1,1])
assert np.allclose(tanh(0.0), 0.0)
assert np.allclose(sigmoid(0.0), 0.5)

print("\n All activations test passed!")

