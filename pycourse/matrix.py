"""
Matrix and vectors product
马云飞
2020118092
"""


# Create a new vector of a certain size initialised to the value given.
def make_vector(length, values):
    my_vector = []
    for i in range(0, length):
        my_vector.append(values)
    return my_vector


# Create a new matrix initialised to the value given
def make_matrix(row, column, values):
    my_matrix = []
    for i in range(0, row):
        temp = []
        my_matrix.append(temp)
        for j in range(0, column):
            temp.append(values)
    return my_matrix


# Compute the dot product of two vectors and return it as a value
def dot_product(vector1, vector2):
    result = 0
    for a, b in zip(vector1, vector2):
        result += a * b
    return result


# Compute the product of two matrices and return as a new matrix
def matrix_product(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Can not be computed: the column num of m1 is not equal to the row num of m2!!!")
        return -1
    result = make_matrix(len(matrix1), len(matrix2[0]), 0)
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix2[0])):
            temp = 0
            for k in range(0, len(matrix2)):
                temp += matrix1[i][k] * matrix2[k][j]
            result[i][j] = temp
    return result


v1 = make_vector(3, 2)
v2 = make_vector(3, 3)
ans = dot_product(v1, v2)
print(v1)
print(v2)
print(ans)

m1 = make_matrix(2, 2, 2)
m2 = make_matrix(2, 2, 3)
m3 = matrix_product(m1, m2)
print(m1)
print(m2)
print(m3)

"""
>>> v1 = make_vector(3, 2)
>>> v2 = make_vector(3, 3)
>>> ans = dot_product(v1, v2)
>>> print(v1)
[2, 2, 2]
>>> print(v2)
[3, 3, 3]
>>> print(ans)
18

>>> m1 = make_matrix(2, 2, 2)
>>> m2 = make_matrix(2, 2, 3)
>>> m3 = matrix_product(m1, m2)
>>> print(m1)
[[2, 2], [2, 2]]
>>> print(m2)
[[3, 3], [3, 3]]
>>> print(m3)
[[12, 12], [12, 12]]
"""