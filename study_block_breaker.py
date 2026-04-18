import pygame
import random

# Initialize pygame
pygame.init()
# 1st_window_tab
def window():
    # Dimensions of the screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Brick Breaker !!")
    return screen

def main():
    # Screen
    tab = window()
    # Bar
    # start position
    x = 400
    y = 500

    width = 20
    height = 20
    vel = 5

    # Ball
    ball_x = 400
    ball_y = 400
    dx = 4
    dy = 4
    ball_radius = 10

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Operate bar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 800 - width:
            x += vel
        # Operate ball
        if keys[pygame.K_SPACE]:
            ball_x += dx
            ball_y += dy

        # rebound wall
        if ball_x <= 0 or ball_x >= 800:
            dx *= -1
        if ball_y <= 0 or ball_x >= 600:
            dy *= -1

        # drawing
        tab.fill((0, 0, 0))
        # drawing bar
        pygame.draw.rect(tab, (255, 0, 0), (x, y, width, height))
        # drawing ball
        pygame.draw.circle(tab, (255, 255, 0), (ball_x, ball_y), ball_radius)

        pygame.display.update()
    pygame.quit()

    pygame.quit()
if __name__ == "__main__":
     main()