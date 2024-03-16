import numpy as np

# Take input from the user for numerator coefficients
numerator_str = input("Enter the numerator coefficients separated by spaces: ")
numerator = list(map(float, numerator_str.split()))

# Take input from the user for denominator coefficients
denominator_str = input("Enter the denominator coefficients separated by spaces: ")
denominator = list(map(float, denominator_str.split()))

# Convert transfer function to state space model
numerator_pad = numerator + [0] * (len(denominator) - len(numerator))
denominator_pad = denominator + [0] * (len(numerator) - len(denominator))

# Create the state space model matrices
A = np.zeros((len(denominator_pad) - 1, len(denominator_pad) - 1))
A[:-1, 1:] = np.eye(len(denominator_pad) - 2)
A[-1, :] = -np.array(denominator_pad[1:])
B = np.zeros((len(denominator_pad) - 1, 1))
B[-1, 0] = 1
matrix= np.array([[numerator_pad[0], numerator_pad[1], numerator_pad[2]]])
C = matrix[:,::-1]
D = np.array([[0]])

# Reverse the last row of matrix A
A[-1, :] = A[-1, ::-1]

# Display the state space model matrices
print("State Space Model Matrices:")
print("A:\n", A)
print("B:\n", B)
print("C:\n", C)
print("D:\n", D)
