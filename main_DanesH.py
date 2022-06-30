from turtle import color, pos
import pygame
import sys
from dokusan import generators, renderers, solvers
import numpy as np
from time import sleep
from pygame.rect import *

SIZE = (800, 800)
Width, Height = SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (178, 34, 34)
GREEN = (0, 100, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
MY_COLOR = (204, 229, 255)
MY_COLOR = (176, 224, 230)
MY_COLOR = (253, 245, 230)

Orginal_Sudoko_number_color = (25, 25, 112)
background_color = MY_COLOR


def new_rect(screen, rect, border_color, inner_color, border, Horizental_diff, Vertical_diff, margin, bottom_margin):
    pygame.draw.rect(
        screen,
        border_color,
        (rect.left, rect.top, Horizental_diff +
         border, Vertical_diff + border), border
    )

    inner = pygame.Rect(rect.left + border, rect.top +
                        border, Horizental_diff - border, Vertical_diff - border)
    pygame.draw.rect(screen, inner_color, inner)

    add_lines(screen, Horizental_diff, Vertical_diff, margin, bottom_margin)

    pygame.display.update()


def add_lines(screen, Horizental_diff, Vertical_diff, margin, bottom_margin):
    for i in range(10):
        if(i % 3 == 0):
            pygame.draw.line(
                screen,
                BLACK,
                (margin + Horizental_diff * i, margin),
                (margin + Horizental_diff * i, Height - bottom_margin),
                6,
            )  # Draw Vertical Lines

            pygame.draw.line(
                screen,
                BLACK,
                (margin, margin + Vertical_diff * i),
                (margin + Horizental_diff * 9, margin + Vertical_diff * i),
                6,)

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
            4,
        )  # Draw Horizental Lines

    pygame.display.update()


def draw_text(screen, text, pos, color):
    font = pygame.font.SysFont('Comic Sans MS', 70)
    img = font.render(text, True, color)
    pos = img.get_rect(center=pos)
    screen.blit(img, pos)
    pygame.display.update()


def insert(screen, position, margin, Horizental_diff, Vertical_diff, bottom_margin, orginal_sudoko, solution_sudoko, rects,  totall_mistakes):
    i, j = position[1], position[0]

    i, j = (i-margin) // Vertical_diff, (j-margin) // Horizental_diff

    tmp = orginal_sudoko.copy()
    tmp_color = np.zeros((9, 9), dtype=tuple)
    # print("************************************************************")
    # for ii in range(9):
    #     for jj in range(9):
    #         print(tmp[ii, jj], end=" ")
    #     print("\n")
    # print("************************************************************")

    if i > 8 or j > 8:
        return totall_mistakes, tmp

    # print(i, j)
    # myfont = pygame.font.SysFont('Comic Sans MS', 70)
    # print(position)

    if (tmp[i][j] != 0):
        return totall_mistakes, tmp

    # if (tmp[i][j] != 0):
    #     return totall_mistakes, tmp

    new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 3,
             Horizental_diff, Vertical_diff, margin, bottom_margin)

    while True:
        if totall_mistakes >= 3:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if (orginal_sudoko[i][j] != 0):
                    return totall_mistakes, tmp

                if(event.key == 8):
                    new_rect(screen, rects[9*i + j], BLACK,  (173, 216, 230), 3,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)
                    tmp[i][j] = 0

                if(0 < event.key - 48 < 10):
                    # new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 3,
                    #          Horizental_diff, Vertical_diff, margin, bottom_margin)
                    if (event.key - 48 != tmp[i][j]):
                        new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 3,
                                 Horizental_diff, Vertical_diff, margin, bottom_margin)

                        if (event.key - 48) == solution_sudoko[i][j]:
                            draw_text(screen, str(event.key - 48),
                                      rects[9*i + j].center, GREEN)
                            # orginal_sudoko[i][j] = event.key - 48
                            tmp[i][j] = event.key - 48
                            tmp_color[i][j] = GREEN
                            new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 3,
                                     Horizental_diff, Vertical_diff, margin, bottom_margin)
                            draw_text(screen, str(tmp[i][j]),
                                      rects[9*i + j].center, tmp_color[i][j])

                            return totall_mistakes, tmp

                        else:
                            draw_text(screen, str(event.key - 48),
                                      rects[9*i + j].center, RED)

                            tmp[i][j] = event.key - 48
                            tmp_color[i][j] = RED
                            totall_mistakes += 1

                if(0 < event.key - 1073741922 + 10 < 10):
                    # new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 3,
                    #          Horizental_diff, Vertical_diff, margin, bottom_margin)

                    if (event.key - 1073741922 + 10 != tmp[i][j]):
                        new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 3,
                                 Horizental_diff, Vertical_diff, margin, bottom_margin)

                        if (event.key - 1073741922 + 10) == solution_sudoko[i][j]:
                            draw_text(screen, str(event.key - 1073741922 + 10),
                                      rects[9*i + j].center, GREEN)
                            # orginal_sudoko[i][j] = event.key - 1073741922 + 10
                            tmp[i][j] = event.key - 1073741922 + 10
                            tmp_color[i][j] = GREEN
                            new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 3,
                                     Horizental_diff, Vertical_diff, margin, bottom_margin)
                            draw_text(screen, str(tmp[i][j]),
                                      rects[9*i + j].center, tmp_color[i][j])

                            return totall_mistakes, tmp

                        else:
                            draw_text(screen, str(event.key - 1073741922 + 10),
                                      rects[9*i + j].center, RED)

                            tmp[i][j] = event.key - 1073741922 + 10
                            tmp_color[i][j] = RED
                            totall_mistakes += 1

            # print(i, j)
            if event.type == pygame.MOUSEBUTTONUP and is_valid(tmp, solution_sudoko):
                pos = pygame.mouse.get_pos()
                new_i, new_j = pos[1], pos[0]
                new_i, new_j = (
                    new_i-margin) // Vertical_diff, (new_j-margin) // Horizental_diff

                if(i != new_i or j != new_j):
                    new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 3,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)

                    totall_mistakes, tmp = insert(screen, pos, margin, Horizental_diff, Vertical_diff, bottom_margin,
                                                  tmp, solution_sudoko, rects,  totall_mistakes)

                    return totall_mistakes, tmp


def add_grid(screen):
    margin = Width // 80
    bottom_margin = 15 * margin

    Horizental_diff = (Width - 2 * margin) // 9
    Vertical_diff = (Height - margin - bottom_margin) // 9

    add_lines(screen, Horizental_diff, Vertical_diff, margin, bottom_margin)

    Rects = []
    for i in range(9):
        for j in range(9):
            Rects.append(pygame.Rect(margin + (j*Horizental_diff),
                         margin + (i*Vertical_diff), Horizental_diff, Vertical_diff))

    [pygame.draw.rect(screen, BLACK, r, 1) for r in Rects]
    pygame.display.update()

    orginal_sudoko, solution_sudoko = add_sudoko_table(screen, Horizental_diff,
                                                       Vertical_diff, margin, Rects, bottom_margin)

    return orginal_sudoko, solution_sudoko, margin, Horizental_diff, Vertical_diff, bottom_margin, Rects


def add_sudoko_table(screen, Horizental_diff, Vertical_diff, margin, rects, bottom_margin):

    sudoku = generators.random_sudoku(avg_rank=20)  # Generate a Sudoku
    sudoku_np_array = np.array(list(str(sudoku)), dtype=int).reshape(9, 9)

    for i in range(len(sudoku_np_array)):
        for j in range(len(sudoku_np_array)):
            if (0 < sudoku_np_array[i][j] < 10):

                new_rect(screen, rects[i*9 + j], BLACK,
                         "#FFE4E1", 3, Horizental_diff, Vertical_diff, margin, bottom_margin)
                draw_text(screen, str(
                    sudoku_np_array[i][j]), rects[i*9 + j].center, Orginal_Sudoko_number_color)

                sleep(0.008)
                pygame.display.update()

    solution = solvers.backtrack(sudoku)  # Solve a Sudoku
    sudoku_solution_np_array = np.array(
        list(str(solution)), dtype=int).reshape(9, 9)

    return sudoku_np_array, sudoku_solution_np_array

    # print(renderers.colorful(solution))  # Print Solved Sudoku

    # sudoku.update(  # Update Sudoku
    #     Sudoku.from_list(
    #         sudoku_np_array.tolist(),
    #         box_size=BoxSize(3, 3),
    #     ).cells()
    # )


def is_valid(tmp, solution):
    for i in range(9):
        for j in range(9):
            if tmp[i][j] != 0 and tmp[i, j] != solution[i, j]:
                return False

    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("SUDOKU")
    screen.fill(background_color)
    pygame.display.update()

    # myfont = pygame.font.SysFont('Comic Sans MS', 70)

    orginal_sudoko, solution_sudoko, margin, Horizental_diff, Vertical_diff, bottom_margin, rects = add_grid(
        screen)

    # current_mistake = 0
    totall_mistakes = 0
    tmp = orginal_sudoko.copy()
    # add_sudoko_table(screen, myfont)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if totall_mistakes < 3:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if (margin < pos[1] < Height - bottom_margin) and (margin < pos[0] < Width - margin):
                        totall_mistakes, tmp = insert(screen, pos, margin, Horizental_diff, Vertical_diff,
                                                      bottom_margin, tmp, solution_sudoko, rects,
                                                      totall_mistakes)
                        tmp = tmp
            else:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
