import numpy as np
from scipy.sparse import csr_matrix

row_a = np.array([0, 0, 1, 1, 1])
column_a = np.array([0, 0, 2, 0, 2])
data_a = np.array([1, 3, 5, 7, 9])
sparse_matrix_a = csr_matrix((data_a, (row_a, column_a)),shape = (3, 3)).toarray()
print("first Sparse Matrix : ", sparse_matrix_a)


row_b = np.array([0, 0, 1, 1, 2])
column_b = np.array([2, 1, 1, 0, 2])
data_b = np.array([3, 4, 7, 8, 9])
sparse_matrix_b = csr_matrix((data_b, (row_b, column_b)),shape = (3, 3)).toarray()
print("second Sparse Matrix : ", sparse_matrix_b)

row_c = np.array([0, 0, 1, 1, 1])
column_c = np.array([0, 0, 2, 0, 2])
data_c = np.array([1, 3, 5, 7, 9])
sparse_matrix_c = csr_matrix((data_c, (row_c, column_c)),shape = (3, 3)).toarray()
print("third Sparse Matrix : ", sparse_matrix_c)


subtract_matrix = sparse_matrix_a - sparse_matrix_b
print("addtion of the three matrices  : ", subtract_matrix)

print("transpose of the given matrix  ", sparse_matrix_a.transpose())
##output:
##first Sparse Matrix :  [[ 4  0  0]
## [ 7  0 14]
## [ 0  0  0]]
##second Sparse Matrix :  [[0 4 3]
## [8 7 0]
## [0 0 9]]
##third Sparse Matrix :  [[ 4  0  0]
## [ 7  0 14]
## [ 0  0  0]]
##addtion of the three matrices  :  [[ 4 -4 -3]
## [-1 -7 14]
## [ 0  0 -9]]
##transpose of the given matrix   [[ 4  7  0]
## [ 0  0  0]
## [ 0 14  0]]

##acquired it from the faculty(suraj sir) 
