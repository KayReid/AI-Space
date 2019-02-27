from time import sleep, time

# superclass for puzzles
class  Puzzle(object):

    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    # return a boolean of whether puzzle is solved
    def solved(self):
        raise NotImplementedError

    # return a list of legal moves
    def moves(self):
        raise NotImplementedError

    # return a new puzzle that is created by making a move in current puzzle
    def neighbor(self, move):
       raise NotImplementedError

    # print puzzle to console
    def display(self):
        raise NotImplementedError

    # estimate on how many moves until solved
    def heuristic(self):
        raise NotImplementedError

    # tie breaker
    def __lt__(self, other):
        raise NotImplementedError

# superclass for a puzzle solver
class Agent(object):

    # return the move this agent wants to make
    def move(self, puzzle):
        raise NotImplementedError

    # watch this agent solve a puzzle
    def solve(self, puzzle, interval=0.25):
        print("Solving puzzle:")
        puzzle.display()
        moves = 0

        while not puzzle.solved():

            start = time()
            move = self.move(puzzle)
            seconds = time() - start
            print("After", seconds, "seconds: ")

            puzzle = puzzle.neighbor(move)
            puzzle.display()
            moves += 1
            sleep(interval)

        print ("Puzzle solved in", moves, "moves.")