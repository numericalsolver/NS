# import numpy as np

# # Get input for the numerator coefficients of the transfer function
# numerator_str = input("Enter the numerator coefficients of the transfer function separated by spaces: ")
# numerator = list(map(float, numerator_str.split()))

# # Get input for the denominator coefficients of the transfer function
# denominator_str = input("Enter the denominator coefficients of the transfer function separated by spaces: ")
# denominator = list(map(float, denominator_str.split()))

# # Ensure the denominator is not empty
# if not denominator:
#     print("Denominator coefficients cannot be empty. Exiting.")
#     exit()

# # Extract the order of the transfer function
# order = len(denominator) - 1

# # Create the state space model matrices
# A = np.zeros((order, order))
# B = np.zeros((order, 1))
# C = np.zeros((1, order))
# D = np.zeros((1, 1))

# # Populate the state space model matrices
# A[:-1, 1:] = np.eye(order - 1)
# A[-1, :] = -np.array(denominator[:-1])

# B[-1, 0] = 1
# #C[0, :len(numerator)] = numerator
# C[0, :] = np.flip(numerator[:-1])
# D[0, 0] = numerator[-1]
# #D[0, 0] = 0  # D matrix should be zeros for transfer functions

# # Display the state space model matrices
# print("State Space Model Matrices:")
# print("A:\n", A)
# print("B:\n", B)
# print("C:\n", C)
# print("D:\n", D)


# import numpy as np

# # Transfer function coefficients
# numerator = [1, 3, 3]
# denominator = [1, 2, 3, 1]

# # Extract the order of the transfer function
# order = len(denominator) - 1

# # Create the state space model matrices
# A = np.zeros((order, order))
# B = np.zeros((order, 1))
# C = np.zeros((1, order))
# D = np.zeros((1, 1))

# # Populate the state space model matrices
# A[:-1, 1:] = np.eye(order - 1)
# A[-1, :] = -np.array(denominator[1:])
# B[-1, 0] = 1

# # Check if the numerator has enough coefficients
# if len(numerator) < order:
#     print("Insufficient numerator coefficients provided. Exiting.")
#     exit()

# # Assign coefficients from numerator to C in reverse order
# C[0, :] = np.flip(numerator[:-1])
# D[0, 0] = numerator[-1]

# # Display the state space model matrices
# print("State Space Model Matrices:")
# print("A:\n", A)
# print("B:\n", B)
# print("C:\n", C)
# print("D:\n", D)




import numpy as np

# Transfer function coefficients
numerator = [1, 3, 3]
denominator = [1, 2, 3, 1]

# Extract the order of the transfer function
order = len(denominator) - 1

# Create the state space model matrices
A = np.zeros((order, order))
B = np.zeros((order, 1))
C = np.zeros((1, order))
D = np.zeros((1, 1))

# Populate the state space model matrices
A[:-1, 1:] = np.eye(order - 1)
A[-1, :] = -np.array(denominator[1:])
B[-1, 0] = 1

# Check if the numerator has enough coefficients
if len(numerator) < order:
    print("Insufficient numerator coefficients provided. Exiting.")
    exit()

# Assign coefficients from reversed numerator to C
C[0, -len(numerator[:-1]):] = np.flip(numerator[:-1])
D[0, 0] = numerator[-1]

# Display the state space model matrices
print("State Space Model Matrices:")
print("A:\n", A)
print("B:\n", B)
print("C:\n", C)
print("D:\n", D)
