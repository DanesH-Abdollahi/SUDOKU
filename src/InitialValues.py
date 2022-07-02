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
