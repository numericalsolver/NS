import sympy as sp
s = sp.symbols('s')

# identity matric function
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

m=int(input("Enter the order of the system,which should be a sqaure matrix[A]:"))

# function to square matrix as input
def take_square_matrix_input(size):
    matrix = []
    print("Enter the elements of the square matrix row-wise[A]:")
    for _ in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

matrix1 = take_square_matrix_input(m)
print("Entered square matrix[A]:")
for row in matrix1:
    print(row)

identity=identity_matrix(m)
print("SI")
for row in identity:
    print(row)

# function to subtract two matrices
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

# function to find transpose
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# function to multiply two matrices
def matrix_multiply(A, B):
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
    
  
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

#function to find inverse of a matrix
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

# Get user input for the size of the matrix2
row_col_input=input("Enter the number of rows and columns of input matrix sperated by space[B]:")
rows,cols=map(int,row_col_input.split())

# Take matrix input from user
input_matrix = take_matrix_input(rows, cols)

if input_matrix:
    # Print the matrix
    print("User Input Matrix:")
    print_matrix(input_matrix)
else:
    print("Matrix input error. Please try again.")


# Get user input for the size of the matrix2
row_col_input=input("Enter the number of rows and columns of output matrix sperated by space[C]:")
rows,cols=map(int,row_col_input.split())

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

# Get user input for the size of the matrix
row_col_input=input("Enter the number of rows and columns of Relevance matrix sperated by space[D]:")
rows,cols=map(int,row_col_input.split())

relevance_matrix = take_matrix_input(rows, cols)
if relevance_matrix:
    # Print the matrix
    print("User Relevance Matrix:")
    print_matrix(relevance_matrix)
else:
    print("Matrix input error. Please try again.")

# function to add two matrices
def add_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for addition."

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Perform addition
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

result_matrix = add_matrices(multiply2,relevance_matrix)
print_matrix(result_matrix)





