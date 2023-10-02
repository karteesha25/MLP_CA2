import numpy as np
def read_matrix(rows, cols):
 matrix = []
 print(f"Enter the elements of the matrix ({rows}x{cols}):")
 for _in range(rows):
 row = [int(x) for x in input().split()]
 if len(row) != cols:
 raise ValueError("Invalid number of columns!")
 matrix.append(row)
 return matrix
def print_matrix(matrix):
 for row in matrix:
 print(" ".join(str(x) for x in row))
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix1 = read_matrix(rows, cols)
matrix2 = read_matrix(rows, cols)
add_result = np.add(matrix1,matrix2)
sub_result = np.subtract(matrix1, matrix2)
mul_result = np.dot(matrix1, matrix2)
transpose_result = np.transpose(matrix1)
inverse_result = np.linalg.inv(matrix1)
print("\nMatrix Addition:")
print_matrix(add_result)
print("\nMatrix Subtraction:")
print_matrix(sub_result)
print("\nMatrix Multiplication:")
print_matrix(mul_result)
print("\nMatrix Transpose:")
print_matrix(transpose_result)
print("\nMatrix Inverse:")
print_matrix(inverse_result)