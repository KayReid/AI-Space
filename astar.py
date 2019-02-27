from solving.utils.framework import Agent
from solving.utils.structures import PriorityQueue, SearchTree

class AStarAgent(Agent):

    def __init__(self):
        self.moves = dict()

    # return the move this agent wants to make
    def move(self, puzzle):

        if puzzle not in self.moves:
            self.astar(puzzle)

        return self.moves[puzzle]

    # use A* search to plan moves
    def astar(self, puzzle):

        tree = SearchTree(puzzle)
        finalized = set()
        frontier = PriorityQueue()

        # initialize with starting puzzle
        frontier.push(puzzle, puzzle.heuristic())

        while len(frontier) > 0:
            leaf = frontier.pop()
            finalized.add(leaf)

            if leaf.solved():
                self.moves = tree.branch(leaf)
                return

            for move in leaf.moves():
                neighbor = leaf.neighbor(move)

                if neighbor not in finalized:
                    if neighbor not in tree:
                        tree.connect(neighbor, leaf, move)
                        frontier.push(neighbor, tree.depth(neighbor) + neighbor.heuristic())

                    # not sure if this works
                    # check
                    if tree.depth(neighbor) > tree.depth(leaf) + 1:
                        tree.connect(neighbor, leaf, move)
                        frontier.push(neighbor, tree.depth(neighbor) + neighbor.heuristic())

        # should not get here
        print("Failed to solve.")
        quit()
