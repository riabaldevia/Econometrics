import numpy as np
m = np.matrix([[2, 4, 6], [-2, 3, 5], [4, 6, -2]])
m

matrix([[ 2,  4,  6],
        [-2,  3,  5],
        [ 4,  6, -2]])

#Transpose
m.T

matrix([[ 2, -2,  4],
        [ 4,  3,  6],
        [ 6,  5, -2]])

#2

import numpy as np
m = np.matrix([[1, 3, 6], [2, 6, 8], [6, 8, 3]])
m
matrix([[1, 3, 6],
        [2, 6, 8],
        [6, 8, 3]])

m.T
matrix([[1, 2, 6],
        [3, 6, 8],
        [6, 8, 3]])
