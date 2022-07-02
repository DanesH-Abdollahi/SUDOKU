import sys
from time import sleep, time
from pygame.rect import *
from typing import Tuple, Any
import easygui
from DrawFuntions import *
from GameFunctions import *


# Define a function to insert numbers to cells
def insert(screen, position, margin, Horizental_diff, Vertical_diff, bottom_margin,
           curr_sudoko_table, solution_sudoko, rects,  totall_mistakes, orginal_sudoko, hint_numbers, new_game_sound,
           ss_sound, res_sound, hint_sound, start, correct_sound, mistake_sound, is_muted):

    i, j = position[1], position[0]
    i, j = (i-margin) // Vertical_diff, (j-margin) // Horizental_diff
    tmp_color = np.zeros((9, 9), dtype=tuple)

    # if input position is out of game table
    if i > 8 or j > 8:
        return totall_mistakes, curr_sudoko_table, hint_numbers, is_muted

    if (curr_sudoko_table[i][j] != 0):
        return totall_mistakes, curr_sudoko_table, hint_numbers, is_muted

    # Colorize The Selected Cell
    new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 1,
             Horizental_diff, Vertical_diff, margin, bottom_margin)

    while True:
        elapsed = round(time() - start) - 1
        Time_Elapsed["text"] = f"Elapsed Time: {(elapsed // 60)//60 } : {elapsed // 60 } : {elapsed % 60}"
        draw_button(Time_Elapsed, screen=screen)

        # Check The # of Totall Mistakes
        if totall_mistakes >= 3:
            Errors_Happened["text"] = f"Total Mistakes : {totall_mistakes}"
            draw_button(Errors_Happened, screen=screen)
            pygame.display.update()
            return totall_mistakes, curr_sudoko_table, hint_numbers, is_muted

        Errors_Happened["text"] = f"Total Mistakes : {totall_mistakes}"
        draw_button(Errors_Happened, screen=screen)

        Remaining_Hints_Num = 3 - hint_numbers
        # Check The # of Remaining Hints
        if Remaining_Hints_Num == 0:
            hint_btn = draw_button(Hint, screen=screen, mouse_over=1)
            Remaining_Hints["text_color_inactive"] = RED
        else:
            hint_btn = draw_button(Hint, screen=screen)
            Remaining_Hints["text_color_inactive"] = "#003566"
        draw_button(Remaining_Hints, screen=screen)

        # Draw Buttons
        new_game_btn = draw_button(New_Game, screen=screen)
        restart_game_btn = draw_button(Restart_Game, screen=screen)
        screen_shot_btn = draw_button(Screen_Shot, screen=screen)
        mute_btn = draw_button(Mute, screen=screen)

        # Check if The mouse cursor is over the specific bottun or not
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

        pygame.display.update()

        for event in pygame.event.get():
            # Check for the Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                # if the hint button is clicked
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
                    draw_button(Remaining_Hints, screen=screen)
                    pygame.display.update()
                    sleep(0.1)
                    if not(is_muted):
                        hint_sound.play()
                    curr_sudoko_table = hint_func(screen, position, curr_sudoko_table, tmp_color,  solution_sudoko,
                                                  rects, Horizental_diff, Vertical_diff)
                    hint_numbers += 1
                    tmp_color[i][j] = GREEN
                    new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 1,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)
                    draw_text(screen, str(curr_sudoko_table[i][j]),
                              rects[9*i + j].center, tmp_color[i][j])

                    return totall_mistakes, curr_sudoko_table, hint_numbers, is_muted

                # if the New Game button is clicked
                elif new_game_btn.collidepoint(pygame.mouse.get_pos()):
                    new_game_btn = draw_button(New_Game, screen=screen)
                    pygame.display.flip()
                    if not(is_muted):
                        new_game_sound.play()
                    sleep(0.1)
                    main()

                # if the Restart button is clicked
                elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
                    restart_game_btn = draw_button(Restart_Game, screen=screen)
                    pygame.display.flip()
                    if not(is_muted):
                        res_sound.play()
                    sleep(0.1)
                    main(orginal_sudoko)

                # if the ScreenShot button is clicked
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

                # if the Mute button is clicked
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
                # if the Back Space key pressed
                if(event.key == 8):
                    new_rect(screen, rects[9*i + j], BLACK,  (173, 216, 230), 1,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)
                    curr_sudoko_table[i][j] = 0

                # if the left numbers pressed
                if(0 < event.key - 48 < 10):
                    if (event.key - 48 != curr_sudoko_table[i][j]):
                        new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 1,
                                 Horizental_diff, Vertical_diff, margin, bottom_margin)

                        # if the input number is correct
                        if (event.key - 48) == solution_sudoko[i][j]:
                            if not(is_muted):
                                correct_sound.play()
                            draw_text(screen, str(event.key - 48),
                                      rects[9*i + j].center, GREEN)
                            curr_sudoko_table[i][j] = event.key - 48
                            tmp_color[i][j] = GREEN
                            new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 1,
                                     Horizental_diff, Vertical_diff, margin, bottom_margin)
                            draw_text(screen, str(curr_sudoko_table[i][j]),
                                      rects[9*i + j].center, tmp_color[i][j])
                            return totall_mistakes, curr_sudoko_table, hint_numbers, is_muted

                        # if the input number is wrong
                        else:
                            draw_text(screen, str(event.key - 48),
                                      rects[9*i + j].center, RED)

                            curr_sudoko_table[i][j] = event.key - 48
                            tmp_color[i][j] = RED
                            totall_mistakes += 1
                            if totall_mistakes < 3:
                                if not(is_muted):
                                    mistake_sound.play()

                # if the right numbers pressed
                if(0 < event.key - 1073741922 + 10 < 10):
                    if (event.key - 1073741922 + 10 != curr_sudoko_table[i][j]):
                        new_rect(screen, rects[9*i + j], BLACK, (173, 216, 230), 1,
                                 Horizental_diff, Vertical_diff, margin, bottom_margin)

                        # if the input number is correct
                        if (event.key - 1073741922 + 10) == solution_sudoko[i][j]:
                            if not(is_muted):
                                correct_sound.play()
                            draw_text(screen, str(event.key - 1073741922 + 10),
                                      rects[9*i + j].center, GREEN)
                            curr_sudoko_table[i][j] = event.key - \
                                1073741922 + 10
                            tmp_color[i][j] = GREEN
                            new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 1,
                                     Horizental_diff, Vertical_diff, margin, bottom_margin)
                            draw_text(screen, str(curr_sudoko_table[i][j]),
                                      rects[9*i + j].center, tmp_color[i][j])
                            return totall_mistakes, curr_sudoko_table, hint_numbers, is_muted

                        # if the input number is wrong
                        else:
                            draw_text(screen, str(event.key - 1073741922 + 10),
                                      rects[9*i + j].center, RED)

                            curr_sudoko_table[i][j] = event.key - \
                                1073741922 + 10
                            tmp_color[i][j] = RED
                            totall_mistakes += 1
                            if totall_mistakes < 3:
                                if not(is_muted):
                                    mistake_sound.play()

            if event.type == pygame.MOUSEBUTTONUP and is_valid(curr_sudoko_table, solution_sudoko):
                pos = pygame.mouse.get_pos()
                new_i, new_j = pos[1], pos[0]
                new_i, new_j = (
                    new_i-margin) // Vertical_diff, (new_j-margin) // Horizental_diff
                # if a new cell is selected
                if(i != new_i or j != new_j):
                    new_rect(screen, rects[9*i + j], BLACK, MY_COLOR, 1,
                             Horizental_diff, Vertical_diff, margin, bottom_margin)
                    totall_mistakes, curr_sudoko_table, hint_numbers, is_muted = insert(screen, pos, margin, Horizental_diff, Vertical_diff, bottom_margin,
                                                                                        curr_sudoko_table, solution_sudoko, rects,  totall_mistakes,
                                                                                        orginal_sudoko, hint_numbers, new_game_sound,
                                                                                        ss_sound, res_sound, hint_sound, start, correct_sound, mistake_sound, is_muted)
                    return totall_mistakes, curr_sudoko_table, hint_numbers, is_muted


# Define The GameOver Menu
def game_over(screen, orginal_sudoku, is_muted):
    menu = pygame_menu.Menu("Game Over", SIZE[0], SIZE[1], theme=My_theme)

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


# Define The Game_Solved Menu
def sudoku_solved(screen):
    menu = pygame_menu.Menu(
        "Congratulations !", SIZE[0], SIZE[1], theme=My_theme)

    def play():
        main()

    menu.add.button("Play", play)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.display.update()


# Define the Game start function
def start_the_game(initial_sudoko, is_muted, difficulty=1):
    screen = pygame.display.set_mode(SIZE, pygame.HWSURFACE)
    pygame.display.set_caption("SUDOKU")
    screen.fill(background_color)
    pygame.display.update()

    # Define the Start Time for calculating Elapsed Time
    start = time()

    # Add Grid to The Screen
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
        Time_Elapsed["text"] = f"Elapsed Time: {(elapsed // 60)//60 } : {elapsed // 60 } : {elapsed % 60}"
        draw_button(Time_Elapsed, screen=screen)

        Errors_Happened["text"] = f"Total Mistakes : {totall_mistakes}"
        draw_button(Errors_Happened, screen=screen)

        # Draw Buttons
        new_game_btn = draw_button(New_Game, screen=screen)
        restart_game_btn = draw_button(Restart_Game, screen=screen)
        screen_shot_btn = draw_button(Screen_Shot, screen=screen)
        mute_btn = draw_button(Mute, screen=screen)
        draw_button(Remaining_Hints, screen=screen)
        Remaining_Hints_Num = 3 - hint_numbers

        # Check The # of Remaining Hints
        if Remaining_Hints_Num == 0:
            hint_btn = draw_button(Hint, screen=screen, mouse_over=1)
            Remaining_Hints["text_color_inactive"] = RED
        else:
            hint_btn = draw_button(Hint, screen=screen)
            Remaining_Hints["text_color_inactive"] = "#003566"

        # Check if The mouse cursor is over the specific bottun or not
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

        # Check if the current sudoku table is completely Solved or Not
        if is_solved(tmp, solution_sudoko):
            if not(is_muted):
                win_sound.play()
            sleep(1)
            sudoku_solved(screen)

        for event in pygame.event.get():
            # Check for the Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check The # of Totall Mistakes
            if totall_mistakes < 3:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()

                    # if clicked On the Game Table
                    if (margin < pos[1] < Height - bottom_margin) and (margin < pos[0] < Width - margin):
                        totall_mistakes, tmp, hint_numbers, is_muted = insert(screen, pos, margin, Horizental_diff, Vertical_diff,
                                                                              bottom_margin, tmp, solution_sudoko, rects,
                                                                              totall_mistakes,  orginal_sudoko, hint_numbers, new_game_sound,
                                                                              ss_sound, res_sound, hint_sound, start, correct_sound,
                                                                              mistake_sound, is_muted)
                        # tmp = tmp

                    # if the New Game button is clicked
                    elif new_game_btn.collidepoint(pygame.mouse.get_pos()):
                        new_game_btn = draw_button(New_Game, screen=screen)
                        pygame.display.flip()
                        if not(is_muted):
                            new_game_sound.play()
                        sleep(0.1)
                        main()

                    # if the Restart button is clicked
                    elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
                        restart_game_btn = draw_button(
                            Restart_Game, screen=screen)
                        pygame.display.flip()
                        if not(is_muted):
                            res_sound.play()
                        sleep(0.1)
                        main(orginal_sudoko)

                    # if the ScreenShot button is clicked
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

                    # if the Mute button is clicked
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

            # if The # of Totall Mistakes >= 3
            else:
                if not(is_muted):
                    gameover_sound.play()
                sleep(1)
                game_over(screen, orginal_sudoko, is_muted)

        pygame.display.update()


def main(initial_sudoko=np.zeros((9, 9), dtype=int)):
    # initiale the screen
    screen, is_muted, Mute["text"], Mute["color_inactive"], Mute[
        "text_color_inactive"], Remaining_Hints["text_color_inactive"] = screen_init()

    # If the User want to Restart The Game
    if initial_sudoko.tolist() != np.zeros((9, 9), dtype=int).tolist():
        start_the_game(initial_sudoko, is_muted)

    # Define Callbacks for Menu Buttons
    def play_button():
        global Difficulty
        if not(is_muted):
            res_sound.play()
        start_the_game(initial_sudoko, is_muted, difficulty=Difficulty)

    # Set The Difficulty Level Of The New Game
    def set_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
        global Difficulty
        selected = value[0]
        Difficulty = int(selected[1])

    # The First Menu
    menu = pygame_menu.Menu(
        "Welcome", SIZE[0], SIZE[1], theme=My_theme)

    s = menu.add.selector("Difficulty :", [
                          ("Easy", 1), ("Medium", 2), ("Hard", 3)], onchange=set_difficulty)
    # When The menu is loaded , call set_difficulty func.
    s.set_onselect(set_difficulty(s.get_value(), s.get_index()))
    menu.add.button("Play",  play_button)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.display.update()


if __name__ == "__main__":
    main()
