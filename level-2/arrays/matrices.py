from numpy import *

matrix1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
matrix2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')

# diagonal elements
print(matrix1.diagonal())
print(matrix1.max())
print(matrix1.min())
print("Sum", matrix2 + matrix1)
print("Sum", matrix2 * matrix1)