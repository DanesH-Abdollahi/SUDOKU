import pygame
import sys

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


def add_grid(screen):
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


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("SUDOKU")
    screen.fill(background_color)
    pygame.display.update()

    add_grid(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
