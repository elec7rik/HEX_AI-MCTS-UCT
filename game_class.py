import numpy as np
from constants import SIZE


class Board:

    def __init__(self):
        self.nodes = np.zeros((SIZE, SIZE))
        self.isolated_nodes = self.nodes
        self.colored_nodes = 0

    def empty_cell(self, row, col):
        return self.nodes[row][col] == 0

    def get_empty_cells(self):
        empty_cells = []
        for row in range(SIZE):
            for col in range(SIZE):
                if self.empty_cell(row, col):
                    empty_cells.append((row, col))
        return empty_cells

    def mark_cell(self, row, col, player):
        self.nodes[row][col] = player
        self.colored_nodes += 1

    # def next_state(self, nodes, play):
    #     self.nodes[row][col] =