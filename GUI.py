import pygame
import pygame.draw
from constants import *
from game_class import Board


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.set_caption('HEX AI')


class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1

    def make_move(self, row, col):
        self.board.mark_cell(row, col, self.player)
        self.color_cell(row, col)
        self.current_player()

    def current_player(self):
        self.player = self.player % 2 + 1

    def color_cell(self, row, col):

        x_offset = CELL_RAD * row / 2
        y_offset = (2 * row + 1) * CELL_RAD / 2
        x = x_offset + (2 * col + 1) * CELL_RAD
        y = y_offset
        if self.player == 1:
            pygame.draw.circle(screen, P1_COLOR, (x, y), CELL_RAD, 0)
        if self.player == 2:
            pygame.draw.circle(screen, P2_COLOR, (x, y), CELL_RAD, 0)

    def show_cells(self):
        screen.fill(BG_COLOR)

        for row in range(SIZE):
            x_offset = CELL_RAD * row
            # y_offset = (HEIGHT - (SIZE * 2 * CELL_RAD)) / 2
            for col in range(SIZE):
                # y_offset = (2 * row + 1) * CELL_RAD / 2
                x = x_offset + (2 * col + 1) * CELL_RAD
                y = (2 * row + 1) * CELL_RAD
                pygame.draw.circle(screen, CELL_COLOR, (x, y), CELL_RAD, 2)


