from solving.utils.framework import Agent
from random import choice, random
from math import exp
# citation: Professor Lisa Torrey identified problems with the random number I was using
# and the way I was passing move back to my move function

class SimulatedAnnealingAgent(Agent):
    # initialize the temperature
    def __init__(self):
        self.temperature = 1.0

    # return the move this agent wants to make
    def move(self, puzzle):
        return self.anneal(puzzle)

    def anneal(self, puzzle, Tstop=0.01, Tdecay=0.99):

        # temperature is greater than stopping point, keep going
        while self.temperature > Tstop:
            move = choice(puzzle.moves())
            neighbor = puzzle.neighbor(move)

            rand = random()
            probability = exp((puzzle.heuristic() - neighbor.heuristic()) / self.temperature)

            # return a move
            if neighbor.heuristic() < puzzle.heuristic() or probability >= rand:
                self.temperature *= Tdecay
                return move

        # temperature is lower than the stop point
        print("Failed to find a solution.")
        quit()