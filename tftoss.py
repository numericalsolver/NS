import numpy as np
# taking the inputs from the user
numerator_str = input("Enter the numerator coefficients separated by spaces: ")
numerator = list(map(float, numerator_str.split()))

denominator_str = input("Enter the denominator coefficients separated by spaces: ")
denominator = list(map(float, denominator_str.split()))

# function to convert transfer function to state space model
def tftossm(numerator,denominator):
    numerator_pad = numerator + [0] * (len(denominator) - len(numerator))
    denominator_pad = denominator + [0] * (len(numerator) - len(denominator))
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
    result_A=A
    result_B=B
    result_C=C
    result_D=D
    return result_A,result_B,result_C,result_D
    
result_A,result_B,result_C,result_D=tftossm(numerator,denominator)
print("A")
print(result_A)
print("B")
print(result_B)
print("C")
print(result_C)
print("D")
print(result_D)


