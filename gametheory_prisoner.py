#Prisoners Dilemma
import numpy as np
import quantecon.game_theory as gt

g_PD = gt.NormalFormGame((2, 2))  # There are 2 players, each of whom has 2 actions
g_PD[0, 0] = 1, 1
g_PD[0, 1] = -2, 3
g_PD[1, 0] = 3, -2
g_PD[1, 1] = 0, 0


print(g_PD)


#Axelrod library
def strategy(self, opponent):
    # First move
    if len(self.history) == 0:
        return C
    # React to the opponent's last move
    if opponent.history[-1] == D:
        return D
    return C
  
  def strategy(self, opponent):

    # if there is no history, then this is the first turn, so cooperate
    if not opponent.history:
        return C

    # if this is either the last or second-to-last turn, defect
    if len(opponent.history) > (self.tournament_attributes['length'] - 3):
        return D

    # if the opponent did not defect on any of the first six turns,
    # and we are not in the last 20 turns, cooperate
    if len(opponent.history) < 180:
        if len(opponent.history) > 6:
            if D not in opponent.history[:7]:
                 return C

    # if the total number of defections by the opponent is 
    # greater than three, always defect
    if opponent.defections > 3:
        return D

    # failsafe; if none of the other conditions are true,
    # cooperate
    return C
