import pygame
import sys
from dokusan import generators, renderers, solvers
from dokusan.boards import BoxSize, Sudoku
import numpy as np
from time import process_time_ns, sleep, time
from pygame.rect import *
import pygame_menu
import pygame_menu.themes

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((700, 700), pygame.HWSURFACE)

screen.fill((152, 52, 96))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            img = pygame.transform.scale(
                screen, (event.w, event.h), DestSurface=None)
            pygame.display.update()
