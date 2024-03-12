# import sympy as sp
# s = sp.symbols('s')
# def identity_matrix(n):
    
#     result = []
#     for i in range(n):
#         row = []
#         for j in range(n):
            
#             if i == j:
#                 row.append('s')
#             else:
#                 row.append(0)
#         result.append(row)
#     return result
# m=int(input("enter order "))
# identity=identity_matrix(m)
# print("si=")
# for row in identity:
#     print(row)


# import sympy as sp
# s = sp.symbols('s')
# def inverse_2x2(matrix):
#     # Extract elements
#     a, b = matrix[0][0], matrix[0][1]
#     c, d = matrix[1][0], matrix[1][1]

#     # Calculate determinant
#     det = a*d - b*c
#     if det == 0:
#         raise ValueError("The matrix is singular and its inverse does not exist.")

#     # Calculate inverse elements
#     inv_a = d / det
#     inv_b = -b / det
#     inv_c = -c / det
#     inv_d = a / det

#     # Create the inverse matrix
#     inverse = [
#         [inv_a, inv_b],
#         [inv_c, inv_d]
#     ]
#     return inverse

# # Create the 2x2 matrix with 's' on diagonal
# matrix_with_s = [
#     [s, 0],
#     [0, s]
# ]

# # Calculate the inverse
# try:
#     inv_matrix = inverse_2x2(matrix_with_s)
#     print("Inverse matrix:")
#     for row in inv_matrix:
#         print(row)
# except ValueError as e:
#     print(e)





# import sympy as sp
# s = sp.symbols('s')

# def identity_matrix(n):
    
#     result = []
#     for i in range(n):
#         row = []
#         for j in range(n):
            
#             if i == j:
#                 row.append(s)
#             else:
#                 row.append(0)
#         result.append(row)
#     return result


# m=int(input("Enter the order of the system, which is square matrix "))

# def take_square_matrix_input(size):
#     matrix = []
#     print("Enter the elements of the square matrix row-wise:")
#     for _ in range(size):
#         row = [int(x) for x in input().split()]
#         matrix.append(row)
#     return matrix





# matrix = take_square_matrix_input(m)


# print("Entered square matrix:")
# for row in matrix:
#     print(row)



# identity=identity_matrix(m)
# print("si=")
# for row in identity:
#     print(row)




# def subtract_matrices(matrix1, matrix2):
#     result = []
#     for i in range(len(matrix1)):
#         row = []
#         for j in range(len(matrix1[0])):
#             # Subtract the elements, treating 's' as a special case
#             if matrix1[i][j] == 's' and matrix2[i][j] == 0:
#                 row.append('s')
#             elif matrix1[i][j] == 's' and matrix2[i][j] == 's':
#                 row.append('s')
#             elif matrix1[i][j] == 's':
#                 row.append(f"s - {matrix2[i][j]}")
#             elif matrix2[i][j] == 's':
#                 row.append(f"{matrix1[i][j]} - s")
#             else:
#                 row.append(matrix1[i][j] - matrix2[i][j])
#         result.append(row)
#     return result


# y=subtract_matrices(identity,matrix)
# print("Result of si-A")
# for row in y:
#     print(row)


# def determinant(matrix):
#     # Base case for 2x2 matrix
#     if len(matrix) == 2:
#         return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

#     det = 0
#     for c in range(len(matrix)):
#         sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
#         det += (-1) ** c * matrix[0][c] * determinant(sub_matrix)
#     return det

# def transpose(matrix):
#     return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# def cofactor(matrix):
#     cofactor_matrix = []
#     for r in range(len(matrix)):
#         row = []
#         for c in range(len(matrix)):
#             minor_matrix = [row[:c] + row[c+1:] for row in (matrix[:r] + matrix[r+1:])]
#             sign = (-1) ** (r + c)
#             row.append(sign * determinant(minor_matrix))
#         cofactor_matrix.append(row)
#     return cofactor_matrix

# def inverse(matrix):
#     det = determinant(matrix)
#     if det == 0:
#         raise ValueError("The matrix is singular, and its inverse does not exist.")
    
#     # Calculate the adjugate matrix
#     adjugate = transpose(cofactor(matrix))
    
#     # Calculate the inverse by dividing adjugate by the determinant
#     inverse_matrix = [[adjugate[i][j] / det for j in range(len(adjugate[0]))] for i in range(len(adjugate))]
    
#     return inverse_matrix

# try:
#     inv_matrix = inverse(y)
#     print("\nInverse matrix:")
#     for row in inv_matrix:
#         print(row)
# except ValueError as e:
#     print(e)



import sympy as sp
s = sp.symbols('s')

def identity_matrix(n):
    
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            
            if i == j:
                row.append(s)
            else:
                row.append(0)
        result.append(row)
    return result


m=int(input("Enter the order of the system,which should be a sqaure matrix"))

def take_square_matrix_input(size):
    matrix = []
    print("Enter the elements of the square matrix row-wise[A]:")
    for _ in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix





matrix1 = take_square_matrix_input(m)


print("Entered square matrix:")
for row in matrix1:
    print(row)



identity=identity_matrix(m)
print("SI")
for row in identity:
    print(row)

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            element = matrix1[i][j] - matrix2[i][j]
            row.append(element)
        result.append(row)
    return result

result_matrix = subtract_matrices(identity,matrix1 )


print("SI-A")
for row in result_matrix:
    print(row)


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_multiply(A, B):
    """
    Multiply two matrices A and B.
    
    Parameters:
        A: List of lists, first matrix
        B: List of lists, second matrix
    
    Returns:
        result: List of lists, result of matrix multiplication
    """
    # Get dimensions of the matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        print("Cannot multiply the matrices. Inner dimensions do not match.")
        return None
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result





def inverse_matrix(matrix):
    n = len(matrix)
    if len(matrix) != len(matrix[0]):
        print("Matrix is not square. Inverse does not exist.")
        return None
    
    # Augmenting the matrix with identity matrix of same size
    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]
    
    # Applying Gauss-Jordan Elimination
    for i in range(n):
        if augmented_matrix[i][i] == 0:
            print("Matrix is singular. Inverse does not exist.")
            return None
        for j in range(n):
            if i != j:
                ratio = augmented_matrix[j][i] / augmented_matrix[i][i]
                for k in range(2*n):
                    augmented_matrix[j][k] -= ratio * augmented_matrix[i][k]
    
    # Scaling to make diagonal elements 1
    for i in range(n):
        divisor = augmented_matrix[i][i]
        for j in range(2*n):
            augmented_matrix[i][j] /= divisor
    
    # Extracting the inverse from the augmented matrix
    inverse = [row[n:] for row in augmented_matrix]
    
    return inverse

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Find inverses
inverse1 = inverse_matrix(result_matrix)
print("Inverse of Matrix 1:")
if inverse1:
    print_matrix(inverse1)


def take_matrix_input(rows, cols):
    matrix = []
    print("Enter the elements of the matrix row-wise:")
    for i in range(rows):
        row_input = input(f"Enter elements of row {i+1} separated by space: ")
        row_elements = [float(x) for x in row_input.split()]
        if len(row_elements) != cols:
            print(f"Please enter {cols} elements for each row.")
            return None
        matrix.append(row_elements)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Get user input for the size of the matrix
rows = int(input("Enter the number of rows of input matrix: "))
cols = int(input("Enter the number of columns of input matrix: "))

# Take matrix input from user
input_matrix = take_matrix_input(rows, cols)

if input_matrix:
    # Print the matrix
    print("User Input Matrix:")
    print_matrix(input_matrix)
else:
    print("Matrix input error. Please try again.")

rows = int(input("Enter the number of rows of output matrix: "))
cols = int(input("Enter the number of columns of output matrix: "))

# Take matrix input from user
output_matrix = take_matrix_input(rows, cols)

if output_matrix:
    # Print the matrix
    print("User Output Matrix:")
    print_matrix(output_matrix)
else:
    print("Matrix input error. Please try again.")


multiply1=matrix_multiply(output_matrix, inverse1)
if multiply1:
    print("Multiplication of output matices and inverse1")
    print_matrix(multiply1)

multiply2=matrix_multiply(multiply1, input_matrix)
if multiply2:
    print("Multiplication of multiply1 and input matrix")
    print_matrix(multiply2)








