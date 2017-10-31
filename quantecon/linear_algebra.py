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
