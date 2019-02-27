from collections import deque
from heapq import *

# FIFO structure
class Queue(object):

    def __init__(self):
        self.items = deque()

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.popleft()

class SearchTree(object):

    def __init__(self, root):
        self.parents = dict()
        self.moves = dict()
        self.levels = {root: 0}

    def __contains__(self, node):
        return node in self.levels

    def depth(self, node):
        return self.levels[node]

    def connect(self, child, parent, move):
        self.parents[child] = parent
        self.moves[child] = move
        self.levels[child] = self.levels[parent] + 1

    def branch(self, node):
        moves = dict()

        while node in self.parents:
            move = self.moves[node]
            parent = self.parents[node]
            moves[parent] = move
            node = parent

        return moves

class PriorityQueue(object):

    # Initialize an empty priority queue
    def __init__(self):
        self.items = list()
        self.pops = set()
        self.length = 0

    # Return the length of this priority queue
    def __len__(self):
        return self.length

    # Add a new item with the given priority
    def push(self, item, priority):
        heappush(self.items, (priority, item))
        self.length += 1

    # Change the priority of an existing item
    def prioritize(self, item, priority):
        heappush(self.items, (priority, item))

    # Return (and remove) the item with the highest (smallest) priority
    def pop(self):
        while len(self.items) > 0:
            (priority, item) = heappop(self.items)
            if item not in self.pops:
                self.pops.add(item)
                self.length -= 1
                return item