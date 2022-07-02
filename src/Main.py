import sys
from time import sleep, time
from pygame.rect import *
from typing import Tuple, Any
import easygui
from DrawFuntions import *
from GameFunctions import *


def insert(screen, position, margin, Horizental_diff, Vertical_diff, bottom_margin,
           curr_sudoko_table, solution_sudoko, rects,  totall_mistakes, orginal_sudoko, hint_numbers, new_game_sound,
           ss_sound, res_sound, hint_sound, start, correct_sound, mistake_sound, is_muted):

    i, j = position[1], position[0]

    i, j = (i-margin) // Vertical_diff, (j-margin) // Horizental_diff

    tmp = curr_sudoko_table.copy()
    tmp_color = np.zeros((9, 9), dtype=tuple)

    if i > 8 or j > 8:
        return totall_mistakes, tmp, hint_numbers, is_muted

    if (tmp[i][j] != 0):
        return totall_mistakes, tmp, hint_numbers, is_muted

    new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 1,
             Horizental_diff, Vertical_diff, margin, bottom_margin)

    while True:

        elapsed = round(time() - start) - 1
        Time_Elapsed[
            "text"
        ] = f"Elapsed Time: {(elapsed // 60)//60 } : {elapsed // 60 } : {elapsed % 60}"
        draw_button(
            Time_Elapsed, screen=screen
        )

        if totall_mistakes >= 3:
            Errors_Happened[
                "text"
            ] = f"Total Mistakes : {totall_mistakes}"
            draw_button(
                Errors_Happened, screen=screen
            )
            pygame.display.update()
            return totall_mistakes, tmp, hint_numbers, is_muted

        Errors_Happened[
            "text"
        ] = f"Total Mistakes : {totall_mistakes}"
        draw_button(
            Errors_Happened, screen=screen
        )

        Remaining_Hints_Num = 3 - hint_numbers
        if Remaining_Hints_Num == 0:
            hint_btn = draw_button(Hint, screen=screen, mouse_over=1)
            Remaining_Hints["text_color_inactive"] = RED
        else:
            hint_btn = draw_button(Hint, screen=screen)
            Remaining_Hints["text_color_inactive"] = "#003566"
        draw_button(Remaining_Hints, screen=screen)

        new_game_btn = draw_button(New_Game, screen=screen)
        restart_game_btn = draw_button(Restart_Game, screen=screen)
        screen_shot_btn = draw_button(Screen_Shot, screen=screen)
        mute_btn = draw_button(Mute, screen=screen)

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
                    if Remaining_Hints_Num != 0:
                        hint_btn = draw_button(Hint, screen=screen)
                        Remaining_Hints["text_color_inactive"] = "#003566"
                    Remaining_Hints_Num = 2 - hint_numbers
                    if Remaining_Hints_Num == 0:
                        hint_btn = draw_button(
                            Hint, screen=screen, mouse_over=1)
                        Remaining_Hints["text_color_inactive"] = RED
                    Remaining_Hints["text"] = f"Remaining Hints: {Remaining_Hints_Num}"
                    remaining_hints_btn = draw_button(
                        Remaining_Hints, screen=screen)

                    pygame.display.flip()
                    sleep(0.1)
                    if not(is_muted):
                        hint_sound.play()

                    tmp = hint_func(screen, position, tmp, tmp_color,  solution_sudoko,
                                    rects, Horizental_diff, Vertical_diff)

                    hint_numbers += 1

                    tmp_color[i][j] = GREEN
                    new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 1,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)
                    draw_text(screen, str(tmp[i][j]),
                              rects[9*i + j].center, tmp_color[i][j])

                    return totall_mistakes, tmp, hint_numbers, is_muted

                elif new_game_btn.collidepoint(pygame.mouse.get_pos()):
                    new_game_btn = draw_button(New_Game, screen=screen)
                    pygame.display.flip()
                    if not(is_muted):
                        new_game_sound.play()
                    sleep(0.1)

                    main()

                elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
                    restart_game_btn = draw_button(Restart_Game, screen=screen)
                    pygame.display.flip()
                    if not(is_muted):
                        res_sound.play()
                    sleep(0.1)
                    main(orginal_sudoko)

                elif screen_shot_btn.collidepoint(pygame.mouse.get_pos()):
                    screen_shot_btn = draw_button(Screen_Shot, screen=screen)
                    pygame.display.flip()
                    if not(is_muted):
                        ss_sound.play()

                    file = easygui.filesavebox(
                        title="Browser",
                        msg="Select a folder:",
                        filetypes=["*.jpg"],
                        default="Sudoku Screenshot",
                    )
                    if file != None:
                        pygame.image.save(screen, f"{file}.jpg")
                    sleep(0.1)

                elif mute_btn.collidepoint(pygame.mouse.get_pos()):
                    is_muted = not (is_muted)
                    if is_muted == 1:
                        Mute["text"] = "Muted"
                        Mute["color_inactive"] = "#ee4266"
                        Mute["text_color_inactive"] = "#ffd500"
                        mute_btn = draw_button(
                            Mute, screen=screen
                        )
                    elif is_muted == 0:
                        Mute["text"] = "Unmuted"
                        Mute["color_inactive"] = "#2ec4b6"
                        Mute["text_color_inactive"] = "#560bad"
                        mute_btn = draw_button(Mute, screen=screen)

            if event.type == pygame.KEYDOWN:
                if (curr_sudoko_table[i][j] != 0):
                    return totall_mistakes, tmp, hint_numbers, is_muted

                if(event.key == 8):
                    new_rect(screen, rects[9*i + j], BLACK,  (173, 216, 230), 1,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)
                    tmp[i][j] = 0

                if(0 < event.key - 48 < 10):
                    if (event.key - 48 != tmp[i][j]):
                        new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 1,
                                 Horizental_diff, Vertical_diff, margin, bottom_margin)

                        if (event.key - 48) == solution_sudoko[i][j]:
                            if not(is_muted):
                                correct_sound.play()
                            draw_text(screen, str(event.key - 48),
                                      rects[9*i + j].center, GREEN)
                            tmp[i][j] = event.key - 48
                            tmp_color[i][j] = GREEN
                            new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 1,
                                     Horizental_diff, Vertical_diff, margin, bottom_margin)
                            draw_text(screen, str(tmp[i][j]),
                                      rects[9*i + j].center, tmp_color[i][j])

                            return totall_mistakes, tmp, hint_numbers, is_muted

                        else:
                            draw_text(screen, str(event.key - 48),
                                      rects[9*i + j].center, RED)

                            tmp[i][j] = event.key - 48
                            tmp_color[i][j] = RED
                            totall_mistakes += 1
                            if totall_mistakes < 3:
                                if not(is_muted):
                                    mistake_sound.play()

                if(0 < event.key - 1073741922 + 10 < 10):
                    if (event.key - 1073741922 + 10 != tmp[i][j]):
                        new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 1,
                                 Horizental_diff, Vertical_diff, margin, bottom_margin)

                        if (event.key - 1073741922 + 10) == solution_sudoko[i][j]:
                            if not(is_muted):
                                correct_sound.play()
                            draw_text(screen, str(event.key - 1073741922 + 10),
                                      rects[9*i + j].center, GREEN)
                            tmp[i][j] = event.key - 1073741922 + 10
                            tmp_color[i][j] = GREEN
                            new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 1,
                                     Horizental_diff, Vertical_diff, margin, bottom_margin)
                            draw_text(screen, str(tmp[i][j]),
                                      rects[9*i + j].center, tmp_color[i][j])

                            return totall_mistakes, tmp, hint_numbers, is_muted

                        else:
                            draw_text(screen, str(event.key - 1073741922 + 10),
                                      rects[9*i + j].center, RED)

                            tmp[i][j] = event.key - 1073741922 + 10
                            tmp_color[i][j] = RED
                            totall_mistakes += 1
                            if totall_mistakes < 3:
                                if not(is_muted):
                                    mistake_sound.play()

            if event.type == pygame.MOUSEBUTTONUP and is_valid(tmp, solution_sudoko):
                pos = pygame.mouse.get_pos()
                new_i, new_j = pos[1], pos[0]
                new_i, new_j = (
                    new_i-margin) // Vertical_diff, (new_j-margin) // Horizental_diff

                if(i != new_i or j != new_j):
                    new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 1,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)

                    totall_mistakes, tmp, hint_numbers, is_muted = insert(screen, pos, margin, Horizental_diff, Vertical_diff, bottom_margin,
                                                                          tmp, solution_sudoko, rects,  totall_mistakes,
                                                                          orginal_sudoko, hint_numbers, new_game_sound,
                                                                          ss_sound, res_sound, hint_sound, start, correct_sound, mistake_sound, is_muted)

                    return totall_mistakes, tmp, hint_numbers, is_muted


def game_over(screen, orginal_sudoku, is_muted):
    menu = pygame_menu.Menu(
        "Game Over", SIZE[0], SIZE[1], theme=My_theme)

    def reset():
        if not(is_muted):
            res_sound.play()
        main(orginal_sudoku)

    def play():
        main()

    menu.add.button("Play", play)
    menu.add.button("Reset", reset)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.display.update()


def sudoku_solved(screen):
    menu = pygame_menu.Menu(
        "Congratulations !", SIZE[0], SIZE[1], theme=My_theme)

    def play():
        main()

    menu.add.button("Play", play)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.display.update()


def start_the_game(initial_sudoko, is_muted, difficulty=1):

    size = SIZE
    screen = pygame.display.set_mode(size, pygame.HWSURFACE)
    pygame.display.set_caption("SUDOKU")
    screen.fill(background_color)
    pygame.display.update()
    start = time()

    orginal_sudoko, solution_sudoko, margin, Horizental_diff, Vertical_diff, bottom_margin, rects = add_grid(
        screen,  difficulty, initial_sudoko)

    totall_mistakes = 0
    hint_numbers = 0
    tmp = orginal_sudoko.copy()

    Remaining_Hints_Num = 3
    Remaining_Hints["text"] = f"Remaining Hints: {Remaining_Hints_Num}"
    draw_button(Remaining_Hints, screen=screen)

    while True:

        elapsed = round(time() - start) - 1
        Time_Elapsed[
            "text"
        ] = f"Elapsed Time: {(elapsed // 60)//60 } : {elapsed // 60 } : {elapsed % 60}"
        draw_button(
            Time_Elapsed, screen=screen
        )

        Errors_Happened[
            "text"
        ] = f"Total Mistakes : {totall_mistakes}"
        draw_button(
            Errors_Happened, screen=screen
        )

        new_game_btn = draw_button(New_Game, screen=screen)
        restart_game_btn = draw_button(Restart_Game, screen=screen)
        screen_shot_btn = draw_button(Screen_Shot, screen=screen)
        mute_btn = draw_button(Mute, screen=screen)
        draw_button(Remaining_Hints, screen=screen)
        Remaining_Hints_Num = 3 - hint_numbers
        if Remaining_Hints_Num == 0:
            hint_btn = draw_button(Hint, screen=screen, mouse_over=1)
            Remaining_Hints["text_color_inactive"] = RED
        else:
            hint_btn = draw_button(Hint, screen=screen)
            Remaining_Hints["text_color_inactive"] = "#003566"

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

        if is_solved(tmp, solution_sudoko):
            if not(is_muted):
                win_sound.play()
            sleep(1)
            sudoku_solved(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if totall_mistakes < 3:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if (margin < pos[1] < Height - bottom_margin) and (margin < pos[0] < Width - margin):
                        totall_mistakes, tmp, hint_numbers, is_muted = insert(screen, pos, margin, Horizental_diff, Vertical_diff,
                                                                              bottom_margin, tmp, solution_sudoko, rects,
                                                                              totall_mistakes,  orginal_sudoko, hint_numbers, new_game_sound,
                                                                              ss_sound, res_sound, hint_sound, start, correct_sound,
                                                                              mistake_sound, is_muted)
                        tmp = tmp

                    elif new_game_btn.collidepoint(pygame.mouse.get_pos()):
                        new_game_btn = draw_button(New_Game, screen=screen)
                        pygame.display.flip()
                        if not(is_muted):
                            new_game_sound.play()
                        sleep(0.1)
                        main()

                    elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
                        restart_game_btn = draw_button(
                            Restart_Game, screen=screen)
                        pygame.display.flip()
                        if not(is_muted):
                            res_sound.play()
                        sleep(0.1)
                        main(orginal_sudoko)

                    elif screen_shot_btn.collidepoint(pygame.mouse.get_pos()):
                        screen_shot_btn = draw_button(
                            Screen_Shot, screen=screen)
                        pygame.display.flip()
                        if not(is_muted):
                            ss_sound.play()
                        file = easygui.filesavebox(
                            title="Browser",
                            msg="Select a folder:",
                            filetypes=["*.jpg"],
                            default="Sudoku Screenshot",
                        )
                        if file != None:
                            pygame.image.save(screen, f"{file}.jpg")
                        sleep(0.1)

                    elif mute_btn.collidepoint(pygame.mouse.get_pos()):
                        is_muted = not (is_muted)
                        if is_muted == 1:
                            Mute["text"] = "Muted"
                            Mute["color_inactive"] = "#ee4266"
                            Mute["text_color_inactive"] = "#ffd500"
                            mute_btn = draw_button(
                                Mute, screen=screen
                            )
                        elif is_muted == 0:
                            Mute["text"] = "Unmuted"
                            Mute["color_inactive"] = "#2ec4b6"
                            Mute["text_color_inactive"] = "#560bad"
                            mute_btn = draw_button(Mute, screen=screen)

            else:
                if not(is_muted):
                    gameover_sound.play()
                sleep(1)
                game_over(screen, orginal_sudoko, is_muted)

        pygame.display.flip()


def main(initial_sudoko=np.zeros((9, 9), dtype=int)):
    is_muted = 0
    Mute["text"] = "Unmuted"
    Mute["color_inactive"] = "#2ec4b6"
    Mute["text_color_inactive"] = "#560bad"
    Remaining_Hints["text_color_inactive"] = "#003566"

    # initiale the screen
    screen = screen_init()

    # For Reset The Game
    if initial_sudoko.tolist() != np.zeros((9, 9), dtype=int).tolist():
        start_the_game(initial_sudoko, is_muted)

    # Define Callbacks for Menu Bottoms
    def play_buttom():
        global Difficulty
        if not(is_muted):
            res_sound.play()
        start_the_game(initial_sudoko, is_muted, difficulty=Difficulty)

    def set_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
        global Difficulty
        selected = value[0]
        Difficulty = int(selected[1])

    # The First Menu
    menu = pygame_menu.Menu(
        "Welcome", SIZE[0], SIZE[1], theme=My_theme)

    s = menu.add.selector(
        "Difficulty :", [("Easy", 1), ("Medium", 2), ("Hard", 3)], onchange=set_difficulty)
    s.set_onselect(set_difficulty(s.get_value(), s.get_index()))
    menu.add.button("Play",  play_buttom)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.display.update()


if __name__ == "__main__":
    main()
