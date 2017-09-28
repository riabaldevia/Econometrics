#Prisoners Dilemma
import numpy as np
import quantecon.game_theory as gt

g_PD = gt.NormalFormGame((2, 2))  # There are 2 players, each of whom has 2 actions
g_PD[0, 0] = 1, 1
g_PD[0, 1] = -2, 3
g_PD[1, 0] = 3, -2
g_PD[1, 1] = 0, 0


print(g_PD)
