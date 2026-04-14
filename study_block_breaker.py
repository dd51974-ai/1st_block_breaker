import pygame
import random

# 1st_window_tab
def window():
    pygame.init()
    # Dimensions of the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Brick Breaker !!")


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
     window()