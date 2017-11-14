#NashPy library is included in SciPy. This is a library for simple 2 player games. 

>>> import nash
>>> A = [[1, 2], [3, 0]]
>>> B = [[0, 2], [3, 1]]
>>> battle_of_the_sexes = nash.Game(A, B)
>>> for eq in battle_of_the_sexes.support_enumeration():
...     print(eq)
(array([ 1.,  0.]), array([ 0.,  1.]))
(array([ 0.,  1.]), array([ 1.,  0.]))
(array([ 0.5,  0.5]), array([ 0.5,  0.5]))
>>> battle_of_the_sexes[[0, 1], [1, 0]]
array([3, 3])

##Add explanations
