import pygame_menu.themes
import pygame

# Define Size Of The Window
SIZE = (720, 720)
Width, Height = SIZE

# Define Colors
BLACK = (0, 0, 0)
RED = (178, 34, 34)
GREEN = (0, 100, 0)
MY_COLOR = (253, 245, 230)
Orginal_Sudoko_number_color = (25, 25, 112)
background_color = MY_COLOR

# Define Our Costume Pygame_menu Theme
My_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
My_theme.title_font = "../resources/FORTE.ttf"
My_theme.title_font_size = 80
My_theme.background_color = "#f2e9e4"
# My_theme.title_bar_style = 1001
My_theme.widget_font_size = 50
My_theme.widget_font = "../resources/FORTE.ttf"

# Params for drawing Screen Properly
Margin = Width // 80
Button_Border = 0
Button_Width = Width // 5
Button_Height = (Height * 3) // 40
Horizontal_Space_Between_Buttons = Width // 40
Vertical_Space_Between_Buttons = Height // 80

# Param For Checking
Remaining_Hints_Num = 3

pygame.mixer.init()

gameIcon = pygame.image.load('../resources/icon.png')
ss_sound = pygame.mixer.Sound("../resources/ScreenShot.wav")
new_game_sound = pygame.mixer.Sound("../resources/NewGame.wav")
res_sound = pygame.mixer.Sound("../resources/ResSound.wav")
hint_sound = pygame.mixer.Sound("../resources/Hint.wav")
gameover_sound = pygame.mixer.Sound("../resources/GameOver.wav")
win_sound = pygame.mixer.Sound("../resources/Win.wav")
correct_sound = pygame.mixer.Sound("../resources/Correct.wav")
mistake_sound = pygame.mixer.Sound("../resources/Mistake.wav")


def screen_init():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(SIZE, pygame.HWSURFACE)
    pygame.display.set_icon(gameIcon)
    pygame.display.set_caption("SUDOKU")
    return screen


# Define Buttons
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
    "font": "../resources/FORTE.ttf",
    "font_size": 25,
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
    "font": "../resources/FORTE.ttf",
    "font_size": 25,
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
    "font": "../resources/FORTE.ttf",
    "font_size": 25,
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
    "font": "../resources/FORTE.ttf",
    "font_size": 25,
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
    "font": "../resources/FORTE.ttf",
    "font_size": 27,
}

Remaining_Hints = {
    "left": Width - Margin - 4 * Button_Border - 2*Button_Width - Horizontal_Space_Between_Buttons,
    "top": Height
    - Margin
    - Button_Border * 6
    - Button_Height * 3
    - Vertical_Space_Between_Buttons * 2,
    "width": 2 * Button_Width + Horizontal_Space_Between_Buttons,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#adc178",
    "color_active": "#",
    "border_color": background_color,
    "text": f"Remaining Hints: {Remaining_Hints_Num}",
    "text_color_inactive": "#003566",
    "text_color_active": "#",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Errors_Happened = {
    "left": Width
    - Margin
    - 4 * Button_Border
    - 2 * Button_Width
    - Horizontal_Space_Between_Buttons,
    "top": Height
    - Margin
    - Button_Border * 4
    - Button_Height * 2
    - Vertical_Space_Between_Buttons * 1,
    "width": 2 * Button_Width + Horizontal_Space_Between_Buttons,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#bbd0ff",
    "color_active": "#",
    "border_color": background_color,
    "text": f"Remaining Hints: {Remaining_Hints_Num}",
    "text_color_inactive": RED,
    "text_color_active": "#",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}

Mute = {
    "left": Width
    - Margin
    - 4 * Button_Border
    - 2 * Button_Width
    - Horizontal_Space_Between_Buttons,
    "top": Height - Margin - Button_Border * 2 - Button_Height * 1,
    "width": 2 * Button_Width + Horizontal_Space_Between_Buttons,
    "height": Button_Height,
    "border": Button_Border,
    "color_inactive": "#2ec4b6",
    "color_active": "#",
    "border_color": background_color,
    "text": "Unmuted",
    "text_color_inactive": "#560bad",
    "text_color_active": "#",
    "font": "../resources/FORTE.ttf",
    "font_size": 30,
}
