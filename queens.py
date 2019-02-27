from solving.utils.framework import Puzzle

SIZE = 8
START = [0, 1, 2, 3, 4, 5, 6, 7]
# or [i for i in range(SIZE)]  or list(range(SIZE))

class Queens(Puzzle):

    def __init__(self, columns=START):
        self.columns = columns

    def __eq__(self, other):
        return self.columns == other.columns

    def __hash__(self):
        return hash(str(self.columns)) # or use a tuple

        # return a boolean of whether puzzle is solved
    def solved(self):
        return self.heuristic() == 0

        # return a list of legal moves
    def moves(self):
        moves = list()
        for r in range(SIZE):
            for c in range(SIZE):
                if c != self.columns:
                    moves.append((r,c))
        return moves

        # return a new puzzle that is created by making a move in current puzzle
    def neighbor(self, move):
        (r,c) = move
        new_columns = self.columns.copy()
        new_columns[r] = c
        return Queens(new_columns)

        # print puzzle to console
    def display(self):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.columns[r] == c:
                    print(" ", end=' ')
                else:
                    print("X", end=' ')
            print()
        print()

        # estimate on how many moves until solved
    def heuristic(self):
        conflicts = 0

        # check for paris of queens in the same column
        for r1 in range(SIZE):
            c1 = self.columns[r1]
            for r2 in range(r1 + 1, SIZE):
                c2 = self.columns[r2]
                if c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                    conflicts += 1
        return conflicts

        # tie breaker
    def __lt__(self, other):
        return self.columns < other.columns
