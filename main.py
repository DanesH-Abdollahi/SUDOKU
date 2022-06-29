# import pygame
# from pygame.locals import *

# screen = pygame.display.set_mode((1280, 720))

# YELLOW = (255, 255, 0)
# BLACK = (0, 0, 0)
# GRAY = (127, 127, 127)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# CYAN = (0, 255, 255)
# MAGENTA = (255, 0, 255)

# key_dict = {
#     K_k: BLACK,
#     K_r: RED,
#     K_g: GREEN,
#     K_b: BLUE,
#     K_y: YELLOW,
#     K_c: CYAN,
#     K_m: MAGENTA,
#     K_w: WHITE,
# }

# background = GRAY
# screen.fill(background)
# pygame.display.update()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == KEYDOWN:
#             if event.key in key_dict:
#                 background = key_dict[event.key]
#                 screen.fill(background)
#                 pygame.display.update()

#                 caption = "background color = " + str(background)
#                 pygame.display.set_caption(caption)

# pygame.quit()


import pygame
from pygame.locals import *

from pygame.rect import *

pts = (
    "topleft",
    "topright",
    "bottomleft",
    "bottomright",
    "midtop",
    "midright",
    "midbottom",
    "midleft",
    "center",
)
SIZE = 500, 200
RED = (255, 0, 0)
GRAY = (150, 150, 150)
pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
rect = Rect(50, 60, 200, 80)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        screen.fill(GRAY)
        pygame.draw.rect(screen, GRAY, rect, 4)

        for pt in pts:
            pos = eval("rect." + pt)
            # pygame.draw_text(pt, pos)
            pygame.draw.circle(screen, RED, pos, 3)

    pygame.display.flip()

pygame.quit()
