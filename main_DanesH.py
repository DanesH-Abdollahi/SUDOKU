import pygame
import sys
from dokusan import generators, renderers, solvers
import numpy as np
from time import sleep

SIZE = (800, 800)
Width, Height = SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
MY_COLOR = (204, 229, 255)
MY_COLOR = (176, 224, 230)
MY_COLOR = (253, 245, 230)

background_color = MY_COLOR


def add_grid(screen, font):
    margin = Width / 80
    bottom_margin = 15 * margin

    Horizental_diff = (Width - 2 * margin) / 9
    Vertical_diff = (Height - margin - bottom_margin) / 9

    for i in range(10):
        if(i % 3 == 0):
            pygame.draw.line(
                screen,
                BLACK,
                (margin + Horizental_diff * i, margin),
                (margin + Horizental_diff * i, Height - bottom_margin),
                4,
            )  # Draw Vertical Lines

            pygame.draw.line(
                screen,
                BLACK,
                (margin, margin + Vertical_diff * i),
                (margin + Horizental_diff * 9, margin + Vertical_diff * i),
                4,)

        pygame.draw.line(
            screen,
            BLACK,
            (margin + Horizental_diff * i, margin),
            (margin + Horizental_diff * i, Height - bottom_margin),
            2,
        )  # Draw Vertical Lines

        pygame.draw.line(
            screen,
            BLACK,
            (margin, margin + Vertical_diff * i),
            (margin + Horizental_diff * 9, margin + Vertical_diff * i),
            2,
        )  # Draw Horizental Lines

    pygame.display.update()

    add_sudoko_table(screen, font, Horizental_diff, Vertical_diff, margin)


def add_sudoko_table(screen, font, horizental_diff, vertical_diff, margin):

    sudoku = generators.random_sudoku(avg_rank=150)  # Generate a Sudoku
    sudoku_np_array = np.array(list(str(sudoku)), dtype=int).reshape(9, 9)

    for i in range(len(sudoku_np_array)):
        for j in range(len(sudoku_np_array)):
            if (0 < sudoku_np_array[i][j] < 10):
                value = font.render(str(sudoku_np_array[i][j]), True, BLACK)
                screen.blit(
                    value, ((horizental_diff/2)+(j*horizental_diff)-3, (vertical_diff/2) + (i * vertical_diff) - margin))
                pygame.display.update()
                sleep(0.01)

    pygame.display.update()

    # solution = solvers.backtrack(sudoku)  # Solve a Sudoku
    # sudoku_solution_np_array = np.array(
    #     list(str(solution)), dtype=int).reshape(9, 9)
    # print(renderers.colorful(solution))  # Print Solved Sudoku

    # sudoku.update(  # Update Sudoku
    #     Sudoku.from_list(
    #         sudoku_np_array.tolist(),
    #         box_size=BoxSize(3, 3),
    #     ).cells()
    # )


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("SUDOKU")
    screen.fill(background_color)
    pygame.display.update()

    myfont = pygame.font.SysFont('Comic Sans MS', 70)

    add_grid(screen, myfont)
    # add_sudoko_table(screen, myfont)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
