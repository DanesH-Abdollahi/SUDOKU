import pygame
import sys
from dokusan import generators, renderers, solvers
from dokusan.boards import BoxSize, Sudoku
import numpy as np
from time import process_time_ns, sleep, time
from pygame.rect import *
import pygame_menu
import pygame_menu.themes
from typing import Tuple, Any


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

Margin = Width // 80

Button_Border = 0
Button_Width = int(Width / 5)
Button_Height = int(Height * 3 / 40)
Horizontal_Space_Between_Buttons = int(Width / 40)
Vertical_Space_Between_Buttons = int(Height / 80)
New_Game = {
    "left": Margin,
    "top": Height
    - Margin
    - Button_Border * 4
    - Button_Height * 2
    - Vertical_Space_Between_Buttons,
    "width": Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#7678ed",
    "color_active": "#3d348b",
    "border_color": background_color,
    "text": "New Game",
    "text_color_inactive": "#000000",
    "text_color_active": "#ffffff",
    "font": "FORTE.ttf",
    "font_size": 30,
}
Restart_Game = {
    "left": Margin,
    "top": Height - Margin - Button_Border * 2 - Button_Height,
    "width": Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#ff4d6d",
    "color_active": "#800f2f",
    "border_color": background_color,
    "text": "Restart",
    "text_color_inactive": "#000000",
    "text_color_active": "#ffffff",
    "font": "FORTE.ttf",
    "font_size": 30,
}
Hint = {
    "left": Margin
    + Button_Border * 2
    + Button_Width
    + Horizontal_Space_Between_Buttons,
    "top": Height
    - Margin
    - Button_Border * 4
    - Button_Height * 2
    - Vertical_Space_Between_Buttons,
    "width": Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#06d6a0",
    "color_active": "#2c6e49",
    "border_color": background_color,
    "text": "Hint",
    "text_color_inactive": "#000000",
    "text_color_active": "#ffffff",
    "font": "FORTE.ttf",
    "font_size": 30,
}
Screen_Shot = {
    "left": Margin
    + Button_Border * 2
    + Button_Width
    + Horizontal_Space_Between_Buttons,
    "top": Height - Margin - Button_Border * 2 - Button_Height,
    "width": Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#ffb700",
    "color_active": "#eb5e28",
    "border_color": background_color,
    "text": "Screen Shot",
    "text_color_inactive": "#000000",
    "text_color_active": "#ffffff",
    "font": "FORTE.ttf",
    "font_size": 30,
}

Time_Elapsed = {
    "left":  Margin,
    "top": Height
    - Margin
    - Button_Border * 6
    - Button_Height * 3
    - Vertical_Space_Between_Buttons * 2,
    "width": 2 * Button_Width + Horizontal_Space_Between_Buttons,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#6c757d",
    "color_active": "#",
    "border_color": background_color,
    "text": "",
    "text_color_inactive": "#fefee3",
    "text_color_active": "#",
    "font": "FORTE.ttf",
    "font_size": 30,
}


def draw_button(Button_Name, screen,  mouse_over=0):

    left = Button_Name["left"]
    top = Button_Name["top"]
    width = Button_Name["width"]
    height = Button_Name["height"]
    border = Button_Name["border"]
    if mouse_over == 0:
        color = Button_Name["color_inactive"]
    else:
        color = Button_Name["color_active"]
    border_color = Button_Name["border_color"]
    text = Button_Name["text"]
    if mouse_over == 0:
        text_color = Button_Name["text_color_inactive"]
    else:
        text_color = Button_Name["text_color_active"]

    font = Button_Name["font"]
    font_size = Button_Name["font_size"]

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


def insert(screen, position, margin, Horizental_diff, Vertical_diff, bottom_margin,
           curr_sudoko_table, solution_sudoko, rects,  totall_mistakes, orginal_sudoko, hint_numbers, new_game_sound,
           ss_sound, res_sound, hint_sound, start):

    i, j = position[1], position[0]

    i, j = (i-margin) // Vertical_diff, (j-margin) // Horizental_diff

    tmp = curr_sudoko_table.copy()
    tmp_color = np.zeros((9, 9), dtype=tuple)

    if i > 8 or j > 8:
        return totall_mistakes, tmp, hint_numbers

    if (tmp[i][j] != 0):
        return totall_mistakes, tmp, hint_numbers

    new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 3,
             Horizental_diff, Vertical_diff, margin, bottom_margin)

    while True:

        elapsed = round(time() - start) - 1
        Time_Elapsed[
            "text"
        ] = f"Elapsed Time: {(elapsed // 60)//60 } : {elapsed // 60 } : {elapsed % 60}"
        time_elapsed_btn = draw_button(
            Time_Elapsed, screen=screen
        )

        if totall_mistakes >= 3:
            pygame.quit()
            sys.exit()

        new_game_btn = draw_button(New_Game, screen=screen)
        restart_game_btn = draw_button(Restart_Game, screen=screen)
        hint_btn = draw_button(Hint, screen=screen)
        screen_shot_btn = draw_button(Screen_Shot, screen=screen)

        if new_game_btn.collidepoint(pygame.mouse.get_pos()):
            new_game_btn = draw_button(New_Game, mouse_over=1, screen=screen)
        elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
            restart_game_btn = draw_button(
                Restart_Game, mouse_over=1, screen=screen)
        elif hint_btn.collidepoint(pygame.mouse.get_pos()):
            hint_btn = draw_button(Hint, mouse_over=1, screen=screen)
        elif screen_shot_btn.collidepoint(pygame.mouse.get_pos()):
            screen_shot_btn = draw_button(
                Screen_Shot, mouse_over=1, screen=screen)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if hint_btn.collidepoint(pygame.mouse.get_pos()) and hint_numbers < 3:
                    hint_btn = draw_button(Hint, screen=screen)
                    pygame.display.flip()
                    sleep(0.1)
                    # hint_sound = pygame.mixer.Sound("Hint.wav")
                    hint_sound.play()

                    tmp = hint_func(screen, position, tmp, solution_sudoko,
                                    rects, Horizental_diff, Vertical_diff)

                    hint_numbers += 1

                    tmp_color[i][j] = GREEN
                    new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 3,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)
                    draw_text(screen, str(tmp[i][j]),
                              rects[9*i + j].center, tmp_color[i][j])

                    return totall_mistakes, tmp, hint_numbers

                elif new_game_btn.collidepoint(pygame.mouse.get_pos()):
                    new_game_btn = draw_button(New_Game, screen=screen)
                    pygame.display.flip()
                    new_game_sound.play()
                    sleep(0.1)
                    main()

                elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
                    restart_game_btn = draw_button(Restart_Game, screen=screen)
                    pygame.display.flip()
                    res_sound.play()
                    sleep(0.1)
                    main(orginal_sudoko)

                elif screen_shot_btn.collidepoint(pygame.mouse.get_pos()):
                    screen_shot_btn = draw_button(Screen_Shot, screen=screen)
                    pygame.display.flip()
                    # ss_sound = pygame.mixer.Sound("ScreenShot.wav")
                    ss_sound.play()
                    pygame.image.save(screen, "ScreenShot.jpg")
                    sleep(0.1)

            if event.type == pygame.KEYDOWN:
                if (curr_sudoko_table[i][j] != 0):
                    return totall_mistakes, tmp, hint_numbers

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

                            return totall_mistakes, tmp, hint_numbers

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

                            return totall_mistakes, tmp, hint_numbers

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

                    totall_mistakes, tmp, hint_numbers = insert(screen, pos, margin, Horizental_diff, Vertical_diff, bottom_margin,
                                                                tmp, solution_sudoko, rects,  totall_mistakes,
                                                                orginal_sudoko, hint_numbers, new_game_sound,
                                                                ss_sound, res_sound, hint_sound, start)

                    return totall_mistakes, tmp, hint_numbers


def add_grid(screen, difficulty, initial_sudoko=np.zeros((9, 9), dtype=int)):
    margin = Width // 80
    # bottom_margin = 15 * margin

    bottom_margin = Margin + 3 * Button_Height + 6 * \
        Button_Border + 3 * Vertical_Space_Between_Buttons

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
                                                       Vertical_diff, margin, Rects, bottom_margin, difficulty, initial_sudoko)

    return orginal_sudoko, solution_sudoko, margin, Horizental_diff, Vertical_diff, bottom_margin, Rects


def add_sudoko_table(screen, Horizental_diff, Vertical_diff, margin, rects, bottom_margin, difficulty, initial_sudoko=np.zeros((9, 9), dtype=int)):

    if difficulty == 1:
        sudoku = generators.random_sudoku(avg_rank=25)
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
                         "#FFE4E1", 3, Horizental_diff, Vertical_diff, margin, bottom_margin)
                draw_text(screen, str(
                    sudoku_np_array[i][j]), rects[i*9 + j].center, Orginal_Sudoko_number_color)

                sleep(0.008)
                pygame.display.update()

    solution = solvers.backtrack(sudoku)  # Solve a Sudoku
    sudoku_solution_np_array = np.array(
        list(str(solution)), dtype=int).reshape(9, 9)

    return sudoku_np_array, sudoku_solution_np_array


def is_valid(tmp, solution):
    for i in range(9):
        for j in range(9):
            if tmp[i][j] != 0 and tmp[i, j] != solution[i, j]:
                return False

    return True


def hint_func(screen, position, temp, solution, rects, Horizental_diff, Vertical_diff):

    font = pygame.font.SysFont('Comic Sans MS', 70)
    i, j = position[1], position[0]
    i, j = (i-Margin) // Vertical_diff, (j-Margin) // Horizental_diff

    if i > 8 or j > 8:
        return temp

    if(temp[i, j] != 0):
        return temp

    pos = rects[9*i + j].center
    text = str(solution[i, j])
    temp[i, j] = solution[i, j]
    img = font.render(text, True, GREEN)
    pos = img.get_rect(center=pos)
    screen.blit(img, pos)
    pygame.display.update()

    return temp


def main(initial_sudoko=np.zeros((9, 9), dtype=int),):
    # size = SIZE
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

    ss_sound = pygame.mixer.Sound("ScreenShot.wav")
    new_game_sound = pygame.mixer.Sound("NewGame.wav")
    res_sound = pygame.mixer.Sound("ResSound.wav")
    hint_sound = pygame.mixer.Sound("Hint.wav")

    def start_the_game(difficulty=1):
        print(difficulty)
        size = SIZE
        # pygame.init()
        # pygame.mixer.init()

        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption("SUDOKU")
        screen.fill(background_color)
        pygame.display.update()
        start = time()

        orginal_sudoko, solution_sudoko, margin, Horizental_diff, Vertical_diff, bottom_margin, rects = add_grid(
            screen,  difficulty, initial_sudoko)

        totall_mistakes = 0
        hint_numbers = 0
        tmp = orginal_sudoko.copy()

        while True:

            elapsed = round(time() - start) - 1
            Time_Elapsed[
                "text"
            ] = f"Elapsed Time: {(elapsed // 60)//60 } : {elapsed // 60 } : {elapsed % 60}"
            time_elapsed_btn = draw_button(
                Time_Elapsed, screen=screen
            )

            new_game_btn = draw_button(New_Game, screen=screen)
            restart_game_btn = draw_button(Restart_Game, screen=screen)
            hint_btn = draw_button(Hint, screen=screen)
            screen_shot_btn = draw_button(Screen_Shot, screen=screen)

            if new_game_btn.collidepoint(pygame.mouse.get_pos()):
                new_game_btn = draw_button(
                    New_Game, mouse_over=1, screen=screen)
            elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
                restart_game_btn = draw_button(
                    Restart_Game, mouse_over=1, screen=screen)
            elif hint_btn.collidepoint(pygame.mouse.get_pos()):
                hint_btn = draw_button(Hint, mouse_over=1, screen=screen)
            elif screen_shot_btn.collidepoint(pygame.mouse.get_pos()):
                screen_shot_btn = draw_button(
                    Screen_Shot, mouse_over=1, screen=screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if event.type == pygame.VIDEORESIZE:
                #     # screen = pygame.display.set_mode(
                #     #     (event.w, event.h), pygame.RESIZABLE)

                #     new_size = (event.w, event.h)
                #     main(_size=new_size)
                #     # pygame.display.update()

                if totall_mistakes < 3:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        pos = pygame.mouse.get_pos()

                        if (margin < pos[1] < Height - bottom_margin) and (margin < pos[0] < Width - margin):
                            totall_mistakes, tmp, hint_numbers = insert(screen, pos, margin, Horizental_diff, Vertical_diff,
                                                                        bottom_margin, tmp, solution_sudoko, rects,
                                                                        totall_mistakes,  orginal_sudoko, hint_numbers, new_game_sound,
                                                                        ss_sound, res_sound, hint_sound, start)
                            tmp = tmp

                        elif new_game_btn.collidepoint(pygame.mouse.get_pos()):
                            new_game_btn = draw_button(New_Game, screen=screen)
                            pygame.display.flip()
                            new_game_sound.play()
                            sleep(0.1)
                            main()

                        elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
                            restart_game_btn = draw_button(
                                Restart_Game, screen=screen)
                            pygame.display.flip()
                            res_sound.play()
                            sleep(0.1)
                            main(orginal_sudoko)

                        elif screen_shot_btn.collidepoint(pygame.mouse.get_pos()):
                            screen_shot_btn = draw_button(
                                Screen_Shot, screen=screen)
                            pygame.display.flip()
                            ss_sound.play()
                            pygame.image.save(screen, "ScreenShot.jpg")
                            sleep(0.1)

                else:

                    # pygame.display.set_caption("SUDOKU")
                    # game_over_screen.fill(CYAN)
                    # pygame.display.update()

                    # while True:
                    #     for event in pygame.event.get():
                    #         pass

                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

    if initial_sudoko.tolist() != np.zeros((9, 9), dtype=int).tolist():
        start_the_game()

    def play_buttom():
        global Difficulty
        res_sound.play()
        start_the_game(Difficulty)

    def set_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
        global Difficulty
        selected = value[0]
        Difficulty = int(selected[1])

    menu = pygame_menu.Menu(
        "Welcome", SIZE[0], SIZE[1], theme=pygame_menu.themes.THEME_SOLARIZED)
    # menu.add.text_input("Name :", default="John Doe")

    s = menu.add.selector(
        "Difficulty :", [("Easy", 1), ("Medium", 2), ("Hard", 3)], onchange=set_difficulty)

    s.set_onselect(set_difficulty(s.get_value(), s.get_index()))

    menu.add.button("Play",  play_buttom)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.display.update()


if __name__ == "__main__":
    main()
