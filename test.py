import sys
import pygame
from constants import *

pygame.init()
wind = pygame.display.set_mode((WIDTH, HEIGHT))
wind.fill(BG_COLOR)
pygame.display.set_caption('test')

pygame.draw.circle(wind, (15, 15, 15), (10, 10), 10)


def main():
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()