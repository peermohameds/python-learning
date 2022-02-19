from numpy import *
two_dim = array([[1, 2, 3], [4, 5, 6], [5, 4, 9], [11, 6, 22]], int)
print(two_dim)
print("data type:", two_dim.dtype)

# accessing a specific element
print("row 1 - column 3 : [index 0, 2]", two_dim[0][2])
print("row 2 - column 2 : [index 1, 1]", two_dim[1][1])

# size of the array
print("Size of two dimension array",two_dim.size)
print("Shape of two dimension array",two_dim.shape)
print("two dimension array flattened as single dimension array",two_dim.flatten())
print(two_dim.reshape(2, 2, 3))