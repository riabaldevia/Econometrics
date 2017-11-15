#Nash Equilibrium--In the Nash Equilibrium, each player's strategy is optimal when considering the decisions of other players

Read more: Nash Equilibrium https://www.investopedia.com/terms/n/nash-equilibrium.asp#ixzz4ySuAWtbx 
Follow us: Investopedia on Facebook#NashPy library is included in SciPy. This is a library for simple 2 player games. 

#Example 1
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


#Example 2
>>> import nash
>>> A = [[1, 2], [3, 0]]
>>> B = [[4, 2], [9, 8]]
>>> battle_of_the_sexes = nash.Game(A, B)
>>> for eq in battle_of_the_sexes.support_enumeration():
...     print(eq)
... 
(array([ 0.,  1.]), array([ 1.,  0.]))
>>> battle_of_the_sexes[[0, 1], [1, 0]]
array([3, 9])
