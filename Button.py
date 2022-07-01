import time
from unittest import runner
import pygame
from pygame.locals import *
import sys

# ----------------------------------------------------- #
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

Orginal_Sudoko_number_color = (25, 25, 112)
background_color = MY_COLOR

SIZE = (800, 800)
Width, Height = SIZE
Margin = int(Width / 80)

# ----------------------------------------------------- #
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("SUDOKU")
screen.fill(background_color)
pygame.display.update()

# --------------------------- __NEW__ -------------------------- #
start = time.time()  # NEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
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
Time_Elapsed = {  # NEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    "left": Width - Margin - Button_Border * 2 - Button_Width * 2,
    "top": Height
    - Margin
    - Button_Border * 4
    - Button_Height * 2
    - Vertical_Space_Between_Buttons,
    "width": 2 * Button_Width,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#2c6e49",
    "color_active": "#",
    "border_color": background_color,
    "text": "",
    "text_color_inactive": "#fefee3",
    "text_color_active": "#",
    "font": "FORTE.ttf",
    "font_size": 30,
}

# --------------------------- __NEW__ -------------------------- #
def draw_button(Button_Name, mouse_over=0):

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


# --------------------------- __NEW__ -------------------------- #

running = True
while running:

    elapsed = round(time.time() - start)  # NEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    Time_Elapsed[
        "text"
    ] = f"Elapsed Time: {(elapsed // 60)//60 } : {elapsed // 60 } : {elapsed % 60}"  # NEWWWWWWWWWWWWWWWWWWWWWWWWW
    time_elapsed_btn = draw_button(
        Time_Elapsed
    )  # NewWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    new_game_btn = draw_button(New_Game)
    restart_game_btn = draw_button(Restart_Game)
    hint_btn = draw_button(Hint)
    screen_shot_btn = draw_button(Screen_Shot)

    if new_game_btn.collidepoint(pygame.mouse.get_pos()):
        new_game_btn = draw_button(New_Game, mouse_over=1)
    elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
        restart_game_btn = draw_button(Restart_Game, mouse_over=1)
    elif hint_btn.collidepoint(pygame.mouse.get_pos()):
        hint_btn = draw_button(Hint, mouse_over=1)
    elif screen_shot_btn.collidepoint(pygame.mouse.get_pos()):
        screen_shot_btn = draw_button(Screen_Shot, mouse_over=1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if new_game_btn.collidepoint(pygame.mouse.get_pos()):
                new_game_btn = draw_button(New_Game)
                pygame.display.flip()
                time.sleep(0.1)

            elif restart_game_btn.collidepoint(pygame.mouse.get_pos()):
                restart_game_btn = draw_button(Restart_Game)
                pygame.display.flip()
                time.sleep(0.1)
            elif hint_btn.collidepoint(pygame.mouse.get_pos()):
                hint_btn = draw_button(Hint)
                pygame.display.flip()
                time.sleep(0.1)
            elif screen_shot_btn.collidepoint(pygame.mouse.get_pos()):
                screen_shot_btn = draw_button(Screen_Shot)
                pygame.display.flip()
                time.sleep(0.1)
                pygame.image.save(screen, "ScreenShot.jpg")

    pygame.display.flip()

pygame.quit()
