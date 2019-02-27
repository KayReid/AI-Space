# Kayleigh Reid

from solving.utils.framework import Puzzle

SIZE = 3

SOLVED = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

GRID = [
    [8,6,7],
    [2,5,4],
    [3,0,1]
]

class Tiles(Puzzle):

    def __init__(self, positions=GRID, row=2, column=1):
        self.row = row
        self.column = column
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]

        for r in range(SIZE):
            for c in range(SIZE):
                self.grid[r][c] = positions[r][c]

    def __eq__(self, other):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.grid[r][c] != other.grid[r][c]:
                    return False
        return True

    def __hash__(self):
        return hash((self.grid[0][0], self.grid[0][1], self.grid[0][2],
                     self.grid[1][0], self.grid[1][1], self.grid[1][2],
                     self.grid[2][0], self.grid[2][1], self.grid[2][2]))

    # return a boolean of whether puzzle is solved
    def solved(self):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.grid[r][c] != SOLVED[r][c]:
                    return False
        return True

    # return a list of legal moves
    def moves(self):
        moves = list()
        if self.row > 0:
            moves.append((-1, 0))
        if self.row < SIZE - 1:
            moves.append((1, 0))
        if self.column < SIZE - 1:
            moves.append((0, 1))
        if self.column > 0:
            moves.append((0, -1))
        return moves

    # return a new puzzle that is created by making a move in current puzzle
    def neighbor(self, move):
        (dr, dc) = move

        row = self.row
        column = self.column

        fliprow = self.row + dr
        flipcolumn = self.column + dc
        curr = self.grid[fliprow][flipcolumn]

        # do a deep copy instead to beef up efficiency
        positions = [[0,0,0], [0,0,0], [0,0,0]]

        for r in range(SIZE):
            for c in range(SIZE):
                if (r, c) == (row, column):
                    positions[r][c] = curr
                elif (r, c) == (fliprow, flipcolumn):
                    positions[r][c] = 0
                else:
                    positions[r][c] = self.grid[r][c]

        return Tiles(positions, self.row + dr, self.column + dc)

    # print puzzle to console
    def display(self):
        print(" _____________")
        for r in range(SIZE):
            for c in range(SIZE):
                print(" | ", end='')
                # can change the 0 to a " " if I want to match the assignment exactly
                print(self.grid[r][c], end='')
            print(" |")
            print(" _____________")

    def heuristic(self):
        # fix this heuristic value
        count = 0
        for r in range(SIZE):
            for c in range(SIZE):
                if self.grid[r][c] != SOLVED[r][c] and self.grid[r][c] != 0:
                    (x, y) = (((self.grid[r][c] - 1) % 3), (self.grid[r][c] - 1) // 3)
                    count += abs(x - r) + abs(y - c)
        return count

    def __lt__(self, other):
        return True
