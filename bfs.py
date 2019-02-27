from solving.utils.framework import Agent
from solving.utils.structures import Queue, SearchTree

class BFSAgent(Agent):

    def __init__(self):
        self.moves = dict()

    # return the move this agent wants to make
    def move(self, puzzle):

        if puzzle not in self.moves:
            self.bfs(puzzle)

        return self.moves[puzzle]

    # use breadth-first search to plan moves
    def bfs(self, puzzle):

        tree = SearchTree(puzzle)

        frontier = Queue()
        frontier.push(puzzle)

        while len(frontier) > 0:
            leaf = frontier.pop()

            for move in leaf.moves():
                neighbor = leaf.neighbor(move)

                if neighbor not in tree:
                    tree.connect(neighbor, leaf, move)
                    frontier.push(neighbor)

                    if neighbor.solved():
                        self.moves = tree.branch(neighbor)
                        return

        # should not get here
        print("Failed to solve.")
        quit()