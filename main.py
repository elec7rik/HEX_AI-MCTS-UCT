import copy
import sys
import pygame
import numpy as np
import random

import GUI
# from GUI import Game
from constants import WIDTH, HEIGHT, CELL_RAD, BG_COLOR, SIZE
import game_class


def main():
    game = GUI.Game()
    board = GUI.Board()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                y_offset = (HEIGHT - (SIZE * CELL_RAD)) / 2
                # row = (pos[1] - y_offset) // (2 * CELL_RAD)

                row = ((pos[1] - HEIGHT/2 + SIZE * CELL_RAD)//(2 * CELL_RAD * SIZE)) * (SIZE - 1)
                x_offset = CELL_RAD * row / 2
                col = (pos[0] - x_offset) // (2 * CELL_RAD)
                row = int(row)


                print(row)
                col = int(col)
                print(col)
                if board.empty_cell(row, col):
                    game.make_move(row, col)

        game.show_cells()
        pygame.display.update()


main()
