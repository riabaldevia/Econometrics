#Functions are declared using the def keyword, and the value produced is returned using the
#return keyword. Consider a simple function which returns the square of the input, y = x^2.

from __future__ import print_function, division
def square(x):
return x**2

# Call the function
x = 2
y = square(x)
print(x,y)
