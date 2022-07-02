from InitialValues import *
from dokusan import generators, solvers
from dokusan.boards import BoxSize, Sudoku
from time import sleep
import numpy as np


# draw a button with specific properties
def draw_button(Button_Name, screen,  mouse_over=0):
    left, top, width, height, border, border_color, text, font, font_size = Button_Name["left"], Button_Name["top"], Button_Name["width"], Button_Name[
        "height"], Button_Name["border"], Button_Name["border_color"], Button_Name["text"], Button_Name["font"], Button_Name["font_size"]

    if mouse_over == 0:
        color = Button_Name["color_inactive"]
    else:
        color = Button_Name["color_active"]

    if mouse_over == 0:
        text_color = Button_Name["text_color_inactive"]
    else:
        text_color = Button_Name["text_color_active"]

    pygame.draw.rect(
        screen,
        border_color,
        (left, top, width + border * 2, height + border * 2),
    )

    button = pygame.Rect(left + border, top + border, width, height)
    pygame.draw.rect(screen, color, button, 0, 30)
    font = pygame.font.Font(font, font_size)
    text = font.render(text, True, text_color)
    xpos, ypos = button.center
    textbox = text.get_rect(center=(xpos, ypos))
    screen.blit(text, textbox)
    return button


# draw new rects
def new_rect(screen, rect, border_color, inner_color, border, Horizental_diff, Vertical_diff, Margin, bottom_Margin):
    pygame.draw.rect(
        screen,
        border_color,
        (rect.left, rect.top, Horizental_diff +
         border, Vertical_diff + border), border
    )

    inner = pygame.Rect(rect.left + border, rect.top +
                        border, Horizental_diff - border, Vertical_diff - border)
    pygame.draw.rect(screen, inner_color, inner)
    add_lines(screen, Horizental_diff, Vertical_diff, Margin, bottom_Margin)
    pygame.display.update()


# draw table lines
def add_lines(screen, Horizental_diff, Vertical_diff, Margin, bottom_Margin):
    for i in range(10):
        if(i % 3 == 0):
            pygame.draw.line(
                screen,
                BLACK,
                (Margin + Horizental_diff * i, Margin),
                (Margin + Horizental_diff * i, Height - bottom_Margin),
                5,
            )  # Draw Vertical Lines
            if i == 9:

                pygame.draw.line(
                    screen,
                    BLACK,
                    (Margin, Height - bottom_Margin),
                    (Margin + Horizental_diff * 9, Height - bottom_Margin),
                    5,)  # Draw Horizental Lines
            else:
                pygame.draw.line(
                    screen,
                    BLACK,
                    (Margin, Margin + Vertical_diff * i),
                    (Margin + Horizental_diff * 9, Margin + Vertical_diff * i),
                    5,)  # Draw Horizental Lines

        pygame.draw.line(
            screen,
            BLACK,
            (Margin + Horizental_diff * i, Margin),
            (Margin + Horizental_diff * i, Height - bottom_Margin),
            3,
        )  # Draw Vertical Lines

        pygame.draw.line(
            screen,
            BLACK,
            (Margin, Margin + Vertical_diff * i),
            (Margin + Horizental_diff * 9, Margin + Vertical_diff * i),
            3,
        )  # Draw Horizental Lines

    pygame.display.update()


# draw text in a specifi Position
def draw_text(screen, text, pos, color):
    font = pygame.font.SysFont('Comic Sans MS', 50)
    img = font.render(text, True, color)
    pos = img.get_rect(center=pos)
    screen.blit(img, pos)
    pygame.display.update()


# draw girds & Define a rect list which contains all cells as a rect
def add_grid(screen, difficulty, initial_sudoko=np.zeros((9, 9), dtype=int)):
    bottom_Margin = Margin + 3 * Button_Height + 6 * \
        Button_Border + 3 * Vertical_Space_Between_Buttons
    Horizental_diff = (Width - 2 * Margin) // 9
    Vertical_diff = (Height - Margin - bottom_Margin) // 9
    add_lines(screen, Horizental_diff, Vertical_diff, Margin, bottom_Margin)
    Rects = []
    for i in range(9):
        for j in range(9):
            Rects.append(pygame.Rect(Margin + (j*Horizental_diff),
                         Margin + (i*Vertical_diff), Horizental_diff, Vertical_diff))

    [pygame.draw.rect(screen, BLACK, r, 1) for r in Rects]
    pygame.display.update()

    orginal_sudoko, solution_sudoko = add_sudoku_table(screen, Horizental_diff,
                                                       Vertical_diff, Margin, Rects, bottom_Margin, difficulty, initial_sudoko)

    return orginal_sudoko, solution_sudoko, Margin, Horizental_diff, Vertical_diff, bottom_Margin, Rects


# Generate Sudoku
def add_sudoku_table(screen, Horizental_diff, Vertical_diff, Margin, rects, bottom_Margin, difficulty, initial_sudoko=np.zeros((9, 9), dtype=int)):
    if difficulty == 1:
        sudoku = generators.random_sudoku(avg_rank=5)
    elif difficulty == 2:
        sudoku = generators.random_sudoku(avg_rank=70)
    elif difficulty == 3:
        sudoku = generators.random_sudoku(avg_rank=130)

    if initial_sudoko.tolist() != np.zeros((9, 9), dtype=int).tolist():
        sudoku.update(  # Update Sudoku
            Sudoku.from_list(
                initial_sudoko.tolist(),
                box_size=BoxSize(3, 3),
            ).cells()
        )

    sudoku_np_array = np.array(list(str(sudoku)), dtype=int).reshape(9, 9)

    for i in range(len(sudoku_np_array)):
        for j in range(len(sudoku_np_array)):
            if (0 < sudoku_np_array[i][j] < 10):

                new_rect(screen, rects[i*9 + j], BLACK,
                         "#FFE4E1", 1, Horizental_diff, Vertical_diff, Margin, bottom_Margin)
                draw_text(screen, str(
                    sudoku_np_array[i][j]), rects[i*9 + j].center, Orginal_Sudoko_number_color)
                sleep(0.008)
                pygame.display.update()

    solution = solvers.backtrack(sudoku)  # Solve a Sudoku
    sudoku_solution_np_array = np.array(
        list(str(solution)), dtype=int).reshape(9, 9)

    return sudoku_np_array, sudoku_solution_np_array
