>>>import numpy as np
>>>m = np.matrix([[2, 4, 6], [-2, 3, 5], [4, 6, -2]])
>>>m

matrix([[ 2,  4,  6],
        [-2,  3,  5],
        [ 4,  6, -2]])

#Transpose
>>>m.T

matrix([[ 2, -2,  4],
        [ 4,  3,  6],
        [ 6,  5, -2]])

>>>m.I

matrix([[ 0.23684211, -0.28947368, -0.01315789],
        [-0.10526316,  0.18421053,  0.14473684],
        [ 0.15789474, -0.02631579, -0.09210526]])



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

>>>m.I

matrix([[ 1.15 , -0.975,  0.3  ],
        [-1.05 ,  0.825, -0.1  ],
        [ 0.5  , -0.25 ,  0.   ]])

#3
import numpy as np
m = np.matrix([[-5,2], [1, -3], [0,4]])
m.T
matrix([[-5,  1,  0],
        [ 2, -3,  4]])


#4
import numpy as np
np.matrix([[1, 1, 1, 1],[-3, 5, -2, 7]])
m

matrix([[ 1,  1,  1,  1],
        [-3,  5, -2,  7]])

m.T
matrix([[ 1, -3],
        [ 1,  5],
        [ 1, -2],
        [ 1,  7]])


#5
import numpy as np
a = np.array([[1, 2, -1], [0,-5,3]])
b = np.array([[4],[3],[7]])
print(a.dot(b))


array([[3],
       [6]])

#6 Matrix Transformations. This is a rough; needs to be revisited.
import numpy as np
M, N = 2, 2
matrix = np.arange(M*N).reshape((M,N))
matrix
array([[0, 1],
       [2, 3]])
points = np.mgrid[0:N, 0:M].reshape((2, M*N))
points
array([[0, 0, 1, 1],
       [0, 1, 0, 1]])
x, y = np.mgrid[0:N, 0:M]
points = np.vstack([x.ravel(), y.ravel()])

a = np.array([[1,0],[0,1]])
new_points = np.linalg.inv(a).dot(points).astype(int)
new_points
array([[0, 0, 1, 1],
       [0, 1, 0, 1]])
x, y = new_points.reshape((2, M,N), order='F')
x + N*y
array([[0, 1],
       [2, 3]])
