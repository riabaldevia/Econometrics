#Linear algebra and vectors.
#Using numpy
import numpy as np
a = np.array([2, 5, 1]) #This tuple is now an array
a
array([2, 5, 1])

b = np.ones(3) #numpy.ones(shape, dtype=None, order='C'). Return a new array of given shape and type, filled with ones.
a + b
array([ 3.,  6.,  2.])

3*a #multiple arry([2, 5, 1]) by 3
array([ 6, 15,  3])


#More array fun with numpy
d = np.array([24,5,6])
d
array([24,  5,  6])

d.shape
(3,)

d.ndim
1

#Matrices with numpy
A = np.matrix([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
A
matrix([[3, 1, 4],
        [1, 5, 9],
        [2, 6, 5]])
A.T
matrix([[3, 1, 2],
        [1, 5, 6],
        [4, 9, 5]])
A.H
matrix([[3, 1, 2],
        [1, 5, 6],
        [4, 9, 5]])

A.I
matrix([[ 0.32222222, -0.21111111,  0.12222222],
        [-0.14444444, -0.07777778,  0.25555556],
        [ 0.04444444,  0.17777778, -0.15555556]])

A.A
array([[3, 1, 4],
       [1, 5, 9],
       [2, 6, 5]])

A.A1
array([3, 1, 4, 1, 5, 9, 2, 6, 5])

A
matrix([[3, 1, 4],
        [1, 5, 9],
        [2, 6, 5]])

A*A.I
matrix([[  1.00000000e+00,   0.00000000e+00,   0.00000000e+00],
        [  0.00000000e+00,   1.00000000e+00,  -1.38777878e-16],
        [  5.55111512e-17,  -1.38777878e-16,   1.00000000e+00]])

A**3
matrix([[ 168,  424,  565],
        [ 346,  990, 1294],
        [ 302,  854, 1081]])

b = np.mat('1; 2; 3')
b
matrix([[1],
        [2],
        [3]])
A*b
matrix([[17],
        [38],
        [29]])

b.T * A
matrix([[11, 29, 37]])

A
matrix([[3, 1, 4],
        [1, 5, 9],
        [2, 6, 5]])

b
matrix([[1],
        [2],
        [3]])

x = A.I * b
x
matrix([[ 0.26666667],
        [ 0.46666667],
        [-0.06666667]])

A*x - b
matrix([[  0.00000000e+00],
        [ -4.44089210e-16],
        [  4.44089210e-16]])

np.linalg.solve(A, b)
matrix([[ 0.26666667],
        [ 0.46666667],
        [-0.06666667]])

#Example: Build on this with explanations
>>> A = np.matrix([[2, 1, 3], [1, 2, 3], [3, 5, 3]])
>>> A.T
matrix([[2, 1, 3],
        [1, 2, 5],
        [3, 3, 3]])

#Exmaple: Try a 5xt5 matrix

#Example: Using Plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy

matrix1 = np.matrix(
    [[0, 4],
     [2, 0]]
)

matrix2 = np.matrix(
    [[-1, 2],
     [1, -2]]
)

matrix_sum = matrix1 + matrix2

colorscale = [[0, '#EAEFC4'], [1, '#9BDF46']]
font=['#000000', '#000000']

table = FF.create_annotated_heatmap(matrix_sum.tolist(), colorscale=colorscale, font_colors=font)
py.iplot(table, filename='matrix-sum')
