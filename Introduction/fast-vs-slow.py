import math
import time

import numpy as np

SIZE = int(1E6)

x = np.random.uniform(size=SIZE)
y = np.random.uniform(size=SIZE)

# dot product (x . y) = sum(x_i
start = time.time()
sum_var = 0.0
for i in range(SIZE):
    sum_var += x[i] * y[i]
end = time.time()
print("sum senza libreria: ", sum_var)
print(end - start)

# Using library 600 times faster, the library doesn't change the original values.
start = time.time()
dotProduct = x.dot(y)
end = time.time()
print("sum con library: ", dotProduct)
print(end - start)

# Evaluating ||x - y||_2
start = time.time()

total = 0.0
for i in range(SIZE):
    total += math.pow(x[i] - y[i], 2)
total = math.sqrt(total)

end = time.time()
print("norma without library: ", total)
print("tempo", end - start)

# Using library 600 times faster, the library doesn't change the original values.
start = time.time()

norm = np.linalg.norm(x - y)
end = time.time()

print("norma con library: ", norm)
print("tempo", end - start)

# Matrix multiplication
N, M = 300, 300

# create the matrix
mat1 = np.random.uniform(size=[M, N])
mat2 = np.random.uniform(size=[N, M])
res = np.zeros(shape=[M, M])


def my_dot(mat1, mat2, mat1_nrow, i, j):
    sum_mat = 0.0
    for k in range(mat1_nrow):
        sum_mat += mat1[i, k] * mat2[k, j]
    return sum_mat


# naive time = 11.292561292648315
start = time.time()
for i in range(M):
    for j in range(N):
        res[i, j] = my_dot(mat1, mat2, M, i, j)

end = time.time()
print("matrix without library: ")
print("time: ", end - start)

# lib time = 0.0007369518280029297 20'000 times faster, 
# sequential access of memory instead of random one. quadratic complexity
start = time.time()
res_lib = np.matmul(mat1, mat2)
end = time.time()
print("matrix con library: ", res_lib)
print("time: ", end - start)
